# Publisher (AWS Lambda)

This folder contains the Python code for the **Publisher**, an AWS Lambda function that simulates an online webshop by sending order details (such as items ordered and customer information) to an **AWS SNS Topic**.

## 📑 Files

- **`lambda_function.py`**: The Python code for the AWS Lambda function that publishes messages to SNS.
- **`requirements.txt`**: Lists the dependencies required by the AWS Lambda function.
- **`deploy-publisher.yml`**: GitHub Action workflow to automate the deployment of the Publisher.

## 🚀 How to Deploy

### Prerequisites

1. **AWS Account**: You need an active AWS account to deploy resources.
2. **AWS CLI**: Installed and configured with the appropriate credentials.
3. **GitHub Secrets Configuration**:
   - **`AWS_ACCESS_KEY_ID`**: Your AWS access key ID.
   - **`AWS_SECRET_ACCESS_KEY`**: Your AWS secret access key.

### Steps to Deploy the Publisher

1. **Add Required Secrets to GitHub**:
   - Go to your repository's **Settings > Secrets and variables > Actions > New repository secret**.
   - Add the following secrets:
     - **`AWS_ACCESS_KEY_ID`**: Your AWS access key ID.
     - **`AWS_SECRET_ACCESS_KEY`**: Your AWS secret access key.

2. **Push Changes to the `main` Branch**:
   - Commit and push the changes to the `main` branch of your repository. This will automatically trigger the GitHub Action workflow to deploy the Publisher AWS Lambda.

3. **Monitor the Deployment**:
   - Go to the **Actions** tab in your GitHub repository.
   - Select the **Deploy Publisher AWS Lambda** workflow to monitor the deployment progress.

## 📂 Folder Structure

- **`lambda_function.py`**: AWS Lambda function code to publish messages to SNS.
- **`requirements.txt`**: Python dependencies for the AWS Lambda function.
- **`.github/workflows/deploy-publisher.yml`**: GitHub Actions workflow file for deployment.

## 📝 Usage Instructions

### How the Publisher Works

1. **Trigger the Publisher Lambda Function**:
   - The function can be triggered manually or scheduled to run at specific intervals.
   - Upon triggering, it sends a message to the SNS topic containing order details in JSON format.

2. **Example Message**:

   ```json
   {
       "orderId": "12345",
       "customerName": "John Doe",
       "items": ["Laptop", "Smartphone", "Headphones"]
   }
   ```

## 🔧 Customization

- **SNS Topic ARN**: Modify the SNS Topic ARN in the environment variables or code as needed.
- **Message Content**: Update the message content in `lambda_function.py` to include additional or different data fields.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
