import csv
import httplib2

from apiclient import discovery
from apiclient.http import MediaFileUpload


def to_csv_file(dst_file, rows, credentials=None, new_file=None, finalize=False):
    if new_file:
        assert dst_file['dest']
        dst_file['local'] = new_file
        fp = open(new_file, "w")
        dst_file['fp'] = fp
        csv_writer = csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dst_file['csv'] = csv_writer
    else:
        csv_writer = dst_file['csv']
    for row in rows:
        csv_writer.writerow(row)
    if finalize:
        dst_file['fp'].close()
        local = dst_file['local']
        upload_dest = dst_file['dest']
        dict_keys = dst_file.keys()
        for x in dict_keys:
            del dst_file[x]
        upload_file(credentials, local, **upload_dest)


def upload_file(credentials, local, folder_id=None, file_name=None, file_id=None):
    assert file_name
    media_body = MediaFileUpload(local, chunksize=1024*256, resumable=True)
    metadata = {'name': file_name, 'mimeType': 'text/csv'}
    http = credentials.get().authorize(httplib2.Http())
    client = discovery.build('drive', 'v3', http=http).files()
    if file_id:
        res = client.update(fileId=file_id, body=metadata, media_body=media_body).execute()
    else:
        if folder_id:
            metadata['parents'] = [folder_id]
        res = client.create(body=metadata, media_body=media_body).execute()
        if res:
            print('Uploaded "{}" to "{}"'.format(file_name, res['id']))
    if not res:
        raise Exception('Failed to upload "{}"'.format(file_name))
