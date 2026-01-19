# Color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print("Welcome to the Quizineer App!")
print("This quiz covers Physics, Thermodynamics, and Basic ECE concepts.")
print("Answer the questions by typing A, B, C, D, or E.\n")

def start_quiz():
    total_score = 0
    section_scores = {"Physics": 0, "Thermodynamics": 0, "ECE": 0}

    questions = [
        # Physics
        {
            "section": "Physics",
            "question": "1. Which of the following is a vector quantity?",
            "choices": ["A. Speed", "B. Distance", "C. Velocity", "D. Time", "E. Temperature"],
            "answer": "C",
            "explanation": "Velocity has both magnitude and direction, making it a vector."
        },
        {
            "section": "Physics",
            "question": "2. The force that resists motion between two surfaces is called?",
            "choices": ["A. Gravity", "B. Friction", "C. Tension", "D. Voltage", "E. Current"],
            "answer": "B",
            "explanation": "Friction resists motion between surfaces in contact."
        },
        {
            "section": "Physics",
            "question": "3. Work done is calculated by which formula?",
            "choices": ["A. Work = Force / Distance", "B. Work = Force x Distance", "C. Work = Mass x Velocity",
                        "D. Work = Force + Distance", "E. Work = Power x Time"],
            "answer": "B",
            "explanation": "Work is calculated as force multiplied by distance."
        },
        {
            "section": "Physics",
            "question": "4. Which law explains why a hot cup of coffee cools down in a cooler room?",
            "choices": ["A. Newton's Law of Cooling", "B. Boyle's Law", "C. Ohm's Law", "D. Pascal's Law", "E. Hooke's Law"],
            "answer": "A",
            "explanation": "Heat flows from hot to cold objects; described by Newton's Law of Cooling."
        },
        # Thermodynamics
        {
            "section": "Thermodynamics",
            "question": "5. Which law states that energy cannot be created or destroyed?",
            "choices": ["A. Newton's Second Law", "B. First Law of Thermodynamics", "C. Boyle's Law",
                        "D. Ohm's Law", "E. Hooke's Law"],
            "answer": "B",
            "explanation": "The First Law of Thermodynamics describes conservation of energy."
        },
        {
            "section": "Thermodynamics",
            "question": "6. When the volume of a gas is constant, increasing temperature will:",
            "choices": ["A. Decrease pressure", "B. Increase pressure", "C. Keep pressure same", "D. Reduce particle mass", "E. Change gas type"],
            "answer": "B",
            "explanation": "Pressure increases with temperature if volume is constant (Gay-Lussac's Law)."
        },
        {
            "section": "Thermodynamics",
            "question": "7. In thermodynamics, entropy is best described as:",
            "choices": ["A. Energy per unit mass", "B. Measure of disorder", "C. Heat capacity", "D. Internal energy", "E. Work done"],
            "answer": "B",
            "explanation": "Entropy measures disorder or randomness of a system."
        },
        # ECE
        {
            "section": "ECE",
            "question": "8. What is the SI unit of electric current?",
            "choices": ["A. Volt", "B. Ohm", "C. Ampere", "D. Watt", "E. Coulomb"],
            "answer": "C",
            "explanation": "Electric current is measured in amperes."
        },
        {
            "section": "ECE",
            "question": "9. Which component is used to limit current in a circuit?",
            "choices": ["A. Battery", "B. Resistor", "C. Switch", "D. LED", "E. Capacitor"],
            "answer": "B",
            "explanation": "A resistor limits the flow of electric current."
        },
        {
            "section": "ECE",
            "question": "10. Which device converts electrical energy into light?",
            "choices": ["A. Resistor", "B. Motor", "C. LED", "D. Capacitor", "E. Inductor"],
            "answer": "C",
            "explanation": "LED converts electrical energy into light energy."
        }
    ]

    for q in questions:
        print(f"\n[{q['section']}] {q['question']}")
        for choice in q["choices"]:
            print(choice)

        user_answer = input("Your answer: ")
        if user_answer.upper() == q["answer"]:
            print(f"{GREEN}Correct!{RESET}")
            total_score += 1
            section_scores[q["section"]] += 1
        else:
            print(f"{RED}Incorrect.{RESET}")
            print("Explanation:", q["explanation"])

    # Calculate percentage
    percentage = (total_score / len(questions)) * 100
    print("\nQuiz finished!")
    print(f"Your final score: {total_score} out of {len(questions)} ({percentage:.1f}%)")

    # Overall performance comment
    if percentage == 100:
        print(f"{GREEN}🏆 Excellent! You got all questions correct!{RESET}")
    elif percentage >= 70:
        print(f"{YELLOW}👍 Good job! You understand most concepts.{RESET}")
    else:
        print(f"{RED}⚠ Keep studying! Review concepts in each section.{RESET}")

    # Section performance
    print("\nSection Scores:")
    for section, score_sec in section_scores.items():
        total_sec = len([q for q in questions if q["section"] == section])
        pct_sec = (score_sec / total_sec) * 100
        color = GREEN if pct_sec >= 70 else RED
        print(f"{section}: {score_sec}/{total_sec} ({pct_sec:.1f}%)", end="")
        if pct_sec < 70:
            print(f" {RED}→ Review needed{RESET}")
        else:
            print(f" {GREEN}→ Good{RESET}")

# Main loop to allow retry
while True:
    start_quiz()
    retry = input("\nDo you want to retry the quiz? (yes/no): ")
    if retry.lower() != "yes":
        print("Thank you for playing the Quizineer App!")
        break

