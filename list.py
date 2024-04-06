color=['green','blow','white','red','yellow']
color.append('black')
color.insert(0,'gray')
print(color)
print('After remove ')
color.pop()
color.remove('green')
print("/n")
del color[3]
print(color)
# it use to make list element full clear.
# color.clear()
#now change list item,
color[2]='nabil'



students = ["Sakshi", "Aaditya", "Ritika"]
students2 = {"Yash":18, "Devika":19, "Soham":19}    #only add keys, does not add values
print(students2)
students.extend(students2)
print(students)