import pandas as pd

def explore_csv_range(path_to_csv_file, row_begin, row_end):
    df = pd.read_csv(path_to_csv_file)
    df_range = df.iloc[int(row_begin):int(row_end)]
    print (df_range)

if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 4:
        print ("Usage: python explore_csv_range.py path_to_csv_file row_begin row_end")
    else:
        # PATH TO CSV FILE TO BE EXPLORED ON YOUR DISK
        path_to_csv_file = sys.argv[1]
        # FIRST ROW TO BE DISPLAYED
        row_begin = sys.argv[2]
        # LAST ROW TO BE DISPLAYED
        row_end = sys.argv[3]
        explore_csv_range(path_to_csv_file, row_begin, row_end)
