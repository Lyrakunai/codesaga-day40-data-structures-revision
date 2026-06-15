# Codesaga Day 40
# Mini Challenge

user = {
    "name": "Nainu",
    "email": "nainu@gmail.com",
    "skills": {"Python", "AI", "ML"},
    "completed_courses": {"Python Basics", "C Basics", "Java Basics"},
    "quiz_scores": [19, 84, 6, 92, 33]
}
print("User Details")
print(user)

total = 0
for score in user["quiz_scores"]:
    total += score
average = total / len(user["quiz_scores"])
print("Total Score:", total)
print("Average Score:", average)