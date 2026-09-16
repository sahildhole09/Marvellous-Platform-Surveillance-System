# 🖥️ Marvellous Platform Surveillance System

A Python-based Platform Surveillance and System Monitoring Automation Tool that periodically collects CPU, RAM, disk, network, and running-process information, stores the report in timestamped log files, and automatically emails each generated log file to a specified receiver. 

## 📌 Project Overview

The system automates monitoring and reporting. At every configured interval it:

1. Collects CPU information.
2. Collects RAM information.
3. Collects disk information.
4. Collects network usage.
5. Scans running processes.
6. Creates a timestamped log file.
7. Sends the generated log file as an email attachment.

The main program imports `ProcessScan` and `SendMail`, and `PlatformSurveillance()` accepts both a log-folder name and receiver email address.

## ✨ Features

- 🧠 CPU monitoring
  - Physical CPU cores
  - Logical CPU cores
  - CPU usage
- 💾 RAM monitoring
  - Total RAM
  - Available RAM
  - Used RAM
  - RAM usage percentage
- 💽 Disk monitoring
  - Total disk space
  - Used disk space
  - Free disk space
  - Disk usage percentage
- 🌐 Network monitoring
  - Data sent
  - Data received
- ⚙️ Running process monitoring
  - PID
  - Process name
  - Username
  - Status
  - CPU usage
  - Memory usage
- 📝 Timestamped log-file generation
- ⏰ Automatic periodic scheduling
- 📧 Automatic email delivery
- 📎 Log file sent as an email attachment
- 🛡️ Handles inaccessible or terminated processes safely

## 🗂️ Project Structure

```text
Marvellous-Platform-Surveillance/
│
├── PlatformSurveillance.py
├── ProcessScan.py
├── Email.py
└── README.md
```

### `PlatformSurveillance.py`

This is the main automation program. It creates/verifies the log directory, generates the timestamped report, collects system information, scans processes, closes the log file, and then calls `SendMail()` to email the generated report.

### `ProcessScan.py`

This module scans running processes using `psutil` and collects PID, name, username, status, CPU usage, memory usage, and process creation time.

### `Email.py`

Contains `SendMail(FileName, ReceiverMail)`. It creates an email, attaches the generated log file, connects to Gmail SMTP over SSL, authenticates, sends the message, and closes the connection.

## 📧 Email Functionality

The project automatically sends every generated surveillance log to the receiver email.

Email subject:

```text
Marvellous Platform Surveillance System Log File
```

The generated `.log` file is attached to the email.

The implementation uses:

```text
SMTP Server : smtp.gmail.com
Port        : 465
Connection  : SMTP over SSL
```

## 🔐 Security Warning

**Never commit email passwords or Gmail App Passwords to GitHub.**

The current `Email.py` contains sender credentials directly in the source code. Before publishing the project, move them to environment variables or another secure configuration method.

Example:

```python
SenderMail = os.getenv("SENDER_EMAIL")
AppPassword = os.getenv("EMAIL_APP_PASSWORD")
```

If a real App Password has already been exposed, revoke it and create a new one.

## 🛠️ Requirements

- Python 3.x
- `psutil`
- `schedule`

The email functionality uses Python's built-in `smtplib` and `email` modules.

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Marvellous-Platform-Surveillance.git
cd Marvellous-Platform-Surveillance
pip install psutil schedule
```

| Argument | Description |
|---|---|
| `Time_Interval` | Time interval in minutes between executions |
| `Folder_Name` | Directory where log files are created |
| `Receiver_Email` | Email address receiving the generated log |

### Example

```bash
python PlatformSurveillance.py 5 Logs receiver@example.com
```

This runs the surveillance every 5 minutes, stores logs in `Logs`, and emails each generated log to the specified receiver.

Stop the scheduler with:

```text
Ctrl + C
```

## 📖 Command-Line Options

### Help

```bash
python PlatformSurveillance.py --h
```

or:

```bash
python PlatformSurveillance.py --H
```

The help option displays the tasks performed by the automation system.

### Usage

```bash
python PlatformSurveillance.py --u
```

or:

```bash
python PlatformSurveillance.py --U
```

This displays the command syntax and explains the time interval and folder-name parameters.

## 📝 Log Files

A new timestamped log file is created for each surveillance execution.

Example:

```text
Logs/
├── Marvellous_2026-09-11_20-30-15.log
├── Marvellous_2026-09-11_20-35-15.log
└── Marvellous_2026-09-11_20-40-15.log
```

The generated report contains sections for:

```text
CPU INFORMATION
RAM INFORMATION
DISK INFORMATION
NETWORK INFORMATION
RUNNING PROCESS INFORMATION
```

After the report is completed, it is passed to the email function as an attachment.

## 🔄 Working Flow

```text
Start Program
     │
     ▼
Read Command-Line Arguments
     │
     ▼
Create / Verify Log Directory
     │
     ▼
Create Timestamped Log File
     │
     ├──► CPU Information
     │
     ├──► RAM Information
     │
     ├──► Disk Information
     │
     ├──► Network Information
     │
     └──► Running Process Information
                    │
                    ▼
             Write System Report
                    │
                    ▼
              Close Log File
                    │
                    ▼
                SendMail()
                    │
                    ▼
             Attach Log File
                    │
                    ▼
              Gmail SMTP SSL
                    │
                    ▼
               Send Email
                    │
                    ▼
             Wait for Interval
                    │
                    └──────► Repeat
```

## 🧩 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| psutil | System and process information |
| schedule | Periodic task scheduling |
| smtplib | SMTP email communication |
| EmailMessage | Email creation and attachments |
| datetime | Process creation-time formatting |
| os | Directory and file operations |
| sys | Command-line argument handling |
| time | Timestamps and execution delay |

## ⚠️ Important Notes

- Gmail SMTP SSL is configured on port `465`.
- Email credentials should be kept out of source control.
- Some process information may require appropriate operating-system permissions.
- Processes that cannot be accessed are skipped safely.
- Disk monitoring currently uses the `/` filesystem path.
- A new log file is generated each time the surveillance function executes.
- The scheduler continues running until interrupted with `Ctrl + C`.
- Email errors are caught and displayed by the email module.

## 🚀 Future Enhancements

- [ ] Move email credentials to environment variables
- [ ] Add `.env` configuration
- [ ] Add configurable SMTP settings
- [ ] Add threshold-based email alerts
- [ ] Add Windows-specific disk monitoring
- [ ] Add CPU temperature monitoring
- [ ] Add battery monitoring
- [ ] Add GPU monitoring
- [ ] Export reports to CSV/JSON
- [ ] Add a graphical user interface
- [ ] Add configurable log retention
- [ ] Add network connection details
- [ ] Add HTML email reports

## 👨‍💻 Author

Name : Sahil Ashok Dhole

Course : Python Automation & Machine Learning

**Marvellous Platform Surveillance System**

Developed using Python for automated system monitoring, logging, scheduling, and email-based report delivery.

## 📜 License

Choose an appropriate open-source license for your GitHub repository. The MIT License is one possible option.

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
