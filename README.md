# concat_csv_files
My first ever Python program

This is a simple GUI program which allows the user to select multiple csv files and concatenate them - ie for files with identical headers the resulting file can be manually created by opening one csv file and copying and pasting the content of another file without the header to the first empty row after the contents of the first csv file and doing this for all selected csv files. The program is based on the pandas.concat function and thus it also works for files with non-identical headers but this is not the primary purpose of this program. The point is to merge csv files presenting "batches" of the same results, specifically I wrote it to merge result files downloaded from Web of Science.

concat_csv4: The resulting file will be saved under the name myMergedFiles.csv

concat_csv5: This version allows the user to select location and file name for the resulting file.

Known issue: I decided to use wb mode to save the csv using pandas' to_csv method to avoid having blank rows added after each row, which is what to_csv seems to do when w  mode is used; even though using w mode in combination with line_terminator="\n" parameter prevented the blank rows, I ran into encoding problems with the w method.
Therefore I think that using the wb method is a safer option and it works perfectly on my Latitude with Python 3.8.2., but I was surprised to find out that it threw an error on my Surface with Python 3.6.3 (Anaconda) installed. 

There is only very simple error handling - if there is any error such as that the selected files are not valid csv files, no files are selected or if their headers don't match, or if there are other issues, this should cause the program to announce there was an error and let the user select files again.
Watch the video demo to see how it works.

I cannot provide a compiled exe here because pyinstall generates a huge file (48MB) which takes a couple of seconds to launch. This seems to be a known issue with converting Python programs to single exe files and I need to learn more about it to find out if there is a way to reduce the size such as limiting imports.
