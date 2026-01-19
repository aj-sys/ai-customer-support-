# AI Customer Support Demo



## 🚀 Project Introduction

This project demonstrates how to build and deploy a **simple AI-powered Customer Support application** using **Python, Flask, and AWS EC2 (Free Tier)**. It is designed to help learners move beyond theory and gain **hands-on experience** with cloud deployment, basic AI logic, and secure application setup on AWS.

The application allows users to submit customer messages through a web interface and automatically classifies them as **Complaint, Inquiry, or Feedback**. While the AI logic is intentionally simple, the project mirrors how real-world cloud applications are structured, deployed, and managed.

### 🔑 What You’ll Learn
- Deploying a Flask web application on an AWS EC2 instance  
- Using IAM roles instead of hard-coded credentials  
- Implementing basic AI-style text classification logic  
- Structuring a cloud project suitable for a professional portfolio  

This project is **AWS Free Tier compatible**, beginner-friendly, and ideal for learners looking to strengthen their cloud and Python skills through practical implementation rather than theory alone.


---

## Features
- Web-based message input
- Classifies messages into: **Complaint**, **Inquiry**, **Feedback**
- Hosted on **AWS EC2 Free Tier**
- Beginner-friendly and easy to extend

---

## Architecture Diagram

The diagram below shows the workflow of the AI Customer Support App:

![Architecture Diagram ](screenshots/architectural_diagram.png)


- Users submit messages via the web interface.  
- Flask app processes the messages and classifies them.  
- Optional: Messages can be stored in **S3** or **DynamoDB** for analytics.  
- The entire app runs on an **AWS EC2 Free Tier instance** with port 5000 open.


## Step-by-Step Instructions

### 1. Launch an EC2 Instance
1. Open the **AWS EC2 console** → Launch Instance  
2. Choose **Amazon Linux 2023**  
3. Instance type: **t2.micro** (Free Tier eligible)  
4. Configure security group:  
   - **SSH (port 22)** from your IP  
   - **Custom TCP (port 5000)** from anywhere (0.0.0.0/0)  
5. Launch and connect via SSH:

```bash
ssh -i <your-key>.pem ec2-user@<EC2-PUBLIC-IP>
````

**Screenshot:**
![Running EC2 Instance ](screenshots/01_running_ec2_instance.png)

---

### 2. Update System & Install Dependencies

```bash
sudo yum update -y
sudo yum install python3 python3-pip -y
pip3 install --user flask
```

**Screenshot:**
![Dependencies Installed ](screenshots/03_dependencies_installed.png)

---

### 3. Configure Security Group for Port 5000

**Screenshot:**
![Security Group Rules ](screenshots/02_security_groups.png)


---

### 4. Create Project Folder and Flask App

```bash
mkdir ai-support-app
cd ai-support-app
nano app.py
```

Paste your Flask code into `app.py` and save.

**Screenshots:**

* Flask script in editor (Nano or VS Code)
![Flask App Script ](screenshots/04_flask_app_script.png)
![Flask Script in Nano ](screenshots/05_flask_app_in_nano.png)
---

### 5. Run the Flask App

```bash
python3 app.py
```

* Flask will start on port **5000**
* Access it in your browser:

```
http://<EC2-PUBLIC-IP>:5000
```

**Screenshot:**
![Flask App Running ](screenshots/06_flask_app_running.png)

---

### 6. Test the App

Try typing these messages in the app:

| Message                      | Classification |
| ---------------------------- | -------------- |
| “I want a refund”            | Complaint      |
| “Can you help with pricing?” | Inquiry        |
| “Great service, thanks!”     | Feedback       |

**Screenshot:**
![Message Classification Results ](screenshots/07_message_classification_results.png)
---

### 7. Optional Enhancements

* Add `/support` API endpoint to accept JSON messages
* Store messages in **S3** or **DynamoDB**
* Add **CloudWatch logging** for requests
* Deploy with **Elastic IP** for consistent public access

---

## Conclusion

This project showcases how even beginners can leverage **AWS EC2, Python, and Flask** to build a real-world web application with AI-powered functionality.  

Through this demo, you’ve seen how to:  
- Launch and configure an EC2 instance  
- Install Python and Flask dependencies  
- Develop a web application to classify messages  
- Open ports and configure Security Groups for public access  

This project is **fully Free Tier-compatible**, beginner-friendly, and can easily be extended with additional features. 


### Future Enhancements
Here are some ideas to take this project further and make it more professional:  
- **Integrate real AI/NLP services**: Use Amazon Comprehend or OpenAI API for more accurate message classification and sentiment analysis.  
- **Store messages in AWS**: Log messages in S3 or DynamoDB for analytics or historical reference.  
- **Create a web UI**: Build a simple front-end with HTML, CSS, or Bootstrap for a better user experience.  
- **Deploy with a production server**: Use Gunicorn + Nginx instead of Flask’s development server; add SSL for secure access.  
- **Add authentication**: Restrict access to authorized users only.  
- **Expand message categories**: Include categories like Technical Support, Sales Inquiry, Returns, etc.  
- **Automate responses**: Generate template or AI-based auto-replies for faster customer support.  
- **Logging & Monitoring**: Use AWS CloudWatch to monitor server performance, errors, and traffic patterns.

Feel free to explore, improve, and adapt this project to make it your own portfolio highlight!









