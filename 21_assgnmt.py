"""
21. Given an age, figure out whether someone's a \
baby, toddler, child, teenager, adult or old codger.
"""
age=input("Enter the age of the person to check ")
if age<3:
    print "toddler"
elif age>3 and age<=8:
    print "Baby"
elif age>8 and age<=12:
    print "Child"
elif age>12 and age<=20:
    print "Teenager"
elif age>20 and age<=48:
    print "Adult"
elif age>48 and age>=100:
    print "Old age"
