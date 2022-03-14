# Problem 3
# Problem Set due Feb 11, 2022 02:30 +03 - Past due

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# s = 'azcbobobegghakl'
# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.



# Image result for substring definition In other words you can say that beginIndex is inclusive and endIndex is exclusive while getting the substring. For example – "Chaitanya". substring(2,5) would return "ait" . It throws IndexOutOfBoundsException If the beginIndex is less than zero OR beginIndex > endIndex OR endIndex is greater than the length of String.



s = "azcbobobegghakl"

hold = s[0]
compare = s[0]

for i in s[1:]:
    if i >= compare[-1]:
        compare += i
        if len(hold) < len(compare):
            hold = compare
    else:
        compare = i

print("Longest substring in alphabetical order is:",hold)