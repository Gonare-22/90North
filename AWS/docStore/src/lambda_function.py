import json
import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    try:
        # Extract parameters from the event
        bucket_name = event['bucket_name']
        file_name = event['file_name']
        file_content = event['file_content']  # Base64-encoded file content

        # Decode the Base64 file content
        file_bytes = base64.b64decode(file_content)

        # Upload the file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_bytes)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f"File {file_name} uploaded successfully to {bucket_name}."})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f"Missing parameter: {str(e)}"})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
