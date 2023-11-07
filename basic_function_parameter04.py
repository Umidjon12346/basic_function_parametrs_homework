# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
def calculate_average(l):
    a = 0 
    for i in l:
        a+=i 
    return a//len(l) 
print(calculate_average([2,4,6,8]))