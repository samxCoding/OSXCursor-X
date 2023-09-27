import shutil

# Define the source and destination file paths
source_file = "path/to/source/file"
destination_file = "path/to/destination/file"

# Use shutil.copy2 to replace the destination file with the source file
try:
    shutil.copy2(source_file, destination_file)
    print(f"File '{destination_file}' has been replaced with '{source_file}'.")
except FileNotFoundError:
    print("One or both of the files do not exist.")
except PermissionError:
    print("Permission denied. Make sure you have the necessary permissions to replace the file.")
except Exception as e:
    print(f"An error occurred: {e}")
