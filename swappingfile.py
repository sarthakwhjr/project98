file1 = open("sample1.txt","r")
file2 = open("sample2.txt","r")
filename=input("enter your file name")
if(filename=="sample1.txt"):
    print(file2.read())
elif(filename=="sample2.txt"):
    print(file1.read())


