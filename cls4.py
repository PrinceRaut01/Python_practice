#for i in range (5):
#   print("hlo  world")
#   print("hlo  world2")
#a=  [10,40,'prince',5.6]
#for item in a:
#   print(item, end=" ")
#st = "programming"
#n=len(st)
#for  i in range(n):
# print(st,'='n)
#st = "programming"
#for i in st:
#   print(i)
#else:
#   print("else part")
#for i in range(5):
#    name=input('enter your name:')
#    print(f" This is parent loop called by {name}",i)
#    for  j in range(3):
#        print(name,j)
#print("bye")
#for i in range(5):
#if (i==5):
 #  break
#else:
 #   print("else part")
#print("rest of the code")
#list=[11,5,17,18,23]
#s=0
#for i in range(0,len(list)):

#    s=s+ list[i]
#print(f"the total sum is {s}")
#i=1
#while i<3:
#    print("the value of i is :",i)
#    i+=1
#    j=1
#    while j<=5:
#        print("you are ",j)
#        j+=1
#print ("loop ended")
#a=int(input('enter your number:'))
#b=10
#while b>=1:
#    product= a * b
#    print(f"{a}x{b}={product}")
#    b-=1
#a=int(input('enter your number:'))
#b=1
#while b<=10:
#    product= a * b
#    print(f"{a}x{b}={product}")
#    b+=1
#ta,2,3,4,'prince','aayush']
#ata2=[980,960,7965]
#ata2.extend(data2)
#rint(data2)
#data=(4,45,67,89,["prince","rahul",7,4])
#print(data)
#data[4][0]=100
#print(data)
#data[4].remove(100)
#print(data)
#data={1,'c'}
#data2={'hello data2 here ','c'}
#data.add(0)
#data.pop()
#print(data)
#data.update(data2)
#print(data)
#data.remove
#print(type(data))
#data.clear()
#print(data)
#data={'name':"Prince",'age':24,'city':"janakpur"}
#print(data["name"])
#print("hi",data["name"],"your age is",data["age"],"and you are from",data["city"])
#a_dict ={"a":1,"b":2,"c":3}

#new_key = "A"
#old_key  ="a"
#a_dict[new_key] = a_dict.pop(old_key)
#print(a_dict)
a=int(input('enter your number a:'))
b=int(input('enter your numberb:'))
def add():
    c=a+b
    print("sum of two number is",c)
add()

def pag():
    x=int(input('enter your number x:'))
    y=int(input('enter your number y:'))
    mul=x/y
    print("hi",mul)
pag()

def page(k,r):
    m=k-r
    print("hi",m)
page(4,2)

def hlo(y):
    x=10
    return x+y
sum= hlo(20)
print(sum)
