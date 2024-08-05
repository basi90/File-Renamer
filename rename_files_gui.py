import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import logging

# Configure logging
logging.basicConfig(filename="file_renamer.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def rename_files(directory):
    logging.info(f"Renaming files in directory: {directory}")
    files = sorted(os.listdir(directory))
    logging.debug(f"Original files: {files}")
    num_pattern = re.compile(r"^(\d+)\. ")
    files_with_nums = sorted([(file, int(num_pattern.search(file).group(1))) for file in files if num_pattern.search(file)], key=lambda x: x[1])
    logging.debug(f"Files with numbers: {files_with_nums}")

    temp_files = {}

    # Rename files to temporary names to avoid conflicts
    for i, (file, num) in enumerate(files_with_nums):
        new_num = i + 1
        temp_name = f"temp_{new_num}_{file}"
        os.rename(os.path.join(directory, file), os.path.join(directory, temp_name))
        temp_files[temp_name] = file
        logging.info(f"Temporarily renamed {file} to {temp_name}")

    # Rename temporary files to final names
    for temp_name, original_name in temp_files.items():
        new_num = int(re.search(r"temp_(\d+)_", temp_name).group(1))
        title = original_name.split(' ', 1)[1]  # Get the title part
        final_name = f"{new_num}. {title}"
        os.rename(os.path.join(directory, temp_name), os.path.join(directory, final_name))
        logging.info(f"Renamed {temp_name} to {final_name}")

def insert_file(directory, new_file_path, position):
    logging.info(f"Inserting file: {new_file_path} at position: {position} in directory: {directory}")
    files = sorted(os.listdir(directory))
    logging.debug(f"Current files: {files}")
    num_pattern = re.compile(r"^(\d+)\. ")
    files_with_nums = sorted([(file, int(num_pattern.search(file).group(1))) for file in files if num_pattern.search(file)], key=lambda x: x[1])
    logging.debug(f"Files with numbers: {files_with_nums}")

    # Correct validation for the position
    if position < 1 or position > len(files_with_nums) + 1:
        raise ValueError("Invalid position to insert the new file.")

    # Move files to make space for the new file
    for i in range(len(files_with_nums), position - 1, -1):
        src = os.path.join(directory, files_with_nums[i-1][0])
        dst = os.path.join(directory, f"temp_{i + 1}_{files_with_nums[i-1][0]}")
        os.rename(src, dst)
        logging.info(f"Moved {src} to {dst}")

    new_file_name = os.path.basename(new_file_path)
    title = new_file_name.split(' ', 1)[1]  # Get the title part
    insert_name = f"{position}. {title}"
    insert_path = os.path.join(directory, insert_name)
    os.rename(new_file_path, insert_path)
    logging.info(f"Inserted {new_file_name} as {insert_name}")

    # Rename temporary files to final names
    for i in range(position, len(files_with_nums) + 1):
        temp_name = f"temp_{i + 1}_{files_with_nums[i - 1][0]}"
        title = files_with_nums[i - 1][0].split(' ', 1)[1]  # Get the title part
        final_name = f"{i + 1}. {title}"
        if os.path.exists(os.path.join(directory, temp_name)):
            os.rename(os.path.join(directory, temp_name), os.path.join(directory, final_name))
            logging.info(f"Renamed {temp_name} to {final_name}")
        else:
            logging.warning(f"Temporary file {temp_name} does not exist")

def run_script():
    try:
        directory = filedialog.askdirectory(title="Select Directory")
        if not directory:
            return

        new_file_path = filedialog.askopenfilename(title="Select New File")
        if not new_file_path:
            return

        files = sorted(os.listdir(directory))
        num_pattern = re.compile(r"^(\d+)\. ")
        files_with_nums = sorted([(file, int(num_pattern.search(file).group(1))) for file in files if num_pattern.search(file)], key=lambda x: x[1])

        position = simpledialog.askinteger("Input", "Enter the position to insert the new file:", minvalue=1, maxvalue=len(files_with_nums) + 1)
        if not position:
            return

        rename_files(directory)
        insert_file(directory, new_file_path, position)

        messagebox.showinfo("Success", "Files have been renamed and new file inserted successfully.")
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        messagebox.showerror("Error", str(e))

def create_gui():
    root = tk.Tk()
    root.title("File Renamer")

    frame = tk.Frame(root)
    frame.pack(padx=64, pady=64)

    run_button = tk.Button(frame, text="Run", command=run_script)
    run_button.pack(side=tk.LEFT, padx=5, pady=5)

    quit_button = tk.Button(frame, text="Quit", command=root.quit)
    quit_button.pack(side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
