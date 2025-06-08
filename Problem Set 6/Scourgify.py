import sys
import csv
def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    try:
        with open(input_file, "r", newline="") as infile:
            reader = csv.DictReader(infile)
            students = []
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                students.append({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
    with open(output_file, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)
if __name__ == "__main__":
    main()
