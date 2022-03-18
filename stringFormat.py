# str.format() = optional method that gives users more control when displaying output
# {} acts as placeholders

animal = "cow"
item = "moon"

#print("the "+animal+" jumped over the "+item)
#print("the {} jumped over the {}".format(animal,item))
#print("the {1} jumped over the {0}".format(animal,item)) #positional argument 
#print("the {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

text = "the {} jumped over the {}"

print(text.format(animal,item))

name = "nish"

print("hello my name is {} ".format(name))
print("hello my name is {:10}. nice to meet you".format(name))
print("hello my name is {:<10}. nice to meet you".format(name)) #left align
print("hello my name is {:>10}. nice to meet you".format(name)) #right align
print("hello my name is {:^10}. nice to meet you".format(name)) #center align

number = 1000

print("the number pi is {:.2f} ".format(number)) #will round your numbers
print("the number is {:,} ".format(number)) #adds a comma
print("the number is {:b} ".format(number)) #displays binary
print("the number is {:o} ".format(number)) #displays octal
print("the number is {:X} ".format(number)) #displays hexadecimal
print("the number is {:E} ".format(number)) #displays scientific notation
