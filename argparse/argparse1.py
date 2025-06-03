##import argparser
import argparse

##build the parser, create parser object

parser = argparse.ArgumentParser(description="hello this is new")

## parse the arguments

parser.add_argument('filename', help="this is the file to work on")
parser.add_argument('--limit','-l', help="check the length of the file")

args= parser.parse_args()

with open(args.filename) as f:
    lines=f.readlines()
    new_lines= lines[::-1]
print(new_lines)
    
    



