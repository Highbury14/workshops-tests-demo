from ollama import chat

response = chat(
  model="qwen2.5:3b",
  messages=[{
    "role": "user",
    "content": "Explain the difference between supervised and unsupervised learning in three bullet points."
  },]
)

print("Question: Explain the difference between supervised and unsupervised learning in three bullet points.")
print("Answer:", response["message"]["content"])

response = chat(
  model="qwen2.5:3b",
  messages=[{
    "role": "user",
    "content": "Explain neural networks as if you were teaching a 12-year-old."
  },]
)

print("Question: Explain neural networks as if you were teaching a 12-year-old.")
print("Answer:", response["message"]["content"])
