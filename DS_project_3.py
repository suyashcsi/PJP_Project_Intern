dict_1 = {'krishna' : [67,68,69] ,'Arjun' : [70,98,63] ,'Malika' : [52,56,60]}

print("krishna , Arjun , Malika")
name = input("Enter Name : ")

sum = 0

#avg = 0

for i in dict_1[name]:

    sum+=i

avg = sum / 3

print("The average of ",name, "is ",avg)
