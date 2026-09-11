import psutil
import sys
import os
import time
import schedule

from ProcessScan import ProcessScan

def PlatformSurveillance(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("\nDirectory for the log file gets created successfully\n")

    timestamp  = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets successfully created with name\n {FileName}\n")

    fobj.write(Border+"\n")
    fobj.write("----Marvellous Platform Surveillance System----\n")
    fobj.write("Log file gets created at "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-------------- System Report --------------\n")
    
    # CPU Information
    fobj.write("* CPU INFORMATION *\n")
    fobj.write(Border + "\n")
    fobj.write("Physical Cores : %s\n"% psutil.cpu_count(logical=False))
    fobj.write("Logical Cores : %s\n"% psutil.cpu_count())
    fobj.write("CPU Usage : %.2f %%\n"% psutil.cpu_percent())
    fobj.write(Border + "\n\n")

    # RAM Information
    memory = psutil.virtual_memory()

    fobj.write("* RAM INFORMATION *\n")
    fobj.write(Border + "\n")
    fobj.write("Total RAM : %.2f GB\n"% (memory.total / (1024 ** 3)))
    fobj.write("Available RAM : %.2f GB\n"% (memory.available / (1024 ** 3)))
    fobj.write("Used RAM : %.2f GB\n"% (memory.used / (1024 ** 3)))
    fobj.write("RAM Usage : %.2f %%\n"% memory.percent)
    fobj.write(Border + "\n\n")

    # Disk Information
    disk = psutil.disk_usage('/')

    fobj.write("* DISK INFORMATION *\n")
    fobj.write(Border + "\n")
    fobj.write("Total Disk : %.2f GB\n"% (disk.total / (1024 ** 3)))
    fobj.write("Used Disk : %.2f GB\n"% (disk.used / (1024 ** 3)))
    fobj.write("Free Disk : %.2f GB\n"% (disk.free / (1024 ** 3)))
    fobj.write("Disk Usage : %.2f %%\n"% disk.percent)
    fobj.write(Border + "\n\n")

    # Network Usage
    netobj = psutil.net_io_counters()
    
    fobj.write("* NETWORK INFORMATION *\n")
    fobj.write(Border + "\n")
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # Running Processes
    fobj.write("* RUNNING PROCESS INFORMATION *\n")
    fobj.write(Border + "\n")

    Data = ProcessScan()

    for info in Data:
        
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("User Name : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("CPU Usage : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory Usage : %.2f\n" %info.get("memory_percent"))
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("-------------- End of Log File ------------\n")
    fobj.write(Border+"\n")
    
    fobj.close()

def main():
    Border = "-"*50
    print(Border)
    print("----- Marvellous Platform Survillence System -----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to performs the following tasks:")
            print("1 : It fetch the information about the microprocessor")
            print("2 : It fetch the information about the primary storage as RAM")
            print("3 : It fetch the information about the secondary storage as HDD")
            print("4 : It fetch the information of Network Usage")
            print("5 : It fetch the information of running processes")
            print("6 : It gets auto scheduled periodically")
            print("7 : It maintain all records into log file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of Folder for log file creation")
            
        else:
            print("Unable to proceed as arguments are not matching")
            print("Please use --h or --u flag for getting more details")

    elif(len(sys.argv) == 3):
        try:
            print("Scheduler started successfully")
            print("Press Ctrl + C to abort the automation script")

            schedule.every(int(sys.argv[1])).minutes.do(PlatformSurveillance,sys.argv[2])

            while(True):
                schedule.run_pending()
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nAutomation Stopped Successfully")

        except Exception as e:
            print("Error :", e)

    else:
        print("Invalid number of argument")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("----Thank you for using our Automation System----")
    print(Border)

if __name__ == "__main__":
    main()