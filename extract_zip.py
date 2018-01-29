import zipfile

def extract_zip(path_to_zip_file, destination_file_path):
    with zipfile.ZipFile(path_to_zip_file,"r") as zip_ref:
        zip_ref.extractall(destination_file_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        print ("Usage: python extract_zip.py path_to_zip_file destination_file_path")
    else:
        # PATH TO FILE TO BE UNZIPPED ON YOUR DISK
        path_to_zip_file = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination_file_path = sys.argv[2]
        extract_zip(path_to_zip_file, destination_file_path)