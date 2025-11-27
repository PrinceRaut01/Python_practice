
#def add(name):
#   print("good morning")
#    print("hlo"+str(name))
#print("go")
#add("world")
#reading files
#read line by line
#file=open("note.txt","r")
#for line in  file:
#    print(line.strip())
#file.close()
#file=open("myfile.txt",'w')
#lines=["hello class\n" ,"welcome to this online"]
#file.writelines(lines)
#file.close()

#readlines() function
#readlines() function
'''file = open("marks.txt", "r")
i = 0
while True:
    i = i + 1
    line = file.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    m4 = int(line.split(",")[3])
file.close()

total = int(m1) + int(m2) + int(m3) + int(m4)
print(total)

file = open("marks.txt", "a")
file.write("total=",total)
file.close()
'''