import boto3 #it is an sdk used to create aws resource in the cloud 

ecr_client = boto3.client('ecr')

repository_name="my-cloude-native-repo"#uppercase letters are not allowed
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)

# creating image in repository
# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 617187150547.dkr.ecr.us-east-1.amazonaws.com
# login succeed
#docker build -t my-cloud-native-repo .
#docker tag my-cloud-native-repo:latest 617187150547.dkr.ecr.us-east-1.amazonaws.com/my-cloude-native-repo:latest
#docker push 617187150547.dkr.ecr.us-east-1.amazonaws.com/my-cloude-native-repo:latest
#