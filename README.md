
Multi-Protocol Tester 🌐

A modern, multi-threaded Python graphical user interface (GUI) application designed for testing and interacting with various network protocols. 

The ultimate goal of this project is to consolidate the core functionalities of tools like Postman (HTTP), PuTTY (SSH), and FileZilla (FTP) into a single, cohesive, and visually appealing environment.

## 🚀 Current Status: Phase 1 (HTTP)

The application currently supports HTTP(S) interactions. It provides a non-blocking GUI to send GET requests and inspect server responses, including status codes, headers, and body content.

### Features
- **Modern UI:** Built with `CustomTkinter` featuring a dark mode and sleek design.
- **Threaded Execution:** Network operations run in background daemon threads, preventing GUI freezes during long timeouts.
- **Auto-Formatting:** Automatically prepends `https://` to URLs if the protocol scheme is omitted.
- **Detailed Inspection:** Clearly separates HTTP Status Codes, Response Headers, and the Response Body for easy debugging.
- **Error Handling:** Gracefully handles timeouts (10s limit), connection errors, and invalid inputs.

## 📋 Prerequisites

- **Python 3.8+**
- Recommended OS: Linux (Tested on Kali Linux), macOS, or Windows.

## 🛠️ Installation & Setup

To avoid system-wide package conflicts (especially on Linux distributions enforcing PEP 668, like Kali Linux or Debian), it is highly recommended to run this project inside a Python Virtual Environment.

1. **Clone the repository:**
```bash
   git clone https://github.com/yourusername/multi-protocol-tester.git


   cd multi-protocol-tester





EHSAN SALEHI


