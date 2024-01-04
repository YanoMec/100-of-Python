# Caesar Cipher

#simple function
# def greet():
#     print("Hello")
#     print("this is a test")
#     print("statement 3")

# greet()

#Fucntion that allows input

# def greet_with_name(name):
#     print(f'Hello {name}')
#     print(f'How do you do {name} ?')

# greet_with_name("Cem")

#Function with more than 1 input.
# def greet_with(name,location):
#     print(f'Good Day {name}!')
#     print(f'How is the weather at {location}?')

# greet_with(location="Glasgow",name="Cem")
test_h = 4
test_w = 5
coverage = 5
number_of_cans = 0 
def paint_calc(height,width,cover):
  number_of_cans = ((height*width)/cover)
  print(round(number_of_cans))
paint_calc(height=test_h, width = test_w,cover=coverage)