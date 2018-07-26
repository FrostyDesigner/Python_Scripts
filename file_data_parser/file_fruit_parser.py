#import regular expressions
import re



# read the file back as a list of lines
fname = "myfruits.txt"
fin = open(fname, "r")
data_list = fin.readlines()
fin.close()
print(data_list)

# now you can access each line (list item) by the index
# the index of a list is zero based
print(data_list[0])  # apple
print(data_list[3])  # melon


#loop attempt
i=0
for line in data_list:
    line=line.replace("\n","")
    if line=="banana":
        print(line)
    else:
        print("false")
    i=i+1

