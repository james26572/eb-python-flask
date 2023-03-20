from sagemaker.huggingface.model import HuggingFaceModel

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
   model_data="s3://sagemaker-eu-west-1-752763431782/huggingface-pytorch-training-2023-03-19-00-22-30-107/output/model.tar.gz",  # path to your trained SageMaker model
   role="arn:aws:iam::752763431782:role/localAccessToSage",                                            # IAM role with permissions to create an endpoint
   transformers_version="4.6",                           # Transformers version used
   pytorch_version="1.7",                                # PyTorch version used
   py_version='py36',                                    # Python version used
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
   initial_instance_count=1,
   instance_type="ml.m5.xlarge"
)

# example request: you always need to define "inputs"
data = {
   "inputs": '''The Company’s operating results could be negatively impacted by changes in its excess and obsolete inventory reserves.
	The Company maintains reserves for excess and obsolete inventory resulting from the potential inability to sell its products at prices in excess of current carrying costs. The markets in which the Company operates are highly competitive, and new products and surgical procedures are introduced on an ongoing basis. Such marketplace changes may cause some of the Company’s products to become obsolete. The Company makes estimates regarding the future recoverability of the costs of these products and records a provision for excess and obsolete inventories based on historical experience, expiration of sterilization dates and expected future trends. If actual product life cycles, product demand or acceptance of new product introductions are less favorable than projected by management, additional inventory write-downs may be required, which could unfavorably affect future operating results.'''
}

# request
print(predictor.predict(data))