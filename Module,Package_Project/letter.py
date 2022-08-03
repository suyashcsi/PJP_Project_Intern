string = input("Enter the word : ")
def letter(string):
    for i in string:
        frequency = string.count(i)
        print(str(i) + ": " + str(frequency), end=", ")
        return string




print(letter(string))
