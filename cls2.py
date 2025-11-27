age=int(input('enter your age:'))
if(age==12):
    print("you are child go for free")


elif (age>=12 and age<=60):
    membership = input('DO You membership yes or no :')
    if (membership=="yes"):
        print("go a head in RS.150")
    else:
        print("Ticket rate is 200")

else:
    print("you are senior citizen Ticket rate is 100")