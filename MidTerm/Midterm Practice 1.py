# Midterm Practice 1
# Heather Gates

percent_dem = []
percent_rep = []

i = 1
while i <= 3:
    print('Debate:', i)
    dem_percent_in = int(input('Please enter the percentage for Democrat cadidate: '))
    rep_percent_in = int(input('Please enter the percentatge for Republican candidate: '))
    percent_dem.append(dem_percent_in)
    percent_rep.append(rep_percent_in)
    i = i + 1

i = 0
dem_winner = 0
rep_winner = 0
for per in range(len(percent_dem)):
    i = i + 1
    print('Debate', i)
    print("What percentage of people think Democrat's candidate has won?", percent_dem[per])
    print("What percentage of people think Republican's candidate has won?", percent_rep[per])
    if percent_dem[per] > percent_rep[per]:
        ddif = percent_dem[per] - percent_rep[per]
        dem_winner = dem_winner +1
        if ddif <= 3:
            print('It is a tie.')
            dem_winner = dem_winner - 1
        else:
            print('The Democrat candidate won.')
    else:
        rdif = percent_rep[per] - percent_dem[per]
        rep_winner = rep_winner + 1
        if rdif <= 3:
            print('It is a tie.')
            rep_winner = rep_winner - 1
        else:
            print('The Republican candidate won.')

print("Number of debates Democrat's candidate has won:",dem_winner)
print("Number of debates Republican's candidate has won:", rep_winner)

if dem_winner > rep_winner:
    print('The Democrat candidate has won more debates.')
elif rep_winner > dem_winner:
    print('The Republican candidate has won more debates.')
elif rep_winner == dem_winner:
    print('The two candidates have won the same number of debates')
