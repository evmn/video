#!/usr/bin/python3
import glob
import os
for video in glob.glob('*.mp4'):
	audio = os.path.splitext(video)[0]+".aac"
	print("ffmpeg -i \"{0}\" -vn -acodec copy \"{1}\"".format(video, audio))
	os.system("ffmpeg -i \"{0}\" -vn -acodec copy \"{1}\"".format(video, audio))
