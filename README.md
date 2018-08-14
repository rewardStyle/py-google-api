# py-google-api

A Python3 library for accessing Google API functionality

## Installation

```bash
pipenv install git+git://github.com/rewardStyle/py-google-api.git#egg=py-google-api
```

## Goole API Authentication

Google API authentication is handled by the [rewardStyle/google_auth](https://github.com/rewardStyle/google_auth)
library.

For more information on how to ensure that this library is able to authenticate
with the Google API, please see [rewardStyle/google_auth's documentation](https://github.com/rewardStyle/google_auth#required-configuration).

## Use Cases

Use when needing to interact with Google services from within Python applications.

### Usage of google_sheets

For creating a Google Sheet in Google Drive.

- Setting `clear_columns=True` will actually overwrite the data in the sheet.

```python
from google_sheets import to_sheet

rows = [ ['1a', '1b'], ['2a', '2b'] ]

to_sheet('someGoogleSheetId', [ ['1a', '1b'], ['2a', '2b'] ], app_name='myUniqueAppName')
```

#### Example: CircleCI Report

```python
from __future__ import print_function
from datetime import datetime
import csv
from google_sheets import to_sheet
from io import StringIO

REPORT_SHEET = '1guDUZjDsAGDphn_oe6NFFxmmI702sWSJUE4Y0lXoq60'

HEADERS = ['CIRCLECI_VERSION', 'REPO']


def to_csv_str(mylist):
    strbuff = StringIO()
    csv_writer = csv.writer(strbuff, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(mylist)
    result = strbuff.getvalue().strip()
    strbuff.close()
    return result


def compile_report(rows):
    footer = [[''], [str(datetime.utcnow()) + '+00:00']]
    rows = sorted(rows, key=to_csv_str)
    to_sheet(REPORT_SHEET, [HEADERS] + rows + footer, clear_columns=True, app_name='circle-ci-report')
```

### Usage of google_drive

For creating a CSV file and uploading it to Google Drive.

- Setting `finalize=True` will actually finalize the file and upload it to Google Drive.
- The value for the `new_file` argument determines where the local file is kept while being written to.

```python
from google_drive import to_csv_file

my_csv_dst = {
    'dest': {
        'folder_id': 'googleDriveFolderId',
        'file_name': 'myFile.csv',
        'file_id': 'preexistingMyFileCsvId'
    }
}

rows = [ ['1a', '1b'], ['2a', '2b'] ]

to_csv_file(my_csv_dst, rows, new_file='./.myLocalFile.csv', finalize=True, app_name='myUniqueAppName')
```

#### Example: track-cost-allocation-tagging
See: https://github.com/rewardStyle/devops-tools/blob/master/python/track-cost-allocation-tagging/main.py

## The WHYs

### Why was this module developed ?

Using Google services can be somewhat arcane, at least from within Python applications.

This module was developed to make common interaction as simple as possible.

More specifically, a pattern emerged from DevOps creating self-service tooling,
in that oftentimes a tool would generate a report and publish it either via Google Drive or Google Sheets directly. Rather than copy and paste the code throughout
these individual tools, it makes more sense to develop the libraries separately
so that any future application can take advantage of the functionality.
