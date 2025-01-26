#!/bin/bash
zip get_employee.zip lambda_functions/get_employee.py
zip post_employee.zip lambda_functions/post_employee.py

aws lambda create-function \
    --function-name GETEmployee \
    --runtime python3.x \
    --role <LAMBDA_EXECUTION_ROLE_ARN> \
    --handler get_employee.lambda_handler \
    --zip-file fileb://get_employee.zip

aws lambda create-function \
    --function-name POSTEmployee \
    --runtime python3.x \
    --role <LAMBDA_EXECUTION_ROLE_ARN> \
    --handler post_employee.lambda_handler \
    --zip-file fileb://post_employee.zip