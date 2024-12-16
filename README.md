# **LSB Steganography Web App**

A Python-powered web application that allows users to hide and extract secret messages in images and audio files using the Least Significant Bit (LSB) steganography technique. Processed image and audio files will look and sound the same after hiding messages.

---

## **Table of Contents**
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)

---

## **About**

This project is a Flask-based web application that utilizes **Pillow (PIL)** for image processing and **NumPy** library for audio processing. Users can upload files, hide or extract secret messages, and download processed files. The application opens automatically when executed via the terminal.

---

## **Features**

- Upload images or audio files for steganography operations.
- Hide messages using the Least Significant Bit (LSB) method.
- Extract hidden messages from processed files.
- Download modified files containing hidden messages.

---

## **Installation**

### **1. Prerequisites**
- Python 3.8 or later
- Flask
- Pillow (PIL)
- NumPy

### **2. Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/oscarr-1/lsb-steganography-webapp.git
2. Navigate to the project directory:
   ```bash
   cd lsb-steganography-webapp
3. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/Mac
   venv\Scripts\activate       # For Windows
4. Install dependencies:
   ```bash
   pip install flask pillow numpy
5. Run the application:
   ```bash
   python run.py
6. The application will automatically open in your default web browser.

## **Usage**
### 1. Running the application
   - Open a terminal (e.g. VS Code terminal)
   - Navigate to the project directory and execute:
     ```bash
     python run.py
   - The application will launch in your default web browser. If it doesn't open automatically, visit:
     ```arduino
     http://127.0.0.1:5000
### 2. Hiding a message
   - Choose image or audio steganography.
   - Upload an image or audio file, depending which type chosen.
   - Enter the secret message to hide.
   - Download the modified file containing the hidden message.
   - Compare the orignal and modified files.
### 3. Extracting a message
   - Upload a processed file
   - Retrieve the extracted hidden message directly in the app interface.

## **Requirements**
- Python 3.8+
- Flask: a micro web framework for Python
- Pillow (PIL): for image processing
- NumPy: for numerical operations
Install the requirements with:
```bash
pip install flask pillow numpy
