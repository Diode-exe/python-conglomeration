import os

# Get the current directory
directory = os.getcwd()

# Loop through all files in the directory
for filename in os.listdir(directory):
    if " " in filename:
        new_name = filename.replace(" ", "-")
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"Renamed: '{filename}' -> '{new_name}'")
