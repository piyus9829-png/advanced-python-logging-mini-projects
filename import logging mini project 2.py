import logging
try:
    sgpa1=float(input("Enter your sgpa1: "))
    sgpa2=float(input("Enter your sgpa2: "))
    cgpa=(sgpa1+sgpa2)/2
    print("Your cgpa is: ",cgpa)
except ValueError:
    logging.error("Invalid input. Please enter numeric values for sgpa1 and sgpa2.")                    