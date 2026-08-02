import logging
try:
    sgpa = float(input("Enter your SGPA: "))
    if sgpa != 6.5 and sgpa >= 9.2:
        print("You are eligible for the scholarship.")
    else:
        print("You are not eligible for the scholarship.")
except ValueError:
    logging.error("Invalid input. Please enter a numeric value for SGPA.")