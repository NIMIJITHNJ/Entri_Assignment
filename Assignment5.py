Sample1 = [7,9,6,3,0,4,1,4]         # Creating a sample list
Sample2 = [9,3,5,6,2,7,1]           # Creating another sample
print(Sample1)
print(Sample2)

#   append()	Adds an element at the end of the list
Sample1.append(5)
print(Sample1)  

#   clear()	Removes all the elements from the list
Sample2.clear()
print(Sample2)

#   copy()	Returns a copy of the list
Copy_Sample1 = Sample1.copy()
print(Copy_Sample1)

#   count()	Returns the number of elements with the specified value
countof_Sample1 = Sample1.count(4)
print(countof_Sample1)

#   extend() Add the elements of a list (or any iterable), to the end of the current list
Sample2.extend([4,9,6,1])
Sample1.extend([3,5])
print(Sample1,Sample2)

#   index()	Returns the index of the first element with the specified value
indexof_1 = Sample1.index(1)    # Index of 1 in the list Sample1
print(indexof_1)
indexof_1 = Sample2.index(1)    # Index of 1 in the list Sample2
print(indexof_1)

#   insert() Adds an element at the specified position
Sample2.insert(1,7)             # 7 will be inserted at index 1 in Sample2
print(Sample2)

#   pop() Removes the element at the specified position
Sample2.pop(3)                  # Removes the element 6 at index 3 in Sample2
print(Sample2)

#   remove() Removes the first item with the specified value
Sample1.remove(3)               # Removes the element 3 from Sample1
print(Sample1)
Sample1.remove(4)               # Removes the element 4 from its first occurance in the Sample1 
print(Sample1)

#   reverse() Reverses the order of the list
Sample1.reverse()
print(Sample1)

#   sort() Sorts the list
Sample1.sort()
print(Sample1)