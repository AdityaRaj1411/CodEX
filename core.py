from agents import generate_code, critic_review, select_best
from executor import run_code
from memory import Memory
from analyzer import Analyzer
from utils import extract_code
from config import FAST_MODE


def run_agent_system(query):
    memory = Memory()
    analyze = Analyzer()

    max_iter = analyze.analyze(query)
    print("Max_iter:", max_iter)

    # Fast mode limiter
    if FAST_MODE:
        max_iter = min(2, max_iter)

    feedback = None
    attempts = []

    for i in range(max_iter):
        print(f"\n--- Iteration {i+1} ---")

        # 🔹 Step A: Generate code
        raw_code = generate_code(query, feedback)
        code = extract_code(raw_code)

        print("\nGenerated Code:\n", code)

        # 🔹 Step B: Execute code
        output, error = run_code(code)

        print("\nOutput:\n", output)
        print("\nError:\n", error)

        # 🔹 Step C: Critic review
        if error.strip() == "":
            critique = "No issues"
        else:
            critique = critic_review(code, output, error)

        print("\nCritique:\n", critique)

        # 🔹 Store in memory
        memory.add(code, output, error, critique)

        # 🔹 Store attempt for UI
        attempts.append({
            "code": code,
            "output": output,
            "error": error,
            "critique": critique,
            "iteration": i + 1
        })

        # 🔹 Feedback loop
        feedback = critique

        # 🔹 Early stopping
        if error.strip() == "" and output.strip() != "":
            print("\n✅ Good result found. Stopping early.")
            break

    # 🔹 Step D: Selector (LLM-based)
    try:
        selector_output = select_best(memory.get_all_codes())
    except Exception as e:
        print("\n[ERROR] Selector crashed:", str(e))
        selector_output = "LLM_ERROR"

    # 🔹 Fallback safety
    if not selector_output or selector_output == "LLM_ERROR":
        print("\n[WARNING] Selector failed. Using best known code.")
        best_code = memory.get_best_code()
    else:
        best_code = selector_output
    best_index = -1

    for idx, attempt in enumerate(attempts):
        if attempt["code"].strip() == best_code.strip():
            best_index = idx
            attempt["is_best"] = True
        else:
            attempt["is_best"] = False    

    # 🔹 Final structured return (VERY IMPORTANT for UI)
    return {
    "best_solution": best_code,
    "all_attempts": attempts,
    "iterations": len(attempts),
    "best_index": best_index
}