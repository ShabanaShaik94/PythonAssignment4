# Write and Append data to a File

# Open the file in write mode ('w') to overwrite
with open('output.txt', 'w') as file1:
    content_to_write = "Hello, Python!"
    file1.write(content_to_write)
    file1.close();
    # Print the confirmation
    print(f"Enter text to write to the file : {content_to_write}")
    print(f"Data successfully written to {file1.name}")


# Open the file in append mode ('a')
with open('output.txt', 'a') as file1:
    content_to_write = "\nLearning file handling in Python."
    file1.write(content_to_write)
    file1.close();
    # Print the confirmation
    print(f"Enter additional text to append: {content_to_write}")
    print(f"Data successfully appended.")

file1=open('output.txt','r')
reading_file=file1.read()
print(reading_file);
file1.close();