class Memory:
    def __init__(self):
        self.history = []

    def add(self, code, output, error, critique):
        self.history.append({
            "code": code,
            "output": output,
            "error": error,
            "critique": critique
        })

    def get_all_codes(self):
        return [item["code"] for item in self.history]

    def get_last_feedback(self):
        if not self.history:
            return None
        return self.history[-1]["critique"]
    def get_best_code(self):
        for entry in reversed(self.history):
            code, output, error, critique = entry
            if error.strip() == "":
                return code
        return self.history[-1]["code"]  # fallback last code