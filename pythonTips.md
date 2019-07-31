
1. lists all the functions \
	`print(dir(dataframe.show()))`
2. usage of any function in python \
	`help(dataframe.show)`
3. Type of object/class \
	`print(type(dataframe))`
4. Importing functions
	- One way of importing \
`import pyspark.sql.functions as fun
sales.select(fun.avg('Sales').alias("average_sales")).show()` \
	- Other way is to import specific functions itself \
	`from pyspark.sql.functions import countDistinct,avg,stddev
	sales.select(avg('Sales').alias("average_sales")).show()`
5. Convert True/False value read from file to boolean
	>>> eval('True')
	True
	>>> eval('False')
	False
6. 



## Setting up env and project [How to Setup a new Python Project EuroPython 2014]:

Currently, there are two common tools for creating Python virtual environments:

    venv is available by default in Python 3.3 and later, and installs pip and setuptools into created virtual environments in Python 3.4 and later.
    
	virtualenv needs to be installed separately, but supports Python 2.7+ and Python 3.3+, and pip, setuptools and wheel are always installed into created virtual environments by default (regardless of Python version).

The basic usage is like so:

Using virtualenv: \
	virtualenv [DIR] \
	source [DIR]/bin/activate

Using venv:\
	python3 -m venv [DIR]
	source [DIR]/bin/activate





In Windows set following command in Powershell 
Set-ExecutionPolicy Unrestricted	

1. Set up virtualenv

$virtualenv venv

This will create a folder with required libs for its setup. Now 

$cd venv
$.\Scripts\activate  --> Powershell
#source venv/bin/activate --> Unix like

Now check which all packages are installed 
$python -V
$pip freeze

2. Now install pyscaffold project which helps you to easily setup a new Python project

$pip install pyscaffold

Or use cookiecutter which has specific templates for various languages and projects

$ pip install cookiecutter

and choose a template for eg a sample pyspark template is 

$ cookiecutter https://github.com/roryhr/cookiecutter-pyspark

Now create a sample project

$putup myproject

This will create a sample project with docs lib etc

3. To build and install the file 

$python .\setup.py install

This will create build and dist folder. 

**Note** :
1. **sdist** means source distribution and **bdist** means build distribution
2. The requirement.txt is used by pip to help developers develop the code, also a destination folder can optionally be mentioned to install them.

pip install -r requirements.txt -t ./lib

While install_requires in setuptools is for end user who will be using the code.

Installing development requirements



$python .\setup.py install sdist

This will create a source distribution tar file in dist folder which will have all the code docs test etc.

$python .\setup.py install sdist --format=zip

$python .\setup.py install bdist

This will create a build distribution zip file which will depend on the system on which it is build 


4. For testing the code
python .\setup.py install test




5. Building sphinx compatible documents
First install :
$pip install sphinx

$python .\setup.py install docs

It will create files under "\build\sphinx\html" folder .

6. Building wheel packages

$ python setup.py bdist_wheel



-----------------------------
Downloading packages as wheel in a folder
pip wheel -r requirements.txt -w lib


-------------------------------
pip

Use Pip --user installs for your default environment

pip install --user mypackage


## Python Special Variables and Methods

>__name__ and __main__ : 

>__doc__ :  __doc__ will print out the docstring that appears in a class or method

>__getattr__ and getattr :

>__setattr__ and setattr :

>__class__ and type :

>__bases__ : __bases__ is a variable that contains as a tuple all the classes that a class inherites from

>__subclasses__() : __subclasses__ is a method that will return all the subclasses of a class in a list

>locals() and globals() : locals is a native method that displays all the local variables as dictionary entries. globals does the same with global variables

>__dict__ : __dict__ will return, as a dictionary, all attributes of a class instance

 

## Try Except Finally block

It will always go to the finally block, so it will ignore the return in the try and except. If you would have a return above the try and except, it would return that value.
```
def func1():
    try:
        return 1 # ignoring the return
    finally:
        return 2 # returns this return

def func2():
    try:
        raise ValueError()
    except:
        # is going to this exception block, but ignores the return because it needs to go to the finally
        return 1
    finally:
        return 3

def func3():
    return 0 # finds a return here, before the try except and finally block, so it will use this return 
    try:
        raise ValueError()
    except:
        return 1
    finally:
        return 3


func1() # returns 2
func2() # returns 3
func3() # returns 0
```

## Test	