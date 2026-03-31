from utils import call_llm
from config import (
    GENERATOR_MODEL, CRITIC_MODEL, SELECTOR_MODEL,
    GENERATOR_TEMP, CRITIC_TEMP, SELECTOR_TEMP
)


def generate_code(query, feedback=None):
    messages = [
        {
            "role": "system",
            "content": "You are an expert Python developer. Write clean, correct, efficient code. You can include some features and be a creative coder but make sure there is no error in the code"
        },
        {
            "role": "user",
            "content": f"""
Task:
{query}

Previous feedback:
{feedback if feedback else "None"}

Return ONLY Python code inside ```python``` block.
"""
        }
    ]

    return call_llm(messages, GENERATOR_MODEL, GENERATOR_TEMP)


def critic_review(code, output, error):
    messages = [
        {
            "role": "system",
            "content": "You are a strict code reviewer. Find bugs and suggest precise fixes. Can be harsh but constructive. Focus on correctness and efficiency.Can also suggest some new features to speed up the code but make sure to be  recise and consise"                
        },
        {
            "role": "user",
            "content": f"""
Code:
{code}

Output:
{output}

Error:
{error}

Give concise feedback.
"""
        }
    ]

    return call_llm(messages, CRITIC_MODEL, CRITIC_TEMP)


def select_best(candidates):
    messages = [
        {
            "role": "system",
            "content": "You select the best, correct, and efficient Python code."
        },
        {
            "role": "user",
            "content": f"""
Candidates:
{candidates}

Return ONLY the best code.
"""
        }
    ]

    return call_llm(messages, SELECTOR_MODEL, SELECTOR_TEMP)