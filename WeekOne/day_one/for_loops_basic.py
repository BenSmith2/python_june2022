for i in range(0,150+1):
    print(i)

for i in range(5,1000+1):
    if (i % 5 == 0):
        print(i)

for i in range(1,100+1):
    if (i % 10 == 0):
        print('Coding Dojo')
    elif (i % 5 == 0):
        print('Coding')
    else:
        print(i)

for i in range(2018, 0-1, -4):
    print(i)

lowNum = 3
highNum = 30
mult = 3
# print(lowNum,highNum,mult)
for i in range(lowNum,highNum+1):
    if (i % mult == 0):
        print(i)