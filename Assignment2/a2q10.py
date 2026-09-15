str1=str(input("Enter a string: "))
strlen_incspas=  len(str1)
strlen_excspas= len(str1.replace(" ",""))
strlen_worcont= len(str1.split())

print(strlen_incspas)
print(strlen_excspas)
print(strlen_worcont)
