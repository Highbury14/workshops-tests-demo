import re
from collections import Counter

from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool

_STOP_WORDS = {
  "a", "an", "and", "are", "as", "at", "be", "been", "but", "by",
  "for", "from", "had", "has", "have", "he", "her", "his", "i", "in",
  "is", "it", "its", "of", "on", "or", "our", "she", "that", "the",
  "their", "them", "there", "they", "this", "to", "was", "we", "were",
  "will", "with", "you", "your",
}
_WORD_PATTERN = re.compile(r"\b[\w'-]+\b", re.UNICODE)

def calculator(
  operation: str,
  a: float,
  b: float
) -> float:
  """
  Perform a mathematical calculation.

  Args:
    operation: The operation to perform.
               Supported operations:
               add, subtract, multiply, divide
    a: First number.
    b: Second number.

  Returns:
    Result of the calculation.
  """

  if operation == "add":
    return a + b

  elif operation == "subtract":
    return a - b

  elif operation == "multiply":
    return a * b

  elif operation == "divide":
    if b == 0:
      return "Cannot divide by zero."

    return a / b

  return "Unsupported operation."

def text_analyzer(text: str) -> dict[str, object]:
  """Analyze text structure, length, character-count, word-count, sentence-count, paragraph-count, vocabulary, and frequently used keywords."""
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
  description = "A multi-tool general-purpose assistant for peforming information-search, math-calculations, and text-analysis.",
  instruction = """
You are a multi-tool general-purpose assistant. Choose the provided tools based on the user's request:
- Use google_search tool for current, external, or otherwise up-to-date information, then answer from its results.
- Cite useful search sources when available and distinguish sourced facts from uncertainty.
- Use calculator tool for mathematical expressions and arithmetic operations; Calculate the result accurately and explicitly. Do not estimate arithmetic mentally when this tool applies.
- Use text_analyzer tool when a user asks to analyze the provided text. Use its measured statistics and keywords, and explain tone, themes, or meaning from the text when requested.
- For requests combining these tasks, use each relevant tool. Do not use a tool when it does not help answer the request.
- If a request is ambiguous, ask the user for clarification before answering.
- Do not invent current information. Always use the appropriate tool when current or external information is required.
- Present the final answer clearly and concisely.
""".strip(),
  tools = [
    # ADK otherwise limits Google Search from sharing an agent with function tools.
    GoogleSearchTool(bypass_multi_tools_limit=True),
    calculator,
    text_analyzer,
  ],
)
