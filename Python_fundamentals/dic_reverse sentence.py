def reverse_words(sentence):
    words=sentence.split()
    reversed_words= words[::-1]
    sentence = " ".join(reversed_words)
    print(sentence)

z=input("Enter the sentence")
reverse_words(z)