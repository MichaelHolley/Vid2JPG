from tkinter import filedialog, messagebox
from tkinter import *
import cv2
import os
import time

filePath = ""
outputFolderPath = ""

def selectVideo():
    global filePath
    filePath = filedialog.askopenfilename(initialdir="C:\\", title="Select input-file", filetypes=(("input-file", "*.mp4"), ("all files", "*.*")))
    print("Selected Video: \t" + filePath)

def selectOutputFolder():
    global outputFolderPath
    outputFolderPath = filedialog.askdirectory(title="Select output folder")
    print("Selected Folder: \t" + outputFolderPath)

def convertVideoToImages():
    video = cv2.VideoCapture(filePath)

    date = time.strftime("%d-%m-%Y")
    localTime = time.strftime("%H-%M-%S")
    timedOutputFolderPath = outputFolderPath + "/" + date + "_" + localTime
    print("Final Output-Folder: \t" + timedOutputFolderPath)

    if not os.path.exists(timedOutputFolderPath):
        os.makedirs(timedOutputFolderPath)

    success,image = video.read()
    i = 0
    success = True
    while success:
        success,image = video.read()
        if(success):
            cv2.imwrite(timedOutputFolderPath + "/" + "frame%d.jpg" % i, image)
            if cv2.waitKey(10) == 27:
                break
            i += 1
        else:
            sys.exit()

Label(text="Video:", width=20).grid(row=0,column=0)
Button(text="Select", command=selectVideo, width=10).grid(row=0, column=1)

Label(text="Output-Folder:", width=20).grid(row=1, column=0)
Button(text="Select", command=selectOutputFolder, width=10).grid(row=1, column=1)

Button(text="Start", command=convertVideoToImages, width=10).grid(row=2, column=0)

mainloop()

