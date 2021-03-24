from cs50 import get_int

# Prompt user for height
answer = get_int("Height: ")

while answer < 1 or answer > 8:
    answer = get_int("Height: ")
    
# Print half-pyramids
for i in range(1, answer + 1):
    # Print first-half
    for j in range(answer - i):
        print(" ", end="")
    for j in range(i):
        print("#", end="")
        
    print("  ", end="")
    
    # Print second-half
    for j in range(i):
        print("#", end="")
        
    print()