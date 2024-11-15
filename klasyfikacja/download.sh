#!/bin/bash

curl -fL -o archive.zip https://www.kaggle.com/api/v1/datasets/download/taweilo/loan-approval-classification-data
unzip archive.zip

echo "Data downloaded, you can run the script now"
