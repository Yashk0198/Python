#class is a blueprint for creating objects.

#creating class
# class Student:
#     name = "karan kumar"

# #creating object (instance)

# s1 = Student()
# print(s1.name)

#------------
# class Student:
#     school_name = "ABC school" #class attribute

#     #default constructor
#     def __init__(self):
#         pass

#     #parametarize constructor
#     def __init__(self,fullname):  #we should always pass self in constructor.
#         self.name = fullname # self is nothing but s1. object attribute
#         print("calling init")

# s1 = Student("karan") #passing karan as fullname . bracktes after student is the constructor.
# print(s1.name)

# print(Student.school_name)

#-----------------------
# class Student:

#     #parametarize constructor
#     def __init__(self,name, marks):  #we should always pass self in constructor.
#         self.name = name # self is nothing but s1. object attribute
#         self.marks = marks

    
#     def welcome(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("karan") #passing karan as fullname . bracktes after student is the constructor.
# print(s1.name)

# s1.welcome()
# print(s1.get_marks())

#---------------------

# class Student:

#     @staticmethod  #decorator
#     def college():
#         print(" ABC college") 

#-----------------

# class Account:
#     def __init__(self, bal, acc):
#         self.bal = bal
#         self.acc = acc
    
#     def debit(self,amount):
#         self.bal += amount
#         print("total balance", self.get_bal())

#     def credit(self,amount):
#         self.bal += amount
#         print("total balance", self.get_bal())

#     def get_bal(self):
#         return self.bal
    

# acc1 = Account(1000, 123456)

# acc1.debit(400)

# acc1.credit(500)

#---------------      

# class Account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # private attribute

#     def get_accpass(self):
#         print("acc_pass", self.__acc_pass)

# acc1 = Account("123","4638")
# # print(acc1.__acc_pass) #not accessible

# print(acc1.get_accpass()) #accessible
 

#-------------------

# class Person:
#     __name = "anonymous"

#     @staticmethod
#     def __hello():
#         print("hello")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# print(p1.welcome())

#--------------------------

#Inheritance

#Single Inheritance
# class Car:
#     color = "black"

#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):

#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# print(car1.color)

# print(car1.start())

# ----------------
# Multilevel Inheritance

# class Car:

#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):

#     def __init__(self,name):
#         self.name = name

# class Fortuner(ToyotaCar):

#     def __init__(self,type):
#         self.type = type

# car1 = Fortuner("diesel")

# print(car1.start())


#----------------

#Multiple Inheritance

# class A:
#     varA = "welcome A"

# class B:
#     varB = "welcome B"

# class C(A,B):
#     varC = "welcome C"

# c1 = C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

#super method

# class Car:
#     def __init__(self,type):
#         self.type =type

#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):

#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name = name
#         super().start()


# car1 = ToyotaCar("toyo","diesel")

# print(car1.type)

#-----------------------------
#classmethod

# class Person:
#     name = "anonymous"

#     #1st method
#     # def changeName(self,name):
#     #     self.__class__.name = "Rahul"

#     #2md method which is useable method
#     @classmethod #decorator
#     def changeName(cls,name):
#         cls.name = name

# p1 = Person()

# p1.changeName("rahul")
# print(p1.name)


#----------------------------------

#@property (which is used to convert a function into a attribute)  #automatic updates based on attributes

# class Student:
#     def __init__(self,chm,phy,math):
#         self.chm = chm
#         self.phy = phy
#         self.math = math

#     @property # it is used when here just like percentage is depend on chm,phy,math so if chm,phy,math this value is change then perctage will be changed so property is used to convert fn into att
#     def percentage(self):
#         return str((self.phy + self.chm + self.math ) / 3) + "%"
    

# s1 = Student(98,97,96)

# print(s1.percentage)

# s1.phy = 80

# print(s1.percentage)

# #polymorphism

# #operator overloading
# print(1+2) #add

# print("yash" + "kumar") #concatenate

#-----------------------------
#polymorphism and below we are doing operator overloading using dunder function
# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNum(self):
#         print(self.real, "i +", self.img, "j")

#     #dunder function
#     def __add__(self,num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal,newImg)
    
# num1 = Complex(1,3)
# num1.showNum()

# num2 = Complex(2,5)
# num2.showNum()

# num3 = num1 + num2
# num3.showNum()


#questions

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,order2):
        return self.price > order2.price


order1 = Order("chips", 20)
order2 = Order("kurkure", 10)

print(order1 > order2) #true