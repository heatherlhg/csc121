string = input('Please type a sequence of characters (letters, numbers, special characters): ')
string = string.upper()

# creating a count list and iterating a comparison through an alphabet list
alphaCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

s = 0
j = 0
ch = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for k in ch: # iterate through alphabet
    for letter in string:
        if letter == ch[j]:
            s = s + k.count(ch[j])
            alphaCount[j] = s
    j = j + 1 # move to next letter (list item)
    s = 0 # reset alpha counter for next letter

j = 0
for k in alphaCount:
    if alphaCount[j] != 0:
        print(ch[j],'-', alphaCount[j])
    j = j + 1

print('\n')
