from flask import Flask, render_template, request
import psutil
import time
import platform
from subprocess import call
from prettytable import PrettyTable
from apscheduler.schedulers.background import BackgroundScheduler


#function to pull system information
def sensor():
    #Pull hostname
    print("--- System Name ---")    
    global hName
    hName = platform.node()
    print(hName)
    print()

    #Pull operating system
    print("--- Operating System ---")  
    global opSystem 
    opSystem = platform.system()
    global opRelease
    opRelease = platform.release()
    print(opSystem + " " + opRelease)
    print()

    #Pull battery information if battery is present
    print("--- Battery Info ---")
    global battery
    if (psutil.sensors_battery()) is None:
        battery = 'No Battery'
        print(" Battery Available: No Battery")
    else: 
        battery = psutil.sensors_battery().persent   
        print(" Battery Available: %d " % (battery,) + "%")
    print()

    #Pull network information
    print("--- Network Info ---")
    global table
    table = PrettyTable(['Network', 'Status', 'Speed'])
    for key in psutil.net_if_stats().keys():
        name = key
        if psutil.net_if_stats()[key].isup:
            up = "Up"
        else:
            up = "Down"
        speed = psutil.net_if_stats()[key].speed
        table.add_row([name, up, speed])
    print(table) # to console

    #convert table to html
    table = table.get_html_string()

    #Pull memory information
    print("--- Memory Info ---")
    global memTable
    memTable = PrettyTable(["Total(GB)", "Used(GB)", "Available(GB)", "Percentage"])
    vm = psutil.virtual_memory()
    memTable.add_row([
        f'{vm.total / 1e9:.3f}',
        f'{vm.used / 1e9:.3f}',
        f'{vm.available / 1e9:.3f}',
        vm.percent])
    print(memTable) #to console

    #convert memTable to html 
    memTable = memTable.get_html_string()

    #Pull the top 5 processes
    print("--- Top 5 Processes ---")
    global procTable
    procTable = PrettyTable(['PID', 'PName', 'Status', 'CPU', 'Num Threads', 'Memory(MB)'])
    proc = []
    for pid in psutil.pids()[1:]:
        try:
            p = psutil.Process(pid)
            p.cpu_percent()
            proc.append(p)

        except Exception as e:
            pass

    top = {}
    time.sleep(0.1)
    for p in proc:
        top[p] = p.cpu_percent() / psutil.cpu_count()

    top_list = sorted(top.items(), key=lambda x: x[1])
    top5 = top_list[-5:]
    top5.reverse()

    for p, cpu_percent in top5:

        try:
            with p.oneshot():
                procTable.add_row([
                    str(p.pid),
                    p.name(),
                    p.status(),
                    f'{cpu_percent:.2f}' + "%",
                    p.num_threads(),
                    f'{p.memory_info().rss / 1e6:.3f}'
                ])
        except Exception as e:
            pass

    print(procTable) #to console

    #convert procTable to html
    procTable = procTable.get_html_string()


#initialize Flask and static folder for css
app = Flask(__name__, static_folder='static')
app.config.from_object(__name__)


#Use APScheduler to update system info at set interval
sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=10)
sched.start()


@app.route('/')
def monitor():
    return render_template("main.html",
        opSystem=opSystem,
        opRelease=opRelease, 
        hName=hName,
        battery=battery, 
        table=table, 
        memTable=memTable,
        procTable=procTable)

