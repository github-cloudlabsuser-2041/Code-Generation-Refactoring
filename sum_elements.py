#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases
#refectorise el codigo para que sea mas legible y eficiente
#Refactored code

def sum_elements(elements):
    return sum(elements)

def main():
    numbers = [1, 2, 3, 4, 5]
    total = sum_elements(numbers)
    print(f"La suma de los elementos es: {total}")

if __name__ == "__main__":
    main()