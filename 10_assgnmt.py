"""
10. Show the below menu to the user until and until user select quit and display corresponding os message

'''
Menu:
1. windows
2. Linux
3. Mac
4. quit
'''
"""
while True:
    print "1.Windows\n2.Linux\n3.Mac\n4.quit"
    x=input("Enter your choice")
    if x==1:
        print "your selection is windows"
        
    elif x==2:
        print "your selection is Linux"
        
    elif x==3:
        print "your selection is Mac"
        
    elif x==4:
        print "Quitting"
        break
    elif x>4:
        z=raw_input("There is no such option.Do you want to continue yes or no?")
        if z=="n" or z=="no":
            print "Quitting"
            break
        elif z=="y" or z=="yes":
            continue
            
        
    


