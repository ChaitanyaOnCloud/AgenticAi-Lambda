# Agentic AI - AWS Lambda

**Agentic AI** is a real-time AI agent deployed on AWS Lambda capable of fetching weather updates and cryptocurrency prices. It also sends query results automatically via email using AWS SNS.

---

## Features

- Fetch **weather information** for any city using OpenWeather API
- Retrieve **live cryptocurrency prices** (Bitcoin, Ethereum) using CoinGecko API
- Send results automatically via **AWS SNS email notifications**
- Fully **serverless architecture** using AWS Lambda

---

## Technologies Used

- **Python 3.12**
- **AWS Lambda**
- **AWS SNS**
- **OpenWeather API**
- **CoinGecko API**
- **Environment Variables** for secure configuration

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/username/Agentic-AI-Lambda.git
cd Agentic-AI-Lambda

### 2. Install dependencies locally (optional)
```bash
pip install -r requirements.txt

### 3. Set the environment variable for your OpenWeather API key
export WEATHER_API_KEY="your_openweather_api_key"

### 4. Zip the Lambda function folder (if deploying manually)
zip -r agentic_lambda.zip .

### 5.Deploy on AWS Lambda

Runtime: Python 3.12

Handler: lambda_function.lambda_handler

Upload the zip file

Set the environment variable in Lambda console

### 6. Configure SNS (optional)

Create SNS topic and subscribe your email

Configure Lambda destination → On success → SNS topic

### 7. Test the function using Lambda test events

Example Event JSON:

{
  "query": "What's the weather in Delhi"
}
