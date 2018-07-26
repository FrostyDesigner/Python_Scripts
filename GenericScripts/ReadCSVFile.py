import csv

#all 3 methods below work
#You need to use a raw string, double slashes or use forward slashes
#with open(r"C:\GitHub\Python_Scripts\Seattle_Wages.csv") as file:
#with open("C:\\GitHub\\Python_Scripts\\Seattle_Wages.csv") as file:
with open("C:/GitHub/Python_Scripts/Seattle_Wages.csv") as file:
    #if the csv is formatted correctly...
    #reader = csv.reader(file)
    #if you need to delimit with a space character instead...
    #reader = csv.reader(file, delimeter=" ")
    #you can also create a DictReader that creates a dictionary out of each row using the header as keys
    reader = csv.DictReader(file)

    count = 0

    for row in reader:
        #to print entire row
        #print(row)
        #to print specific column
        #print(row[4])
        #to print specific column - with DictReader
        #print(row["Jobtitle"])
        #to print multiple columns - with DictReader
        print(row["Jobtitle"], row["Female Avg Hrly Rate"], row["Male Avg Hrly Rate"], row["Notes"])

        #to only print n rows...
        if count > 500:
            break

        count += 1