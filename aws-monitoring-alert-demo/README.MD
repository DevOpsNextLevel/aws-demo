# AWS Monitoring & Real-Time Alert Demo

Welcome to today’s demo on AWS CloudTrail Real-Time Monitoring and Alerting. This session is designed to help you understand how to set up a monitoring and alerting system using AWS services like CloudTrail, SNS, Lambda, and S3.

Let’s start with a simple question: How confident are you in knowing every action happening within your AWS environment? Whether it’s unauthorized API calls, accidental resource deletions, or compliance violations, organizations must stay aware of their cloud activities in real-time.

**Why This Demo is Important**

***Real-World Challenge:***

Imagine an attacker or an unauthorized user trying to exploit your environment by accessing sensitive data or making prohibited API calls. Without a monitoring and alerting system, you wouldn’t even know such actions occurred until it’s too late.
Or consider a compliance audit requiring detailed logs of API activity. Manually managing this data would be tedious and error-prone.
AWS Services as a Solution:

AWS CloudTrail ensures every API call in your AWS account is logged securely.
SNS and Lambda provide real-time alerting for critical activities.
S3 and CloudWatch offer centralized storage and monitoring for logs.
What You Will Learn
Today, we will:

- Configure CloudTrail to capture and securely store API activity logs.
- Set up a real-time alerting system using SNS and Lambda for detecting unauthorized or suspicious activities.
- Use an encrypted S3 bucket for compliance-friendly log storage.
- Understand how this setup fits into broader use cases in an organization.

## **Use Case Scenarios for Organizations**
1. **Security Monitoring**
Organizations can monitor unauthorized API calls (e.g., UnauthorizedOperation) in real-time and take immediate action.
Example: If an unauthorized user tries to describe or modify EC2 instances, an alert is sent to the security team.

2. **Compliance and Audit Readiness**
Logs stored in an encrypted S3 bucket help meet compliance standards like SOC 2, HIPAA, or GDPR.
Example: Auditors request logs for API activity over the last 6 months. With this setup, these logs are securely available.

3. **Incident Response**
Automatically alert security teams about suspicious activity to reduce response time.
Example: If root account credentials are used unexpectedly, an immediate notification can help mitigate potential risks.

4. **Cost Optimization**
Monitor actions that could lead to unexpected billing issues.
Example: Detect if an unauthorized user attempts to create costly resources (e.g., high-end EC2 instances).

## **Applicability in an Organization
- Cloud Security Teams:
Monitor and secure AWS environments by identifying unauthorized access or suspicious activity in real-time.
- DevOps Engineers:
Automate log storage, alerting, and monitoring workflows to reduce manual overhead.
- Compliance Officers:
Ensure all API activity is logged and securely stored for audits.
- Incident Response Teams:
Receive immediate notifications for critical activities, enabling faster resolution.

## **Our Ultimate Goal Today
By the end of this session, you will:

Understand how AWS services integrate seamlessly for monitoring and alerting.
Learn how to build a scalable, real-time monitoring system applicable to any organization.
Gain hands-on experience that can be applied to enhance security, compliance, and operational efficiency in real-world scenarios.


This demo showcases how to monitor AWS account activities using CloudTrail, process logs in real-time using Lambda, and send alerts via SNS.

## **Architecture Overview**

![Architecture Diagram][https://drive.google.com/file/d/1BpqO_ujIUa90nTsMYK5JItfcTHebI_si/view?usp=drive_link]

1. **CloudTrail** logs AWS API activity and sends logs to:
   - **S3** for long-term storage.
   - **SNS** for real-time processing.
2. **SNS** triggers a **Lambda** function to analyze the logs.
3. **Lambda** sends email or SMS alerts for critical events (e.g., unauthorized API calls).

---

## **Features**
- Real-time detection of unauthorized actions (`UnauthorizedOperation`).
- Automated notifications via SNS.
- Centralized monitoring using CloudTrail and CloudWatch.

---

## **Setup Instructions**

### **1. Prerequisites**
- AWS account.
- IAM user/role with permissions to manage CloudTrail, SNS, Lambda, and S3.

---

### **2. Steps to Set Up**

1. **Create an S3 Bucket**
   - Enable versioning and default encryption (KMS).
   - Use this bucket for storing CloudTrail logs.

2. **Set Up IAM Role**
   - Creat an IAM Role that Cloudtrail needs to act on the cloudwatch log group:
     - For this demo we will use AWS managed policies:
     - AmazonS3FullAccess, AWS CloudTrail_FullAccess, AWSKeyManagementServicePowerUser, CloudWatchFullAccess.
     - A custom managed policy for cloudtrail PutLogEven and CreateLogStream

3. **Set Up CloudTrail**
   - Enable CloudTrail and configure:
     - S3 bucket for log storage.
     - SNS topic for event notifications.

4. **Create an SNS Topic**
   - Name: `cloudtrail-alerts-demo`.
   - Add an email or phone number as a subscriber.

5. **Deploy the Lambda Function**
   - Add the code in `lambda/handler.py`.
   - Set environment variables:
     - `SNS_TOPIC_ARN`: ARN of the SNS topic.
   - Attach the necessary IAM role.

6. **Test the Setup**
   - Use the test event in `scripts/test-events.json`.
   - Simulate an unauthorized action:
     ```bash
     aws ec2 describe-instances --profile unauthorized-user
     ```

---

## **Files in the Directory**

- **lambda/handler.py**: Lambda function code for processing CloudTrail events.
- **scripts/test-events.json**: Test payload for simulating an SNS event.
- **README.md**: Documentation for the demo setup.
- **templates/sns-cloudtrail-lambda.yaml** (Optional): CloudFormation template for automating setup.

---

## **Educational Goals**

- Understand AWS CloudTrail for activity monitoring.
- Automate event processing using AWS Lambda.
- Configure SNS for real-time alerts.

---

## **License**
This demo is provided under the MIT License. See [LICENSE](LICENSE) for more details.

---

## **Contributions**
Feel free to fork this repository and submit pull requests for improvements!


[def]: https://drive.google.com/file/d/1BpqO_ujIUa90nTsMYK5JItfcTHebI_si/view?usp=sharing