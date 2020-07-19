cad = 'looping through a cad using @ while in order to print it'
index = 0
while index < len(cad):
    print(cad[index])
    index = index + 1
    if cad[index] == '@':
        break

aux = 'Could you write a better email than i have written ?'

for item in aux:
    print(item)

array = ['e1','e2','e3','e4']
for it in array:
    print(it)

for i in range(4):
    print(array[i])

for number in range(3, 11, 2):
    print(number)

#doing a dp in oder to use recursive things xd
w, h = 8, 5
dp = [[0 for x in range(w)] for y in range(h)]
dp[0][0] = 1
for l in range(w):
    for r in range(h):
        if l > 0 and r > 0:
            dp[l][r] = dp[l - 1][r - 1] + 1
        else:
            dp[l][r] = 1

print(dp[3][3])