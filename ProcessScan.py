import psutil
import datetime

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","username","status"])

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["start_time"] = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%d-%m-%Y %H:%M:%S")

            listprocess.append(info)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess
