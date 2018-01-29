# -*- coding: utf-8 -*-

import csv

def read_csv_simply(path_to_csv_file, number_of_rows):
    #with open(path_to_csv_file, newline='') as f:
    with open(path_to_csv_file, 'r') as f:
        reader = csv.reader(f)
        for i in range(int(number_of_rows)):
            print (i)
            print (next(reader))
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        print ("Usage: python read_csv_simply.py path_to_csv_file number_of_rows")
    else:
        # PATH TO CSV FILE TO BE EXPLORED ON YOUR DISK
        path_to_csv_file = sys.argv[1]
        # NUMBER OF ROWS TO BE SHOWN
        number_of_rows = sys.argv[2]
        read_csv_simply(path_to_csv_file, number_of_rows)