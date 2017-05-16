"""
69. Bulk file copy. 
     Take source and destination file paths from a file and copy the
     source file content into destination file.
     Maintain configuration file and put the below fields there
      Source not found: Skip the copy
      destination found: skip/replace
     maintain a remarks log. What are the files skiped from copy
     because no source file found. What are the files skip/replaced
     because of destination file foun in the specified path
"""


import os
import shutil
source = "D:\PythonTraining_assignments\source.txt"
dest = "D:\PythonTraining_assignments\dest.txt"
with open('remarks.log','w') as log:
    log.write('')
if not os.path.exists(source):
    if os.path.exists(dest):
        with open('config.txt','r') as conf:
            data = conf.readlines()
        print data[0]
        with open('remarks.log','a') as log:
            log.write('File {} skipped from copy because no source file found'.format(dest))
else:
    if os.path.exists(dest):
        with open('config.txt','r') as conf:
            data = conf.readlines()
        print data[1]
        opt = raw_input()
        if opt.lower() == 'skip':
            print "Skipped the file"
            with open('remarks.log','a') as log:
                log.write('File {} skipped from copy '.format(dest))
        else:
            shutil.copy(source, dest)
            print "Replaced successfully"
            with open('remarks.log','a') as log:
                log.write('File {} copied because destination file found'.format(dest))
        
    


