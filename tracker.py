class StudentTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject."""
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                self.grades[subject] = grade
                print(f"Grade added for {subject}: {grade}")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def calculate_average(self):
        """Calculate the average grade."""
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0

    def determine_letter_grade(self, average):
        """Determine the letter grade based on the average."""
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def calculate_gpa(self, average):
        """Calculate GPA on a 4.0 scale."""
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_report(self):
        """Display the overall report."""
        if not self.grades:
            print("No grades entered yet.")
            return

        average = self.calculate_average()
        letter_grade = self.determine_letter_grade(average)
        gpa = self.calculate_gpa(average)

        print("\nStudent Grade Report")
        print("====================")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")
        print(f"\nAverage Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

# Main program
if __name__ == "__main__":
    tracker = StudentTracker()

    while True:
        print("\nStudent Tracker Menu")
        print("1. Add Grade")
        print("2. Display Report")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            subject = input("Enter the subject: ")
            grade = input("Enter the grade (0-100): ")
            tracker.add_grade(subject, grade)
        elif choice == "2":
            tracker.display_report()
        elif choice == "3":
            print("Exiting Student Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
