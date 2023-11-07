# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest(lst):
    a = lst[0]
    for i in lst:
        if i<a:
          a = i 
    return a
print(find_smallest([12,1,3,4,5]))