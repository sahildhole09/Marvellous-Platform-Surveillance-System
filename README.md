# 🖥️ Marvellous Platform Surveillance System

A Python-based Platform Surveillance and System Monitoring Automation Tool that periodically collects important system information and stores it in timestamped log files.

## 📌 Project Overview

The Marvellous Platform Surveillance System automates the collection of system-level information, including CPU, RAM, disk, network usage, and running processes.

The project uses `psutil` for system/process monitoring and `schedule` for periodic execution.

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
- ⏰ Automatic periodic execution
- 🛡️ Handles inaccessible or terminated processes safely

## 🗂️ Project Structure

```text
Marvellous-Platform-Surveillance/
│
├── PlatformSurveillance.py
├── ProcessScan.py
└── README.md
```

### `PlatformSurveillance.py`

This is the main automation program. It creates/verifies the log directory, creates timestamped log files, collects system information, invokes the process scanner, and writes the complete report to the log file.

### `ProcessScan.py`

This module scans running processes using `psutil` and collects PID, name, username, status, CPU usage, memory usage, and process creation time.

## 🛠️ Requirements

- Python 3.x
- `psutil`
- `schedule`

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Marvellous-Platform-Surveillance.git
```

### 2. Navigate to the project

```bash
cd Marvellous-Platform-Surveillance
```

### 3. Install dependencies

```bash
pip install psutil schedule
```

## ▶️ Usage

The general command format is:

```bash
python PlatformSurveillance.py Time_Interval Folder_Name
```

### Example

Run the surveillance system every 5 minutes and store logs in a `Logs` directory:

```bash
python PlatformSurveillance.py 5 Logs
```

The scheduler will continue running until it is stopped with:

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
| datetime | Process creation-time formatting |
| os | Directory and file operations |
| sys | Command-line argument handling |
| time | Timestamps and execution delay |

## ⚠️ Important Notes

- Some process information may require appropriate operating-system permissions.
- Processes that cannot be accessed are skipped safely.
- Disk monitoring currently uses the `/` filesystem path.
- A new log file is generated each time the surveillance function executes.
- The scheduler continues running until interrupted with `Ctrl + C`.

## 🚀 Future Enhancements

- [ ] Add Windows-specific disk monitoring
- [ ] Add CPU temperature monitoring
- [ ] Add battery monitoring
- [ ] Add GPU monitoring
- [ ] Add email notifications
- [ ] Add threshold-based alerts
- [ ] Export reports to CSV/JSON
- [ ] Add a graphical user interface
- [ ] Add configurable log retention
- [ ] Add network connection details
- [ ] Add configuration-file support

## 👨‍💻 Author

Name : Sahil Ashok Dhole

Course : Python Automation & Machine Learning

**Marvellous Platform Surveillance System**

Developed using Python for automated system monitoring and surveillance.

## 📜 License

Choose an appropriate open-source license for your GitHub repository. The MIT License is one possible option.

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
