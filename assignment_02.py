# Question 1 And 2

def calculate_final_grade(scores):
    final_grades = {}

    for student, components in scores.items():
        
        # Calculate weighted average
        assignment_score = components.get("Assignment", 0)
        midterm_score = components.get("Midterm", 0)
        final_exam_score = components.get("Final Exam", 0)

        final_numeric = (assignment_score * 0.3 +
                         midterm_score * 0.3 +
                         final_exam_score * 0.4)

        if final_numeric >= 90:
            letter_grade = 'A'
        elif final_numeric >= 80:
            letter_grade = 'B'
        elif final_numeric >= 70:
            letter_grade = 'C'
        elif final_numeric >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'

        final_grades[student] = letter_grade

    return final_grades


if __name__ == "__main__":
    student_scores = {
        "Alizay": {"Assignment": 85, "Midterm": 78, "Final Exam": 92},
        "Bushra": {"Assignment": 70, "Midterm": 65, "Final Exam": 60},
        "Eman": {"Assignment": 90, "Midterm": 88, "Final Exam": 95},
        "Diana": {"Assignment": 55, "Midterm": 60, "Final Exam": 58}
    }

    final_results = calculate_final_grade(student_scores)

    print("Final Grades:")
    for student, grade in final_results.items():
        print(f"{student}: {grade}")




