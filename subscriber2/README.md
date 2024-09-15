# Subscriber 2 (AWS Lambda)

This folder contains the Python code for **Subscriber 2**, an AWS Lambda function that listens to messages from **SQS Queue 2** and processes them by storing the data as JSON files in **Amazon S3**.

## 📑 Files

- **`lambda_function.py`**: The Python code for the AWS Lambda function that processes messages.
- **`requirements.txt`**: Lists the dependencies required by the AWS Lambda function.
- **`deploy-subscriber2.yml`**: GitHub Action workflow to automate the deployment of Subscriber 2.

## 🚀 How to Deploy

### Prerequisites

1. **AWS Account**: You need an active AWS account to deploy resources.
2. **AWS CLI**: Installed and configured with the appropriate credentials.
3. **GitHub Secrets Configuration**:
   - **`AWS_ACCESS_KEY_ID`**: Your AWS access key ID.
   - **`AWS_SECRET_ACCESS_KEY`**: Your AWS secret access key.

### Steps to Deploy Subscriber 2

1. **Add Required Secrets to GitHub**:
   - Go to your repository's **Settings > Secrets and variables > Actions > New repository secret**.
   - Add the following secrets:
     - **`AWS_ACCESS_KEY_ID`

2. **: Your AWS access key ID.
     - **`AWS_SECRET_ACCESS_KEY`**: Your AWS secret access key.

3. **Push Changes to the `main` Branch**:
   - Commit and push the changes to the `main` branch of your repository. This will automatically trigger the GitHub Action workflow to deploy the Subscriber 2 AWS Lambda.

4. **Monitor the Deployment**:
   - Go to the **Actions** tab in your GitHub repository.
   - Select the **Deploy Subscriber 2 AWS Lambda** workflow to monitor the deployment progress.

## 📂 Folder Structure

- **`lambda_function.py`**: AWS Lambda function code to process messages.
- **`requirements.txt`**: Python dependencies for the AWS Lambda function.
- **`.github/workflows/deploy-subscriber2.yml`**: GitHub Actions workflow file for deployment.

## 📝 Usage Instructions

### How Subscriber 2 Processes Messages

1. **SQS Trigger**:
   - The function is automatically triggered when a message is published to **SQS Queue 2**.

2. **Processing Logic**:
   - The function extracts the order details from the message and stores them as JSON files in Amazon S3.

## 🔧 Customization

- **S3 Bucket Name**: Modify the S3 bucket name in the environment variables or code as needed.
- **Message Processing Logic**: Update the message processing logic in `lambda_function.py` to handle different types of data.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
