"""Create a context manager TempDir (Use Context Manager protocol - methods __enter__, __exit__):

When entering the context, a new temporary directory is created with a random, unique name. Use os.mkdir to create the directory.
Until exiting this context, the new created directory becomes the current one, and all actions are executed in the scope of this new directory.
When exiting this context, the temporary directory is removed with all files in it. Use rmtree from shutil to remove the whole directory.
The new working directory becomes the same as before entering the context."""

import os
import shutil


class TempDir:
    def __init__(self):
        print("__init__ method called")

    def __enter__(self):
        print("__enter__ method called")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("__exit___ method called")
