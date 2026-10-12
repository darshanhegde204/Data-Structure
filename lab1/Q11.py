#Reverse Words: Write a program to accept a sentence and display by reversing words in a sentence. 

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = " ".join(words[::-1])
print("Reversed sentence:", reversed_sentence)