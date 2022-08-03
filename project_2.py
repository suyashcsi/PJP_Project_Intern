monthdays = int(input("Enter Month Days either 30 0r 31 : "))
permonth1 = 31*24*0.51
permonth2 = 30*24*0.51
totaldays = ((918/0.51)/367)




perhourcost = 0.51

perdaycost = 24*0.51

print("Total cost per day: ", perdaycost)

perweek = 7*24*0.51

print("Total cost per week: ", perweek)


if(monthdays==31):

    print("Total cost permonth of 31 days : ", permonth1)
    print("Total days I can operate at $918 :", totaldays)

if(monthdays==30):

    print("Total cost permonth of 30 days: ", permonth2)
    print("Total days I can operate at $918 :", totaldays)
