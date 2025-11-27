usage=int(input('enter your units:'))
if(usage<100):
    amount=usage*5

elif (usage>=100 and usage<=300):
    amount= 100*5 + (usage-100)*8

else:
    amount=100*5 + 200*8 + (usage-300)*10

print(f"the amount is :{amount}")