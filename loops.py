n = int(input("enter any number"))


#while loop
i = 1
while i <=10:
    print(n*i)
    i +=1

#break & continue
i = 1
while i <=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")

#for loop
for i in range(2,10,2):  #range(start?,stop,step?)
    print(i)