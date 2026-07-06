import json

def lambda_handler(event, context):

    print("========= S3 Trigger Executed =========")

    print(json.dumps(event))

    bucket = event["Records"][0]["s3"]["bucket"]["name"]

    filename = event["Records"][0]["s3"]["object"]["key"]

    print("Bucket :", bucket)

    print("Uploaded File :", filename)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "S3 Trigger Working",
            "bucket": bucket,
            "file": filename
        })
    }
