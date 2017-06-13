import boto3

AWSID = {'Your ID'}
AWSKEY = {'Your key'}

sqs = boto3.resource('sqs', aws_access_key_id=AWSID,
    aws_secret_access_key=AWSKEY,
    region_name={'Your region'}
)

queue_name = {'Your queue'}
queue = sqs.get_queue_by_name(QueueName=queue_name)

for i in range(0, 1):
    msg_list = queue.receive_messages(VisibilityTimeout=1, MaxNumberOfMessages=10, WaitTimeSeconds=5)
    for msg in msg_list:

        with open("writemsg.txt", 'a') as write_file:
            write_file.write(format(msg.body))