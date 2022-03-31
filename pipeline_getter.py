import yaml
import boto3
from easydict import EasyDict

bucket = "xmansion-application"
s3_client = boto3.client("s3")

def get_pipeline_config(scraper_name):
    s3_response = s3_client.get_object(Bucket= bucket, Key=f"jatin/{scraper_name}.yaml")
    try:
        config_json = yaml.safe_load(s3_response["Body"])
        config = EasyDict(config_json)
        return config
    except yaml.YAMLError as error:
        print(error)