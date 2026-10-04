n = 5  # Defines the height of the upper half (number of rows)

# Upper half of the diamond
for i in range(n):
  # Print leading spaces
  print(" " * (n - i - 1), end="")
  if i == 0:
    print("*")
  else:
    # Print the outer border stars with inner spacing
    print("*" + " " * (2 * i - 1) + "*")

# Lower half of the diamond
for i in range(n - 2, -1, -1):
  # Print leading spaces
  print(" " * (n - i - 1), end="")
  if i == 0:
    print("*")
  else:
    # Print the outer border stars with inner spacing
    print("*" + " " * (2 * i - 1) + "*")