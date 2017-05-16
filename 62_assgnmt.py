"""
62. convert .txt file in .json
"""

import json
f=open("string.txt",'r')
data1=f.readlines()
print 'data',data1
data_string = json.dumps(data1)
json_loads=json.loads(data_string)
print 'JSON:', data_string
print json_loads
f.close()

