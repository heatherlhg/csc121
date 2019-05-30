d_wins = 0
r_wins = 0
for i in range(5):
    print("Debate", i+1, ":")
    d_pct = float(input("What percentage of people think Democrat's candidate has won? "))
    r_pct = float(input("What percentage of people think Republican's candidate has won? "))
    if d_pct > r_pct + 3:
        print("Democrat's candidate has won this debate")
        d_wins = d_wins + 1
    elif r_pct > d_pct + 3:
        print("Republican's candidate has won this debate")
        r_wins = r_wins + 1
    else:
        print("It is statistically a tie")
    print()

print("Number of debates Democrat's candidate has won:", d_wins)
print("Number of debates Republican's candidate has won:", r_wins)
if d_wins > r_wins:
    print("Democrat's candidate has won more debates than Republican's candidate")
elif d_wins < r_wins:
    print("Republican's candidate has won more debates than Democrat's candidate")
else:
    print("The two candidates have won the same number of debates")
