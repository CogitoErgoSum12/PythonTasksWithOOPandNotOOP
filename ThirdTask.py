
import sys


def changeRegister(text):
    register_text = ""
    for i in range(0, len(text)):
        element = text[i]
        if element.islower() == True:
            element = element.upper()   
            register_text += element
        else:
            element = element.lower()
            register_text += element

    return register_text
        
input_text = sys.argv[1]
print(changeRegister(input_text))

