
#Thank you for studying my code in detail. This is my first "real" Python program (ie besides the little bits of code
#I wrote while learning) and the very first time I'm using tkinter - I literary had to Google "how to do GUI in Python" to do this.
#So I'm sorry that you will not learn anything new or interesting here... Lucie
#11-Jan-2022, Lucie Kalvodova 

import pandas as pd
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def select_files():
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)  #note that filenames will be a tuple!
    filenames = sorted(filenames)  #so I'm convering it into a sorted list because usually the csv files' names will contain an index such as file1 file2 etc
    
    showinfo(
        title='Selected Files',
        message="Merging "+ str(len(filenames)) + " files in the following order: \n" + str(filenames)
        #message = filenames
    )
    merge_files(filenames)

    

	
def merge_files(files_to_merge): 
	try: 
		i=0
		allFiles = []
	
		df = [None]*len(files_to_merge)

		for myFile in files_to_merge:
			print("Adding " +files_to_merge[i])
			df[i] = pd.read_csv(files_to_merge[i])
			allFiles.append(df[i])
			print(allFiles)
			i=i+1
		
		myResult=pd.concat(allFiles, ignore_index=True, sort=False)
		myResult.to_csv('myMergedFiles.csv')
	except:
		tk.messagebox.showerror("Error :)", "There was an error!\nHowever, the world will continue to exist.")
		exit
	

myForm = tk.Tk()
myForm.text="Lucie's very first real Python program"
myForm.title('Merge csv files')
myForm.resizable(False, False)
myForm.geometry('300x100')


# open button
open_button = tk.Button(
    myForm,
    text='Select CSV files to merge',
    command=select_files
)

open_button.pack(expand=True)

myForm.mainloop()



