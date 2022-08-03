vehicle = input("Let's Start! Do you want to travel Press yes or press no ")
if vehicle == "yes":
    print("Ok, Let's choose the vehicle. ")

    num = int(input("How far do you need to travel?(km)"))
    if num < 3:
        print("You should take the bicycle. ")
    elif num < 300:
        print("You should take Motor-cycle. ")
    elif 300<= num <=3000:
        print("You should ride your supercar ")
elif vehicle == "no":
    print("See you soon ! ")
