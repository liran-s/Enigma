# Write here some instructions and guidance


# Task 1: We want to be able to get the index of a given letter 'c' in the ABC. Lets call this new function abc_index(c)
# For example: abc_index(a) = 0
#              abc_index(d) = 3
# In computers we prefer to start counting from 0 :-)

# In order to be able to implement abc_index(), lets meet python built-in function ord():
# The ord() function returns the number representing the unicode code of a specified character.

# Now lets play a bit with ord()..
# uncomment next line and run
print(ord('A'))

# uncomment the next line and run
print(ord('D'))

# What did happen? Can you think about how can we write abc_index() with that?

# Uncomment the next line and run:
print(ord('D') - ord('A'))

# Try to write now the implementation of abc_index(c):
#def abc_index(c):
# write here implementation and run

 #Here is an example of abc_index(c) which works:
def abc_index(c):
    index = ord(c.upper()) - ord('A')
    print(f"index of {c} is {index}")
    return index
print (abc_index("g"))


# Task 1 completed succefully. Try to go back and to follow what we did already

# Task 2: We want to be able to get the letter from its unicode number:
# For that we have the Python chr() function which returns the character that represents the specified unicode.

# Uncomment and run the next 6 lines till line 45
#c = 'A'
#a = ord(c)
#print(a)
#print(chr(a))
#print(chr(a+1))
#print(chr(a+2))

# Task 2 completed

# Now lets assume our Enigma machine has the following wiring:
WIRING = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

# Task 3: We want to be able to get the index of a given letter in the Enigma wiring: e.g wiring_index('M') = 2
#                      wiring_index('j') = ?? <- what do you think it should be?
# For that we use the find() function of string. Since WIRING is a string, we can call its find() function to look for the index of the letter c:

#def wiring_index(c):
#    return WIRING.find(c.upper())

# Uncomment next 2 lines and run:
#print(wiring_index('M'))
#print(wiring_index('J'))

# What is the wiring index of 'J'?
# Task 3 completed!

# Task 4: Now we want to implement the rotator function map_r_to_l(c) which takes c as a letter on the right side of rotator and return what we will get on the left side
# We will need to get the abc_index of c and access that index in WIRING to get the mapped letter
#def map_r_to_l(c):
#    # print(f"Need to map {letter}")
#    return WIRING[abc_index(c)]

# Uncomment and run the following line:
#print(map_r_to_l('A'))

# Task 5: We want to implement the opposite rotator function from Left to Right. We will need to get the wiring index of the letter c then trasform it to the unicode and run get character of it

#def map_l_to_r(c):
#  print(f"Need to map {c}")
#  return chr(wiring_index(c) + ord("A"))

# Uncomment and run the following line:
#print(map_l_to_r('J'))

  # Task 5 completed with huge success!!

# Uncomment the following lines to see all abc mappings:
#print(f"Assume we have this wiring {WIRING}")
#print("Here are rotor maps:")
# Loop over ABC as follow
#for i in range(26):
#    c = chr(i + ord("A"))
#    print(f"map R: {c} to L: {map_r_to_l(c)}")
#    print(f"map L: {c} to R: {map_l_to_r(c)}")
