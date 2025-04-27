# 🤖 AutoAgent v0.1

**AutoAgent v0.1** is a simple reasoning and acting agent that can take a user's goal, think through steps logically, call external tools when needed, and generate a final answer based on real observations.

It follows the **ReAct pattern**:  
> **Thought → Action → Observation → Final Answer**

This project demonstrates how to build an AI agent that doesn't just generate text, but actually **uses tools to reason, act, and solve tasks dynamically.**

---

## 🚀 Features

- Understands user goals through a conversational interface
- Plans step-by-step reasoning (Thought)
- Calls real tools (Action) like (DUMMY CALLS!):
  - `get_weather(location)`
  - `calculate(expression)`
  - `web_search(query)`
- Observes results and updates its thinking (Observation)
- Stops intelligently when a complete Final Answer is ready
- Dynamically parses tool actions from LLM output
- Modular, extensible design (easy to add more tools later)

---
