import ast
import math
import operator
import re
from collections import Counter
from typing import Callable

from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool

_BINARY_OPERATORS: dict[type[ast.operator], Callable[[int | float, int | float], int | float]] = {
  ast.Add: operator.add,
  ast.Sub: operator.sub,
  ast.Mult: operator.mul,
  ast.Div: operator.truediv,
  ast.FloorDiv: operator.floordiv,
  ast.Mod: operator.mod,
  ast.Pow: operator.pow,
}
_UNARY_OPERATORS: dict[type[ast.unaryop], Callable[[int | float], int | float]] = {
  ast.UAdd: operator.pos,
  ast.USub: operator.neg,
}
_MATH_CONSTANTS = {"pi": math.pi, "e": math.e, "tau": math.tau}
_MATH_FUNCTIONS: dict[str, tuple[Callable[..., int | float], int, int]] = {
  "abs": (abs, 1, 1),
  "acos": (math.acos, 1, 1),
  "asin": (math.asin, 1, 1),
  "atan": (math.atan, 1, 1),
  "ceil": (math.ceil, 1, 1),
  "cos": (math.cos, 1, 1),
  "degrees": (math.degrees, 1, 1),
  "exp": (math.exp, 1, 1),
  "factorial": (math.factorial, 1, 1),
  "floor": (math.floor, 1, 1),
  "log": (math.log, 1, 2),
  "log10": (math.log10, 1, 1),
  "max": (max, 2, 16),
  "min": (min, 2, 16),
  "radians": (math.radians, 1, 1),
  "round": (round, 1, 2),
  "sin": (math.sin, 1, 1),
  "sqrt": (math.sqrt, 1, 1),
  "tan": (math.tan, 1, 1),
}
_STOP_WORDS = {
  "a", "an", "and", "are", "as", "at", "be", "been", "but", "by",
  "for", "from", "had", "has", "have", "he", "her", "his", "i", "in",
  "is", "it", "its", "of", "on", "or", "our", "she", "that", "the",
  "their", "them", "there", "they", "this", "to", "was", "we", "were",
  "will", "with", "you", "your",
}
_WORD_PATTERN = re.compile(r"\b[\w'-]+\b", re.UNICODE)


def _checked_number(value: int | float) -> int | float:
  if type(value) not in (int, float):
    raise ValueError("Complex and non-numeric results are not supported.")
  if isinstance(value, float) and not math.isfinite(value):
    raise ValueError("The calculation produced a non-finite result.")
  if isinstance(value, int) and value.bit_length() > 4096:
    raise ValueError("The calculation result is too large.")
  return value


def _evaluate_expression(node: ast.expr) -> int | float:
  if isinstance(node, ast.Constant) and type(node.value) in (int, float):
    return _checked_number(node.value)

  if isinstance(node, ast.Name) and node.id in _MATH_CONSTANTS:
    return _MATH_CONSTANTS[node.id]

  if isinstance(node, ast.BinOp):
    operation = _BINARY_OPERATORS.get(type(node.op))
    if operation is None:
      raise ValueError("That arithmetic operator is not supported.")

    left = _evaluate_expression(node.left)
    right = _evaluate_expression(node.right)
    if isinstance(node.op, ast.Pow) and abs(right) > 100:
      raise ValueError("Exponents must be between -100 and 100.")
    return _checked_number(operation(left, right))

  if isinstance(node, ast.UnaryOp):
    operation = _UNARY_OPERATORS.get(type(node.op))
    if operation is None:
      raise ValueError("That unary operator is not supported.")
    return _checked_number(operation(_evaluate_expression(node.operand)))

  if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
    if node.keywords:
      raise ValueError("Named function arguments are not supported.")

    function_details = _MATH_FUNCTIONS.get(node.func.id)
    if function_details is None:
      raise ValueError(f"Function '{node.func.id}' is not supported.")

    function, minimum_arguments, maximum_arguments = function_details
    arguments = [_evaluate_expression(argument) for argument in node.args]
    if not minimum_arguments <= len(arguments) <= maximum_arguments:
      raise ValueError(
        f"Function '{node.func.id}' expects "
        f"{minimum_arguments} to {maximum_arguments} argument(s)."
      )
    if node.func.id == "factorial" and (
      not isinstance(arguments[0], int) or not 0 <= arguments[0] <= 1000
    ):
      raise ValueError("factorial expects an integer between 0 and 1000.")
    if (
      node.func.id == "round"
      and len(arguments) == 2
      and not isinstance(arguments[1], int)
    ):
      raise ValueError("The second argument to round must be an integer.")
    return _checked_number(function(*arguments))

  raise ValueError("Only arithmetic expressions and supported math functions are allowed.")


def math_calculator(expression: str) -> dict[str, int | float | str]:
  """Safely evaluate a mathematical expression using arithmetic and common math functions."""
  if len(expression) > 512:
    return {"error": "The expression must be 512 characters or fewer."}

  try:
    parsed_expression = ast.parse(expression, mode="eval")
  except SyntaxError as error:
    return {"error": f"Invalid mathematical expression: {error.msg}"}

  if sum(1 for _ in ast.walk(parsed_expression)) > 128:
    return {"error": "The expression is too complex to calculate safely."}

  try:
    result = _evaluate_expression(parsed_expression.body)
  except (ArithmeticError, ValueError) as error:
    return {"error": str(error)}

  return {"expression": expression, "result": result}


def text_analyzer(text: str) -> dict[str, object]:
  """Analyze text structure, length, vocabulary, and frequently used keywords."""
  words = [match.group().casefold() for match in _WORD_PATTERN.finditer(text)]
  sentences = [
    sentence
    for sentence in re.split(r"[.!?]+(?:\s+|$)", text.strip())
    if sentence.strip()
  ]
  paragraphs = [
    paragraph
    for paragraph in re.split(r"\n\s*\n", text.strip())
    if paragraph.strip()
  ]
  keywords = Counter(
    word
    for word in words
    if len(word) > 2 and word.isalpha() and word not in _STOP_WORDS
  )

  return {
    "characters": len(text),
    "words": len(words),
    "sentences": len(sentences),
    "paragraphs": len(paragraphs),
    "average_words_per_sentence": (
      round(len(words) / len(sentences), 2) if sentences else 0
    ),
    "lexical_diversity": round(len(set(words)) / len(words), 3) if words else 0,
    "top_keywords": [
      {"term": word, "count": count}
      for word, count in keywords.most_common(5)
    ],
  }


root_agent = Agent(
  model = "gemini-3.6-flash",
  name = "root_agent",
  description = "A general-purpose assistant for research, calculations, and text analysis.",
  instruction = """
You are a general-purpose assistant. Choose tools based on the user's request:
- Use google_search for current, external, or otherwise up-to-date information, then answer from its results.
- Cite useful search sources when available and distinguish sourced facts from uncertainty.
- Use math_calculator for mathematical expressions; do not estimate arithmetic mentally when this tool applies.
- Use text_analyzer when a user asks to analyze provided text. Use its measured statistics and keywords, and explain tone, themes, or meaning from the text when requested.
- For requests combining these tasks, use each relevant tool. Do not use a tool when it does not help answer the request.
""".strip(),
  tools = [
    # ADK otherwise limits Google Search from sharing an agent with function tools.
    GoogleSearchTool(bypass_multi_tools_limit=True),
    math_calculator,
    text_analyzer,
  ],
)
