
# 🚀 AWS Serverless S3 ➜ Lambda ➜ CloudWatch ➜ Slack + SNS + DynamoDB Integration

## 📌 Project Overview
This repository contains a step-by-step guide and ready-to-deploy code for building a serverless solution using AWS services.  
The solution helps enterprises monitor file uploads to S3 buckets and instantly notify teams while storing upload metadata.

## 🛠️ Architecture Components
- **Amazon S3** — Upload trigger
- **AWS Lambda** — Event processor
- **CloudWatch Logs** — Lambda logs
- **Slack Webhook** — Real-time notifications
- **Amazon SNS** — Email and other notifications
- **Amazon DynamoDB** — Metadata storage
- **IAM Roles and Policies** — Securing access and permissions

## ✅ Features
- Automatic alerts to Slack on new uploads
- Email notifications using SNS
- Storing upload metadata (filename, timestamp) in DynamoDB
- Fully serverless and event-driven
- Reusable IAM policy example

## 📖 Setup Guide

### 1️⃣ Create S3 Bucket
- Enable versioning and encryption (SSE-S3 or SSE-KMS)

### 2️⃣ Create SNS Topic
- Subscribe your email

### 3️⃣ Configure Slack Webhook
- Generate Slack webhook URL

### 4️⃣ Create DynamoDB Table
- Table name: `s3-upload-metadata`
- Partition key: `fileName`

### 5️⃣ Create IAM Role for Lambda
- Attach policies from `policy_lambda_role.json`

### 6️⃣ Deploy Lambda Function
- Use `lambda_function.py`
- Add environment variables:
  - `SLACK_WEBHOOK_URL`
  - `SNS_TOPIC_ARN`
  - `DDB_TABLE_NAME`

### 7️⃣ Setup S3 Event Notification
- Event type: PUT → Lambda

### 8️⃣ Test the System
- Upload files → Check Slack, SNS email, DynamoDB, and CloudWatch Logs

## 🚦 Optional (Enterprise Bonus)
- Use SSM Parameter Store for Slack webhook
- Add CloudWatch Alarms for Lambda failures
- Implement DLQ for failed Lambda invocations

## 📷 Submission / Demo Checklist
- ✅ Slack Notification screenshot
- ✅ Email received (SNS)
- ✅ DynamoDB entry
- ✅ GitHub repo with code and policies
- ✅ Short video or screenshots proving functionality

---

## 📌 License
MIT License — feel free to fork, clone and use for learning or enterprise demos.

