ids = open("extract.txt","r")
txt = ids.read().split(",")
print(type(txt))

# count = 0
# for i in txt:
#     print(i,end='')
#     count+=1
# print("Total count : ",count)   
    
ids.close()