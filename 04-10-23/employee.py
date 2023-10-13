employee_data = []

def add_employee():
    name = input("Enter a employee name")
    empid = int(input("Enter a employee id"))
    
    emp = {"name":name,
            "empid":empid,
            "salary":salary}
    employee_data.append(emp)
add_employee("rutvik",10,200)
add_employee("Ravi",20,30000)
print(employee_data)