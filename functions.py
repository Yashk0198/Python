#functions

#-------------
def calsum(a,b): #defining function 
    return a + b # giving some output

sum = calsum(2,3) #function call, arguement, input which is the values
print(sum)

#-----------------
def factorial(n):
    fact =1
    for value in range(1,n+1):
        fact *= value 
    return fact
    
a = factorial(4)
print(a)

#-------------
def cal_odeven(n):   
    if (n%2 == 0):
       print("even")
    if (n%2 != 0):
       print("odd")

cal_odeven(6)

#----------------

# recursive functions
#------
def show(n):    
    print(n)
    if(n==0): # base case
        return
    show(n-1)
    
    
show(5)
 #----------------


def cal_sum(n):
    if (n==0):
        return 0   
    return n + cal_sum(n-1) 

print(cal_sum(7))