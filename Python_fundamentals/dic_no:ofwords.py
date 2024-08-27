def count_words(sentence):
    words = sentence.split()
    return len (words)

z=input("enter the sentence ")
x=count_words (z)
print(f"Number of words: {x}")