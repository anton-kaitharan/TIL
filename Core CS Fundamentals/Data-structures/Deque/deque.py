#It supports O(1) time for adding/removing elements from both ends.

from collections import deque

dq = deque([10, 20, 30])


# Add elements to the right
dq.append(40)  

# Add elements to the left
dq.appendleft(5)  

# extend(iterable)
dq.extend([50, 60, 70]) 
print("After extend([50, 60, 70]):", dq)

# extendleft(iterable)
dq.extendleft([0, 5])  
print("After extendleft([0, 5]):", dq)

# remove method
dq.remove(20)
print("After remove(20):", dq)

# Remove elements from the right
dq.pop()

# Remove elements from the left
dq.popleft()  

print("After pop and popleft:", dq)

# clear() - Removes all elements from the deque
dq.clear()  # deque: []
print("After clear():", dq)





# Create a deque
de = deque([10, 20, 30, 40, 50, 20, 30, 20])

# Accessing elements by index
print(de[0])  
print(de[-1]) 

# Finding the length of the deque
print(len(de))

# 1. Counting occurrences of a value
print(de.count(20))  # Occurrences of 20
print(de.count(30))  # Occurrences of 30

# 2. Rotating the deque
de.rotate(2)  # Rotate the deque 2 steps to the right
print(de)

de.rotate(-3)  # Rotate the deque 3 steps to the left
print(de)

# 3. Reversing the deque
de.reverse()  # Reverse the deque
print(de)