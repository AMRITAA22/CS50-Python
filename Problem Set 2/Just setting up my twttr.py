text = input("Input: ")
vowels = "aeiouAEIOU"
print("Output: ", end="")
for c in text:
    if c not in vowels:
        print(c, end="")
print()
