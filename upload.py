import os
import boto3


BUCKET_NAME = 'alexhaight-design'
LOCAL_DIRECTORY = '/Users/alex/Documents/Design'
EXTENSIONS = ['png', 'jpg']

client = boto3.client('s3')

# enumerate local files recursively
for root, dirs, files in os.walk(LOCAL_DIRECTORY):

  for filename in files:

    # construct the full local path
    local_path = os.path.join(root, filename)

    # construct the full Dropbox path
    path = os.path.relpath(local_path, LOCAL_DIRECTORY)

    print('Searching ', path,' in ', BUCKET_NAME)
    parts = path.split('.')
    if parts[len(parts)-1] not in EXTENSIONS:
       print('Skipping non-png ', path)
    else:
        try:
            client.head_object(Bucket=BUCKET_NAME, Key=path)
            print('Path found on S3! Skipping ', path)

            # try:
                # client.delete_object(Bucket=bucket, Key=s3_path)
            # except:
                # print "Unable to delete %s..." % s3_path
        except:
            print('Uploading ', path)
            client.upload_file(local_path, BUCKET_NAME, path, ExtraArgs={'ACL':'public-read'})

