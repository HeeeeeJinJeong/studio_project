from storages.backends.s3boto3 import S3Boto3Storage

from etc import *

class MediaStorage(S3Boto3Storage):
    location = 'media'
    bucket_name = bucket_name
    region_name = 'ap-northeast-2'
    custom_domain = bucket_name
    file_overwrite = False