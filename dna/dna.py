import sys
import csv


def main():

    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py FILENAME.csv FILENAME.txt")

    # Read CSV file contents into memory
    database = {}
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Add dictionary


            print(f"{row}")


main()