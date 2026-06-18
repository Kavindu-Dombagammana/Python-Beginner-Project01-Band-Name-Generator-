#Print function to print the output
print("Hello World")

#use \n to add a new line
print("Hello World ! \nHello World ! \nHello World !")

print("Hello")
print("Word")

# is the same as:

print("Hello\nWorld")

# 2. String Concatenation
# Use the plus symbol `+` to concatenate different strings together

print("My name is" + " " + "Kavindu")

# will output: "My name is Kavindu"

#Multi line string in print function

print("""Shopping List\n
1. eggs
2. Flour
3. Butter
5. Tomato
6. Beef""")

#Input function to give user inputs to the system
# input("What is your name?")

print("Hello " + input("What is your name?") + "!")


#variable        Assign value
name         =    "Kavindu"
age = 21
#######################################
#variable names
#Valid
# name = "Kavindu"
# user_name = "Kavindu"
# user_name1 = "Kavindu"

#variable names
#Invalid
# 1name = "Kavindu" cant start with a number
# user name = "Kavindu" cannot have spaces
#########################################

#can print the variables
print(name)
print(age)

new_name = input("What is your name?")
print(new_name)

# #variables are case sensitive and can be overwritten

# ##################################################
my_name = "Kav"
print(my_name)

my_name = "Divine"
print(my_name)
##################################################
#the variable take the first value, print it and then takes the second value and overwrite the first value of my_name variable

print(len(input("Your Name : ")))

username = input("Please enter your username : ")
length = len(username)
 
print("Your username " + username + " is " + str(length) + " characters Long.")
