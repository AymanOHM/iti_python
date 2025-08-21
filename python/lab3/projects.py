from utils import *
from validation import *
from user import get_current_user, login

def view_projects():
    data = search_db('', True)
    if data:
        print(' | '.join(data[0].keys()))
        print('\n'.join([' | '.join(x.values()) for x in data]))
    else:
        print("No projects")

def input_project():
    data = {}
    data['name'] = input("Enter project name: ")
    data['details'] = input("Enter project details: ")
    data['target'] = input("Enter project target: ")
    data['start_date'] = input("Enter project start date (dd/mm/yyyy): ")
    data['end_date'] = input("Enter project end date (dd/mm/yyyy): ")
    data['status'] = input("Enter project status: ")
    current_user = get_current_user()
    data['owner'] = current_user['name']+'|'+current_user['phone']

    if all(validate_project(data).values()):
        pass
    else:
        print("Invalid input. Please try again.\n")
        data = input_project()
    return data

def new_project():

    if get_current_user():
        project = input_project()
        append_to_file(project, True)
        print("Project created successfully!\n")
    else:
        print("You must be logged in to create a project.\n")
        login()
        new_project()

def edit_projects(type=False):
    # false to edit, true to delete
    if get_current_user():
        name = input("Enter project name to edit/remove: ")
        if validate_name(name) and search_db(name, True):
            print('which project is yours: \n')

            results = search_db(name, True)

            for i, option in enumerate(results):
                print(f'[{i}] - {option['name']}: {option['details']}')

            try:
                choice = int(input())
            except:
                print("Invalid choice")
                return
            
            current_user = get_current_user()
            if results[choice]['owner'] == current_user['name']+'|'+current_user['phone']:    
                old_project = results[choice]
            else:
                print("You can only edit your own projects.\n")
                return
            

            if type:
                edit_remove_entry(old_project, {}, True)
            else:
                new_project = input_project()
                edit_remove_entry(old_project, new_project, True)
        else:
            print("No projects found with that name.\n")
    else:
        print("You must be logged in to edit or remove a project.\n")
        login()
        edit_projects(type)

def search_projects():
    query = input("Enter project name to search: ")
    results = search_db(query, True)
    if results:
        print(' | '.join(results[0].keys()))
        print('\n'.join([' | '.join(x.values()) for x in results]))
    else:
        print("No projects found with that name.\n")