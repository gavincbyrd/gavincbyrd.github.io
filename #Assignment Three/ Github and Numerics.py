#Assignment Three: Github and Numerics
#This code asks for userinput in the form of a base 10 number. 
#Then the code offers the user at least two options from other base systems, say base 2. 
# It then converts the user's number to those systems. 
#Print the converted output to the user.

#Get user input
number = int(input("Schreiben Sie eine Nummer hier, bitte: "))

#Convert to base 2
binary = bin(number)

#Convert to base 16
hexadecimal = hex(number)

#Print the results
print(f"binary:{binary}")
print(f"hexadecimal:{hexadecimal}")