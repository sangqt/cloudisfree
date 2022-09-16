import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    ses.send_email(
        Source='sangqt.inb@gmail.com',
        Destination={
            'ToAddresses': [
                event['destinationEmail'],
            ]
        },
        Message={
            'Subject': {
                'Data': 'Cloudisfree - Project 2'
            },
            'Body': {
                'Text': {
                    'Data': event['message']
                }
            }
        }
    )
    return 'Email sent!'