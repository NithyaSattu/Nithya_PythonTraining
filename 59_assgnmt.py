"""
59. copy 1 file content in to another file(Take the source and
destination file path from the user)
"""
source_path=raw_input("Enter the path of the source file")
target_path=raw_input("Enter the path of the target file")
source_file=open(source_path,'r')
target_file=open(target_path,'a')

for i in source_file.readlines():
    target_file.write(i)
source_file.close()
target_file.close()  
target_file=open(target_path,'r')
print "Copied Lines from source to target are:"
print target_file.readlines()
    



