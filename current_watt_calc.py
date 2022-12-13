import os, time

while 1:
    v = round(int(os.popen("cat /sys/devices/platform/soc/c440000.qcom,spmi/spmi-0/spmi0-00/c440000.qcom,spmi:qcom,pm6150@0:qcom,qpnp-smb5/power_supply/battery/voltage_now").read().replace("\n",''))/1000000, 2)
    a = round(int(os.popen("cat /sys/devices/platform/soc/c440000.qcom,spmi/spmi-0/spmi0-00/c440000.qcom,spmi:qcom,pm6150@0:qcom,qpnp-smb5/power_supply/battery/current_now").read().replace("\n",'').replace("-",''))/1000, 2)
    print(round((v*a)/1000,2),'watts', v, 'v',a, 'ma')
    time.sleep(1)

# use this script to quickly compare values with other apps
# Open issue if you think my math is wrong lol
