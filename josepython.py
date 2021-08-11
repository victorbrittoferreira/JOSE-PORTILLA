## a trick to reverse a string

#x = 'atecubanos'
 
#print (x[::-1])


#x = 'Hello world'
#y = 'Hi this is a string'
## slice
#print (x[8])

## upper case
#print(x.upper())

## create a list
#print(x.split())

## create another list, but considering a paremetter
#print(y.split('s'))

## ways to format a string in

#1
#print ('The {0} {1} {2}'. format ('fox', 'brown', 'quick'))

#2
#print ('The {f} {f} {f}'. format (f = 'fox', b = 'brown', q = 'quick'))

#3
#animal = "fox"
#print ('The {a} {a} {a}'. format (a = animal))

#4
#result = 13.5534534
#print('Resultado {r: 5.2f}'.format (r = result))

## %s  another way inject string into print statement 
#print("Resultado  %s " %' foi esse')

#multiple itens
#print("Resultado  %s e %s" %('A', 'B'))
 
# like math = theres a equality parallel = signal
#a , b = 'A' , 'B'
#print("Resultado  %s e %s" %( b, a ))


### FIRST ASSESTMENT

#
#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
## Print out 'e' using indexing
#s = 'hello'
#print(s[1])
#print(s[0]+s[2:])

#Reverse the string 'hello' using slicing:
#print(s[::-1])

#Reassign 'hello' in this nested list to say 'goodbye' instead:
#x[2] = 'hello'
#
#list3 = [1,2,[3,4,'hello']]
#list3[2][2] = 'goodbye'
#print(list3)

#Sort the list below:
#list4 = [5,3,4,6,1]
#print(sorted(list4)) # sorted não modifica a lista, mas só para o uso
#print(list4)

#DICTIONARIES
#
#Using keys and indexing, grab the 'hello' from the following dictionaries:
#d = {'simple_key':'hello'}
#Grab 'hello'
#print(d['simple_key'])

#d = {'k1':{'k2':'hello'}}
## Grab 'hello'
#print(d['k1']['k2'])

## Getting a little tricker
#d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
##Grab hello
#print(d['k1'][0]['nest_key'][1][0])

## This will be hard and annoying! 
#d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#print(d['k1'][2]['k2'][1]['tough'][2][0])


#Can you sort a dictionary? Why or why not?
#Nope, coz its mappings not a sequence

#TUPLES
# 
#What is the major difference between tuples and lists?
#Tuple are immutable

#How do you create a tuple?
# setting it between ()

#SETS
#
#What is unique about a set?
#This shit dont repeat the same fucking values

#Use a set to find the unique values of the list below:
#list5 = [1,2,2,33,4,4,11,22,3,3,2]
#print(set(list5)) 


## For loops

#my_list = [1,2,3,4,5,6]
#white space is a placeholder
#for _ in my_list:
#    print(_)

##for num in my_list:
##    #print(num, 'hello')
##    if num % 2 == 0:
##        print( num ,"even")
##    else:
##        print( num ,"odd")
#
#list_sum = 0
#
#for num in my_list:
#    list_sum = list_sum + num
#    
### difference between print in or out of loop is:
#    ## print each sum into the end    
#    print(f'Elm {num} - Result {list_sum}')
#
## print in the end
#print(list_sum)

#string = 'Koe Kumpadi'
#
#for letter in string:
#    print(letter)

# tuple inside a list 
#my_list = [(1,2), (3,4)]
#
## each element inside a tuple must be declared, to be unpacked
#    print(a)
#    print(b)

# aplying a even filtering
#my_list = [(1,2,3), (4,5,6)]
#for a,b,c in my_list:
#    if a % 2 == 0:
#        print(a)
#    if b % 2 == 0:
#        print(b)
#    if c % 2 == 0:
#        print(c)

  

#d = {'k1':2,'k2':3,'k3':4}
# only unpack the key
#for item in d:
#    print(item)

#complete unpacking
#for k, v in d.items():
#    print(v, k) 

# only the value    
#for value in d.values():
#    print(value) 

#36. While Loops in Python

#x = 0
#
#while x < 5: 
#    print (f'Print {x}')
#    
#    x += 1
#else:
#    print('Acabou')
    
#break: Breaks out of the current closest enclosing loop.
#continue: Goes to the top of the closest enclosing loop.
#pass: Does nothing at all.

#x = [1,2,3]
#
#for item in x:
    
    #keep as a placeholder to avoid eof error
    #pass
    
    #if item % 2 == 0:
    ## go back to the loop
    #    continue
    #print(item)
    
    
    #if item % 2 == 0:
    #    break
    ## stop to the loop
    #print(item) 
    
# 37 Useful tools

#my_list = [1,2,3]

# use to iterate objects, but its only an information generator 
#for num in range(10):
#    print(num)

#index_count = 1
#
#for letter in 'abcde':
#    print(f'Index {index_count} of the letter {letter}')
#    index_count += 1

## a smart way is use enumerate function to replacte it

#word = 'abcde'
#
#for index, letter in enumerate (word):
#    print(letter)

## ZIP FUNCTION

#my_list1 = [1,2,3]
#my_list2 = ['a','b','c']
#my_list3 = ['@','!','$','%']

# it cast each bit together, but don't show error if there's much more bits than zipeable
#for item in zip (my_list1, my_list2 , my_list3):
#    print(item)

#for a,b,c in zip (my_list1, my_list2 , my_list3):
#    print(a)
    
# to cleat a list of zipped items 

#print ( list ( zip (my_list1, my_list2)))

# to check if exist and x in a set

#z = {'mykey':123}
#
#print( 123 in z.values())
#print( 'mykey' in z.keys())

#shuffle function

# from which func , import what
#from random import shuffle
#
##inplace function
#shuffle(my_list1)
#
#print( my_list1)




#38. List Comprehensions in Python

#my_string = 'hello'

# 1st way
#print(list(my_string))

#2nd way
#lst = [letter for letter in 'hello']
#
#print(lst)

#3rd way

#my_list = []
#
#for letter in  my_string:
#    my_list.append(letter)
#print(my_list)

#my_list = [num for num in range(1,11)]
#
##doing operations
#my_list = [num**2 for num in range(1,11)]
#
##doing operations, with conditional
#my_list = [num**2 for num in range(1,11) if num % 2 == 0  ]

#print(my_list)

#its able to do more complex operations

#celcius = [ temp for temp in range(0, 40, 5)]
##fahrenheit = [ (( 9 / 5) * temp + 32) for temp in celcius]
#
##same thing, but another way
#fahrenheit = []
#
#for temp in celcius:
#    fahrenheit.append( (9/5)*temp + 32)
#
#print(f'Celsius {celcius}')
#print(f'Fahrenheit {fahrenheit}')

#result = [ x if x %2 == 0 else 'ODD' for x in range (1,11)]
#print(result)

#mylist = []
## NESTED FOR
#for x in [2, 4 ,6]:
#    for y in [1, 10, 100]:
#        mylist.append((x * y))
#        #is possibile include another operations
#        #mylist.append((x * y)**2)

# the result [2, 20, 200, 4, 40, 400, 6, 60, 600], like a matriz

#mylist = [(x * y)*1/3 for x in [2, 4 ,6] for y in [1, 10, 100]]
#
#print(mylist)



# Statements Assessment Test

#1 Use for, .split(), and if to create a Statement that will 
# print out words that start with 's':

#st = 'Print only the words that start with s in this sentence'
#
#for word in st.split():
#    #if word[0] == 's' and len(word) != 1:
#    #better way
#    if word[0].lower() == 's' and len(word) != 1:
#        print(word)
         
#2 Use range() to print all the even numbers from 0 to 10.
#x = [num for num in range(0, 10) if num %2 == 0 ]
#print(x)

#if doing a list
#y = []

#for num in range(0, 10):
# a smart way
#    if num % 2 == 0:
#        y.append(num)
#for num in range(0, 11, 2):
#    print(num)

#3 Use a List Comprehension to create a list of all numbers
# between 1 and 50 that are divisible by 3.
#x = [num for num in range(1, 51) if num %3 == 0 ]
#print(x)

#4 Go through the string below and if the length of a word
# is even print "even!"

#st = 'Print every word in this sentence that has an even number of letters'
#
#for word in st.split():
#    if len(word) %2 == 0:
#        #print('Even {}'.format(word))
#        print(word+ 'is even')

#5 Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which 
# are multiples of both three and five print "FizzBuzz".

#for num in range(1, 101):
#    if num % 2 == 0 and num %3 == 0:
#        print(num,  'FizzBuzz')
#    elif num %3 == 0:
#        print(num,  'Fizz')
#    elif num %5 == 0:
#        print(num,  'Buzz')
    

#6 Use List Comprehension to create a list of the first letters
# of every word in the string below:

#st = 'Create a list of the first letters of every word in this string'
# 
#print([word[0] for word in st.split()])
##x = [word[0] for word in st.split()]
##print(x)

#41 Methods and the Python Documentation

# we use return to send back de result of the function and it allows 
# to assign the output of the function to a new variable

#  ' = ' sets a default value
#def say_hello(name = 'foreign'):
#    print(f'Hello {name}')
#
#say_hello()

#def myfunc ( a, b):
#    # a pontual debbugging
#    print (a + b)
#    return (a + b)
#    
#myfunc(10 , 20)
##result = myfunc(10 , 20)

# 45 Logic with Python Functions

#def even_check(number):
#    #print (number % 2 == 0)
#    return number % 2 == 0
#
#even_check (20)

#def check_even_list (num_list):
#    for number in num_list:
#        if number % 2 == 0:
#            return True
#        else:
#            pass
#    return False
#print (check_even_list([1, 2 ,3]))

    #placeholder variables
#    even_numbers = []
#    x = 'x'
#
#    for number in num_list:
#        if number % 2 == 0:
#            #return True
#            even_numbers.append(number)
#        else:
#            pass
#    return even_numbers, x
#
#print (check_even_list([1, 2 ,3]))
## unpacking the tupple
#print (check_even_list([1, 2 ,3])[1])

#46 Tuple unpacking with python functions

#stock_prices = [('APPL',200), ('GOOG',400), ('MSFT',100)]
#
#for mark,price in stock_prices:
#    #print(mark)
#    print(price+ (0.1*price))

#work_hours = [('Abby',100), ('Billy',4000), ('Cassie', 800)]
#
#def employee_check (work_hours):
#    
#    current_max = 0
#    employee_of_month = ''
#    
#    for employee, hours in work_hours:
#        if hours > current_max:
#            current_max = hours
#            employee_of_month = employee
#        else:
#            pass
#    return employee_of_month, current_max
#
#print(employee_check(work_hours))
##way to find out quantity of items
##result = (employee_check(work_hours))
#employee, hours = (employee_check(work_hours))
#
#print(employee)

# 47 Intereactions  between Python functions

#def myfunc(word):
#    outstring = []
#    
#    for index, letter in enumerate (word.lower()):
#        if index % 2 != 0:
#            outstring.append(letter.upper())
#        else:
#            outstring.append(letter)
#    
#    return ''.join(outstring)

#print(myfunc('Xasdasd'))

## an advanced way
#def myfunc(s): return ''.join(char.upper() if s%2 else char.lower() for s, char in enumerate(s))

# portilla's way
#def myfunc(word):
#    out = []
#    for index in range(len(word)):
#        #print(s)
#        if index %2==0:
#            out.append(word[index].lower())
              
# 50 Functions practice Exercises

# WARM UP

#1 LESSER OF TWO EVENS: Write a function that returns 
# the lesser of two given numbers if both numbers are 
# even, but returns the greater if one or both numbers are odd

#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5

#def lesser_of_two_evens(a,b):
#    if a % 2 == 0 and b % 2 == 0:
#        return min (a,b)
#    else:
#        return max (a,b)
#        
#print(lesser_of_two_evens(10,20))

#2 ANIMAL CRACKERS: Write a function takes a two-word string and 
#returns True if both words begin with same letter

#def animal_crackers(text):
####  IMPORTANT  ####
#    words = text.lower().split()
#    
#    return words[0][0] == words[1][0]:
    
    #words = list(text.split(' '))
#    if words[0][0] == words[1][0]:
#        return True        
#    else:
#        return False
#    
#print(animal_crackers('Levelheaded Llama'))

#MAKES TWENTY: Given two integers, return True if the sum 
#of the integers is 20 or if one of the integers is 20.
#If not, return False

#def makes_twenty(n1,n2):
#    
#    return n1 + n2 == 20 or n1 == 20 or n2 == 20
#    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
#        return True
#    else:
#        return False
#print(makes_twenty(2,3))

# LEVEL 1 PROBLEMS (CHECK)

#OLD MACDONALD: Write a function that capitalizes the first
# and fourth letters of a name 

#def old_macdonald(name):
#    
#    return name.capitalize()[:3] + name.capitalize()[3:] 
    #halfname = name[3:]
    #recasedname = name.capitalize()[0:3] + halfname.capitalize() 
    #return name.capitalize()[0:3] + halfname.capitalize() 
    #return recasedname
    
#print(old_macdonald('macdonald'))

#MASTER YODA: Given a sentence, return a sentence with 
#the words reversed  (CHECK)
    
#def master_yoda(text):
#    
#    #reversedtext = list(text.split(' '))[::-1]
#    reversedtext = text.split()[::-1]
#    return  ' '.join(reversedtext)
#    
#    #return joinedtext
#    
# what is inside ' ' is used to concatenate
# # ''
#print(master_yoda('I am home'))


#ALMOST THERE: Given an integer n, return True 
#if n is within 10 of either 100 or 200 

#def almost_there(n):
#    
#    return 90 <= n <= 110 or 190 <= n <= 210
#    return (abs(100-n) <= 10) or (abs(200-n) <= 10)   
 
#print(almost_there(180))


# LEVEL 2 PROBLEMS

#FIND 33:

#Given a list of ints, return True if the array
#contains a 3 next to a 3 somewhere.

#def has_33(nums):

#    return '33' in ''.join(str(n) for n in nums)
    
#    for s in range (0, len(nums)-1):
#        #another way
#        if nums [s:s+2] == [3,3]:
#        #if nums[s] == 3 and nums [s+1] == 3:
#            return True
#    return False    
            
#print(has_33([1,3,1,3]))

#PAPER DOLL: Given a string, return a string where
# for every character in the original there are 
# three characters

#def paper_doll(text):      
#    new_text = []
#    
#    for letter in text:
#        new_text.append(letter*3)
#
#    return ''.join(new_text)
#
##               #or
#    result = ''
#    
#    for letter in text:
#        result += letter *3
#    return result

#print(paper_doll('Hello'))


#BLACKJACK: Given three integers between 1 and 11,
# if their sum is less than or equal to 21,
# return their sum. 
# If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, 
# return 'BUST'

#def blackjack(a, b ,c):
    #bjsum = a+b+c
#def blackjack(*n):
#    bjlist = n
#    bjsum = sum(n)
#
#    if bjsum <= 21:
#        return bjsum
#    elif bjsum > 21 and 11 in bjlist:
#        return bjsum - 10
#    else:
#        return 'BUST'
#    
#print(blackjack(5,6,7))

# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at 
# least one 9). Return 0 for no numbers.

#def summer_69(arr):

#    num_sum = 0
#    for num in arr:
#           
#        if not 6 <= num <= 9:
#            num_sum = num_sum + num 
#        else:
#            pass
#    return num_sum

    ## another way
##    total = 0
##    add = True
##    
##    for num in arr:
##        while add:
##            if num != 6:
##                total += num
##                break
##            else:
##                add = False
##        while not add:
##            if num != 9:
##                break
##            else:
##                add = True
##                break
##    return total
##
#print(summer_69([2, 1, 6,20, 9, 11]))


# CHALLENGING PROBLEMS

#SPY GAME: Write a function that takes in
# a list of integers and returns True if 
# it contains 007 in order

#def spy_game(nums):
#    sp_fdd = []
#    spyer = [0,0,7]
#    for num in nums:
#           
#        if 0 == num or num == 7:
#            sp_fdd.append(num)
#        else:
#            pass
#        
#    return spyer == sp_fdd
## ANTOHER WAY
#    sp_fdd = [0,0,7,'x']
#    
#    for num in nums:
#        if num == sp_fdd[0]:
#            ## take out the item
#            sp_fdd.pop(0)
#    return len(sp_fdd)== 1
#
#print(spy_game([1,2,4,0,0,7,5]))


#COUNT PRIMES: Write a function that 
#returns the number of prime numbers 
#that exist up to and including a given number
#def count_primes(num):
##must be improved
#    x = []
#    for s in range(2, num):
#        if (s % 2 == 0 or s % 3 == 0 
#            or s % 5 == 0 or s % 7 == 0) :
#            pass
#        else:
#            x.append(s)
#    print(x)
#    return (len(x)+4)
#print(count_primes(100))

### ANTOHER way - must be redone
#    # check for 0 or 1 input
#    if num < 2:
#        return 0
#    #2 or greater numbers
#    primes = [2]
#    x = 3
#    # x is going through every number up to input num
#    while x <= num:
#        # check if x is prime
#        for y in range(3, x, 2):
#            if x % y == 0:
#                x += 2
#                break
#        else:
#            primes.append(x)
#            x += 2
#    print(primes)
#    return len(primes)
#    
#print(count_primes(100))

#PRINT BIG: Write a function that takes
# in a single letter, and returns a 5x5
# representation of that letter



## 55 Lambda Expressions Map and Filter

#map function

#The map function allows you to "map" a function to an iterable
#object. That is to say you can quickly call the same function
#to every item in an iterable, such as a list

#def square (num):
#    return num**2
#
#my_nums = [1,2,3,4,5]
#
#for item in map(square, my_nums):
#    print(item)
#
##another way to list, instead of appending to a list
#print(list(map(square, my_nums)))


#def splicer (mystring):
#    if len (mystring)% 2 == 0:
#        return 'Even'
#    else:
#        return mystring[0]
#    
#names = ['Andy', 'Eve', 'Sally']
# 
#print(list(map(splicer, names)))

## filter function

#The filter function returns an iterator yielding those items of
#iterable for which function(item) is true. Meaning you need to 
#filter by a function that returns either True or False. Then 
#passing that into filter (along with your iterable) and you 
#will get back only the results that would return True when 
#passed to the function.

#def check_even(num):
#    return num % 2 == 0
#
#my_nums = [0,1,2,3,4,5,6,7,8,9,10]
#
##filtred = []
##for n in filter(check_even,my_nums):
##    filtred.append(n)
##print(filtred)
#
#print(list(filter(check_even,my_nums)))

## lambda expression

# lambda expressions allow us to create "anonymous" functions.
# This basically means we can quickly make ad-hoc functions
# without needing to properly define a function using def.
#Function objects returned by running lambda expressions work 
# exactly the same as those created and assigned by defs.
# There is key difference that makes lambda useful in
# specialized roles:

#    The lambda's body is similar to what we would put in a def
# body's return statement. We simply type the result as an 
# expression instead of explicitly returning it. Because it
# is limited to an expression, a lambda is less general that 
# a def. We can only squeeze design, to limit program nesting. 
# lambda is designed for coding simple functions, and def 
# handles the larger tasks.

#def square(num):
#    return num**2
## bad style to coding
#def square(num): return num**2
#
#print(square(2))

#This is the form a function that a lambda expression intends 
#to replicate. A lambda expression can then be written as:

#lambda num: num ** 2
#square = lambda num: num **2
#
#print(square(2))

#my_nums = [0,1,2,3,4,5,6,7,8,9,10]
#
#filtred = []
#for n in map(lambda num: num ** 2, my_nums):
#    filtred.append(n)
#    
#print(filtred)

#print(list(map(lambda num: num ** 2, my_nums)))
# 
#print(list(filter(lambda n: n % 2 == 0,my_nums)))

#Here are a few more examples, keep in mind the more comples a
#function is, the harder it is to translate into a lambda 
#expression, meaning sometimes its just easier (and often 
#the only way) to create the def keyword function.

#Lambda expression for grabbing the first character of a string:
#names = ['Andy', 'Eve', 'Sally']
#
#print(list(map(lambda s: s[0], names)))
#
#Lambda expression for reversing a string:
#
#lambda s: s[::-1]
#
#You can even pass in multiple arguments into a lambda expression. Again, keep in mind that not every function can be translated into a lambda expression.
#
#lambda x,y : x + y


##56 Nested Statements and Scope

#x = 25
#
#def printer():
#    x = 50
#    return x
#
#print(x)
#print(printer())
#
#3 general rules:
#
#   1 Name assignments will create or change local names by default.
#   2 Name references search (at most) four scopes, these are:
#        local
#        enclosing functions
#        global
#        built-in
#   3 Names declared in global and nonlocal statements map assigned
#   names to enclosing module and function scopes.
#
#The statement in 2 above can be defined by the LEGB rule.
#
#LEGB Rule:
#
#L: Local — Names assigned in any way within a function 
# (def or lambda), and not declared global in that function.
#
#E: Enclosing function locals — Names in the local scope
# of any and all enclosing functions (def or lambda), from
# inner to outer.
#
#G: Global (module) — Names assigned at the top-level of a
# module file, or declared global in a def within the file.
#
#B: Built-in (Python) — Names preassigned in the built-in
# names module : open, range, SyntaxError,...
#
## Local
#
## x is local here:

#f = lambda x:x**2
#print(f)
#
## Enclosing function locals
#
#name = 'This is a global name'
#
#def greet():
#    # Enclosing function
#    #name = 'This is a enclosing string'
#    
#    def hello():
#        # Local
#        name = 'This a local string'
#        print('Hello! '+name)
#    
#    hello()
#
#greet()
#
#x = 50
#
##Local Variables
#
#x = 50
#
#def func(x):
#    print('x is', x)
#    x = 2
#    print('Changed local x to', x)
#
#func(x)
#print('x is still', x)
#
#If you want to assign a value to a name defined at the top
# level of the program (s.e. not inside any kind of scope 
# such as functions or classes), then you have to tell 
# Python that the name is not local, but it is global. 
# We do this using the global statement. It is impossible 
# to assign a value to a variable defined outside a function
# without the global statement.
#
#You can use the values of such variables defined outside the
# function (assuming there is no variable with the same name
# within the function). However, this is not encouraged and
# should be avoided since it becomes unclear to the reader 
# of the program as to where that variable’s definition is.
# Using the global statement makes it amply clear that the
# variable is defined in an outermost block.
#
#x = 50
#
##def func():
#    #global x
#    
#    # put the statement inside the the func + return statement
#    # to afect it globally.
#    ## safer
#def func(x):
#    print('This function is now using the global x!')
#    print(f'Because of global x is: {x}')
#    x = 200
#    print(f'Run func(), changed global x to {x}')
#    return x
#
#print('Before calling func(), x is: ', x)
#func(x)
#print('Value of x (outside of func()) is: ', x)
#
#The global statement is used to declare that x is a global
# variable - hence, when we assign a value to x inside the
# function, that change is reflected when we use the value
# of x in the main block.
#
#You can specify more than one global variable using the 
# same global statement e.g. global x, y, z.
#
# One last mention is that you can use the globals()
# and locals() functions to check what are your current local
# and global variables.
#
#Another thing to keep in mind is that everything in Python
# is an object! I can assign variables to functions just 
# like I can with numbers!

## 57 Method n Functions Homework

# Write a function that computes the volume of a sphere
#given its radius.

#def vol(rad):
#    
#    pi = 3.14
#         
#    return (4/3)* pi * (rad**3)
#    
#print(vol(2))

# Write a function that checks whether a number is in a 
#given range (inclusive of high and low)

#def ran_check(num,low,high):
#    
#    return low < num < high
#
#print(ran_check(5,2,7))
    
## Write a Python function that accepts a string and calculates
# the number of upper case letters and lower case letters.

#def calc_UL_cases (sample): 
##
##    lowercase, uppercase = 0 , 0
#    lettercase = {'upper':0, 'lower':0}
#
#    for letter in sample:
#        if letter.isupper():
##            uppercase += 1
#            lettercase['upper'] += 1
#        elif letter.islower():
##            lowercase += 1
#            lettercase['lower'] += 1
#        else:
#            pass
##
##    print(f'{uppercase} uppercase')
##    print(f'{uppercase} uppercase')
##
#    print(f'{lettercase["lower"]} lowercase')
#    print(f'{lettercase["upper"]} lowercase')
##    
#calc_UL_cases('Hello Mr. Rogers, how are you this fine Tuesday?')

## Write a Python function that takes a list and returns a new list
# with unique elements of the first list.

#def unique_list(lst):
#    
#    return list(set(lst))
#
#print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


## Write a Python function to multiply all the numbers in a list.

#def multiply(numbers):
#
#    result = 1
#    
#    for n in numbers:
#        result *=  n
#    return result
#            
#print(multiply([1,2,3,-4]))


#   Write a Python function that checks whether a word or
# phrase is palindrome or not.

#def palindrome(s):
#    s.replace(' ','')
#
#    return s == s[::-1]
#
#print(palindrome('kayas'))

#   Write a Python function to check whether a string is
#pangram or not. (Assume the string passed in does not
#have any punctuation)

#import string
#
#def ispangram(str1, alphabet=string.ascii_lowercase):
#    
#    return set(alphabet) == set(list(str1.lower().replace(' ','')))
#
#print(ispangram("The quick brown fox jumps over the lazy dog"))

## 59 

## 60 

## 61

## 62 