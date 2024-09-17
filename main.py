# Kommando för att generera slumpmässiga tal
import random


# Generera matematisk fråga baserat på vald operand
def generate_question(operation, operand1, operand2):
    if operation == "multiplikation":
        return f"{operand1} * {operand2}", operand1 * operand2
    elif operation == "division":
        return f"{operand1} // {operand2}", operand1 // operand2
    elif operation == "modulus":
        return f"{operand1} % {operand2}", operand1 % operand2


# Definierar funktion play_round med parametrar
def play_round(question_number, total_questions, question, answer):
    print(f"\nFråga {question_number}: Vad blir {question}?")

    # Loop för att fortsätta fråga användaren tills ett heltal anges
    while True:
        try:
            user_answer = int(input("Ditt svar: "))
            break  # Bryter loopen om giltig input anges
        except ValueError:
            # Om ogiltig input anges, visas felmeddelande
            print("Vänligen skriv in ett heltal!")

    if user_answer == answer:
        doors_left = total_questions - question_number + 1
        print(f"Bra! Du har nu {doors_left} dörrar kvar.")

        if question_number < total_questions:
            # Visa antal dörrar och låt användaren välja en
            print(
                f"Du står framför {doors_left} dörrar, bakom en av de finns det zombies!"
            )

            # Kontrollerar dörrvalet, giltig/ogiltig input
            while True:
                if doors_left > 1:
                    chosen_door = int(
                        input(f"Välj en dörr (1 - {doors_left}): "))
                    if 1 <= chosen_door <= doors_left:
                        break
                    else:
                        print("Vänligen ange ett giltigt dörrnummer.")
                else:
                    # Vinst när det bara finns en dörr kvar
                    print("Grattis, du vann!")
                    return True

            # Kontrollerar om zombies finns bakom dörren
            zombies_door = random.randint(1, doors_left)
            if chosen_door != zombies_door:
                print(f"Tur! Zombiesarna fanns bakom dörr {zombies_door}.")
                return True
            else:
                print(f"Tyvärr, zombies fanns bakom dörr {zombies_door}.")
                return False
        else:
            # Vinst om det är den sista frågan
            print("Grattis, du vann!")
            return True
    else:
        print("Tyvärr så är det fel svar. Du förlorade.")
        return False


# Definierar funktionen play_game för att spela spelet
def play_game():
    #global game_started

    # Användar input operand/tabell
    #if not game_started:
    #    print("Välkommen till spelet Matematik zombies!")
    #    game_started = True

    operation = input("Välj räknesätt (multiplikation, division, modulus): ")

    table = None
    divisor = None

    if operation == "multiplikation":
        table = int(input("Välj tabell (2 - 12): "))
    elif operation == "division" or operation == "modulus":
        while True:
            try:
                divisor = int(input("Välj divisor (2 - 5): "))
                break
            except ValueError:
                print("Vänligen ange ett heltal.")

    # Skapa lista med frågor
    questions = []
    used_questions = set()  # Dublettkontroll

    for _ in range(12):
        while True:
            if operation == "multiplikation":
                operand1 = random.randint(0, 12)
                question, answer = generate_question(operation, operand1,
                                                     table)
            elif operation == "division":
                operand1 = random.randint(0, 12 * divisor)
                question, answer = generate_question(operation, operand1,
                                                     divisor)
            elif operation == "modulus":
                operand1 = random.randint(0, 12 * divisor)
                question, answer = generate_question(operation, operand1,
                                                     divisor)

            # Dublettkontroll
            if question not in used_questions:
                used_questions.add(question)
                questions.append((question, answer))
                break

    # Börja spelet
    for i, (question, answer) in enumerate(questions, 1):
        if not play_round(i, 12, question, answer):
            return False  # Om användaren svarar fel på en fråga avslutas spelet

    print("\nDu svarade rätt på alla frågor och undvek alla zombies!")
    return True


# Huvudprogrammet för att starta spelet/ge användaren alternativ att spela igen
if __name__ == "__main__":
    play_again = "ja"
    #game_started = False  # Håller reda på om spelet har startat
    print("Välkommen till spelet Matematik zombies!")

    while play_again.lower() == "ja":
        play_game()
        play_again = input("Vill du spela igen? (ja/nej): ")

    print("Spelet avslutas. Tack för att du spelade!")
