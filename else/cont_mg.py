"""Create a context manager TempDir (Use Context Manager protocol - methods __enter__, __exit__):

When entering the context, a new temporary directory is created with a random, unique name. Use os.mkdir to create the directory.
Until exiting this context, the new created directory becomes the current one, and all actions are executed in the scope of this new directory.
When exiting this context, the temporary directory is removed with all files in it. Use rmtree from shutil to remove the whole directory.
The new working directory becomes the same as before entering the context."""

import os
import shutil
import random
import string
from time import sleep


class TempDir:
    def __init__(self):
        self.original_dir = None
        self.dir_name = "".join(
            random.choices(string.ascii_letters + string.digits, k=8)
        )

    def __enter__(self):
        os.mkdir(self.dir_name)
        os.chdir(self.dir_name)

        return self.dir_name

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir("../")

        shutil.rmtree(self.dir_name)


# with TempDir() as temp_dir:
#     print(f"Inside temporary directory: {os.getcwd()}")
#     # Perform file operations inside the temporary directory
#     sleep(1)

# # After exiting the context, the temporary directory should be removed
# print(f"Back to original directory: {os.getcwd()}")


"""Create a context manager Cd which changes the current directory to a pointed one. For example:

with Cd('/home')
When entering the context, you need to save the previous directory, and when you exit, you need to restore it. During context manager initialization, check that the passed directory is a directory and exists. If the passed directory is not a directory or does not exist, raise the ValueError. Use the following functions from the os module: getcwd, chdir, path.isdir"""


class Cd:
    def __init__(self, dir_name):
        if not os.path.isdir(dir_name):
            raise ValueError(f"'{dir_name}' is not a valid directory")

        self.dir_name = dir_name
        self.initial_dir = None

    def __enter__(self):
        self.initial_dir = os.getcwd()
        os.chdir(self.dir_name)

    def __exit__(self, exc_type, exc_value, ecx_traceback):
        os.chdir(self.initial_dir)


# with Cd("dnotes") as cd:
#     print(f"Inside of: {os.getcwd()}")
#     sleep(1)


"""Create a context manager LogFile inherited from the ContextDecorator, which adds text lines into a log file. Every text line must contain the following information:

The date and time started (Start:)
The execution time (Run:)
The error information (in the code wrapped by a context manager) (An error occurred:)
The trace format example when no errors occurred:

Start: 2021-03-22 12:38:24.757637 | Run: 0:00:00.000054 | An error occurred: None
The example in the case of a ZeroDivisionError exception

Start: 2021-03-22 12:38:24.758463 | Run: 0:00:00.000024 | An error occurred: division by zero
The log file name is passed as an argument to the text manager constructor. For example:

@LogFile('my_trace.log')
def some_func():
    ...
The log file has to be open in append mode to allow reopening the existing file and adding new information into this file if the same name is pointed.

When an exception happens, the error message has to be put in (An error occured): into the log and reraised upper.

Use the open built-in function to open the log file."""

from contextlib import ContextDecorator
from datetime import datetime

"""current_time = datetime.now()

# Format the time in the desired format
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")"""


class LogFile(ContextDecorator):
    def __init__(self, log_filename):
        self.log_filename = log_filename
        self.start = datetime.now()
        self.end = None

    def __enter__(self):
        self.file = open(self.log_filename, "a")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.now() - self.start
        self.file.write(
            f"Start: {self.start} | Run: {self.end} | An error occurred: {exc_val}\n"
        )
        self.file.close()


@LogFile("else/my_trace.log")
def some_func():
    return 5 / 0


print(some_func())
