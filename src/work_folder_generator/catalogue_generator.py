import os
import pickle
import gspread
from time import sleep

from pathlib import Path
from googleapiclient.discovery import build

from openpecha.core.ids import get_id
from work_folder_generator.authenticate import authenticate_google
from work_folder_generator.config import SAMPLE_RESOURCE_SHEET_ID, SAMPLE_WORK_SHEET_ID

creds = authenticate_google()

def update_resource_id(file_id, resource_infos):
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(file_id)
    worksheet = spreadsheet.worksheet('Sheet1')


    # Generate and add IDs to the column
    for cell_walker, (resource_id, resource_link) in enumerate(resource_infos.items(), 2):
        worksheet.update_cell(cell_walker, 1, resource_id)
        worksheet.update_cell(cell_walker, 7, resource_link)
        sleep(6)

def add_work_sheet(work_folder_id, file_name):
    """Copy a Google Docs file to a specific folder in Google Drive."""
    
    drive_service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': file_name,
        'parents': [work_folder_id]
    }
    new_file = drive_service.files().copy(
        fileId=SAMPLE_WORK_SHEET_ID, body=file_metadata).execute()


def write_resources_folder_catalogue_sheet(resource_folder_id, resource_infos):
    drive_service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': 'Resources_catalog རྒྱུ་ཆའི་དཀར་ཆག',
        'parents': [resource_folder_id]
    }
    new_file = drive_service.files().copy(
        fileId=SAMPLE_RESOURCE_SHEET_ID, body=file_metadata).execute()
    update_resource_id(new_file['id'], resource_infos)
