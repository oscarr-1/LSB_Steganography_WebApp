# **LSB Steganography Web App**

A Python-powered web application that allows users to hide and extract secret messages in images and audio files using the Least Significant Bit (LSB) steganography technique.

---

## **Table of Contents**
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

---

## **About**

This project is a Flask-based web application that utilizes **Pillow (PIL)** for image processing and **NumPy** and **Wave** libraries for audio processing. Users can upload files, hide or extract secret messages, and download processed files. The application opens automatically when executed via the terminal.

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
- Wave (part of Python’s standard library)

### **2. Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lsb-steganography-webapp.git
