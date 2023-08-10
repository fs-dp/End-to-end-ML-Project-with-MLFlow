""" The __init__.py file in the src folder serves as an initialization module for the project's logging system. 
It sets up logging configuration to control how log messages are formatted and where they are stored. 
The purpose of this file is to provide a consistent and convenient way to manage logging throughout our project.

Here's what each part of the code does:

import os, import sys: Import the necessary modules for interacting with the operating system and system-specific functionality.
import logging: Import the Python built-in logging module to manage and output log messages.
logging_str: Define a string format that specifies how log messages should be formatted. It includes a timestamp, log level, module name, and the log message itself.
log_dir: Define the directory where log files will be stored.
log_filepath: Create the full path to the log file within the specified directory.
os.makedirs(log_dir, exist_ok=True): Create the log directory if it doesn't exist.
logging.basicConfig(...): Configure the logging system with the specified settings. This includes setting the logging level to INFO, formatting log messages using the defined logging_str, and specifying handlers for both writing log messages to a file and printing them to the console.
logger = logging.getLogger("mlProjectLogger"): Create a logger instance named "mlProjectLogger" that can be used throughout your project to log messages.
Overall, the __init__.py file initializes the logging system and sets up the necessary configuration to ensure that log messages are properly captured and formatted for both the log file and console output. It provides a foundation for maintaining a consistent logging approach across different parts of your project. """

import os
import sys
import logging

# Define the log format string with timestamp, log level, module, and message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create a directory for log files
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Use the defined format for log messages

    handlers=[
        logging.FileHandler(log_filepath),  # Save log messages to a file
        logging.StreamHandler(sys.stdout)   # Print log messages to the console
    ]
)

# Create a logger instance with the name "mlProjectLogger"
logger = logging.getLogger("mlProjectLogger")
