"""
Task 16
 Define a function to check whether a number is divisible by 3 or not. Set the default value to 3.
 Pass the value 16 to the function and in the next statement, call the function without any argument.
 Print 'Divisible' if divisible by 3 else print 'Not Divisible'
"""
def divisible3(num=3):
    if num % 3 == 0:
        print('Divisible')
    else:
        print('Not Divisible')

divisible3(16)
divisible3()
