case_base = [
    {
        "student": "Student 1",
        "errors": ["formula"],
        "feedback": "Review the correct formula before solving the problem.",
        "outcome": "Improved"
    },
    {
        "student": "Student 2",
        "errors": ["arithmetic"],
        "feedback": "Check arithmetic calculations carefully.",
        "outcome": "Improved"
    },
    {
        "student": "Student 3",
        "errors": ["formula", "arithmetic"],
        "feedback": "Review the formula and check your calculations.",
        "outcome": "Improved"
    },
    {
        "student": "Student 4",
        "errors": ["equation"],
        "feedback": "Practice setting up equations correctly.",
        "outcome": "Improved"
    },
    {
        "student": "Student 5",
        "errors": ["formula", "equation"],
        "feedback": "Review the formula and practice translating the problem into an equation.",
        "outcome": "Improved"
    }
]


print("CASE-BASED REASONING")
print("====================")
print("\nExisting Case Base:")

for case in case_base:
    print(case)


def calculate_similarity(new_errors, past_errors):
    matches = 0

    for error in new_errors:
        if error in past_errors:
            matches += 1

    return matches
new_student = {
    "student": "New Student",
    "errors": ["formula", "arithmetic"]
}
print("\nNew Problem:")
print("Student:", new_student["student"])
print("Errors:", new_student["errors"])
best_case = None
best_score = -1

print("\nSimilarity Assessment:")

for case in case_base:

    score = calculate_similarity(
        new_student["errors"],
        case["errors"]
    )

    print(
        case["student"],
        "Similarity Score:",
        score
    )

    if score > best_score:
        best_score = score
        best_case = case
        print("\nRetrieved Similar Case:")
print("Student:", best_case["student"])
print("Similarity Score:", best_score)
print("Previous Feedback:", best_case["feedback"])
def adapt_solution(errors):
    feedback = []

    if "formula" in errors:
        feedback.append(
            "Review the correct formula before solving."
        )

    if "arithmetic" in errors:
        feedback.append(
            "Check your arithmetic calculations carefully."
        )

    if "equation" in errors:
        feedback.append(
            "Practice setting up equations correctly."
        )

    return " ".join(feedback)

final_feedback = adapt_solution(
    new_student["errors"]
)

print("\nAdapted Final Solution:")
print(final_feedback)

new_case = {
    "student": new_student["student"],
    "errors": new_student["errors"],
    "feedback": final_feedback,
    "outcome": "Pending"
}

case_base.append(new_case)

print("\nNew case saved successfully.")

print("\nUpdated Case Base:")

for case in case_base:
    print(case)



