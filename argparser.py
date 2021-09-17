import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', action='store_true', help="shows output")
parser.add_argument('-p', '--print', action='store_true', help="shows output")
parser.add_argument('-n', '--name', required=True)

args = parser.parse_args()

if args.output:
    print(f"This is some output --- LOL: {args.output}")

if args.print:
    print("This is some print --- LOL")

print(f"Hello {args.name}")