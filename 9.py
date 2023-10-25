#9. Write a Python program that accepts a string and counts the number of upper and
#lower case letters.

str_0030 = input("Enter the string : ")

count_lower_0030 = 0
count_upper_0030 = 0

for i in str_0030:
    if i.isupper():
        count_upper_0030 = count_upper_0030 + 1
    else: 
        count_lower_0030 = count_lower_0030 + 1
        
print("Number of uppercase etterr is ", count_upper_0030,"and lower case letter is ", count_lower_0030)