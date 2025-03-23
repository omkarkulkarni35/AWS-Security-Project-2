import json
import boto3

securityhub = boto3.client('securityhub')
guardduty = boto3.client('guardduty')

def lambda_handler(event, context):
    print("Event received:", json.dumps(event, indent=2))

    for record in event['Records']:
        message = json.loads(record['body'])
        
        # Extract GuardDuty finding ID
        finding_id = message['detail']['id']
        print(f"Processing GuardDuty Finding: {finding_id}")

        # Auto-archive the GuardDuty finding
        response = guardduty.update_findings(
            DetectorId='YOUR_DETECTOR_ID', # Replace with your GuardDuty Detector ID
            FindingIds=[finding_id],
            Status='ARCHIVED'
        )
        print(f"Archived Finding: {response}")

    return {
        'statusCode': 200,
        'body': json.dumps('Security alert handled successfully!')
    }
