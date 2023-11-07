# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels(s):
    d = s.lower()
    a = 0
    for i in d:
        if i in "aeiuo":
            a+=1
    return a 
print(count_vowels("Hello World"))
