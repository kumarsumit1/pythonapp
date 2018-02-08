#Modules in Python are simply Python files with the .py extension, which implement a set of functions. 
#Modules are imported from other modules using the import command.

'''
NOTE :
The first time a module is loaded into a running Python script, it is initialized by
 executing the code in the module once. If another module in your code imports the same
  module again, it will not be loaded twice but once only - so local variables inside
   the module act as a "singleton" - they are initialized only once.
'''
import urllib
#Exploring built-in modules   

print(dir(urllib))

help (urllib.__doc__)

#Writing packages
'''
Packages are namespaces which contain multiple packages and modules themselves. 
They are simply directories, but with a twist.

Each package in Python is a directory which MUST contain a special file called __init__.py. 
This file can be empty, and it indicates that the directory it contains is a Python package,
 so it can be imported the same way a module can be imported.
'''

