def palindrome_check(word):
    word = word.lower()
    return word == word[::-1]

z=input("Enter the word: ")
if palindrome_check(z):
    print(f" {z} is a palindrome")

else:
    print(f"{z} is not a palindrome")