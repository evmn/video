#!/usr/bin/python3

'''
Rename b_ext file to match a_ext file
All files include string like "S01E01"(case insensitive)

Reference: https://gist.github.com/jasalt/5322340
'''

import os
import re

a_ext = ["mkv","avi","mp4"]
b_ext = ["sub", "srt"]

all_files = os.listdir('.')  # List current directory items

a_list = [f for f in all_files if f[-3:].lower() in a_ext]
b_list = [f for f in all_files if f[-3:].lower() in b_ext]
print(b_list)

unmatched = [f for f in b_list if f[:-4] not in a_list]

for b_file in unmatched:
    print('Finding matches for: "%s"' % b_file)

    IDs = re.findall(r"S\d{2}E\d{2}", b_file.upper())[0]
    print('  ID number is: "%s"' % IDs)
    for a_file in a_list:
        match = re.search("%s" % IDs, a_file.upper())
        if match:
            b_new = a_file[:-3] + b_file[-3:].lower()
            print('    !found match: "%s", new filename: "%s"' % (a_file,b_new))
            if b_new not in b_list:
                print('    !Renaming:    "%s" -> "%s"\n' % (b_file,b_new))
                os.rename(b_file,b_new)
