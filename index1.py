class GradeManager:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject."""
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        """Calculate the average grade."""
        total = 0
        count = 0
        for subject, grades in self.grades.items():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0

    def get_letter_grade(self, average):
        """Convert numerical average to letter grade."""
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(self):
        """Calculate GPA based on average grade."""
        average = self.calculate_average()
        return average / 20  # Assuming GPA is on a scale of 0 to 4

    def display_grades(self):
        """Display all grades."""
        print("Grades:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")

    def display_summary(self):
        """Display a summary of the student's grades."""
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        gpa = self.calculate_gpa()

        print(f"\nOverall Average: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")


def main():
    manager = GradeManager()

    while True:
        print("\nGrade Management System")
        print("1. Add Grade")
        print("2. Display Grades")
        print("3. Display Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            subject = input("Enter the subject name: ")
            try:
                grade = float(input("Enter the grade (0-100): "))
                if 0 <= grade <= 100:
                    manager.add_grade(subject, grade)
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numerical grade.")
        
        elif choice == '2':
            manager.display_grades()
        
        elif choice == '3':
            manager.display_summary()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select from 1-4.")


if __name__ == "__main__":
    main()
