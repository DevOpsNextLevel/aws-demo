# my-cloudformation-repo

This repository contains CloudFormation templates and a GitHub Actions workflow to automatically deploy AWS CloudFormation stacks when changes are pushed.

## How It Works

- Push to GitHub main branch triggers GitHub Actions
- AWS CLI runs cloudformation deploy command
- CloudFormation Stack is created or updated

## Setup

- Configure AWS credentials in GitHub Secrets
