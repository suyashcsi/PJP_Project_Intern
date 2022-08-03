def isPalindrome(s):  #user-defined function
    return s == s[::-1]

# take inputs
string = input('Enter the string: ')

# calling function and display result
reverse = isPalindrome(string)
if reverse:
    print(string,'is a Palindrome')
else:
    print(string,'is not a Palindrome')
