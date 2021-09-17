#!/usr/bin/python3

""" rename multiple files in a given path """


import os

path = "/home/jon/Downloads/Export-5b4db77f-96ef-4377-ba37-61b5eabe24b8/HTB/📁 Windows/"  


def change_name(old_name,new_name):
    # change file/dir name from old to new
    try:
        os.rename(old_name,new_name)
        print ("Change: " + old_name + " >>> " + new_name)
    except IsADirectoryError:
        print("Source is a file but destination is a directory.")
    except NotADirectoryError:
        print("Source is a directory but destination is a file.")
    except PermissionError:
        print("Operation not permitted.")
    except OSError as error:
        print(error)


def clear_text(s):
    # from : "Tabby - 10 10 10 194 b343bfd79d724ea8aa2dbc957a24dab7.md" 
    # to   : "Tabby - 10 10 10 194.md"
    if len(s) < 30 : 
        return s      # in case we stumble apon a 'normal' file name. 
    if "md" in s:
        return (str(s.rsplit(" ", 1)[0]) + ".md")
    else:
        return s.rsplit(" ", 1)[0]


def rename_all(path):
    subdirs = []
    dirs = []
    files = []

    # get all dirs, subdirs and local files in order
    for subdir, dirs, files in os.walk(path,topdown=False):
        subdirs.append(subdir)
        dirs.append(dirs)
        files.append(files)
        
        # Caution! run the following lines only once at a given script. dont re-run the script after!
        # if you have some trouble after it, just mark it as a footnote with '#'   
        clear_subdir = clear_text(subdir)
        if clear_subdir == subdir:
            continue
        change_name(subdir, clear_subdir)
        subdir = clear_subdir
        # -----------------

        # step in the subdirs to change files name
        for count, filename in enumerate(os.listdir(subdir)):
            clear_name = clear_text(filename)
            if clear_name == filename:
                continue
            change_name((subdir + filename), (subdir + clear_name))
        


def main():
  rename_all(path)
  
if __name__ == '__main__':
    main()
    
