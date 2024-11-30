# File Read & Write Challenge
def modify_and_save_file():
    try:
        # Ask the user for the filename
        filename = input("Please enter the filename to read from: ")
        
        # Attempt to open and read the original file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (for example, let's convert it to uppercase)
        modified_content = content.upper()  # You can modify this logic based on your needs
        
        # Ask for a new filename to save the modified content
        new_filename = input("Enter the filename to save the modified content: ")
        
        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content has been written to {new_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    
    except IOError:
        print("Error: The file could not be read or written.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to run the program
modify_and_save_file()
