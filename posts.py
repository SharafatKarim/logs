#!/usr/bin/env python

# A building block!
# This script is made to copy markdown files
# prepand a header like,
# +++
# title = "Hello Friend"
# description = "This is a test post"
# +++
# and paste them to the content/posts directory.

import os

def read_first_line(file):
    with open(file, "r") as f:
        while True:
            str = f.readline()
            if not(str.startswith("#") or str == "\n"):
                break
        return str.strip()

def generate_posts():
    # for root, dirs, files in os.walk(os.curdir):
    dirs = os.listdir(os.curdir)
    # print(dirs)
    # for root, dirs, files in os.walk("src"):
    for directory in dirs:
        if (directory.isdigit and os.path.isdir(directory)):
            # get .md files in this directory
            for file in os.listdir(directory):
                if file.endswith(".md"):
                    with open(os.path.join(directory, file), "r") as src:
                        src_md = src.read()
                        if not os.path.exists("content/posts"):
                            os.makedirs("content/posts")
                        with open(f"content/posts/{file}", "w") as post:
                            post.write("+++\n")
                            post.write(f"title = \"{file[:-3]}\"\n")
                            post.write("description = \""+ read_first_line(os.path.join(directory,file)) + "\"\n")
                            post.write("+++\n")
                            post.write("\n")
                            post.write(src_md)
                            post.write("\n")
                            
if __name__ == "__main__":
    generate_posts()