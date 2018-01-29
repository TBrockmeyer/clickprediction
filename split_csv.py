import os

def split_csv(path_to_csv_file, destination_filename, number_of_lines_per_file):
    command = 'split -dl ' + number_of_lines_per_file + ' --additional-suffix=.csv ' + path_to_csv_file + ' ' + destination_filename
    os.system(command)

if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 4:
        print ("-- ONLY USE ON LINUX/UBUNTU MACHINES -- Usage: python split_csv.py path_to_csv_file destination_filename number_of_lines_per_file")
    else:
        # PATH TO FILE TO BE SPLITTED ON YOUR DISK
        path_to_csv_file = sys.argv[1]
        # DESTINATION FOLDER OF FILES ON YOUR DISK
        destination_filename = sys.argv[2]
        # NUMBER OF LINES PER SPLIT FILE
        number_of_lines_per_file = sys.argv[3]
        split_csv(path_to_csv_file, destination_filename, number_of_lines_per_file)