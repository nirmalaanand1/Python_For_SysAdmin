import argparse
import sys

parser = argparse.ArgumentParser(description="exception handling wth exit code 2")
parser.add_argument('filename')
parser.add_argument('--limit','-l')

args = parser.parse_args()

try:
  f = open(args.filename)
  limit = args.limit
except FileNotFoundError as err:
  print(f"Error: {err}")
  sys.exit(2)
else:
  with f:
    lines = f.readlines()
    lines.reverse()
    for line in lines:
      print(line.strip()[::-1])

finally:
   print("this is done")