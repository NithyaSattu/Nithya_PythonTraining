"""
42.input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]]
"""
"""
x='abc'
k=[]
d=[]
print x,type(x),len(x)
for i in x:
    k=list(i)
    d.append(k)
   
print d
"""
def fun(seq):
    combinations = []
    combinations.append([])
    
    for i in range(0,len(seq)):
        combinations.append([seq[i]])
        for j in range(i+1,len(seq)):
            combinations.append([seq[i],seq[j]])
            for k in range(j+1,len(seq)):
              combinations.append([seq[i],seq[j],seq[k]])
        combinations.sort(key=len)
    return combinations

print "Result is ",fun(['a','b','c'])

