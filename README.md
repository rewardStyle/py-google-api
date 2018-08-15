# py-google-api

A Python3 library for accessing Google API functionality

## Installation

```bash
pipenv install git+git://github.com/rewardStyle/py-google-api.git#egg=google-api
```

## Use Cases

Use when needing to interact with Google services from within Python applications.

```python
from google_api import auth
credentials = auth.GoogleApiCredential(app_name='myUniqueAppName')
# See corresponding documentation for detailed example

from google_api import sheets
sheets.to_sheet('sheet_id', [['values']], credentials)
# See corresponding documentation for detailed example

from google_api import drive
dst_file = {}
drive.to_csv_file(dst_file, [['rows']], credentials)
# See corresponding documentation for detailed example
```

### Usage of google_api.auth

For authenticating with the Google API.

Creating an instance of `GoogleApiCredential` makes it simple for developers
to obtain valid OAuth2 credentials with defined scopes and an app name.

The complexities and intricacies of this process have been abstracted.

See [the documentation for google_api.auth](docs/auth.md).


### Usage of google_api.sheets

For creating and updating Google Sheets.

See [the documentation for google_api.sheets](docs/sheets.md).

### Usage of google_api.drive

For creating, uploading, and modifying CSV files in Google Drive.

See [the documentation for google_api.drive](docs/drive.md).


## The WHYs

### Why was this module developed ?

Authenticating ( and subsequently using ) Google services
can be somewhat arcane, at least from within Python
applications.

This module was developed to make authentication and common interaction as simple as possible.

More specifically, a pattern emerged from DevOps creating self-service tooling,
in that oftentimes a tool would generate a report and publish it either via Google Drive or Google Sheets directly. Rather than copy and paste the code throughout
these individual tools, it makes more sense to develop the libraries separately
so that any future application can take advantage of the functionality.

### Why use OAuth2?
( AKA, "Why not use simple token authentication?" )

Using Google API keys are only usable for accessing _public_ resources in Google.
Accessing _private_ resources ( Sheets, Docs, etc. ) requires OAuth2.

**Important Note**: Authenticating via OAuth2 from scratch requires manual intervention the first time.

### Reference
https://developers.google.com/sheets/api/quickstart/python
