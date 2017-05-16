"""
51. input: google
	output: {'g':2,'o':2,'l':1,'e':1} use dictionary comprehension

"""

input_user1=raw_input("Enter the string")

d={i:input_user1.count(i) for i in input_user1}
print d
