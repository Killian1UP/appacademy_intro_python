
try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Everything went wrong")
finally:    # prints no matter if there is or no exception
    print("The 'try except' is finished")
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")  # raising an exception manually