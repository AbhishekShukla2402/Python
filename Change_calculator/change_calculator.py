##### change calculator
import sys
list_of_change = [1,2,5,10,20,50,100]



val2 = int(input("Bill to be paid: "))
val1 = int(input("Payment made: "))


change = val1 - val2

for i in list_of_change:
    if change == i:
        print("Your change: ", i)
        sys.exit()

list_of_change = sorted(list_of_change,reverse=True)

list_of_change1=[]
your_change = []
n=0
while True:
    for i in list_of_change:
        if i<=change:
            list_of_change1.append(i)

    your_change.append(max(list_of_change1))
    change = change - max(list_of_change1)
    list_of_change1=[]
    
    if change == 0:
        break
print("Your change is:")
for i in your_change:
    print("Rs{}".format(i), end="  ")
    
    
