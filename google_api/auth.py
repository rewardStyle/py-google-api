from __future__ import print_function
import argparse
import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


# https://developers.google.com/sheets/api/quickstart/python

# SCOPES are defined at https://developers.google.com/identity/protocols/googlescopes
# SCOPES are space separated
# If modifying these scopes, delete your previously saved credentials
# at CLIENT_CREDENTIALS_FILE
SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file')
CLIENT_SECRET_FILE = 'client_secret.json'
CLIENT_CREDENTIALS_FILE = 'client_credentials.json'


class GoogleApiCredential:
    def __init__(self, app_name, scopes=None, secret_file=None, credentials_file=None):
        self.app_name = app_name
        # Set() ensures deduplication, sorted() ensures consistency of ordered scopes field per instance
        self.scopes = ' '.join(sorted(list(set(scopes if scopes is not None else SCOPES))))
        self.secret_file = secret_file if secret_file is not None else os.path.join(os.path.expanduser('.'), CLIENT_SECRET_FILE)
        self.credentials_file = credentials_file if credentials_file is not None else os.path.join(os.path.expanduser('.'), CLIENT_CREDENTIALS_FILE)
        self.credentials = None


    def get(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        if self.credentials is not None:
            return self.credentials

        store = Storage(self.credentials_file)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.secret_file, self.scopes)
            flow.user_agent = self.app_name
            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args(args=[])
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + self.credentials_file)
        self.credentials = credentials
        return credentials
