

def generate_answer(question):
    # Simple local answer engine for demonstration.
    # Replace this function with an LLM API for AI-generated answers.
    q = question.lower()

    knowledge = {
        "cpu": "CPU stands for Central Processing Unit. It executes instructions and processes data.",
        "ram": "RAM is temporary memory that stores data currently being used by programs.",
        "python": "Python is a beginner-friendly programming language used in AI, automation and web development.",
        "oops": "OOP stands for Object-Oriented Programming. It uses classes and objects to organize code.",
        "html": "HTML stands for HyperText Markup Language. It structures content on web pages.",
        "ai": "Artificial Intelligence enables machines to perform tasks that usually require human intelligence.",
        "prompt engineering": "Prompt engineering is the process of designing instructions to get useful responses from an AI model.",
        "study plan": "Divide your syllabus into small topics, set daily goals, practise questions and revise regularly."
    }

    for keyword, answer in knowledge.items():
        if keyword in q:
            return answer

    return ("I don't have a prepared answer for this question yet. "
            "Please ask about CPU, RAM, Python, OOP, HTML, AI, "
            "prompt engineering or study planning.")


def faq_assistant():
    faqs = {
        "1": ("How should I prepare for exams?",
              "Create a timetable, study important topics, practise questions and revise."),
        "2": ("How can I improve programming?",
              "Practise coding daily, understand the basics and build small projects."),
        "3": ("What is prompt engineering?",
              "It means writing effective instructions for an AI model."),
        "4": ("How do I manage study time?",
              "Set priorities, use short study sessions and take regular breaks."),
        "5": ("How can I make a study plan?",
              "List your subjects, divide topics by day and track your progress.")
    }

    print("\n--- STUDENT FAQ ASSISTANT ---")
    for key, (question, _) in faqs.items():
        print(f"{key}. {question}")

    choice = input("Choose an FAQ number: ").strip()

    if choice in faqs:
        print("\nAnswer:", faqs[choice][1])
    else:
        print("Invalid choice. Please select 1 to 5.")


def main():
    while True:
        print("\n===== STUDY ASSISTANT AGENT =====")
        print("1. Zero-Shot Prompting")
        print("2. Few-Shot Prompting")
        print("3. Role Prompting")
        print("4. Intelligent FAQ Assistant")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3"]:
            question = input("Enter your study question: ")

            if choice == "1":
                print("\n" + zero_shot_prompt(question))
            elif choice == "2":
                print("\n" + few_shot_prompt(question))
            else:
                print("\n" + role_prompt(question))

        elif choice == "4":
            faq_assistant()

        elif choice == "5":
            print("Thank you for using Study Assistant Agent!")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")


if _name_ == "_main_":
    main()