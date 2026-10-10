# Count Substrings: Find all occurrences of substring in a given string. 
mstring = input("Enter the main string: ")
sstring = input("Enter the substring to search for: ")

count = mstring.count(sstring)
print(f"The substring '{sstring}' appears {count} time(s).")
