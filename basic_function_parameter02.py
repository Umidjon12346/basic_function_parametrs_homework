# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.
def calculate_sum(lst):
    a = 0
    for i in lst:
        a+=i
    return a 
print(calculate_sum([2,4,6,8]))
