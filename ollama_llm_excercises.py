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

"""
[2026-10-14 17:30:38] F:\Project-source-code\workshops tests demo> ollama --version
ollama version is 0.40.4
[2026-10-15 11:12:32] F:\Project-source-code\workshops tests demo> ollama pull qwen2.5:3b
pulling manifest
pulling 5ee4f07cdb9b: 100% ▕██████████████████████████████████████████████████████████▏ 1.9 GB
pulling 161ddde4c9cd: 100% ▕██████████████████████████████████████████████████████████▏  487 B
verifying sha256 digest
writing manifest
success
[2026-10-17 09:07:48] F:\Project-source-code\workshops tests demo> ollama run qwen2.5:3b
>>> Explain machine learning in simple language.
Sure! Imagine you have a computer program that learns from data, just like you learn from experiences. Machine
learning is a way to teach computers to do this automatically.

Here’s a simple way to think about it:

1. **Data**: This is like the information the computer gets to learn from. It could be numbers, pictures, words,
or even videos.

2. **Learning**: Instead of you telling the computer exactly what to do in every situation, you show it examples.
The computer figures out the rules for itself based on these examples.

3. **Pattern Recognition**: Just like you can recognize patterns in your daily life, the computer learns to
recognize patterns in the data it's given. It can find patterns that help it make decisions or predictions.

For example, let’s say you want to teach a computer to recognize cats in pictures. You can show the computer
thousands of pictures of cats and non-cats. Over time, the computer learns to spot what makes a picture look like
a cat. It can then be used to find cats in new pictures.

In summary, machine learning is a tool that lets computers learn and improve their performance on a task without
being explicitly programmed to do so, by using algorithms and models to analyze and learn from data.

>>>"""

"""
[2026-10-17 09:58:56] F:\Project-source-code\workshops tests demo> python .\ollama_llm_excercises.py
Question: Explain the difference between supervised and unsupervised learning in three bullet points.
Answer: - Supervised learning involves training a model on a dataset with labeled data, where the model learns to map inputs to outputs, aiming to predict the correct output for new, unseen inputs.
- Unsupervised learning, on the other hand, involves training a model on unlabeled data, where the model discovers hidden patterns or internal representations in the data without predefined outputs to predict.
- In supervised learning, the focus is on learning a function that can be used to make predictions or classifications, whereas in unsupervised learning, the goal is often to understand the structure or distribution of the data.

Question: Explain neural networks as if you were teaching a 12-year-old.
Answer: Sure! Imagine you have a really smart and curious friend who can solve puzzles really quickly. This friend is always learning new things and can remember a lot of information. We can think of this friend as a neural network, which is a type of computer program designed to learn from data and make predictions or decisions.

### How Neural Networks Work

1. **Neural Networks are Like a Brain:**
   - Just like your brain, a neural network has a bunch of “neurons” that work together to process information. Each neuron is like a little processor that can learn from data.
   - Think of it like a team of people working on a big project. Each person in the team has a job, and they can all learn from each other.

2. **Layers and Nodes:**
   - Neural networks have different layers, kind of like a sandwich with different layers. The outer layers are called "input" and "output" layers, and the middle layers are called "hidden" layers.
   - Each layer has many "nodes" (or "neurons"), which are like the people in the team. Each node gets information fromthe layer below it, does something with it, and then passes it on to the layer above it.
   - For example, in a game where you have to guess what picture someone is looking at, the first layer might look at the edges of the picture, the second layer might look at the colors, and the third layer might combine all these featuresto guess the picture.

3. **Learning:**
   - Just like you learn by doing and making mistakes, a neural network "learns" by adjusting how it works after it makes a guess.
   - If the guess is wrong, it changes how it works a little bit to make a better guess next time. This process is called "training."
   - Imagine if you were trying to guess what color shirt someone is wearing. If you guess wrong, you might learn that sometimes people wear shirts under other clothes, and sometimes they wear them under sunglasses. Your brain makes these adjustments over time.

4. **Making Decisions:**
   - Neural networks can do many different things, like recognize pictures, understand speech, or even play games. Theydo these things by looking at a lot of examples and figuring out what works best.
   - For example, if you taught a neural network to recognize dogs, it might learn from seeing lots of different dogs in photos. Once it’s learned, it can recognize dogs in new pictures or videos.

### Why Neural Networks are Useful

- Neural networks are very good at handling big, complex data. They can find patterns that are hard for us to see on our own, especially when the patterns are in lots of different types of data, like images, sounds, or text.
- They are used in many places, like helping self-driving cars understand the world, making recommendations for movies or songs, or even helping doctors diagnose diseases by looking at medical scans.

So, in short, neural networks are like smart, learning friends who can do amazing things by processing lots of information and finding hidden patterns.

[2026-10-17 10:27:26] F:\Project-source-code\workshops tests demo> ollama ps
NAME          ID              SIZE      PROCESSOR    CONTEXT    RUNNER      UNTIL
qwen2.5:3b    357c53fb659c    2.2 GB    100% CPU     4096       llamacpp    About a minute from now
"""
