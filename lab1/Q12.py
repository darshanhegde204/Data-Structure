#Find longest and shortest words: Write a program to accept a sentence and find the longest and shortest word in a sentence.  
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
shortest_word = min(words, key=len)
print(f"Longest word: {longest_word} (Length: {len(longest_word)})")
print(f"Shortest word: {shortest_word} (Length: {len(shortest_word)})")