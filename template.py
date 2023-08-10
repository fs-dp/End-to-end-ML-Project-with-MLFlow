# Import necessary libraries
import os  # For operating system related functionalities
from pathlib import Path  # For working with file paths
import logging  # For logging messages

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "mlProject"

# List of files and directories to create
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

# Function to create directories and files
def create_directories_and_files(file_list):
    for file_path in file_list:
        # Create parent directories if they don't exist
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        # Create and open the file for writing
        with open(file_path, 'w') as f:
            f.write('')  # Write an empty string to the file

# Main code execution
if __name__ == "__main__":
    # Call the function to create directories and files
    create_directories_and_files(list_of_files)
    # Log a message to indicate successful completion
    logging.info("Project directory structure and files have been created.")
