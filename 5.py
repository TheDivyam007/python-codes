#5. Implement a python function to Reverse a given String and also check for palindrome
#or not.

def revString(val_0030):
    str_0030 = ""
    for i in val_0030:
        str_0030 = i+str_0030
        
    print("Reversed string is : ", str_0030)
    
    if str_0030==val_0030:
        print("String is palimndrome")
    else:
        print("String isn't a palindrome string")
        
string_0030 = "Mom"
revString(string_0030)
