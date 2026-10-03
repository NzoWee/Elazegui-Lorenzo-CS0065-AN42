facts = {
    "temperature": 32,
    "person_present": True,
    "window_open": False,
    "fan_on": False,
    "room_occupied": True
}

print("KNOWLEDGE REPRESENTATION")
print("========================")

print("Knowledge Base:")

for category, value in facts.items():
    print(category, ":", value)

def rule_hot(facts):
    if facts["temperature"] > 30:
        return "Turn on the fan"

def rule_cold(facts):
    if facts["temperature"] < 20:
        return "Turn off the fan"

def rule_empty(facts):
    if not facts["person_present"]:
        return "Turn off the fan"

def inference_engine(facts):
    actions = []

    rules = [
        rule_hot,
        rule_cold,
        rule_empty
    ]

    for rule in rules:
        result = rule(facts)

        if result:
            actions.append(result)

    return actions

actions = inference_engine(facts)

print("\nRULE-BASED REASONING ACTIONS")
print("============================")

for action in actions:
    print("-", action)



case_base = [
    {
        "problem": {
            "temperature": 32,
            "person_present": True
        },
        "solution": "Turn on the fan"
    },
    {
        "problem": {
            "temperature": 28,
            "person_present": True
        },
        "solution": "Keep the fan off"
    },
    {
        "problem": {
            "temperature": 35,
            "person_present": True
        },
        "solution": "Turn on the fan"
    },
    {
        "problem": {
            "temperature": 18,
            "person_present": True
        },
        "solution": "Turn off the fan"
    },
    {
        "problem": {
            "temperature": 32,
            "person_present": False
        },
        "solution": "Turn off the fan"
    }
]



new_problem = {
    "temperature": 32,
    "person_present": True
}

def calculate_similarity(new_problem, past_problem):
    score = 0

    if new_problem["temperature"] == past_problem["temperature"]:
        score += 1

    if new_problem["person_present"] == past_problem["person_present"]:
        score += 1

    return score

best_case = None
best_score = -1

print("\nCASE-BASED REASONING")
print("====================")

print("\nNew Problem:")
print(new_problem)

print("\nSimilarity Assessment:")

for case in case_base:
    score = calculate_similarity(
        new_problem,
        case["problem"]
    )

    print("Similarity Score:", score)

    if score > best_score:
        best_score = score
        best_case = case

print("\nRetrieved Similar Case:")
print("Similarity Score:", best_score)
print("Previous Solution:", best_case["solution"])

reused_solution = best_case["solution"]

print("\nReused Solution:")
print(reused_solution)

revised_solution = reused_solution

print("\nRevised Solution:")
print(revised_solution)

new_case = {
    "problem": new_problem,
    "solution": revised_solution
}

case_base.append(new_case)

print("\nNew case saved successfully.")

print("\nUpdated Case Base:")

for case in case_base:
    print(case)

