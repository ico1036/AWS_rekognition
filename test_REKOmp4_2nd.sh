#!/bin/bash

jobid=$1
region="~~"
endpoint="https://~~~"

aws rekognition get-label-detection  --job-id $jobid \
--endpoint-url $endpoint \
--region $region \
--profile Admin01 
