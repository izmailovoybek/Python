#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
a=4/0
print(a)


#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
a=int(input('matn kiriting:'))
print(a)

#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
with open(r'c:\user\user\deskop\name.ipynb') as f:
    data=f.read()

#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
print('oybek'+12222)

#Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
my_list=[2,4,5,66,777,111,222]
print(my_list[8])


#Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ArithmeticError as e:
        print(f"Arithmetic error occurred: {e}")

safe_divide(5, 0) 


#Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
print('ummon'.append)



#Write a Python program to read an entire text file.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt')as f:
    data=f.read()
print(data)


#Write a Python program to read first n lines of a file.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt')as f:
    data=f.readlines()
print(data)


#Write a Python program to append text to a file and display the text.
with open (r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','a')as f:
    f.write('\nbest of the best good for you')
with open (r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    data=f.read()
print(data)


#Write a Python program to read last n lines of a file.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt') as f:
    data=f.readlines()[-n:]
print(data)


#Write a Python program to read a file line by line and store it into a list.
data=[]
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    data=f.readlines()
print(data)

#Write a Python program to read a file line by line and store it into a variable.
data=[]
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    data=f.readlines()
print(data)

#Write a Python program to read a file line by line and store it into an array.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    data=[line.strip() for line in f]
print(data)

#Write a Python program to find the longest words.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    matn=f.read()
    sozlar=matn.split()#sozlarga bolvoti
    max_sozlar=len(max(sozlar,key=len))
    uzun_soz=[soz for soz in sozlar if len(soz)==max_sozlar]
print(uzun_soz)


#Write a Python program to count the number of lines in a text file.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    matn=f.readlines()
    line_count=len(matn)
print(line_count)


#Write a Python program to count the frequency of words in a file.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    matn=f.read()
    sozlar=matn.split()
    frequency={}
    for soz in sozlar:
        frequency[soz]=frequency.get(soz,0)+1
print(frequency)


#Write a Python program to get the file size of a plain file.
import os
file_siez=r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt'
size=os.path.getsize(file_siez)
print(size,'bayt')


#Write a Python program to write a list to a file.
list=["Olma", "Banan", "Gilos", "Anor"]
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','w')as f:
    for item in list:
        f.write(item+'\n')

print()


#Write a Python program to copy the contents of a file to another file.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    read=f.read()

with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text_2.txt','w')as f2:
    f2.write(read)
print()



#Write a Python program to combine each line from the first file with the corresponding line in the second file.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    read=f.readlines()

with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text_2.txt','r')as f2:
    read2=f2.readlines()
combine=[a.strip()+''+b.strip() for a,b in zip(read,read2)]

with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\out.txt','w')as f_out:
    for line in combine:
        f_out.write(line+'\n')
print()


#Write a Python program to read a random line from a file.
import random
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    read=f.readlines()
random_line=random.choice(read)
print(random_line.strip())


#Write a Python program to assess if a file is closed or not.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    read=f.readlines()
    print('',f.closed)
print('',f.closed)


#Write a Python program to remove newline characters from a file.
with open(r'C:\Users\o.izmailov\Desktop\python\8 dars\text.txt','r')as f:
    read=f.readlines()
    read2=[line.strip()for line in read]
print(read2)





