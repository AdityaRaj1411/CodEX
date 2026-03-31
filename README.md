# 🧠 CodEX: Multi-Agent Code Generation System

CodEX is an intelligent multi-agent system that automatically generates, executes, critiques, and improves Python code using iterative reasoning. It simulates a collaborative workflow between different AI agents to produce the best possible solution for a given task.

---

## 🚀 Features

* 🔁 **Iterative Code Generation** – Improves code over multiple iterations
* ⚙️ **Automatic Code Execution** – Runs generated code and captures output/errors
* 🧪 **Critic Agent** – Reviews errors and suggests improvements
* 🏆 **Selector Agent** – Chooses the best version among all attempts
* 🧠 **Analyzer Agent** – Dynamically decides number of iterations
* 💾 **Memory System** – Stores all attempts for comparison
* 🌐 **Gradio UI** – Interactive frontend with:

  * Version dropdown
  * Best version highlighting ⭐
  * Iteration count
  * Live code display

---

## 📁 Project Structure

```
CodEX/
│
├── core.py          # Main orchestration logic (agent loop)
├── agents.py        # Generator, Critic, Selector agents
├── analyzer.py      # Determines number of iterations
├── executor.py      # Runs generated code safely
├── memory.py        # Stores all attempts
├── utils.py         # Helper functions (e.g., extract_code)
├── config.py        # Config flags (FAST_MODE, etc.)
├── app.py           # Gradio frontend
├── main.py          # CLI entry point
└── README.md
```

---

## ⚙️ How It Works

1. **User Input** → Provide a coding task
2. **Analyzer** → Decides how many iterations to run
3. **Generator** → Produces initial code
4. **Executor** → Runs the code
5. **Critic** → Reviews errors/output
6. **Loop** → Improves code using feedback
7. **Selector** → Picks the best version
8. **UI** → Displays all versions + best one

---

## 🖥️ Running the Project

### 1. Install dependencies

```bash
pip install gradio openai
```

---

### 2. Run CLI version

```bash
python main.py
```

---

### 3. Run UI (Recommended)

```bash
python app.py
```

Then open the local Gradio link in your browser.

---

## 🎯 Example Use Case

**Input:**

```
Write a Python function to calculate factorial
```

**System will:**

* Generate multiple versions
* Fix errors automatically
* Compare outputs
* Select best implementation

---

## 🧩 Output Format

The system returns:

```
{
  "best_solution": "...final code...",
  "all_attempts": [...],
  "iterations": 3,
  "best_index": 1
}
```

---

## 🌟 UI Features

* 📜 Dropdown for all code versions
* ⭐ Best version highlighted
* 🔢 Iteration counter
* 🧾 Clean code display (no markdown clutter)

---

## ⚡ Config Options

In `config.py`:

```python
FAST_MODE = True  # Limits iterations for speed
```

---

## 🔮 Future Improvements

* Live streaming of code generation (ChatGPT-style)
* Diff view between versions
* Error highlighting
* Execution logs panel
* Support for multiple programming languages

---

## 🤝 Contributing

Feel free to fork, improve, and experiment with new agents or models.

---

## 📌 Summary

CodEX is a **self-improving AI coding system** that:

* Thinks
* Writes
* Tests
* Fixes
* Chooses the best solution

All automatically 🚀

---
