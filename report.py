from datetime import datetime as dtime
import os, time, random

# normal charge lasts about 1h 100%
# So it would be fair to report every 10mins = every 10%
# but it heats up quickly and we need data before it heats
# therefore report every 3mins
# time passed shown in report is total time it took
# to charge to 100%
# timer is reset if charger was disconnected
# as it will be inacurrate data

# current date/time
d   = dtime.now()
day = d.strftime("%d%m")
tim = d.strftime("%I:%M:%S %p %d/%m/%Y")

# ask for current code_name
c_n = input("What is code_name you are testing? : ")
if not c_n:
   c_n = f"beta_{day}_{random.randint(0, 100)}"
   print("\n[WARN] You didn't give code_name one of the existing logs may be overwritten")

# run shell commands
def cat(cmd, remove_new_lines=True):
    return os.popen(cmd).read().replace('\n','') if remove_new_lines else os.popen(cmd).read()


# New File
filename = f"vant_{c_n}.txt"
f = open(f"/sdcard/{filename}", "a")
print(f"\n[INFO] Created {filename}")


flavor = cat("getprop ro.build.flavor")
host   = cat("getprop ro.build.host")
id     = cat("getprop ro.build.id")
code   = cat("getprop ro.build.product")

start = f"""
########### BESS VANT ############
##### {tim} #####
######### Charging Report ########
Device Code : {code}
Rom ID      : {id}
Rom Host    : {host}
Rom Flavor  : {flavor}
Test Name   : {c_n} """

print(start, file=f)
f.flush()

def log(t, n):
    timen = timeinletters(int(t))
    temp  = int(cat("cat /sys/devices/virtual/thermal/thermal_zone79/temp"))/1000
    level = cat("cat /sys/class/power_supply/battery/capacity")
    dmesg = cat("su -c 'dmesg | tail -25'", remove_new_lines=False) # last 25 line of dmesg
    # calc watt by Average of volts*amp three times
    data = []
    for i in range(3):
        v = round(int(os.popen("cat /sys/devices/platform/soc/c440000.qcom,spmi/spmi-0/spmi0-00/c440000.qcom,spmi:qcom,pm6150@0:qcom,qpnp-smb5/power_supply/battery/voltage_now").read().replace("\n",''))/1000000, 2)
        a = round(int(os.popen("cat /sys/devices/platform/soc/c440000.qcom,spmi/spmi-0/spmi0-00/c440000.qcom,spmi:qcom,pm6150@0:qcom,qpnp-smb5/power_supply/battery/current_now").read().replace("\n",'').replace("-",''))/1000, 2)
        data.append(round((v*a)/1000,2))
    # calc avg
    watts  = round(sum(data)/len(data),2)
    report = f"""\n\n
####################################################################
########################## Report {n} ################################

Time Passed : {timen}
Charge level: {level}%
Temp        : {temp}°C
Watts       : {watts}w

###########################  DMESG  ################################
{dmesg}
####################################################################
####################################################################
    """
    printf(report)
    if int(level) <= 100:
       printf(f"\n#### CHARGING COMPLETE IN {timen} ####")
       exit()


# check if charging
def is_connected():
    a = int(cat("cat /sys/class/power_supply/usb/online"))
    return bool(a)

# duplicate logging to terminal/text file
def printf(s):
    print(s)
    print(s, file=f)
    f.flush()

# homan readable format
def timeinletters(unixt):
    h = 86400
    m = 3540
    s = 59
    t    = int(time.time())
    diff = abs(t - unixt)
    if   diff < s:  return str(diff) + "s"
    elif diff < m:  return str(round(diff/60)) + "m"
    elif diff < h:  return str(int(diff/3600)) + "h"
    else:           return str(int(diff/86400)) + "days"

# constants
m = 60*3 # 3mins
c = 0     # time passed
n = 0
t = time.time()

# Real Code
while 1:
  # if 10mins passed
  if int(time.time()) >= c + m:
     if not is_connected():
        while 1:
          if not is_connected():
             printf("\n### Please Connect Charger to start logging ###")
             time.sleep(5)
             continue
          else:
             printf("\n### Usb Connected Charging Timer reset ###")
             t = time.time() # reset timer
             break
     c = int(time.time())
     log(t, n)
     n+=1
     continue
  else:
     sleep = (c+m) - int(time.time())
     print(f"\n[INFO] sleeping for {sleep}s")
     time.sleep(sleep)
     continue



# this is part of ln8000_beta_reporting project on github.com/justxd22
# credits goes to the boss bantom for porting ln8000
