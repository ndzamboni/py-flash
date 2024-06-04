import random

class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

class FlashcardApp:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, front, back):
        flashcard = Flashcard(front, back)
        self.flashcards.append(flashcard)

    def review_flashcards(self):
        if not self.flashcards:
            print("No flashcards found.")
            return
        for flashcard in self.flashcards:
            input("Press Enter to reveal the back of the flashcard.")
            print(f"Front: {flashcard.front}")
            print(f"Back: {flashcard.back}")

    def quiz(self):
        if not self.flashcards:
            print("No flashcards found.")
            return
        random_flashcard = random.choice(self.flashcards)
        input("Press Enter to reveal the front of the flashcard.")
        print(f"Front: {random_flashcard.front}")
        guess = input("What is the concept or example? ").strip().lower()
        if guess.lower() == random_flashcard.back.lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {random_flashcard.back}")

def main():
    flashcard_app = FlashcardApp()
    flashcard_app.add_flashcard("What is a variable?", "A variable is a named storage location in memory.")
    flashcard_app.add_flashcard("What is a for loop?", "A for loop is used for iterating over a sequence (list, tuple, dictionary, etc.).")
    flashcard_app.add_flashcard("What is a function?", "A function is a block of reusable code that performs a specific task.")

    while True:
        print("\nFlashcard App Menu:")
        print("1. Review Flashcards")
        print("2. Quiz Yourself")
        print("3. Add Flashcard")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            flashcard_app.review_flashcards()
        elif choice == '2':
            flashcard_app.quiz()
        elif choice == '3':
            front = input("Enter the front side of the flashcard: ")
            back = input("Enter the back side of the flashcard: ")
            flashcard_app.add_flashcard(front, back)
            print("Flashcard added successfully!")
        elif choice == '4':
            print("Exiting Flashcard App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
