#Reading and processing a file

fname = "yourfile.txt"with open(fname, 'r') as fileref: # step 1
lines = fileref.readlines() # step 2
for lin in lines: # step 3
#some code that references the variable lin
#some other code not relying on fileref # step 4

#Another option for efficiency

fname = "yourfile.txt"with open(fname, 'r') as fileref: # step 1
for lin in fileref: # step 2
## some code that reference the variable lin
#some other code not relying on fileref # step 3      
