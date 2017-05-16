"""
33.input: "google" print count of each character
"""
str1=raw_input("Enter the string")
dict_temp={}
for i in str1:
    dict_temp[i]=str1.count(i)
print dict_temp

for i in dict_temp:
    print "character %s count is" %i,dict_temp[i]
    
        

    


