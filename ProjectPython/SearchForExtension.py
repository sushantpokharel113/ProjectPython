#Write a script to search any file extension in your laptop.
#For example: if I give query as &quot;png&quot;, your program should list all png image files that are in your system.


import os

filelist = []
exten_list = []

extension = input("Which extension do you want to search?")
final_extension = "." + extension
for root, dirs, files in os.walk('.', topdown=True):
    filelist.append(files)

for files in filelist:
    for file in files:
        if final_extension in file:
            exten_list.append(file)
else:
    print("Invalid Extension")

for exten in exten_list:
    print(exten)

option = input("Search for a file ?")
if 'y' in option.lower():
    filename = input("Enter filename or keyword")
    for exten in exten_list:
        if filename.lower() in exten.lower():
            print(exten)
    # else:
#        print("No such filename found!!!")
else:
    print("Thanks for using Search Tool")

