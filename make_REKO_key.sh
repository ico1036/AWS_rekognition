#!/bin/bash

bucket_name=
file_name=
#file_default: test.mp4
endpoint="https://rekognition~~~~"
sns_arn="arn:aws:sns:~~"
role_arn="arn:aws:iam::~~"
region=""



aws rekognition start-label-detection --video "S3Object={Bucket="$bucket_name",Name="$file_name"}" \
--endpoint-url $endpoint \
--notification-channel "SNSTopicArn=$sns_arn,RoleArn=$role_arn" \
--region $region \
--profile Admin01

