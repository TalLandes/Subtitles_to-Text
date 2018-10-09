


import os
import glob
import re
from operator import itemgetter

Class_Name = "Advanced Operating Systems Subtitles"

for filepath_root in glob.iglob(Class_Name + '/*'):
    #print("==========================================================================")
    folder_name = os.path.basename(os.path.normpath(filepath_root))
    print(folder_name)
    new_folder = 'texts/' + Class_Name + '/' + folder_name
    if not os.path.exists(new_folder):
        os.makedirs(new_folder);



    #first go through the file name, get the numbers and sort them.
    file_list = []
    for filepath_chapter in glob.iglob(filepath_root + '/*.srt'):

        number = re.sub(' - .*', '', os.path.basename(filepath_chapter))

        file_list.append({'FileName': filepath_chapter,
                          'Num':      int(number),
            })

    #same list as above just orderred.
    newlist = sorted(file_list, key=itemgetter('FileName'))


    # go through the files and write them into one file
    text_file = open(new_folder + '/' + folder_name + '.txt', "w")
    for file_in_list in newlist:
        #print(L)
        f = open(file_in_list['FileName'], "r")
        file_contents = f.read()
        file_contents = re.sub('\n.*\n\d\d:\d\d:.*\n', '', file_contents.rstrip())
        file_contents = re.sub('1\n\d\d:\d\d:.*\n', '', file_contents.rstrip())

        #put a line between the videos to seperate the capters somewhat, and add filename to make sure ordering was right
        text_file.write("\n========================================================================================================================\n")
        text_file.write("[ " + os.path.basename(file_in_list['FileName']) + " ]\n")

        text_file.write(file_contents)

        f.close()

    text_file.close()

