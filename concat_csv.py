
#Thank you for studying my code in detail. I'm sorry that you will not learn anything new or interesting here... Lucie
#05-Jan-2022, Lucie Kalvodova 

import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

#import os

#filename = fd.askopenfilename()

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
    #print (len(filenames))
    #print (filenames[0])
    #print (filenames[1])
    

	
def merge_files(files_to_merge): 
	i=0
	allFiles = []
	
	#print(len(files_to_merge))
	
	df = [None]*len(files_to_merge)

	for myFile in files_to_merge:
		print("Adding " +files_to_merge[i])
		df[i] = pd.read_csv(files_to_merge[i])
		allFiles.append(df[i])
		print(allFiles)
		#allFiles.sort()
		#print(allFiles)
		i=i+1
	myResult=pd.concat(allFiles, ignore_index=True, sort=False)
	#myResult=pd.concat(allFiles)
	myResult.to_csv('myMergedFiles.csv')
	

myForm = tk.Tk()

myForm.title('Merge csv files downloaded from WoS')
myForm.resizable(False, False)
myForm.geometry('300x300')


# open button
open_button = ttk.Button(
    myForm,
    text='Select CSV Files to merge',
    command=select_files
)

open_button.pack(expand=True)

myForm.mainloop()



