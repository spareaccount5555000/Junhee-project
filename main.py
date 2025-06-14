#names = {
   #"Hannah" : 23,
   #"Johanna" : 21,
   #"Lionel" : 22,
   #"Jaycas" : 20
#}

#print(names.values())


sample_dict = {
    "name" : "junhee",
    "age" : 12,
    "city" : "Singapore"
}

print(sample_dict["name"])

print(sample_dict)

sample_list = ["Pulkit", 23 , "Agra"]
print(sample_list[0])

print(sample_dict.values())

for key in sample_dict.keys():
   print(key, sample_dict[key])

if "name" in sample_dict:
   print(sample_dict["name"])
else:
   print("key does not exist")


sample_dict["profession"] = "Software Engineer"
print(sample_dict)

del(sample_dict["profession"])
print(sample_dict)

sample_dict["city"] = "Bangalore"
print(sample_dict)

sample_dict["marks"] = [99,87,85,92,90]
print(sample_dict )

x = sample_dict["marks"][1]
print(x)

classroom = {
   "Jaycas" : {
      "age" : 11,
      "marks":[75,79,87,90,85]
   }
   ,"Alex" : {
      "age" : 12,
      "marks" : [90,96,84,79,88]
   }
}

print(classroom.keys())

print(classroom.values())

for i in classroom.keys():
   print(classroom[i])












