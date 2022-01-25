# Initializing a dummy list
l = ['a', 'l', 'p', 'h', 'a', 'a', 'p', 'p', 'l', 'e']

print(l)

print('length of the list {} is = {}'.format(l,len(l)))

for i in range(0,5):
    l.append(i+10)

print('list l = {}'.format(l))
print("Enter number of students you want to enter details for:")

n = int(input())

class_list = []

for i in range(0, n):
    student = []

    print("Enter details of {} student as per the below instruction".format(i))

    print("Enter Full name of the {} student".format(i))
    student.append(input())

    print("Enter Roll number of the {} student".format(i))
    student.append(input())

    class_list.append(student)

print("Details of all students are:")
for student in class_list:
    print("student {} details are: {}".format(class_list.index(student), student))


