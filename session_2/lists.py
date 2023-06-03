# Store multiple data points, that take different data types

list_name = ["Asli", 1, 4.5, []] # list can take different data types: strings, integer, float, other lists

digits = [1, 2, 3, 4, 5] #it makes sense to store similar data types together
print(list_name)
print(type(list_name))
# Lists are index based which starts from 0.
print(digits[4])
# if we say print(digits[5]), which does not exist, it'll give an error "Index error: list index out of range"
print(digits[-1]) #gives very last element. print(digits[-2]) give the secon from the last element


# Slicing a list
print(digits[0:4]) #start (inclusive) and End index (exclusive)
print(digits[3:]) #will print everything starting with fourth element
print (digits[-2:-1])
print(digits[-2:5]) #index5 doesn't exist, but it won't be an error


print(digits[0:5:2]) #last digit means "extract", now it means we skip every second in between when we are printing


print(len(digits)) #shows the length of the list


digits.append(6)  #whatever i put will be added to the list
print(digits)


digits.pop() #removes the last item added
print(digits)

digits.pop(0)
print(digits)

popped_element = digits.pop(0) #we can save this removed item and use it somewhere else
print(popped_element)

digits[1] = 90 #change the element number 1 in the list
print(digits)

letters = ['a', 'b', 'c', 'd', ['Emily', 'Julie']] # a list of strings with an inner list (as an element)
print(letters[4][0]) #if we want to get an element from the nested list

# or we can do this:

outer_list = letters[4]
print(outer_list[0])

#checking if an element exists in a list
if 'a' in letters:
    print("It is in the list")
