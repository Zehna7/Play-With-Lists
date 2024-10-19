L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List: ", L)

#variable to store the sum of the list
count = 0

#Finding the sum
for i in L:
    count += i

#divide the total elements by the number of elements
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

#Sorting the elements of the list
L.sort()

#Printing the first element
print("Smallest element is: ", L[0])

#Printing the last element
print("Largest element is: ", L[-1])