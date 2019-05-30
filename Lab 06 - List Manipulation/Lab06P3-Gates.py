# Lab 06 - List Manipulation Problem 3 -
# Heather Gates
# Three figure skaters, Jean, Kayla and Connie, compete in a meet.  Each skater receives 4 scores.  Write a program to do the following.

skaters = ['Jean','Kayla','Connie']

# (a) Ask the user to enter 4 scores for Jean. Store the scores in a list. Display the list.

print('Please enter scores for Jean.')
jean_scores = []
i = 0
while i < 4:
    score = float(input('Score: '))
    if score <= 0:
        print('Error: score must be a positive number.')
        score = float(input('Score: '))
    jean_scores.append(score)
    i = i + 1
print("Jean's Scores: ", jean_scores)

# (b) Ask the user to enter 4 scores for Kayla. Store the scores in a list. Display the list.

print('Please enter scores for Kayla.')
kayla_scores = []
i = 0
while i < 4:
    score = float(input('Score: '))
    if score <= 0:
        print('Error: score must be a positive number.')
        score = float(input('Score: '))
    kayla_scores.append(score)
    i = i + 1
print("Kayla's Scores: ", kayla_scores)

# (c) Ask the user to enter 4 scores for Connie. Store the scores in a list. Display the list.

print('Please enter scores for Connie.')
connie_scores = []
i = 0
while i < 4:
    score = float(input('Score: '))
    if score <= 0:
        print('Error: score must be a positive number.')
        score = float(input('Score: '))
    connie_scores.append(score)
    i = i + 1
print("Connie's Scores: ", connie_scores)

# (d) Create a list to store the three score lists.  This is a list of lists that contains three elements:
# Jean’s score list, Kayla’s score list, Connie’s score list. Display this list of lists.

all_scores = [jean_scores, kayla_scores, connie_scores]
print('All scores: ', all_scores)
for name in range(len(skaters)):
    print(skaters[name],' : ', all_scores[name])

# (e) Use a set of nested for loops to add 1 extra point to every score of every skater in the
# list of lists created in part (d).

for row in range(len(skaters)):
    for col in range(4):
        all_scores[row][col] = all_scores[row][col] + 1

# (f) Display the modified list of lists. Each score should be 1 point higher than before.

print('All scores with extra point:', all_scores)

# (g) For each skater in the list of lists, sort her 4 scores in ascending order.

for name in range(len(skaters)):
    all_scores[name].sort()
    print(skaters[name],' : ', all_scores[name])

#(h) Display the modified list of lists. Each skater’s 4 scores should be in ascending order.
print('All scores with extra point sorted:', all_scores)
