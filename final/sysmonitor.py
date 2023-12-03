from flask import Flask, render_template, request
import psutil
import time
import platform
# from subprocess import call
from prettytable import PrettyTable
from apscheduler.schedulers.background import BackgroundScheduler


#function to pull system information
#global variables used so Flask has access to them later
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
    #Report no battery if None is detected
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
    #Use of PrettyTable([list of headings])
    #      .add_row([list of cells in row])
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
    #Use of PrettyTable again
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
    #Use of PrettyTable again
    #CPU percentage needs two calls, first to have a point of reference, 
    #   then a delay, and second call to record the measurement. Several
    #   posts about psutil cpu usage is less than task manager.
    print("--- Top 5 Processes ---")
    global procTable
    procTable = PrettyTable(['PID', 'PName', 'Status', 'CPU', 'Num Threads', 'Memory(MB)'])
    proc = []
    #Pull the pids, omitting pid 0 system idle process
    for pid in psutil.pids()[1:]:
        try:
            p = psutil.Process(pid)
            p.cpu_percent() #first time return 0.0
            proc.append(p)

        except Exception as e:
            pass

    top = {}
    time.sleep(0.1) #Delay to allow for cpu measurement
    for p in proc:
        #second time for measurement
        top[p] = (p.cpu_percent() / psutil.cpu_count())*7.5 

    top_list = sorted(top.items(), key=lambda x: x[1])
    top5 = top_list[-5:]
    top5.reverse()

    for p, cpu_percent in top5:
        #Some proecesses may exit so use of try-except block
        #May show on console now and then, but html should not be affected.
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

    #Atempted delay between scheduled tasks, some issues reported if scheduled 
    #   tasks start and stop at same time
    time.sleep(2) 


#initialize Flask and static folder for css
app = Flask(__name__, static_folder='static')
app.config.from_object(__name__)


#Use APScheduler to update system info at set interval
#With Debug mode on, Scheduler would initialize and run sensor function twice instead of once.
#Turned Debug mode off for this reason. Is a know issue with apscheduler.
sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=10)
sched.start()

#Have flask send variables to HTML.
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

