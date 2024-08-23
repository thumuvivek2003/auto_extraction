import re
a = open("Grades.txt","r")
a = a.readlines()
std =[]
count = -1
for i in range(len(a)):
    if not(("2019" in a[i]) or ("SUBJECT" in a[i]) or ("Note" in a[i]) or ("Rajiv Gandhi" in a[i])):
        if("ID:" in a[i]):
            id = re.findall("S1.....",a[i])
            std.append(id)
        elif("record" in a[i]):
            sno = re.findall(".*th",a[i])
            std.append(sno)
        else:
            grade = a[i][-2:-1]
            std.append(grade)
print(std)
# print(std)

