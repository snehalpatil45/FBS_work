# Enter number of students from user .for those many students accept marks of 5 subject marks from user and calculate percentage.display all
# percentage and average percentage of students.

num = int(input('Enter number of students:'))
total = 0
for i in range(1,num+1):
    print('student',i)
    s1 = int(input('Enter marks of subject 1:'))
    s2 = int(input('Enter marks of subject 2:'))
    s3 = int(input('Enter marks of subject 3:'))
    s4 = int(input('Enter marks of subject 4:'))
    s5 = int(input('Enter marks of subject 5:'))
    percentage = (s1+s2+s3+s4+s5)/5
    print(f'percentage of student is {percentage}')
    total = total+ percentage 
average = total/num
print(f'Average percentage of student is {average}')