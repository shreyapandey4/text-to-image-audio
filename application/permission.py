import os

directory_path = 'application/static/uploaded_files'

# Check if the directory is readable
if os.access(directory_path, os.R_OK):
    print(f"Directory '{directory_path}' is readable")
else:
    print(f"Directory '{directory_path}' is not readable")

# Check if the directory is writable
if os.access(directory_path, os.W_OK):
    print(f"Directory '{directory_path}' is writable")
else:
    print(f"Directory '{directory_path}' is not writable")

# Check if the directory is executable
if os.access(directory_path, os.X_OK):
    print(f"Directory '{directory_path}' is executable")
else:
    print(f"Directory '{directory_path}' is not executable")
