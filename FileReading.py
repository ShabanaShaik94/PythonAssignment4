# Reading a File and Handle Errors
try:
    # Open the file in read mode
    with open('sample.txt', 'r') as file:
        # Read and print each line from the file
        for line in file:
            print(line)
except FileNotFoundError:
    # Handle the error if the file does not exist
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")
