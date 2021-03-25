import sys
import csv


def main():

    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read CSV file contents into memory
    database = {}
    strs = [] 
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        # Get column names
        header = next(reader) 
        for col in header:
            if col != "name":
                strs.append(col)
        rest = list(reader) 
        # Add individuals and their info to database
        for person in rest: 
            name = ""
            sequences = {}
            for i in range(len(header)): 
                if i == 0:
                    name = person[i]
                else:
                    sequences[header[i]] = int(person[i])
            database[name] = sequences

    # Read txt file contents into memory
    file = open(sys.argv[2], "r")
    dna = file.read() 
    # Track longest run
    counts = {} 
    for s in strs:
        counts[s] = 0
    # Search dna
    currentIndex = 0
    for base in dna: 
        for s in strs: 
            # Get longest run from that index
            if dna[currentIndex:(currentIndex + len(s))] == s: 
                count = get_longest_run(s, dna[(currentIndex + len(s)):])

                # Update longest run
                if count > counts[s]:
                    counts[s] = count
        currentIndex += 1
        
    # Find matched individuals 
    match = ""
    for key in database.keys(): 
        count = 0
        for s in strs:
            if counts[s] == database[key][s]:
                count += 1
        if count == len(strs):
            match = key
            
    # Print results
    if match == "":
        print("No match")
    else:
        print(f"{match}")


# Gets the count of the longest run
def get_longest_run(s, dna):
    count = 1
    # Check for consecutive strs
    currentIndex = 0
    isConsecutive = True
    while isConsecutive:
        if dna[currentIndex:(currentIndex + len(s))] == s:
            count += 1
            currentIndex += len(s)
        else:
            isConsecutive = False
            
    return count
    

main()