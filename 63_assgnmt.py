"""
63. Take three columns disease, symptoms, advice in a file and fill the details
	Ask the user to enter symptoms. Based on this symptoms
	Suggest the user to what disease it may be and few advices.

"""
if __name__ == "__main__":
    f1 = open('Source_63_csv.csv','r')
    read_lines = f1.readlines()
    f1.close()
    print read_lines
    menu = raw_input("Enter your symptoms")
    for i in read_lines:
        if menu in i:
            j=i.split(',')
            print "Mentioned symptoms Disease could be %s and Advices are %s"%(j[0],j[4])
    
    
    
