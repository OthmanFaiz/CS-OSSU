# Problem 1
# Problem Set due Feb 11, 2022 02:30 +03 - Past due

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

s = 'azcbobobegghakl'
v = "aeiou"
count = 0

for vo in s:
    if vo in v:
        count += 1


print("Number of vowels:", count)