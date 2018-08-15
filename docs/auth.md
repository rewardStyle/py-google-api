# google_api.auth
A Python3 library for handling Google authentication for services such as Google Drive and Google Docs

## Required configuration

In order to authenticate with Google API services ( such as Google Drive ),
this module requires a valid `client_secret.json` file in the working directory
of the application using the module.

This file can be obtained from devops@rewardstyle.com and will resemble this:

```
{"installed":{"client_id":"xxxxx.apps.googleusercontent.com","project_id":"carbon-inkwell-194003","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"xxxxx","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}
```

## Use Cases

This module is intended to serve as a universal means of authenticating
with Google services such as Google Drive and Google Sheets.

It is probably best used as a submodule within other libraries
that are purpose-built for accessing those Google services.

### Usage

In a module which needs to authenticate with Google:

```python
import httplib2
from google_api import auth

credentials = auth.GoogleApiCredential(app_name='myUniqueAppName')
http = credentials.get().authorize(httplib2.Http())
```

If no valid credentials have been stored locally, then the module will
complete the OAuth2 flow ( with Google ) in order to obtain
new credentials ( stored locally as `client_credentials.json` ).

Once the credentials have been obtained, they are stored in the instance:
```python
import httplib2
from google_api import auth

credentials = auth.GoogleApiCredential(app_name='myUniqueAppName')
http = credentials.get().authorize(httplib2.Http())
# Actual API credentials saved in the credentials instance for easy access
newHttp = credentials.credentials.authorize(httplib2.Http())
# http and newHttp were both authenticated with the same set of credentials
```

### Scopes

- Scopes are defined at https://developers.google.com/identity/protocols/googlescopes
- Scopes are space separated, and order matters
- If modifying the module's scopes, delete the previously saved credentials at `client_credentials.json`

This module has default Scopes defined.
HOWEVER -- scopes can be passed into the `GoogleApiCredential()` constructor as a named argument
for users who wish to specify different Scopes:

```python
myScopes = ('foo', 'bar')
credentials = auth.GoogleApiCredential(app_name='myUniqueAppName', scopes=myScopes)
```


### File Names

The local secrets file and local system-generated credentials file paths
can be specified manually via passing in the named `secret_file` and `credentials_file`
params to the `GoogleApiCredential()` constructor.

If not specified explicitly, the defaults will be used.
