import sqlite3
import os
from shutil import copyfile

print ("CopyingData..............")
oscwd = os.getcwd()
db = 'C:\\Users\\Mech Warriors\\Desktop\\2019_Scouting_App\\db'
dbnew = 'db'
filestart = 0

for filename in os.listdir("D:/"):
    if filename.endswith(".sqlite3"):
        filenamenum = filename[-4:-3]
        if int(filenamenum) > filestart:
            filestart = int(filenamenum)

dbnew = 'db' + str(filestart+1)
print(dbnew)
copyfile(db+'.sqlite3', 'D:/'+ dbnew + '.sqlite3')
#'573MatchScouting.db'
print ('Data Export Complete')
