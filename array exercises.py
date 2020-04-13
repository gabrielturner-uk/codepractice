# 1. Write a Python program to create an array of 5 integers and display the array items. 
# Access individual element through indexes. Go to the editor
print ("exercise 1")
import array
from array import *
arraynum = array('i',[1,3,5,7,9])
for i in arraynum:
    print (i)
print (arraynum[1])


#2. Write a Python program to append a new item to the end of the array. Go to the editor
print ("exercise 2")
arraynum.append(10)
for i in arraynum:
    print (i)
#3. Write a Python program to reverse the order of the items in the array. Go to the editor
print ("exercise 3")
arraynum.reverse()
print (arraynum)
#4. Write a Python program to get the length in bytes of one array item in the internal representation. Go to the editor
print ("exercise 4")
print (str(arraynum.itemsize))

#5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes. Go to the editor
print ("exercise 5")
#6. Write a Python program to get the number of occurrences of a specified element in an array. Go to the editor
print ("exercise 6")

