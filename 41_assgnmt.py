"""
41.
input: fun(5) output: [1,2,3,4,3,2,1]
"""

def fun(a):
    
    b=range(1,a)
    x=range(a-2,0,-1)
    d=b+x
    return d
if __name__ == "__main__":
    a=input("Enter a number")
    print "Result is ",fun(a)


