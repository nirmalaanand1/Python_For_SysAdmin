import argparse

parser = argparse.ArgumentParser(description="This deals with exception handling")

parser.add_argument('filename',help="file to work on")
parser.add_argument('--limit','-l',help="lemgth of file")

args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]
        for line in lines:
            print(line.strip()[::-1])
finally:
    print("finally")