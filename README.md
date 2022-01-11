# concat_csv_files
My first ever Python program

This is a simple GUI program which allows the user to select multiple csv files (they must have the same header, ie identical columns) and concatenate them - ie the resulting file can be manually created by opening one csv file and copying and pasting the content of another file without the header to the first empty row after the contents of the first csv file and doing this for all selected csv files. 
The resulting file will be saved under the name myMergedFiles.csv with an added index column. 
There is currently no error handling, ie if the selected files are not valid csv files or if their headers don't match, or if there are other issues, the program is going to throw an error. I have to learn more about error handling and implement it. 
