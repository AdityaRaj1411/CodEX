from utils import call_llm
import re
from config import GENERATOR_MODEL  


class Analyzer:
    def __init__(self, model=None):
        self.model = model if model else GENERATOR_MODEL

    def analyze(self, query):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a system analyzer.\n"
                    "Your job is to decide how many refinement iterations are needed "
                    "to solve a coding task.\n\n"
                    "Rules:\n"
                    "- Return ONLY a number: 1, 2, or 3\n"
                    "- 1 = very simple (basic print, math)\n"
                    "- 2 = moderate (functions, small logic)\n"
                    "- 3 = complex (classes, APIs, multiple steps, algorithms)\n"
                    "- Do NOT explain anything\n"
                    "Just return a number between 1 and 3 based on the complexity of the task.Nothing Else"
                )
            },
            {
                "role": "user",
                "content": query
            }
        ]

        result = call_llm(messages, self.model, temperature=0)
        print("\n[DEBUG] Analyzer raw output:")
        print(result)
        print("[END DEBUG]\n")

        # Safety parsing
        

        try:
            match = re.search(r"\d+", result)
            value = int(match.group()) if match else 2
            return max(1, min(3, value))
        except:
            return 2