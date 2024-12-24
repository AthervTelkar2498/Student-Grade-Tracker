class StudentTracker:
    def __init__(self):
        """Initialize the tracker with an empty dictionary to store grades."""
        self.grades = {}

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject.

        Args:
            subject (str): The subject name.
            grade (float): The grade received, must be between 0 and 100.
        """
        try:
            grade = float(grade)  # Convert grade to a float.
            if 0 <= grade <= 100:  # Check if grade is within valid range.
                self.grades[subject] = grade  # Add grade to dictionary.
                print(f"Grade added for {subject}: {grade}")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def calculate_average(self):
        """Calculate the average grade of all subjects.

        Returns:
            float: The average grade, or 0 if no grades are entered.
        """
        if self.grades:  # Check if there are any grades.
            return sum(self.grades.values()) / len(self.grades)  # Calculate average.
        return 0  # Return 0 if no grades.

    def determine_letter_grade(self, average):
        """Determine the letter grade based on the average grade.

        Args:
            average (float): The average grade.

        Returns:
            str: The corresponding letter grade (A-F).
        """
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
        """Calculate GPA on a 4.0 scale based on the average grade.

        Args:
            average (float): The average grade.

        Returns:
            float: The GPA on a 4.0 scale.
        """
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
        """Display the overall report of grades, average, letter grade, and GPA."""
        if not self.grades:  # Check if there are any grades to display.
            print("No grades entered yet.")
            return

        # Calculate statistics.
        average = self.calculate_average()
        letter_grade = self.determine_letter_grade(average)
        gpa = self.calculate_gpa(average)

        # Display the report.
        print("\nStudent Grade Report")
        print("====================")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")
        print(f"\nAverage Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

# Main program
if __name__ == "__main__":
    tracker = StudentTracker()  # Create an instance of StudentTracker.

    while True:
        # Display menu options.
        print("\nStudent Tracker Menu")
        print("1. Add Grade")
        print("2. Display Report")
        print("3. Exit")

        # Get user choice.
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a grade.
            subject = input("Enter the subject: ")
            grade = input("Enter the grade (0-100): ")
            tracker.add_grade(subject, grade)
        elif choice == "2":
            # Display the report.
            tracker.display_report()
        elif choice == "3":
            # Exit the program.
            print("Exiting Student Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

      
      
   
