import sys
import csv
from tabulate import tabulate
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(filename, newline="") as file:
            reader = csv.DictReader(file)
            table = [row for row in reader]
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(table, headers="keys", tablefmt="grid"))
if __name__ == "__main__":
    main()
