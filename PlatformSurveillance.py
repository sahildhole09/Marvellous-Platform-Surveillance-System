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
        print("Directory for the log file gets created successfully")

    timestamp  = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets successfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("----Marvellous Platform Surveillance System----\n")
    fobj.write("Log file gets created at "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-------------- System Report --------------\n")

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
            print("This automation script is used to perform")
            print("1 : It fetch the information of running processes")
            print("2 : It gets auto scheduled periodically")
            print("3 : It maintain all records into log file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of Folder for log file creation")
            
        else:
            print("Unable to proceed as arguments are not matching")
            print("Please use --h or --u flag for getting more details")

    elif(len(sys.argv) == 3):

        print("Scheduler started successfully")
        print("Press Ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurveillance,sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of argument")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("----Thank you for using our Automation System----")
    print(Border)

if __name__ == "__main__":
    main()