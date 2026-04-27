# Create a python script that will check if a particular string is a palindrome or not. (Reads the same forwards and backwards). You can either pass the string as an argument or ask for user input.

def palindrome(word: str):

    w = "".join(word.split()).lower()

    return  w == w[::-1]


if __name__ == "__main__":
    print(palindrome("heart")) # False
    print(palindrome("racecar")) # True
    print(palindrome("civic")) # True
    print(palindrome("miffy"))  # False
    print(palindrome("Hannah"))  # True
    print(palindrome("please"))  # False
