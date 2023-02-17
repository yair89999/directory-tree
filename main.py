import os

__version__ = "1.0.0"

print("\n\n\n")

# the idea is from "https://realpython.com/directory-tree-generator-python/"

checking_path = "" # optional(can place the path in the input, next line)
checking_path = input("Enter the folder's path(the full path):\n")

os.chdir(checking_path)

pipe = "│"
elbow = "└──"
tee = "├──"
pipe_prefix = "│   "
space_prefix = "    "

folders_tree = {}


def folders_files_recursion(folders_list,parent_string): # parent_string => what should be before the folder/file
    final_dict = {}

    original_parent_string = parent_string
    for name in folders_list:
        if name == folders_list[-1]:
            print(parent_string + elbow,name)
        else:
            if "." in name:
                print(parent_string + tee,name)
            else:
                print(parent_string + elbow,name)
            
        if "." in name:
            final_dict[name] = ""
        else:
            parent_string += pipe_prefix
            
            folders = os.listdir(name)
            os.chdir(name)
            final_dict[name] = folders_files_recursion(folders,parent_string)

            path_parent = os.path.dirname(os.getcwd()) # goes one folder before, for example c:\\users => c:\\
            os.chdir(path_parent)
        parent_string = original_parent_string
        
    return final_dict

print("...\\"+checking_path.split("\\")[-1]+"\\")
print(pipe)

files_in_main_folder = os.listdir(checking_path)
for name in files_in_main_folder:
    parent_string = ""
    if name == files_in_main_folder[-1]:
        print(elbow, name)
        parent_string += space_prefix
    else:
        parent_string += pipe + space_prefix
        print(tee, name)
    if "." in name:
        folders_tree[name] = ""
    else:
        """the dict.update(dict) function => appending the dict that is in the () to the dict before the .update, no need to do dict = .update()..."""
        os.chdir(checking_path + "\\" + name)
        folders_tree.update( folders_files_recursion( os.listdir(),parent_string ) ) # appends folders_files_recursion([name]) to folders_tree


exit()
print("\n\nfinal dict:")
for name in folders_tree:
    print(name,":",folders_tree[name])
