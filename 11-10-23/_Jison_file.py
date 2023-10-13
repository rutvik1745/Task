# import json

# #key:value mapping

# student = {
#     "Name" : "Peter",
#     "Roll_no": "0090014",
#     "Grade" : "A",
#     "Age" : 20,
#     "Subject" : ["Computer Graphics","Discrete Mathematics","Data Structure"]

# }


# with open("data.json",'w')as write_file:
#     json.dump(student,write_file)

# import json
# #Key:Value mapping

# student = {
#     "Name" : "Peter",
#     "Roll_no" : "0090014",
#     "Grade" : "A",
#     "Age" : 20
# }
# b = json.dump(student)
# print(b)



# import json
# #Python list conversion to JSON Array
# print(json.dumps(['Welcome', "to","javaTpoint"]))

# #python tuple conversion to JSON Array
# print(json.dumps(("Welcome","to","javatpoint")))

# # Python string conversion to JSON String   
# print(json.dumps("Hello"))  
  
# # Python int conversion to JSON Number   
# print(json.dumps(1234))  
  
# # Python float conversion to JSON Number   
# print(json.dumps(23.572))  
  
# # Boolean conversion to their respective values   
# print(json.dumps(True))  
# print(json.dumps(False))  
  
# # None value to null   
# print(json.dumps(None)) 


# import json
# a = (10,20,30,40,50,60,70)
# print(type(a))
# b=json.dumps(a)
# print(type(json.loads(b)))
# print(type(b))



# import json  
# # Key:value mapping  
# student  = {  
# "Name" : "Peter",  
# "Roll_no" : "0090014",  
# "Grade" : "A",  
# "Age": 20,  
# }  
  
# with open("data.json","w") as write_file:  
#     json.dump(student,write_file)  
  
# with open("data.json", "r") as read_file:  
#     b = json.load(read_file)  
# print(b)  


# import json
# a = ["Mathew","Peter",(10,32.9,80),{"Name":"Tokyo"}]

# #Python object into JSON
# b = json.dumps(a)
# print(type(b))

# #JSON into Python Object
# c=json.loads(b)
# print(c)

# import json
# person = '{"Name": "Andrew","City":"English", "Number":90014, "Age": 23,"Subject": ["Data Structure","Computer Graphics", "Discrete mathematics"]}'  
# per_dict = json.loads(person)
# print(type(per_dict))

# print(json.dumps(per_dict,indent = 5,sort_keys=True))
# print(type(per_dict))

import demjson
a = [{"Name":'Peter',"Age":20,"Subject":"Electronics"}]
print(demjson.encode(a))