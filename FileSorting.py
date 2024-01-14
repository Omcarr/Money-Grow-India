import os
import shutil

def move_files(source_folder,client_name,client_id):
    destination_folder=f"{source_folder}{client_name.strip()}"

    #create dedicated folder for each client if it doesnt exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of files in the source folder
    all_pdfs = os.listdir(source_folder)

    # Iterate through each file in the source folder
    for pdf_name in all_pdfs:
        id=pdf_name.split('_')
        if str(client_id) in id:
            source_file_path = os.path.join(source_folder, pdf_name)

            #check the file extension
            _, file_extension = os.path.splitext(source_file_path)
            file_ext=file_extension.lower()
            
            if file_ext=='.pdf':
                # Move the file to the destination folder
                if os.path.exists(source_file_path):
                 shutil.move(src=source_file_path, dst=destination_folder)

