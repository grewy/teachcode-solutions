"""
Rahul scores 90, 85,70, 75, 80 in his exams. The grading criteria for an exam is given below(based on average):
 A+ => 91 -100
 A => 81-90
 B => 71-80
 C => 61- 70
 D => 51- 60
 F => 50 & Less than 50.
 Calculate and print his average as well as the grade.
"""

scores = [90, 85, 70, 75, 80]
avg = sum(scores) / len(scores)
print(avg)

if avg <= 50:
    print('F')
elif avg > 50 and avg < 61:
    print('D')
elif avg > 60 and avg < 71:
    print('C')
elif avg > 70 and avg < 81:
    print('B')
elif avg > 80 and avg < 91:
    print('A')
else:
    print('A+')
