"""
78. WAP to replace perticular number of substings with a
given destination string
"""
str1=raw_input("Enter the actual string")
source_str=raw_input("Enter the source string ")
dest_str=raw_input("Enter the destination string")

if source_str not in str1:
    print "Sub string not found"
else:
    limit=input("Enter the number of times that the substring should be removed")
    replaced_str = str1.replace(source_str,dest_str,limit)
    print "Replaced string is ",replaced_str
        
        
    

