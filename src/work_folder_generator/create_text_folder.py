import os
import pickle

from pathlib import Path
from googleapiclient.discovery import build

from work_folder_generator.authenticate import authenticate_google



def create_folder(parent_id, folder_name):
    """Create a folder in Google Drive within the specified parent folder."""
    creds = authenticate_google()
    drive_service = build('drive', 'v3', credentials=creds)
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    folder = drive_service.files().create(body=folder_metadata,
                                          fields='id').execute()
    folder_id = folder.get('id')
    print(f"Created folder '{folder_name}' with ID: {folder_id}")
    return folder_id