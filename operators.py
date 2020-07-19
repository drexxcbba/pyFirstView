band = False

if band:
    print('the flag is on')
else:
    print('the flag is off')

aux = input('get flag: ')

if bool(aux):
    print('yes')
elif band:
    print('no, okey this not work xd')

band1 = False
band2 = True

if band1 and band2:
    print('both on')
#elif band1 or band2:
#  print('one is on')
elif band1 and not band2:
    print('the first one is on')
elif band2 and not band1:
    print('the second one is on')
else:
    print('both off')

temp = 41

if temp <= 25 and temp > 10:
    print('this will be a nice day')
elif temp > 40:
    print('this will be a horrible day to have a day in the beach')

lucky = "sss"

if len(lucky) == 3:
    print('you have a lucky cad')