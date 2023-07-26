from pathlib import Path

from openpecha.core.ids import get_id

from work_folder_generator.authenticate import authenticate_google
from work_folder_generator.create_text_folder import create_folder
from work_folder_generator.catalogue_generator import add_work_sheet, write_resources_folder_catalogue_sheet



def populate_resource_folders(resource_folder_id):
    res_folder_names = {}
    for res_folder_walker in range(5):
        res_folder_name = get_id('R', 8)
        res_folder_id = create_folder(resource_folder_id, res_folder_name)
        add_work_sheet(res_folder_id, res_folder_name)
        res_folder_names[res_folder_name] = f"https://drive.google.com/drive/folders/{res_folder_id}"
    return res_folder_names

def generate_work_folder(parent_folder_id, work_title):
    work_folder_id = create_folder(parent_folder_id, work_title)
    resource_folder_id = create_folder(work_folder_id, 'Resources')
    resource_folder_names = populate_resource_folders(resource_folder_id)
    write_resources_folder_catalogue_sheet(resource_folder_id, resource_folder_names)
    add_work_sheet(work_folder_id, work_title)
    return work_folder_id


parent_folder_id = '1MmZ-CK9vQ8A8GXnRRQhAYJeSdlBbFjEX'
work_title = 'work_test'
generate_work_folder(parent_folder_id, work_title)


