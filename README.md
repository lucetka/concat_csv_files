# concat_csv_files
My first ever Python program

This is a simple GUI program which allows the user to select multiple csv files (they must have the same header, ie identical columns) and concatenate them - ie the resulting file can be manually created by opening one csv file and copying and pasting the content of another file without the header to the first empty row after the contents of the first csv file and doing this for all selected csv files. 
The resulting file will be saved under the name myMergedFiles.csv. 
There is only very simple error handling - if there is any error such as that the selected files are not valid csv files, no files are selected or if their headers don't match, or if there are other issues, this should cause the program to announce there was an error and let the user select files again.
Watch the video demo to see how it works. 
I cannot provide a compiled exe here because pyinstall generates a huge file (48MB) which takes a couple of seconds to launch. This seems to be a known issue with converting Python programs to single exe files and I need to learn more about it to find out if there is a way to reduce the size such as limiting imports.
