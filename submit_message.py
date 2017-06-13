import boto3

AWSID = {'Your ID'}
AWSKEY = {'Your key'}

sqs = boto3.resource('sqs', aws_access_key_id=AWSID,
    aws_secret_access_key=AWSKEY,
    region_name={'Your region'}
)

queue_name = ({'Your queue'})

response = sqs.create_queue( QueueName=queue_name,
Attributes={'FifoQueue': 'true',
'ContentBasedDeduplication': 'true'})

queue = sqs.get_queue_by_name(QueueName={'Your queue'})

with open("read.txt",'r') as myfile:
    for line in myfile:
        queue.send_message(MessageBody=line, MessageGroupId='Group1')