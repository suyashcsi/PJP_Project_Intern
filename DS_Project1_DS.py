dict_1 = {"Jeff : " : " Is afraid of dogs" , "David : " : " Plays the piano", "Jason : " : " Can fly an aeroplane"}
for k in dict_1:
    v = dict_1[k]
    print(k + str(v))
dict_1["Jeff : "] = " Is afraid of height"
dict_1["Jill : "] = " Can hula dance"
print("**Updated the dictionary**")
for k in dict_1:
    v = dict_1[k]
    print(k + str(v))
