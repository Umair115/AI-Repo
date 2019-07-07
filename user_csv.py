import csv
with open("student.csv","a",newline="") as f:
    data_handler = csv.writer(f,delimiter = ",")
    name = input("Enter name of student")
    age = input("Enter age of student")
    rollno = input("Enter rollno of student")
    data_handler.writerow([name,age,rollno])