import gradio as gr
from core import run_agent_system  # if no streaming, we’ll simulate


# 🧼 Clean code
def clean_code(code):
    if not code:
        return ""
    if "```" in code:
        parts = code.split("```")
        for part in parts:
            if part.strip() and not part.strip().startswith("python"):
                return part.strip()
        return parts[1].replace("python", "").strip()
    return code.strip()


# 🔥 MAIN FUNCTION (SIMULATED STREAMING)
def solve_task_ui(query, history):
    result = run_agent_system(query)

    attempts = result.get("all_attempts", [])
    best_index = result.get("best_index", -1)

    codes = [a["code"] for a in attempts]

    history = codes

    # ✅ Mark BEST in dropdown
    dropdown_choices = []
    for i in range(len(codes)):
        label = f"Version {i+1}"
        if i == best_index:
            label += " ⭐ BEST"
        dropdown_choices.append(label)

    selected_code = codes[best_index] if best_index != -1 else codes[-1]

    iterations = result.get("iterations", len(codes))

    return (
        selected_code,
        history,
        gr.update(choices=dropdown_choices, value=dropdown_choices[best_index] if best_index != -1 else dropdown_choices[-1]),
        gr.update(choices=dropdown_choices, value=dropdown_choices[best_index] if best_index != -1 else dropdown_choices[-1]),
        f"Iterations: {iterations}"
    )
# 🔁 Show selected version
def show_version(selected, history_state):
    if not selected or not history_state:
        return ""

    index = int(selected.split()[-1]) - 1
    return history_state[index]


# 🎨 UI
with gr.Blocks(title="AI Coding Agent") as demo:

    gr.Markdown("# 🤖 AI Coding Agent")
    gr.Markdown("Live code generation + version tracking + iteration count")

    state = gr.State([])

    user_input = gr.Textbox(
        label="Enter your task",
        placeholder="e.g. print first 5 fibonacci numbers",
        lines=2
    )

    run_btn = gr.Button("Run Agent 🚀")

    iteration_box = gr.Textbox(
        label="Iterations",
        interactive=False
    )

    dropdown = gr.Dropdown(
        label="Select Version",
        choices=[],
        interactive=True
    )

    code_output = gr.Code(
        label="Code Viewer",
        language="python"
    )

    # 🔥 Run agent
    run_btn.click(
        fn=solve_task_ui,
        inputs=[user_input, state],
        outputs=[code_output, state, dropdown, dropdown, iteration_box]
    )

    # 🔁 Switch versions
    dropdown.change(
        fn=show_version,
        inputs=[dropdown, state],
        outputs=code_output
    )

# 🚀 Launch
if __name__ == "__main__":
    demo.launch(debug=True)