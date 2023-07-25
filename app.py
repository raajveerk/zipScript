import os
import schedule
import time
from zipfile import ZipFile

zipFile = " "
isFile = False
erZipFile = " "

def job():
    for file in os.listdir("C:/Users/Raajveer/Downloads"):
        if file.endswith(".zip"):
            zipFile = "C:/Users/Raajveer/Downloads/" + str(file)
            isFile = True
            break

    if (isFile == True):
        erZipFile = os.path.splitext(zipFile)[0]

        with ZipFile(zipFile, 'r') as zip:
            zip.extractall(path=erZipFile)
        
        print("Extracted the zip file successfully.")
            
        os.remove(zipFile)
        
        print("Removed the zip file successfully.")
    else:  
        print("No zip file found, Couldn't run the script.")
        
schedule.every(120).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(120)