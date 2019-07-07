import csv

with open("student.csv","w",newline="") as f:
    data_handler = csv.writer(f,delimiter = ",")
    data_handler.writerow(["Name","Age","RollNo"])
    data_handler.writerow(["Umair","22","057"])
    data_handler.writerow(["Ammar","22","055"])
    data_handler.writerow(["Abdullah","20","060"])

with open("student.csv","r") as f:
    data_handler = csv.reader(f)
    for data in data_handler:
        # print(data)
        if data[0] == "Ammar":
            print("Yes the person is in the list")
        else:
            print("Person is not in the list")
    
