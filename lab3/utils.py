
def txt_to_dict(txt: str, type: bool = False):
#False for user data, True for project data
    if type:
        # project data
        keys = ["name", "details", "target", "start_date", "end_date", "status", "owner"]
    else:
        # user data
        keys = ["name", "email", "password", "phone"]

    data = []
    lines = txt.splitlines()
    for line in lines:
        values = line.split("||")
        data.append(dict(zip(keys,values)))

    return data

import os

def append_to_file (data: dict, type: bool = False):
    #false for user data, true for project data
    file_path = 'projects.txt' if type else 'users.txt'
    txt = '||'.join(data.values())

    with open(file_path, 'a') as f:
        f.write(f"{txt}\n")


def search_db(query: str, type: bool = False):
    # search by name for users and project title for projects
    file_path = 'projects.txt' if type else 'users.txt'
    results = []

    with open(file_path, 'r+') as f:
        txt = f.read()

    data = txt_to_dict(txt, type)
    
    for item in data:
        if query in item['name']:
            results.append(item)

    return results
    
def edit_remove_entry(old_entry: dict, new_entry: dict, type: bool = False):
   #false for user data, true for project data 
   file_path = 'projects.txt' if type else 'users.txt' 
   data = search_db('', type)
   data.remove(old_entry)
   data.append(new_entry)

   os.remove(file_path)

   for entry in data:
       append_to_file(entry, type)