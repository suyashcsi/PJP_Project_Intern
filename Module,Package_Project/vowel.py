def countVowels(string):
    num_vowels=0
    # to count the vowels
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

# take input
string = input('Enter any string: ')

# calling function and display result
print('No of vowels =',countVowels(string))
