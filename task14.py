"""
Task 14
 Reverse the string 'AJCE' and print it using for loop.
"""
a='AJCE'[::-1]
for i in a:
    if i != 'A':
        print(i,end='',flush=True)
    else:
        print(i)
