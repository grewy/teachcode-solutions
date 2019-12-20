"""
 Now let's move on to Type Coercion in Python.
 Coercion happens in the case of binary operations: if you do x+y , and x and y have different types,
 they are coerced into a single type before performing the operation.

 Task 11
 Initialize two numbers with values 10 and 12.506. Add them and print their sum and average. (This is the way how Python handles two datatypes by default).
"""

a, b = 10, 12.506

print(sum([a, b]))
print(sum([a, b])/2)

