import os
List1 = [8, 9, 3, 6, 1, 10]
List1.reverse()
print("Odwrócona koleność listy jest", List1)

List2 = [91,53, 120, 23, 332,32, 53,64,84]
List2.sort()
print("posortowane", List2)

List3 = []
List3 = List1.copy()
print("List3 =", List3)

indexvalue = List2[2:6]
print("wartości:", indexvalue)

marks = [65, 71, 68, 74, 61]

# find sum of all marks 
total_marks = sum(marks)
print(total_marks)

# testuje
print(total_marks)
