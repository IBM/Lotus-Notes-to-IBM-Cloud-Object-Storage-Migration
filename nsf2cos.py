import ibm_boto3
from ibm_botocore.client import Config, ClientError
import requests
import pprint
import base64
import os

# Cloud Object Storage credentials
credentials = {
    "apikey": "<API-KEY>",
    "endpoints": "<ENDPOINT>",
    "iam_apikey_description": "<API-KEY-DESCRIPTION>",
    "iam_apikey_name": "<API-KEY-NAME>",
    "iam_role_crn": "<ROLE-CRN>",
    "iam_serviceid_crn": "<SERVICE-ID-CRN>",
    "resource_instance_id": "<INSTANCE-ID>"
}
# Create COS Client
cos = ibm_boto3.client(service_name='s3',
                       ibm_api_key_id=credentials['apikey'],
                       ibm_service_instance_id=credentials['resource_instance_id'],
                       ibm_auth_endpoint="<AUTH-ENDPOINT>",
                       config=Config(signature_version='oauth'),
                       endpoint_url="<ENDPOINT-URL>")

# Get list of all the buckets [Optional]
res = cos.list_buckets()
print(res['Buckets'])

domino_url = "https://<SERVER>/<DATABASEPATH>/api/data/documents/unid/<DOC_UNID>"
resp = requests.get(domino_url, verify=False)
# JSON response of Notes document
resp_json = resp.json()
# In this case, "Body" field has attachments. So we are getting the content of Body field.
# If there are more fields with attachments, you have to include those fields as well.
body_content = resp_json['Body'].get('content')
for item in body_content:
    # Check if content is base64
    if item.get('contentTransferEncoding') == "base64":
        # Get attachment name
        start_string = item.get('contentDisposition').find("=")
        attachmentName = item.get('contentDisposition')[start_string + 1:].replace('"', '')
        print(attachmentName)
        # Get base64 attachment data
        b64Data = item.get("data")
        # Encode to utf-8
        b64Data_bytes = b64Data.encode('utf-8')
        # Decode base64 data and store it in a local file in your computer
        with open(attachmentName, 'wb') as f:
            decoded_file_data = base64.decodebytes(b64Data_bytes)
            f.write(decoded_file_data)
        # Read attachment file as binary
        with open(attachmentName, 'rb') as f_cos:
            # Upload to IBM Cloud Onject Storage
            cos.upload_fileobj(f_cos, Bucket='swlc-cloud-object-storage-cos-migration-test', Key=attachmentName)
        # Remove attachment file from your local computer
        os.remove(attachmentName)
        print(f'Attachment {attachmentName} is successfully migrated to IBM Cloud Object Storage')
