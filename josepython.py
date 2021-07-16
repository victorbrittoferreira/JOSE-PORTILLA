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
#print(y.split('i'))

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

my_list1 = [1,2,3]
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

my_lis = A + B

sec_lis = C