# Codesaga Day 40
# Data Structures Revision

# List
quiz_scores = [80, 90, 70, 60]
quiz_scores.append(100)
print("Quiz Scores:", quiz_scores)

# Tuple
location = (25.6, 85.1)
print("Location:", location)

# Set
skills = {"Python", "AI", "ML"}
skills.add("Data Science")
print("Skills:", skills)

# Dictionary
user = {
    "name": "Nainu",
    "email": "nainu@gmail.com",
    "skills": skills,
    "scores": quiz_scores
}
print("User Profile:")
print(user)

# Average Score
total = 0
for score in quiz_scores:
    total += score
average = total / len(quiz_scores)
print("Average Score:", average)