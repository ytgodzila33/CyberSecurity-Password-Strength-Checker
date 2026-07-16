# 🔐 CyberShield – Password Strength Analyzer

> A Python-based Password Strength Analyzer designed to evaluate password security by analyzing complexity, entropy, dictionary words, and password composition. Developed as part of my **Week 1 Cybersecurity Internship Project at DecodeLabs**.

---

## 📖 Overview

CyberShield is a command-line password analysis tool that helps users evaluate the strength of their passwords using multiple security checks. Instead of only verifying password length, the application analyzes password complexity and estimates its resistance against brute-force attacks.

The project was developed to gain practical experience in secure authentication principles and defensive cybersecurity concepts.

---

## ✨ Features

### 🔍 Password Strength Analysis

* Analyze password length
* Detect uppercase letters
* Detect lowercase letters
* Detect numeric characters
* Detect special characters
* Classify password strength

### 📊 Entropy Calculation

* Calculate password entropy
* Estimate password search space
* Evaluate password complexity

### 📚 Dictionary Detection

* Detect common dictionary words
* Identify weak passwords based on known word lists

### 🔑 Password Generator

Generate secure random passwords with customizable complexity.

### 📄 Report Generation

Generate a detailed password analysis report and save it to:

* `password_report.txt`

---

## 📂 Project Structure

```text
CyberShield/
│
├── main.py                    # Application entry point
├── analyzer.py                # Password analysis engine
├── entropy.py                 # Entropy calculations
├── generator.py               # Secure password generator
├── report.py                  # Report generation
├── utils.py                   # Helper functions
├── common_passwords.txt        # Common password database
├── dictionary.txt             # Dictionary words database
├── password_report.txt        # Generated analysis report
└── README.md
```

---

## ⚙️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* File Handling
* JSON
* String Processing
* Mathematical Calculations
* Password Entropy Analysis
* Cybersecurity Fundamentals

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ytgodzila33/CyberSecurity-Password-Strength-Checker.git
```

Navigate to the project directory:

```bash
cd CyberSecurity-Password-Strength-Checker
```

(Optional) Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Run the application:

```bash
python main.py
```

---

## 📋 How It Works

The application evaluates a password using several criteria:

* Password length
* Character diversity
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Dictionary word detection
* Entropy calculation

After evaluation, CyberShield assigns a strength rating and generates a detailed report.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Password Security Principles
* Secure Authentication Concepts
* Password Entropy
* Defensive Cybersecurity
* Python Programming
* Modular Software Development
* File Handling
* Algorithm Design

---

## 📌 Future Improvements

Planned enhancements include:

* Interactive terminal interface
* Password breach detection
* Keyboard pattern detection
* Leetspeak detection
* Password history
* JSON report export
* PDF report generation
* Graphical User Interface (GUI)
* API integration for leaked password databases

---

## 👨‍💻 Author

**Abdul Rehman Tahir**

* BS Computer Science Student
* Cybersecurity Enthusiast
* Python Developer
* Cybersecurity Intern at DecodeLabs

---

## 📜 License

This project was created for educational and learning purposes as part of my cybersecurity internship. You are welcome to explore, learn from, and modify the code for educational use.

---

## ⭐ Support

If you found this project helpful, please consider giving the repository a **Star ⭐**.

Your support motivates me to continue building and sharing cybersecurity projects.
