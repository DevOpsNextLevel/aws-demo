# AWS Monitoring & Real-Time Alert Demo

This demo showcases how to monitor AWS account activities using CloudTrail, process logs in real-time using Lambda, and send alerts via SNS.

## **Architecture Overview**

![Architecture Diagram](link-to-diagram-if-any)

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
