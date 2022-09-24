import sys
import ast

try:
    input_element = ast.literal_eval(sys.argv[1])
    print(type(input_element))
except:
    print("<class 'string'>")
