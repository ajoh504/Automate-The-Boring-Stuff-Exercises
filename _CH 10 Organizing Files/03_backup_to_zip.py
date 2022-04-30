#! python3
# 02_backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backup_to_zip(folder):
    # Back up the entire contents of "folder" into a ZIP file
    folder = os.path.abspath(folder) # Make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1

    # Create the ZIP file
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    
    # Walk the entire folder tree and compress the files in each folder
    for folder_name, sub_folders, file_names in os.walk(folder):
        print(f'Adding files in {folder_name}...')
        # Add the current folder to the ZIP file
        for file_name in file_names:
            new_base = os.path.basename(folder) + '_'
            if file_name.startswith(new_base) and file_name.endswith('.zip'):
                continue # don't back up the ZIP files
            backup_zip.write(os.path.join(folder_name, file_name))
    backup_zip.close()
    print('Done.')
    
backup_to_zip('C:\\delicious')

