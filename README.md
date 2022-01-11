# concat_csv_files
My first ever Python program

This is a simple GUI program which allows the user to select multiple csv files (they must have the same header, ie identical columns) and concatenate them - ie the resulting file can be manually created by opening one csv file and copying and pasting the content of another file without the header to the first empty row after the contents of the first csv file and doing this for all selected csv files. 
The resulting file will be saved under the name myMergedFiles.csv with an added index column. 
There is only very simple error handling - if there is any error such as that the selected files are not valid csv files, no files are selected or if their headers don't match, or if there are other issues, this should cause the program to announce there was an error and let the user select files again.
