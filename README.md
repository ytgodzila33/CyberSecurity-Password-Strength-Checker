# 🔐 CyberShield - Advanced Password Strength Analyzer

> A professional Python-based Password Strength Analyzer that evaluates password security using modern cybersecurity principles such as entropy analysis, breach detection, keyboard pattern recognition, dictionary attacks, and secure password generation.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Project](https://img.shields.io/badge/DecodeLabs-Cybersecurity%20Internship-red.svg)

---

# 📌 Overview

CyberShield is an advanced password security analyzer developed as part of my **Cybersecurity Internship at DecodeLabs**.

Unlike traditional password checkers that only verify length and character types, CyberShield performs multiple security analyses to estimate password strength and identify common weaknesses.

The project demonstrates practical cybersecurity concepts including entropy calculation, password complexity analysis, keyboard pattern detection, dictionary attacks, common password detection, and secure password generation.

---

# ✨ Features

### 🔐 Password Strength Analysis

* Password Length Validation
* Uppercase Letter Detection
* Lowercase Letter Detection
* Numeric Character Detection
* Special Character Detection

---

### 📊 Entropy Analysis

* Password Entropy Calculation
* Character Set Analysis
* Password Search Space Estimation
* Online Attack Time Estimation
* Offline Attack Time Estimation
* Entropy Rating

---

### 🚨 Breach Detection

* Common Password Detection
* Leaked Password Database Detection
* Dictionary Word Detection
* Personal Information Detection
* Birth Year Detection
* Phone Number Detection

---

### 🧠 Smart Detection

* Leetspeak Detection
* Keyboard Pattern Detection
* Sequential Character Detection
* Reverse Sequence Detection
* Repeated Character Detection
* Repeated Pattern Detection

---

### 📈 Password Scoring

CyberShield evaluates passwords using a weighted scoring system based on:

* Length
* Character Variety
* Entropy
* Dictionary Checks
* Keyboard Pattern Checks
* Breach Detection
* Password Complexity

Final ratings include:

* 🔴 Very Weak
* 🟠 Weak
* 🟡 Medium
* 🟢 Strong
* 🟢 Very Strong

---

### 🔑 Password Generator

Generate highly secure passwords using:

* Uppercase Letters
* Lowercase Letters
* Numbers
* Symbols
* Custom Length

---

### 📄 Reports

CyberShield automatically generates reports including:

* Text Report
* JSON Report

---

# 📁 Project Structure

```text
CyberShield/
│
├── assets/
│   ├── logo.txt
│   └── banner.txt
│
├── database/
│   ├── common_passwords.txt
│   ├── leaked_passwords.txt
│   ├── dictionary.txt
│   └── keyboard_patterns.txt
│
├── reports/
│   ├── password_report.txt
│   └── report.json
│
├── analyzer.py
├── breach_checker.py
├── config.py
├── entropy.py
├── generator.py
├── keyboard_detector.py
├── leetspeak.py
├── report.py
├── ui.py
├── utils.py
├── main.py
│
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Regular Expressions (Regex)
* JSON
* File Handling
* Math Module
* Random Module
* Colorama
* Cybersecurity Fundamentals

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CyberShield.git
```

Navigate into the project:

```bash
cd CyberShield
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

# 📸 Sample Features

✔ Password Strength Meter

✔ Entropy Calculation

✔ Breach Detection

✔ Keyboard Pattern Detection

✔ Dictionary Attack Detection

✔ Leetspeak Detection

✔ Secure Password Generator

✔ Security Recommendations

---

# 🎯 Learning Objectives

This project was developed to strengthen practical understanding of:

* Password Security
* Authentication Principles
* Secure Coding Practices
* Cybersecurity Fundamentals
* Python Programming
* Modular Software Design
* Defensive Security Concepts

---

# 📚 Future Improvements

* GUI Version (Tkinter / PyQt)
* Password Hashing Support
* Have I Been Pwned API Integration
* Password History Management
* Multi-language Support
* Export to PDF Reports
* Dark Mode Interface
* Multi-threaded Password Analysis

---

# 👨‍💻 Author

**Abdul Rehman Tahir**

BS Computer Science Student

Cybersecurity Enthusiast

Digital Marketing & Graphic Design Background

Currently exploring Python, Ethical Hacking, and Defensive Security.

---

# 📄 License

This project is intended for educational purposes as part of my cybersecurity learning journey and internship. Feel free to fork, explore, and learn from it.

---

## ⭐ Support

If you found this project useful or interesting, consider giving it a **Star ⭐** on GitHub.

Your support motivates me to build more cybersecurity and Python projects.
