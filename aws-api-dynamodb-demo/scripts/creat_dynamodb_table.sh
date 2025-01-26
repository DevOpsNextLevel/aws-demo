#!/bin/bash
aws dynamodb create-table \
    --table-name EmployeeTable \
    --attribute-definitions AttributeName=employee_id,AttributeType=S \
    --key-schema AttributeName=employee_id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST