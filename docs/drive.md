# google_api.drive

## Usage

For creating a CSV file and uploading it to Google Drive.

- Setting `finalize=True` will actually finalize the file and upload it to Google Drive.
- The value for the `new_file` argument determines where the local file is kept while being written to.
- When setting up the Google Drive destination argument ( the first param passed to `to_csv_file()` ), the `dest.file_id` JSON field only needs to be specified if the destination file already exists. If this field is left blank, then the system will create a _new_ Google Drive file, with the given name in the given folder.

```python
from google_api import auth
from google_api import drive

credentials = auth.GoogleApiCredential(app_name='myUniqueAppName')

my_csv_dst = {
    'dest': {
        'folder_id': 'googleDriveFolderId',
        'file_name': 'myFile.csv',
        'file_id': 'preexistingMyFileCsvId'
    }
}

rows = [ ['1a', '1b'], ['2a', '2b'] ]

drive.to_csv_file(my_csv_dst, rows, credentials=credentials, new_file='./.myLocalFile.csv', finalize=True)
```

In this example, Google API Credentials are first set up for authentication.
These credentials are passed into the `drive.to_csv_file()` function.

#### Example: track-cost-allocation-tagging
See: https://github.com/rewardStyle/devops-tools/blob/master/python/track-cost-allocation-tagging/main.py
