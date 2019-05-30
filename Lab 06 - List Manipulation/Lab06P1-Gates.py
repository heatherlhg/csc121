#Lab 06 - List Manipulation Problem 1 - Edit Student Test Scores
#Heather Gates


# input 5 test scores into a list. Display list
orig_scores = []
i = 0
while i < 5:
    score = float(input('Please enter a test score: '))
    orig_scores.append(score)
    i = i + 1
print("Original Test Scores: ", orig_scores)

print('Students who score below 60 get 10 point adjustment')
# Copy scores into a new list
new_scores  = orig_scores.copy()

# Add 10 to scores below 60
i = 0
while i < len(new_scores):
    if new_scores[i] < 60:
        new_scores[i] = new_scores[i] + 10
    i = i + 1

# Display the new list
print('Adjusted Test Scores: ', new_scores)

# compare scores from both lists. If score was changed, display both old and new scores.
print('Grades that were changed:')
i=0
for i in range(0,5):
    if orig_scores[i] < new_scores[i]:
        print('Original Score:',orig_scores[i], ' New Score: ', new_scores[i])
