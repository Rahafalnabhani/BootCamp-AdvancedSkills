# Filters
#IF i have a list of number want to check only the even numbers
# Taking the even numbers list and making it in another even list

def is_even(L):
    evenList = []
    for num in L:
        if num%2 == 0: #even
            evenList.append(num)
        return evenList
numbers = [10,2,3,14,17,29,19,18,22,26]
evens = is_even(numbers)
print("Number: " ,numbers)
print ("Even Numbers : " ,evens)


# Using the Filters

#evenUsingFilter = filter(lambda n : n%2 == 0 , numbers)
evenUsingFilter = list(filter(lambda n : n%2 == 0 , numbers))
print("Filtered even: ",evenUsingFilter)