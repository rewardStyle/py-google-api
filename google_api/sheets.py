import httplib2

from apiclient import discovery


def to_sheet(spreadsheet_id, values, credentials, sheet_name='Sheet1', row_offset=0, clear_columns=False):
    http = credentials.get().authorize(httplib2.Http())
    discoveryUrl = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)

    # determine columns and cell ranges
    last_column = ord('A') + len(values[0])
    if last_column != ord('A'):
        last_column -= 1
    last_column = chr(last_column)
    ranges = 'A' + str(row_offset + 1) + ':' + last_column + str(row_offset + len(values))

    # clear columns that are getting re-written
    if clear_columns:
        request = service.spreadsheets().values().clear(spreadsheetId=spreadsheet_id, range="!".join([sheet_name, 'A:'+last_column]), body={})
        request.execute()

    # Write data to spreadsheet as RAW strings
    for idx, row in enumerate(values):
        values[idx] = [str(x) for x in row]
    request = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range="!".join([sheet_name,ranges]),
        valueInputOption='RAW',
        body={'values':values}
    )
    request.execute()
