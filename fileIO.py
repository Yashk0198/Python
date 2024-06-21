# f = open("data.txt", "rt")
# data = f.read()

# print(data)
# f.close()


#--------------------


f = open("data.txt", "rt")
data = f.read()

print(data) #for data read

line1 = f.readline() #line by line data reading but now you already read the data now the cursor is at last which is empty so it will print empty here.first line
print(line1)

line2 = f.readline() #line by line data reading but now you already read the data now the cursor is at last which is empty so it will print empty here.second line
print(line2)

f.close()

#--------------
f = open("data.txt", "w")

data = f.write("write line") #overwrite the data

f.close()

#------------------

f = open("data.txt", "a")

data = f.write("write line") #append the data

f.close()


#---------------with syntax

with open("data.txt", "r") as f: #alias # with syntax doesnt need to close the connection
    print(f.read())

#deleting a file
import os
os.remove("data.txt")