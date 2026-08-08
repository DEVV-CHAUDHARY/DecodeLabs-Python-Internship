# Project 4 - The General Knowledge Quiz
# DecodeLabs - Python Programming Industrial Training
# Batch: 2026

def ask_question(question, correct_answer, question_number):
    print(f"\nQuestion {question_number}: {question}")
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == correct_answer:
        print("Correct! +1 point")
        return 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer.title()}.")
        return 0


def main():
    print("=" * 50)
    print("       GENERAL KNOWLEDGE QUIZ")
    print("=" * 50)
    print("Answer all 3 questions. Each correct answer = +1 point.")

    score = 0

    score += ask_question(
        "What is the capital of France?",
        "paris",
        1
    )

    score += ask_question(
        "Which planet is known as the Red Planet?",
        "mars",
        2
    )

    score += ask_question(
        "What is the largest ocean on Earth?",
        "pacific ocean",
        3
    )

    print("\n" + "=" * 50)
    print(f"FINAL SCORE: {score}/3")

    if score == 3:
        print("Excellent! You got all answers correct.")
    elif score == 2:
        print("Great job! You got most answers correct.")
    elif score == 1:
        print("Good attempt! Keep learning.")
    else:
        print("Keep practicing. You can do better next time!")

    print("=" * 50)


if __name__ == "__main__":
    main()
