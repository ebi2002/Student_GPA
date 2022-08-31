x = int(input("enter the number of student: "))

name = []
lesson1 = []
lesson2 = []
lesson3 = []
Avg_list = []
whole_lessons = []
class_avg = 0

for i in range(x):
    n = input("your name: ")
    name.append(n)
    s1 = float(input("first score: "))
    lesson1.append(s1)
    s2 = float(input("second score: "))
    lesson2.append(s2)
    s3 = float(input("third score: "))
    lesson3.append(s3)
    lessons = [s1, s2, s3]

    whole_lessons.append(lessons)

    if s1 > s2 and s1 > s3:
        print(f"{n} best score is {s1} in lesson1")
    elif s2 > s1 and s2 > s3:
        print(f"{n} best score is {s2} in lesson2")
    else:
        print(f"{n} best score is {s3} in lesson3")

    total = s1 + s2 + s3
    class_avg = class_avg + total
    Avg = (s1 + s2 + s3) / 3
    Avg = int(Avg * 100) / 100
    Avg_list.append(Avg)
    print(f"{n} average is:{Avg}")

    print("_" * 50)

whole_class = class_avg / len(lesson1 + lesson2 + lesson3)
whole_class = int(whole_class * 100) / 100
print("whole class average is:", whole_class)

'''
if Avg_list[0] > Avg_list[1] and Avg_list[0] > Avg_list[2]:
    print(f"{name[0]} is the best student!!")
elif Avg_list[1] > Avg_list[0] and Avg_list[1] > Avg_list[2]:
    print(f"{name[1]} is the best student!!")
else:
    print(f"{name[2]} is the best student!!")
    
    
'''