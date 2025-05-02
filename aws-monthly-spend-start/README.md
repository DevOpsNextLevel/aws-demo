
# AWS Monthly Spend Report Automation

This repository contains the automation to fetch AWS monthly spend, generate a PDF report, and send it via email to management.

## Components

- AWS Lambda Python script
- Cost Explorer integration
- PDF generation with Matplotlib and FPDF
- Email delivery using AWS SES
- GitHub Actions (optional) for CI/CD deployment

## Usage

- Deploy the Lambda function using the provided script
- Configure CloudWatch Event Rule to run monthly
- Use environment variables to customize recipients and sender email

## Directory Structure

```
aws-monthly-spend-report/
├── README.md
├── lambda/
│   ├── lambda_aws_monthly_spend_report.py
│   ├── requirements.txt
├── .github/workflows/
│   └── deploy.yml
└── LICENSE
```
