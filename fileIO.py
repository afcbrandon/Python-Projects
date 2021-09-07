
import os, sys, time


path = '/Users/b/Documents/text/'
time = os.path.getmtime("/Users/b/Documents/text/")


def read_text_file():
    with open("/Users/b/Documents/text/", 'r') as f:
        print(f.read())

for file in os.listdir():
    if file.endswith(".txt"):
        print (read_text_file, time)

