# File Renamer

## Overview

The File Renamer is a Python script that helps you manage and rename files within a specified directory. It renames files in a sequence and allows you to insert a new file at a specific position, renaming other files accordingly to maintain the sequence.

## Features

- **Batch Rename**: Automatically renames files in a specified directory to maintain a sequential order.
- **File Insertion**: Inserts a new file at a specified position and renames existing files to accommodate the new file.
- **Graphical User Interface**: Provides a simple GUI to select the directory and file for insertion.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python installations)
- `logging` library (standard Python library)

## Usage

1. **Run the Script**: Execute the script by running `python file_renamer.py` in your terminal.
2. **Select Directory**: Use the file dialog to choose the directory containing the files you want to rename.
3. **Select New File**: Use the file dialog to choose the new file you want to insert.
4. **Specify Position**: Enter the position at which you want to insert the new file.
5. **Complete**: The script will rename the files and insert the new file at the specified position.

## Logging

The script logs its operations to a file named `file_renamer.log` in the same directory as the script. This log file contains information about the renaming process and any errors encountered.

## Code Explanation

### Main Functions

- **rename_files(directory)**: Renames files in the specified directory to maintain a sequential order.
- **insert_file(directory, new_file_path, position)**: Inserts a new file at the specified position and renames other files to accommodate the new file.
- **run_script()**: Runs the main logic of the script, including file dialogs and user input.
- **create_gui()**: Creates the graphical user interface.

### Logging

The script uses the `logging` library to log important events and errors. Log messages are written to `file_renamer.log`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or issues, please contact the project maintainer.
