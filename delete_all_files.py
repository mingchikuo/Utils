import os
from tqdm import tqdm

check = input('Warning! Are you sure you want to delete all files? (Y/N)')
if check == 'Y':
    all_files = os.listdir("./")
    for file in tqdm(all_files):
        os.remove(file)

