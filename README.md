# PRODIGY_CS_01

# 🔐 Caesar Cipher with Dynamic Shifting

A simple Python-based command-line tool that implements the Caesar Cipher encryption technique using **dynamic shift values** instead of a fixed key. This project demonstrates how classical cryptography can be enhanced by adding variation in the shifting logic.

## 📌 Features

- Encrypts text using Caesar Cipher with dynamic shifting
- Maps characters to a custom alphabet list before processing
- Modular and clean logic using Python
- CLI-based interaction for easy usage

## 🧠 How It Works

1. **Character Mapping**:  
   Each character from the input text is mapped to a defined alphabet list (including lowercase, uppercase, digits, and optionally symbols).

2. **Dynamic Shifting**:  
   Instead of using a fixed shift, the shift value can vary (e.g., based on character position, user input, or a pattern). The cipher applies a circular shift within the mapped list.

3. **Output Generation**:  
   The shifted values are converted back to characters, forming the encrypted result.

## 🚀 Getting Started

### Requirements

- Python 3.x

### Installation

```bash
git clone https://github.com/yourusername/caesar-dynamic-cipher.git
cd caesar-dynamic-cipher
