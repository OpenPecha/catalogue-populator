import os
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from work_folder_generator.config import SCOPES

def authenticate_google():
    """Authenticate with Google Drive API using OAuth."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('./src/work_folder_generator/creds/token.pickle'):
        with open('./src/work_folder_generator/creds/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './src/work_folder_generator/creds/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('./src/work_folder_generator/creds/token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds