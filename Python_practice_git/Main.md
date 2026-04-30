## Goal post 

## Engineering:
* Optimistic , effective use of resource is engineer main goals    

## calculate grades with input as average :
```
Remember  average as number
if number >=90  & <=100 
  Grade A
elseif number >=80 & <=89
    Grade B
elseif number >=70 & <=79
    Grade c
elseif number >=60 & <=69
    Grade D
elseif number >=0 & <=59
    Grade F
else 
    Say invalid average

```

## Calcuate the sum of the digits of a input 

```
Remember the digit as number 1234
Remember sum as 0

until number > o
        remainder = number % 10 
        sum = sum + remainder 
        number = number // 10 
say sum

```

## Problems Practice:
* Practice in : https://projecteuler.net/problem=1

```
result = 0 
max = 10 
index = 1 
while index < max;
    if index % 3 == 0 or index % 5 == 0; 
        result = result + index
    
    index = index + 1
print(result)
```

## Alogorithm Practice :
* operators < , > , >=, <= , + , _ , / , % , //
* conditions , until 
* Start with algorithm and convert to the script 
* Adding/subtract two numbers 
* multiply 
* % & // 
* adding a four digit car number 
* prime 
* palandrome 
* Project euler three questions 

## Data types:

* We define data types , so that the amemory allocation will be defined
* Two types of data types :
    * Static data type - Int . When value changed , the memory location not changes 
    * dynamci data type - string. When value changed , the memory location changes 
* REPL - Read , evaluate , Print , loop
* Languages can be categorized as two types
    * statically typed programming languages (c, C++, java, C#)
    * dynamically typed programming languages (python, javascript)
* Number :
    * int 
    * float 
    * vector
* text:
    * string 
* Note : Ascii code and uni code 
* Boolean

## Operators practice in basics.ipynb file
* Note : In ipynb file in each cell last value wiil be printed
* casing in languages :
    * Pascal Casing 
        ```
        Value = 10 
        MyValue = 10 
        ```
    * Camel Casing 
        ```
        value = 10 
        myValue = 10
        ```
    * snake casing
        * python uses snake casing for the variable defining
        ```
        value = 10 
        my_value = 10 
        ```
* Simple Interst code and compund interest code in number_operations.ipynb file 
* Note : Operator priorities or precedence while dealing with multiple operators 

## Blocks and indentation in python 
* python doesn't like paranthesis {}
* Block is set of instructions
```
<block> :
    a....
    b....
c....
```
* a and b are inside block 
* c is outside block 

* Take an example of prime number from chatgpt and explain blocks 

* As a conventoin people use four spaces 

* popular blocks 
    * if 
    * while
    * for 
    * def 
    * class

## Conditions :

* I want to print if  thr number is prime or not - conditionals.ipynb
* jupite notebook debugging with examples 

## text_collection dat types 

| Feature / Type | List | Tuple | Set | Frozenset | Dictionary |
|---------------|------|-------|-----|-----------|------------|
| Syntax | [] | () | {} | frozenset() | {key: value} |
| Ordered | ✅ Yes | ✅ Yes | ❌ No | ❌ No | ✅ Yes (Py3.7+) |
| Mutable | ✅ Yes | ❌ No | ✅ Yes | ❌ No | ✅ Yes |
| Allows Duplicates | ✅ Yes | ✅ Yes | ❌ No | ❌ No | ❌ Keys: No / Values: Yes |
| Indexing | ✅ Yes | ✅ Yes | ❌ No | ❌ No | ❌ (use keys) |
| Key-Value Pair | ❌ No | ❌ No | ❌ No | ❌ No | ✅ Yes |
| Can be Dictionary Key | ❌ No | ✅ Yes | ❌ No | ✅ Yes | ❌ No |
| Add Elements | append(), extend() | ❌ Not allowed | add(), update() | ❌ Not allowed | key = value |
| Remove Elements | remove(), pop() | ❌ Not allowed | remove(), discard() | ❌ Not allowed | pop(), del |
| Performance | Medium | Fast | Fast (lookup) | Fast (read-only) | Very fast (lookup) |


| Type | Best Use Case |
|------|--------------|
| List | When you need ordered, changeable data (e.g., user inputs, logs) |
| Tuple | Fixed data that should not change (e.g., coordinates, function returns) |
| Set | Remove duplicates, fast membership checks |
| Frozenset | Immutable set, safe data, dictionary keys |
| Dictionary | Structured data (APIs, configs, agent inputs/outputs) |

## Feb-26 : 
* explain about , if , if else , if elif else in conditionals.ipynb
* example with grades of schools 
* exercise - tax slabs in 2026

## feb 27 :
* loops : - loops.ipynb
    * while
    8 for 
* write our first python code on our own :
    * https://projecteuler.net/problem=1
* prime , fibbonaci , palindrome debug with wrong script 

## Mar-2 :
* Python standard libraries :
    * while installing python , python ships with lots of code 
    * Most of them are created for reusability 
    * This is also referred ass batteries included toy.
    * Most common reusable elements(functions/classes) are reffered as builtins
    * Prompt :
    ```sh
    You are an expert in python. I'm leaning python.
    I want to understand what builtins are and give me a list of builtins in a table with its purpose and an example 

    ```
    * Module :
       *  A module in python refers to a file
       *  If i have created a python file 'test.py' then it is module with name 'test'
       * Python standard library is collection of modules.

    * Lets create a simple module :
        * A module can acts as a library or as an executable 
            * Executable runs  => run program 
            * library => reusbale elements (function or class or variable)
        * pratcice in understanding_module folder
    
    * In python we have some special variables or methods – dunder methods : exercise in a.py,b.py
        * Anything which you see in python with __ double underscores around it , it has a special purpose.
        * prompt:
        ```
        You are an expert in python, i'm learning python.
        I want to understand what dunder variables are and give me a list of dunder variables in a table with its purpose and an example usage
        ```
        

## Mar-5 :

* Lets start writing interactive programs : 
    * Problem 1: Findout if the number is prime or not with user input - prime.py 
    * First way of resuable code is function 
* Functions:  - functions.ipynb 
    * A function is a reusable block :
    * basic syntax:
    ```
    def <functionname>(args):
        ...
        '''
    ```
    * A function can return a value or not return a value 
    * basic print hello 5 times function in functions.ipynb 
        * use help(print)
* Doc strings in python - use Docstring extension in vsc :
    * it is help to your function 
* It is recommended to use type hints - to makesure what types are allowed 
* write utils.py with a prime number and call that in the prime.py 
* write a function for prime & palindrome in utils.py and call it is prime.py and palindrome.py with __name__ = __main__


## Mar-6 :
* Using Functions:
    * python allows to call functions by passing arguments
       * postionally
       * named
       * optional (default values are provided by default)
            * Always define the optinal arguments at the end in the like function(number, a=1)

* Lets write a program which prints n = 3  : - functions.py 
``` 
  *
 ***
*****
```
* if we pass n = 5
```
    *
   ***
  *****
 *******
*********
```

## MAr-9:
*  Sequential Datatypes (list, tuple, range) : sequence.ipynb 


## MAr-10: generator_listcomprehension.ipynb
* generator 
* List comprehension


## March -11 : generator_listcomprehension.ipynb
* sets : It is collection of unique items 
* funtcoin with variable arguments 


## March -14 : dictionaries.ipynb
* Dictionaries : It is collection of key values 
* string 


## March -17 , 20 : POS 
* In D:\Devops\Python\Py_Projects\POS
