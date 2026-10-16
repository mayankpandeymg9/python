a = "Hello G, I am The Top G. The only Alpha of  the whole world."

#**********length*********

'''
print(len(a))
 >>> 60
 
 '''

#*********Count*************
'''
print(a.count("Alpha"))
>>> 1
'''

#***********Upper**********

'''print(a.upper())

>>>HELLO G, I AM THE TOP G. THE ONLY ALPHA OF  THE WHOLE WORLD.
'''


#**********Lower***********

'''
print(a.lower())

>>> hello g, i am the top g. the only alpha of  the whole world.
'''

#***********index**********
'''
print(a.index('G'))

>>>6

'''


#**********capitalize******

'''
print(a.capitalize())

>>>Hello g, i am the top g. the only alpha of  the whole world.
'''

#*********casefold*******

'''
print(a.casefold())

>>>hello g, i am the top g. the only alpha of  the whole world.
'''

#**********find*********

'''
print(a.find("I"))
>>>9
'''

#********Format********
'''
a1 = "Hello G, I am The Top G. {} The only Alpha of  the whole world."
n = "Meow"
print(a1.format(n))

>>>Hello G, I am The Top G. Meow The only Alpha of  the whole world.
'''

#*********center**********
'''
n = "John"
print(n.center(10,"*"))

>>>***John***

'''