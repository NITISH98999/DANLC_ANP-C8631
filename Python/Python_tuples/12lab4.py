# 4.Write a python program and iterate the given tuples
# Input:
# employee1 = ("John Doe", 101, "Human Resources", 60000)
# employee2 = ("Alice Smith", 102, "Marketing", 55000)
# employee3 = ("Bob Johnson", 103, "Engineering", 75000)
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
employ = (employee1,employee2,employee3)
print("Employee Record :  \n")
for i in employ:
    name, employee_id, department, salary = i
    print(f"Name : {name}")
    print(f"Employee ID : {employee_id}")
    print(f"Department : {department}")
    print(f"Salary : ${salary}\n")
