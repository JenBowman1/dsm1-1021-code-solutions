person = {"first_name": "Jenna","last_name": "Bowman", "hobby": "Swimming"}
print(person)
first_name = person["first_name"]
last_name = person.get("last_name")
middle_name = person.get("middle_name")
print(first_name, middle_name, last_name)
person["job"] = "Teacher"
print(person["job"])
person["hobby"] = "Gaming"
print(person["hobby"])
person.pop("last_name")
print(person)
