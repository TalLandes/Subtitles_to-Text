import os
import glob
import re
from operator import itemgetter
import sys



if len(sys.argv) != 2:
    print("Wrong number of command line arguments")
    print("example: python3 Python_to_Script.py <Directory name>")
    exit(-1)


Class_Name = sys.argv[1]

for filepath_root in glob.iglob(Class_Name + '/*'):
    folder_name = os.path.basename(os.path.normpath(filepath_root))
    print(folder_name)
    new_folder = 'texts/' + Class_Name + '/' + folder_name
    if not os.path.exists(new_folder):
        os.makedirs(new_folder);



    #First go through the file name, get the numbers and sort them.
    file_list = []
    for filepath_chapter in glob.iglob(filepath_root + '/*.srt'):

        number = re.sub(' - .*', '', os.path.basename(filepath_chapter))

        file_list.append({'FileName': filepath_chapter,
                          'Num':      int(number),
            })

    #Same list as above just orderred by lesson number
    newlist = sorted(file_list, key=itemgetter('FileName'))


    #Go through the files and write them into one file
    text_file = open(new_folder + '/' + folder_name + '.txt', "w")
    for file_in_list in newlist:

        Subtitle_file_token = open(file_in_list['FileName'], "r")
        file_contents = Subtitle_file_token.read()

        #Remove all the timing and other not interesting content
        file_contents = re.sub('\n.*\n\d\d:\d\d:.*\n', '', file_contents)
        file_contents = re.sub('1\n\d\d:\d\d:.*\n',    '', file_contents)
        #Some files have that in there. No danger in just removing it.
        file_contents = re.sub('\n\[BLANK_AUDIO\]', '', file_contents)

        #Put a line between the videos to seperate the capters somewhat.
        text_file.write("\n========================================================================================================================\n")
        #Add filename for refrence and also to make sure it's right.
        text_file.write("[ " + os.path.basename(file_in_list['FileName']) + " ]\n")

        text_file.write(file_contents)

        Subtitle_file_token.close()

    text_file.close()

