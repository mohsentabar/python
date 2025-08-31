#list
name = "mohsen"
print(name[0])

names = ["mohsen","aysan","Nastaran"]
print (names[0])

names.append("sina")
print(names)
names.sort()
print(names)

#tuple
point = (12.5 , 25)
print (point[0])

#set
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(2)
print(s)

#dict
person = {
    "name" : "aysan",
    "age" : 22 ,
}
print(person)
print(person["age"])