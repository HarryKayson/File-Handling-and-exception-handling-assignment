"""
Assignment
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

"""
# Reading content from an existing file and writing it to a new file with modification
def modify_file(input_filename, output_filename):
    try:
        # Opening the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modifying the content (Example: convert to uppercase)
        modified_content = content.upper()

        # Opening the output file in write mode
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been modified and saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError as e:
        print(f"Error: {e}")

input_filename = input("Enter the input filename: ")
output_filename = input("Enter the output filename: ")
modify_file(input_filename, output_filename)
