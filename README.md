# Lambda-frontend_backend

# 🏏 AWS Serverless Cricket Dashboard

A serverless cricket dashboard built using **AWS Lambda**, **Lambda Function URLs**, and **Amazon S3**. This project demonstrates how to build a frontend and backend using AWS Lambda while also integrating an S3 event trigger.

---

## 📌 Project Overview

This project consists of three AWS Lambda functions:

1. **Frontend Lambda**
   - Serves a responsive HTML dashboard.
   - Fetches live cricket data from the Backend Lambda.

2. **Backend Lambda**
   - Provides cricket match information in JSON format.
   - Accessible through a Lambda Function URL.

3. **S3 Trigger Lambda**
   - Automatically executes whenever a file is uploaded to an S3 bucket.
   - Logs upload details in Amazon CloudWatch.

---

## 🏗️ Architecture

```
               User
                 │
                 ▼
        Frontend Lambda
      (HTML + JavaScript)
                 │
      Fetch API Request
                 │
                 ▼
        Backend Lambda
         (JSON Response)
                 ▲
                 │
        Lambda Function URL


 Amazon S3 ─────────► S3 Trigger Lambda
                        │
                        ▼
                 CloudWatch Logs
```

---

## 🚀 AWS Services Used

- AWS Lambda
- Lambda Function URL
- Amazon S3
- Amazon CloudWatch
- IAM

---

## 📂 Lambda Functions

### 1️⃣ Frontend-Manish-Kumar

**Purpose**
- Displays the cricket dashboard.
- Fetches data from Backend Lambda.

---

### 2️⃣ backend-manish-kumar

**Purpose**
- Returns cricket score data as JSON.
- Works as the backend API.

---

### 3️⃣ manish-s3-trigger

**Purpose**
- Triggered automatically when a file is uploaded to the configured S3 bucket.
- Stores upload information in CloudWatch Logs.

---

## ✨ Features

- Serverless architecture
- Frontend hosted using AWS Lambda
- Backend REST-style API using Lambda Function URL
- JSON data exchange
- Automatic S3 event triggering
- CloudWatch logging
- No EC2 instance required
- Fully managed AWS services

---

## 🛠️ Technologies Used

- Python 3.14
- HTML5
- CSS3
- JavaScript
- AWS Lambda
- Amazon S3
- CloudWatch
- JSON

---

## 📷 Project Workflow

1. User opens the Frontend Function URL.
2. Frontend requests data from Backend Lambda.
3. Backend returns cricket match details.
4. Dashboard displays the received data.
5. Uploading a file to S3 automatically invokes the S3 Trigger Lambda.
6. Upload information is stored in CloudWatch Logs.

---

## 📁 Repository Structure

```
.
├── Frontend-Manish-Kumar
├── backend-manish-kumar
├── manish-s3-trigger
└── README.md
```

---

## 🎯 Learning Outcomes

- AWS Lambda Functions
- Function URLs
- Serverless Web Applications
- REST API Basics
- Event-Driven Architecture
- Amazon S3 Triggers
- CloudWatch Monitoring
- IAM Permissions

---

## 📸 Screenshots

- Lambda Functions
- Frontend Dashboard
- Backend Function URL
- S3 Bucket
- S3 Trigger Configuration
- CloudWatch Logs

---

## 👨‍💻 Author

**Manish Kumar**

B.Tech (Artificial Intelligence & Data Science)

AWS & MLOps Enthusiast

---

## ⭐ Future Improvements

- Live Cricket API Integration
- Team Logos
- Match Statistics
- Authentication
- DynamoDB Integration
- API Gateway
- Responsive Mobile Design

---

## 📄 License

This project is created for educational and learning purposes.
