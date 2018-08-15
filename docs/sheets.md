# google_api.sheets

For creating a Google Sheet in Google Drive.

## Usage

- Setting `clear_columns=True` will actually overwrite the data in the sheet.

```python
from google_api import auth
from google_api import sheets

credentials = auth.GoogleApiCredential(app_name='myUniqueAppName')

rows = [ ['1a', '1b'], ['2a', '2b'] ]

api_access = {
    'app_name': 'myUniqueAppName',
    'scopes': ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']
}

sheets.to_sheet('someGoogleSheetId', [ ['1a', '1b'], ['2a', '2b'] ], credentials)
```

#### Example: CircleCI Report

```python
from __future__ import print_function
from datetime import datetime
import csv
from io import StringIO

from google_api import auth
from google_api import sheets

REPORT_SHEET = '1guDUZjDsAGDphn_oe6NFFxmmI702sWSJUE4Y0lXoq60'

credentials = auth.GoogleApiCredential(app_name='circle-ci-report')

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

    sheets.to_sheet(REPORT_SHEET, [HEADERS] + rows + footer, credentials, clear_columns=True)
```
In this example, Google API Credentials are first set up for authentication.
These credentials are passed into the `sheets.to_sheet()` function.

This example takes a plain list of strings and converts it into a sorted, csv-formatted string as the rows,
then updates the Google Sheet with ID `1guDUZjDsAGDphn_oe6NFFxmmI702sWSJUE4Y0lXoq60`
to include the content `HEADERS`, followed by the rows, followed by the generated footer,
replacing any existing column data because `clear_columns=True`,
