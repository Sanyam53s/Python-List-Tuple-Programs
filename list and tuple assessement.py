"""
li =[21,23,55,535,545,65,23,23]
print(li)
print(li[3])
print(li[-2])
print(li[:4])
print(li[2:4])
print(li[ :])
print(li[  : :-1])
for a in li:
    print(a*24)
print(li*3)
print(sum(li))
print(max(li))
print(len(li))
print(sum(li)//len(li))
for x in range(len(li)):
    print(li[x])
li.append(88)
print(li)
li.insert(1,88)
print(li)
print(li.index(55))

1 # Write a Python program to create a list of integers and print its elements.
li = [ 21,23,45,29,58,54,45]
for a in li:
    print(a)

2 # Write a program to find the sum and average of all elements in a list.
li = [42,49,48,47,45,43]
print(sum(li))
print(sum(li)/len(li))
    
3 # Write a program to find the largest and smallest element in a list.

li = [51,55,17,88,14,99,94]
print(max(li))
print(min(li))

# 4. Write a Python program to count the number of elements in a list without using len().
li = [10, 20, 30, 40, 50, 60]
count = 0
for i in li:
    count += 1
print("Number of elements:", count)

# 5. Write a program to reverse a list without using built-in functions.
li = [45,48,89,78,48,35,253]
print (li[ : :-1])

li = [45, 48, 89, 78, 48, 35, 253]

rev = []

for i in range(len(li)-1, -1, -1):
    rev.append(li[i])

print("Reversed list:", rev)

# 6. Write a program to check if an element exists in a list.
li = [10, 20, 30, 40, 50]

x = int(input("Enter element to search: "))

if x in li:
    print("Element exists in the list.")
else:
    print("Element does NOT exist in the list.")

#7.Write a Python program to remove duplicate elements from a list.
li = [10, 20, 30, 20, 40, 10, 50, 30]

li = list(set(li))

print("List after removing duplicates:", li)

# 8. Write a program to sort a list in ascending and descending order.
li = [100,135,444,524,213,147,459]
print(li)
li.sort()
print("ascending order:",li)
li.sort(reverse= True)
print("descending order:",li)

# 9.Write a program to merge two lists and remove duplicates

Li1 = [1,2,3,4,5,5,6,6,6]
Li2 = [4,5,6,7,8,2,3,9,0]

Merged_list = list(set(Li1+Li2))
print("remove duplicates",Merged_list)



merged_list = []

for item in Li1 + Li2:
    if item not in merged_list:
        merged_list.append(item)

print("Merged list without duplicates:", merged_list)

# 10.Write a program to find common elements between two lists.
Li1 = [1,2,3,4,5,5,6,6,6]
Li2 = [4,5,6,7,8,2,3,9,0]

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = []

for item in Li1:
    if item in Li2:
        common_elements.append(item)

print("Common elements:", common_elements)



# 11. Write a program to split a list into even and odd numbers.
numbers = [12,13,14,15,16,17,18,19,20]
even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)



#  12. Write a program to rotate a list by npositions.
lst = [1, 2, 3, 4, 5]
n = 2

n = n % len(lst)   # handle large n
rotated = lst[-n:] + lst[:-n]

print("Rotated List:", rotated)


# 13. Write a Python program to find the second largest number in a list.
lst = [10, 20, 4, 45, 99]

largest = second = float('-inf')

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest:", second)


lst = [10, 20, 4, 45, 99]

lst.sort()   # ascending order me sort karega

print("Second Largest:", lst[-2])

# 14. Write a program to flatten a nested list.

nested = [[1, 2], [3, 4], [5, 6]]

flattened = []

for sublist in nested:
    for item in sublist:
        flattened.append(item)

print("Flattened List:", flattened)

# 15.Write a program to count frequency of each element in a list.
lst = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for num in lst:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)

# 16. Write a program to replace all negative numbers with zero in a list.
lst = [5, -3, 8, -1, 0, -7]

updated = [x if x >= 0 else 0 for x in lst] # List Comprehension
print(updated)

# 17. Write a program to remove all occurrences of a given element from a list.
lst = [1, 2, 3, 2, 4, 2, 5]
element = 2

result = [x for x in lst if x != element]

print(result)

# 18. Write a program to check if a list is a palindrome.
lst = [1, 2, 3, 2, 1]

if lst == lst[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 19. Write a Python program to find missing numbers in a given list of consecutive integers.
lst = [1, 2, 4, 6, 7]

missing = []

for num in range(min(lst), max(lst)):
    if num not in lst:
        missing.append(num)

print("Missing Numbers:", missing)

# 20.Write a program to perform element-wise addition of two lists.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = [a + b for a, b in zip(list1, list2)]

print(result)

# 21. Write a Python program to find the longest increasing subsequence in a list.
lst = [10, 22, 9, 33, 21, 50, 41, 60]

n = len(lst)
dp = [1] * n

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print("Length of LIS:", max(dp))

# 22. Write a program to group elements based on frequency.
lst = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

grouped = {}

for key, value in freq.items():
    grouped.setdefault(value, []).append(key)

print(grouped)
                        TUPLE
                        

# 1. Write a Python program to create a tuple and print its elements.
t = (1,2,3,4,5,6,7,8,9)
print(tuple(t))

# 2. Write a program to find the length of a tuple.
t = (1,2,3,4,5,6,7,87,)
print(len(t))

# 3. Write a program to find the maximum and minimum element in a tuple.
t = (10, 20, 4, 45, 99)
print (max(t))
print (min(t))

# 4.Write a program to convert a tuple into a list.
t = (1, 2, 3, 45, 6, 76, 868)
li = list(t)
print("Converted List:", li)

# 5. Write a program to check if an element exists in a tuple.

t=(23,34,56,78,98)
element = int(input("element no :"))
if element in t:
    print("element are exist")
else:
    print("element are not exist")
# 6. Write a program to count occurrences of an element in a tuple.
t = (10, 20, 30, 20, 40, 20, 50)

element = 20

occurrences = t.count(element)
# 7. Write a program to slice a tuple and display the result
t = (10, 20, 30, 40, 50, 60, 70)

print(t[:4])     # From start to index 3
print(t[3:])     # From index 3 to end
print(t[-3:])    # Last 3 elements
print(t[::-1])   # Reverse tuple

# 8.Write a program to find repeated elements in a tuple.
t= (22,33,33,44,55,66,66,77,88,22)
repeated = []

for item in t:
    if t.count(item) > 1 and item not in repeated:
        repeated.append(item)

print("Repeated elements:", repeated)

# 9. Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)

merged = t1 + t2

print("Merged Tuple:", merged)

#10. Unpack Tuple into Variables
t = (10, 20, 30)

a, b, c = t

print(a, b, c)

#11. Sort a Tuple
t = (5, 1, 4, 2, 3)

sorted_tuple = tuple(sorted(t))

print("Sorted Tuple:", sorted_tuple)

#12 . Convert List of Tuples into Dictionary
lst = [(1, "A"), (2, "B"), (3, "C")]

result = dict(lst)

print(result)


#13. Find Index of Element in Tuple
t = (10, 20, 30, 40)

index = t.index(30)

print("Index:", index)

#14. Remove Element from Tuple (Indirect Method)
t = (10, 20, 30, 40)

new_tuple = tuple(x for x in t if x != 30)

print("Updated Tuple:", new_tuple)

#15 . Find Common Elements Between Two Tuples
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

common = tuple(set(t1) & set(t2))

print("Common Elements:", common)

#15.  Check if Tuple is Palindrome
t = (1, 2, 3, 2, 1)

if t == t[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#16 . Element with Maximum Frequency
t = (1, 2, 2, 3, 3, 3, 4)

max_freq = 0
max_element = None

for item in t:
    freq = t.count(item)
    if freq > max_freq:
        max_freq = freq
        max_element = item

print("Element with maximum frequency:", max_element)

#17 . Nested Tuple & Access Elements
nested = ((1, 2), (3, 4), (5, 6))

print("First element of first tuple:", nested[0][0])
print("Second element of third tuple:", nested[2][1])

"""



