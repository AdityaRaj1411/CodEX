from core import run_agent_system

if __name__ == "__main__":
    query = input("Enter your task: ")

    result = run_agent_system(query)

    print("\n===== FINAL BEST CODE =====\n")
    print(result)