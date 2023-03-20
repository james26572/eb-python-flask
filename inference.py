#Setup
import boto3
import sagemaker
import io
import csv
region = boto3.Session().region_name
client = boto3.client("sagemaker", region_name=region)

#Role to give SageMaker permission to access AWS services.
sagemaker_role = "arn:aws:iam::752763431782:role/localAccessToSage" 

#Get model from S3
model_url = "s3://sagemaker-eu-west-1-752763431782/huggingface-pytorch-training-2023-03-19-00-22-30-107/output/model.tar.gz"

#Get container image (prebuilt example)
from sagemaker import image_uris
container = image_uris.retrieve("xgboost", region, "0.90-1")

#Create model
model_name = "huggingface-pytorch-training-2023-03-19-00-22-30-107"

# creating a model using the s3 path to training job for item 1A
'''
response = client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = sagemaker_role,
    Containers = [{
        "Image": container,
        "Mode": "SingleModel",
        "ModelDataUrl": model_url,
    }]
)
'''
# creating an endpoint configuration for the model
'''
response = client.create_endpoint_config(
   EndpointConfigName="item1ASummaries",
   
   ProductionVariants=[
        {
            "ModelName": "huggingface-pytorch-training-2023-03-19-00-22-30-107",
            "VariantName": "AllTraffic",
            "ServerlessConfig": {
                "MemorySizeInMB": 5120,
                "MaxConcurrency": 20
            }
        } 
    ]
)
'''
#creating endpoint for the model
'''
response = client.create_endpoint(
    EndpointName="1AInference",
    EndpointConfigName="item1ASummaries"
)
'''



runtime = boto3.client("sagemaker-runtime")

endpoint_name = "1AInference"
content_type = "text/csv"
input_string = {"data":'''The Company’s operating results could be negatively impacted by changes in its excess and obsolete inventory reserves.
	The Company maintains reserves for excess and obsolete inventory resulting from the potential inability to sell its products at prices in excess of current carrying costs. The markets in which the Company operates are highly competitive, and new products and surgical procedures are introduced on an ongoing basis. Such marketplace changes may cause some of the Company’s products to become obsolete. The Company makes estimates regarding the future recoverability of the costs of these products and records a provision for excess and obsolete inventories based on historical experience, expiration of sterilization dates and expected future trends. If actual product life cycles, product demand or acceptance of new product introductions are less favorable than projected by management, additional inventory write-downs may be required, which could unfavorably affect future operating results.'''}






response = runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType=content_type,
    Body=input_string
)

result = response['Body'].read().decode('utf-8')

print(result)




