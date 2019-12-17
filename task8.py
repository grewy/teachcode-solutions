#Print the values from 10 to 20 but skip the value 15 and stop the iteration at value 18

for i in range(10, 21):
    if i == 15:
        continue
    elif i == 18:
        break
    else:
        print(i)
