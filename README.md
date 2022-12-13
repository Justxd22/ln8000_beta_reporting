# ln8000 Reporting

## installation
 - [Install recent version of termux](https://github.com/termux/termux-app#installation)
 - Install Python  
   `pkg install python3 git`
 - Download Or Clone Repo  
   `git clone https://github.com/Justxd22/ln8000_beta_reporting/`
 - Run  
   `cd ln8000_beta_reporting/ && python3 report.py`
 - [Make Shortcut if you want](https://github.com/termux/termux-widget#Installation)
 
## Usage and Notes
 - Dmesg logs require root access, grant from magisk  
   disable dmesg logging if you don't have root
 - Every run it will ask you for codename,  
   type anything uniqe so you can remeber it later  
   ex. RC1 BN0 KRN1 1213 1214  
   Random name will be generated if you press enter  
 - Script will auto report every 3mins  
   you can customize as you want  
 - By default it saves in /sdcard  
 - Sometimes termux is getting killed or whatever  
   Make sure you set wakelock  
 - Usb disconnections are detected (kind of)
 - Values are estimated and approx. so don't take it srsly!
 - Some apps show const. 5v input which is wrong most of the time,
   it's 4.4-4.8 v so watts may appear diff
 - use `current_watt_calc.py` if you want to compare readings with other apps
   
## Output
<details><summary>Sample Output</summary>
<p>

```bash
########### BESS VANT ############
##### 08:53:37 PM 13/12/2022 #####
######### Charging Report ########
Device Code : sweet
Rom ID      : TD1A.221105.003
Rom Host    : PixelOS-CI
Rom Flavor  : aosp_sweet-user
Test Name   : 1212-3 



####################################################################
########################## Report 0 ################################

Time Passed : 0s
Charge level: 39%
Temp        : 38.7Â°C
Watts       : 15.36w

###########################  DMESG  ################################
[ 2512.503180] ln8000@pri: psy_chg_get_ti_alarm_status: st:0x4:0x2:0x0:0x1f alarm=0x0
[ 2512.503705] [USBPD-PM]: usbpd_pm_workfunc: usbpd_pm_workfunc:pd_bat_volt_lp_lmt=4470, vbatt_now=4135
[ 2512.503716] [USBPD-PM]: usbpd_get_effective_fcc_val: effective_fcc_val: 3900
[ 2512.503721] [USBPD-PM]: usbpd_pm_fc2_charge_algo: curr_ibus_limit:2050
[ 2512.503727] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_limit:2150
[ 2512.503732] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_total_ma: 2132
[ 2512.503736] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbus_mv: 8784
[ 2512.503740] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbat_mv: 4135
[ 2512.503745] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibat_ma: 3799
[ 2512.503750] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_ibus:0
[ 2512.503756] [USBPD-PM]: usbpd_pm_fc2_charge_algo: pdpm->cp.vbat_reg:0, pdpm->cp.ibat_reg:0
[ 2512.503760] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_bat_reg:1
[ 2512.503765] [USBPD-PM]: usbpd_pm_fc2_charge_algo: sw_ctrl_steps:0
[ 2512.503769] [USBPD-PM]: usbpd_pm_fc2_charge_algo: hw_ctrl_steps:1
[ 2512.503964] [USBPD-PM]: usbpd_pm_check_cp_enabled: pdpm->cp.charge_enabled:1
[ 2512.503973] [USBPD-PM]: pd_get_batt_current_thermal_level: pval.intval: 5
[ 2512.505934] [USBPD-PM]: pd_disable_cp_by_jeita_status: batt_temp: 388
[ 2512.505944] [USBPD-PM]: usbpd_pm_fc2_charge_algo: is_temp_out_fc2_range:0
[ 2512.505950] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, sw_ctrl_steps:0, hw_ctrl_steps:1
[ 2512.505956] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, pdpm->request_voltage: 9200
[ 2512.506241] usbpd usbpd0: pd->tx_msgid[sop]:6,hdr:1a82
[ 2512.527500] [USBPD-PM]: usbpd_pm_sm: request_voltage:9200, request_current:2050
[ 2512.846473] request pdo: 5, uv: 9220000, ua: 3000000
[ 2512.846488] usbpd usbpd0: PPS is controlled by ourself, return not support
[ 2512.863524] ibat_ua =-3673708

####################################################################
####################################################################
    



####################################################################
########################## Report 1 ################################

Time Passed : 3m
Charge level: 45%
Temp        : 39.5Â°C
Watts       : 18.72w

###########################  DMESG  ################################
[ 2692.266050] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbus_mv: 8960
[ 2692.266055] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbat_mv: 4200
[ 2692.266060] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibat_ma: 4301
[ 2692.266064] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_ibus:1
[ 2692.266069] [USBPD-PM]: usbpd_pm_fc2_charge_algo: pdpm->cp.vbat_reg:0, pdpm->cp.ibat_reg:0
[ 2692.266075] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_bat_reg:1
[ 2692.266079] [USBPD-PM]: usbpd_pm_fc2_charge_algo: sw_ctrl_steps:1
[ 2692.266083] [USBPD-PM]: usbpd_pm_fc2_charge_algo: hw_ctrl_steps:1
[ 2692.266280] [USBPD-PM]: usbpd_pm_check_cp_enabled: pdpm->cp.charge_enabled:1
[ 2692.266288] [USBPD-PM]: pd_get_batt_current_thermal_level: pval.intval: 3
[ 2692.268478] [USBPD-PM]: pd_disable_cp_by_jeita_status: batt_temp: 396
[ 2692.268495] [USBPD-PM]: usbpd_pm_fc2_charge_algo: is_temp_out_fc2_range:0
[ 2692.268505] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 1, sw_ctrl_steps:1, hw_ctrl_steps:1
[ 2692.268510] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 1, pdpm->request_voltage: 9460
[ 2692.268568] usbpd usbpd0: pd->tx_msgid[sop]:5,hdr:1882
[ 2692.271992] pm6150_charger: smblib_set_charge_param: switching frequency = 1050 (0x08)
[ 2692.272038] pm6150_charger: smblib_usb_pd_adapter_allowance_override: set USBIN_ALLOW_OVERRIDE: 8
[ 2692.272079] pm6150_charger: smblib_set_charge_param: AICL CONT threshold = 8440 (0x1e)
[ 2692.272399] fv calibrate = 0, fv = 4470000
[ 2692.272416] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)
[ 2692.294035] pm6150_charger: smblib_usb_pd_adapter_allowance_override: set USBIN_ALLOW_OVERRIDE: 8
[ 2692.294050] pm6150_charger: smblib_set_charge_param: AICL CONT threshold = 8460 (0x1e)
[ 2692.294305] [USBPD-PM]: usbpd_pm_sm: request_voltage:9460, request_current:2350
[ 2692.294445] fv calibrate = 0, fv = 4470000
[ 2692.294464] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)

####################################################################
####################################################################
    



####################################################################
########################## Report 2 ################################

Time Passed : 6m
Charge level: 51%
Temp        : 39.2Â°C
Watts       : 18.2w

###########################  DMESG  ################################
[ 2872.492383] ibat_ua =-4520877
[ 2872.495961] ln8000@pri: psy_chg_get_ti_alarm_status: debug adc_vin=9040(th=11000), adc_iin=2264(th=3500), adc_vbat=4235(th=4525), v_offset=570
[ 2872.496292] ln8000@pri: psy_chg_get_ti_alarm_status: adc_vin=9040(th=11000), adc_iin=2264(th=3500), adc_vbat=4235(th=4525), v_offset=570
[ 2872.496296] ln8000@pri: psy_chg_get_ti_alarm_status: st:0x4:0x2:0x0:0x1f alarm=0x0
[ 2872.496905] [USBPD-PM]: usbpd_pm_workfunc: usbpd_pm_workfunc:pd_bat_volt_lp_lmt=4470, vbatt_now=4235
[ 2872.496923] [USBPD-PM]: usbpd_get_effective_fcc_val: effective_fcc_val: 4500
[ 2872.496932] [USBPD-PM]: usbpd_pm_fc2_charge_algo: curr_ibus_limit:2350
[ 2872.496939] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_limit:2350
[ 2872.496948] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_total_ma: 2229
[ 2872.496954] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbus_mv: 9040
[ 2872.496959] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbat_mv: 4235
[ 2872.496965] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibat_ma: 4520
[ 2872.496971] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_ibus:1
[ 2872.496977] [USBPD-PM]: usbpd_pm_fc2_charge_algo: pdpm->cp.vbat_reg:0, pdpm->cp.ibat_reg:0
[ 2872.496983] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_bat_reg:1
[ 2872.496989] [USBPD-PM]: usbpd_pm_fc2_charge_algo: sw_ctrl_steps:0
[ 2872.496995] [USBPD-PM]: usbpd_pm_fc2_charge_algo: hw_ctrl_steps:1
[ 2872.497233] [USBPD-PM]: usbpd_pm_check_cp_enabled: pdpm->cp.charge_enabled:1
[ 2872.497247] [USBPD-PM]: pd_get_batt_current_thermal_level: pval.intval: 3
[ 2872.499969] [USBPD-PM]: pd_disable_cp_by_jeita_status: batt_temp: 392
[ 2872.499998] [USBPD-PM]: usbpd_pm_fc2_charge_algo: is_temp_out_fc2_range:0
[ 2872.500012] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, sw_ctrl_steps:0, hw_ctrl_steps:1
[ 2872.500020] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, pdpm->request_voltage: 9460
[ 2872.500418] usbpd usbpd0: pd->tx_msgid[sop]:7,hdr:1c82
[ 2872.523826] [USBPD-PM]: usbpd_pm_sm: request_voltage:9460, request_current:2350

####################################################################
####################################################################
    



####################################################################
########################## Report 3 ################################

Time Passed : 9m
Charge level: 56%
Temp        : 40.0Â°C
Watts       : 18.7w

###########################  DMESG  ################################
[ 3052.902571] ibat_ua =-4442752
[ 3052.907414] ln8000@pri: psy_chg_get_ti_alarm_status: debug adc_vin=9120(th=11000), adc_iin=2322(th=3500), adc_vbat=4265(th=4525), v_offset=590
[ 3052.907740] ln8000@pri: psy_chg_get_ti_alarm_status: adc_vin=9120(th=11000), adc_iin=2322(th=3500), adc_vbat=4265(th=4525), v_offset=590
[ 3052.907744] ln8000@pri: psy_chg_get_ti_alarm_status: st:0x4:0x2:0x0:0x1f alarm=0x0
[ 3052.908299] [USBPD-PM]: usbpd_pm_workfunc: usbpd_pm_workfunc:pd_bat_volt_lp_lmt=4470, vbatt_now=4265
[ 3052.908313] [USBPD-PM]: usbpd_get_effective_fcc_val: effective_fcc_val: 4500
[ 3052.908319] [USBPD-PM]: usbpd_pm_fc2_charge_algo: curr_ibus_limit:2350
[ 3052.908325] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_limit:2350
[ 3052.908330] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_total_ma: 2322
[ 3052.908335] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbus_mv: 9120
[ 3052.908340] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbat_mv: 4265
[ 3052.908344] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibat_ma: 4442
[ 3052.908349] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_ibus:0
[ 3052.908354] [USBPD-PM]: usbpd_pm_fc2_charge_algo: pdpm->cp.vbat_reg:0, pdpm->cp.ibat_reg:0
[ 3052.908358] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_bat_reg:1
[ 3052.908363] [USBPD-PM]: usbpd_pm_fc2_charge_algo: sw_ctrl_steps:0
[ 3052.908367] [USBPD-PM]: usbpd_pm_fc2_charge_algo: hw_ctrl_steps:1
[ 3052.908602] [USBPD-PM]: usbpd_pm_check_cp_enabled: pdpm->cp.charge_enabled:1
[ 3052.908616] [USBPD-PM]: pd_get_batt_current_thermal_level: pval.intval: 3
[ 3052.910609] [USBPD-PM]: pd_disable_cp_by_jeita_status: batt_temp: 400
[ 3052.910628] [USBPD-PM]: usbpd_pm_fc2_charge_algo: is_temp_out_fc2_range:0
[ 3052.910638] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, sw_ctrl_steps:0, hw_ctrl_steps:1
[ 3052.910643] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, pdpm->request_voltage: 9540
[ 3052.910702] usbpd usbpd0: pd->tx_msgid[sop]:1,hdr:1082
[ 3052.932841] [USBPD-PM]: usbpd_pm_sm: request_voltage:9540, request_current:2350

####################################################################
####################################################################
    



####################################################################
########################## Report 4 ################################

Time Passed : 12m
Charge level: 61%
Temp        : 40.4Â°C
Watts       : 19.42w

###########################  DMESG  ################################
[ 3232.220610] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbus_mv: 9216
[ 3232.220615] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbat_mv: 4315
[ 3232.220620] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibat_ma: 4587
[ 3232.220624] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_ibus:1
[ 3232.220629] [USBPD-PM]: usbpd_pm_fc2_charge_algo: pdpm->cp.vbat_reg:0, pdpm->cp.ibat_reg:0
[ 3232.220633] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_bat_reg:1
[ 3232.220638] [USBPD-PM]: usbpd_pm_fc2_charge_algo: sw_ctrl_steps:-1
[ 3232.220642] [USBPD-PM]: usbpd_pm_fc2_charge_algo: hw_ctrl_steps:1
[ 3232.220849] [USBPD-PM]: usbpd_pm_check_cp_enabled: pdpm->cp.charge_enabled:1
[ 3232.220859] [USBPD-PM]: pd_get_batt_current_thermal_level: pval.intval: 3
[ 3232.223159] [USBPD-PM]: pd_disable_cp_by_jeita_status: batt_temp: 404
[ 3232.223185] [USBPD-PM]: usbpd_pm_fc2_charge_algo: is_temp_out_fc2_range:0
[ 3232.223199] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: -1, sw_ctrl_steps:-1, hw_ctrl_steps:1
[ 3232.223209] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: -1, pdpm->request_voltage: 9620
[ 3232.223507] usbpd usbpd0: pd->tx_msgid[sop]:4,hdr:1682
[ 3232.227001] pm6150_charger: smblib_usb_pd_adapter_allowance_override: set USBIN_ALLOW_OVERRIDE: 8
[ 3232.227018] pm6150_charger: smblib_set_charge_param: AICL CONT threshold = 8620 (0x1f)
[ 3232.227904] fv calibrate = 0, fv = 4470000
[ 3232.227932] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)
[ 3232.247157] pm6150_charger: smblib_set_charge_param: switching frequency = 1050 (0x08)
[ 3232.247175] pm6150_charger: smblib_usb_pd_adapter_allowance_override: set USBIN_ALLOW_OVERRIDE: 8
[ 3232.247188] pm6150_charger: smblib_set_charge_param: AICL CONT threshold = 8620 (0x1f)
[ 3232.247557] [USBPD-PM]: usbpd_pm_sm: request_voltage:9620, request_current:2350
[ 3232.247703] fv calibrate = 0, fv = 4470000
[ 3232.247724] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)

####################################################################
####################################################################
    



####################################################################
########################## Report 5 ################################

Time Passed : 15m
Charge level: 66%
Temp        : 40.7Â°C
Watts       : 18.49w

###########################  DMESG  ################################
[ 3412.680809] fv calibrate = 0, fv = 4470000
[ 3412.680823] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)
[ 3412.874275] ibat_ua =-4555667
[ 3412.960045] ibat_ua =-4445193
[ 3412.962264] ibat_ua =-4445193
[ 3412.962305] QG-K: qg_battery_soc_smooth_tracking: soc:66, last_soc:66, raw_soc:67, soc_changed:1, update_now:0, charge_status:1, batt_ma:-4445
[ 3412.962329] QG-K: soc_monitor_work: soc:67, raw_soc:67, c:-4445, s:1
[ 3412.962400] batt power supply prop 124 not supported
[ 3412.962517] ibat_ua =-4445193
[ 3412.962694] fv calibrate = 0, fv = 4470000
[ 3412.962698] ibat_ua =-4445193
[ 3412.962732] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)
[ 3412.962779] QG-K: qg_status_change_work: charge_status=1 charge_done=0
[ 3412.963463] ibat_ua =-4445193
[ 3412.966509] QG-K: qg_charge_full_update: msoc=67 health=1 charge_full=0 charge_done=0 charge_status=1
[ 3412.967654] ibat_ua =-4445193
[ 3412.967711] ibat_ua =-4445193
[ 3412.969132] ibat_ua =-4445193
[ 3412.969218] ibat_ua =-4445193
[ 3412.969341] ibat_ua =-4445193
[ 3412.971775] ibat_ua =-4445193
[ 3412.972244] ibat_ua =-4445193
[ 3412.972321] ibat_ua =-4445193
[ 3412.972428] ibat_ua =-4445193
[ 3412.975304] ibat_ua =-4445193

####################################################################
####################################################################
    



####################################################################
########################## Report 6 ################################

Time Passed : 18m
Charge level: 72%
Temp        : 40.9Â°C
Watts       : 19.96w

###########################  DMESG  ################################
[ 3592.296671] ln8000@pri: psy_chg_get_ti_alarm_status: adc_vin=9376(th=11000), adc_iin=2342(th=3500), adc_vbat=4405(th=4525), v_offset=566
[ 3592.296675] ln8000@pri: psy_chg_get_ti_alarm_status: st:0x4:0x2:0x0:0x1f alarm=0x0
[ 3592.297207] [USBPD-PM]: usbpd_pm_workfunc: usbpd_pm_workfunc:pd_bat_volt_lp_lmt=4470, vbatt_now=4405
[ 3592.297219] [USBPD-PM]: usbpd_get_effective_fcc_val: effective_fcc_val: 4500
[ 3592.297224] [USBPD-PM]: usbpd_pm_fc2_charge_algo: curr_ibus_limit:2350
[ 3592.297230] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_limit:2350
[ 3592.297234] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_total_ma: 2342
[ 3592.297239] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbus_mv: 9376
[ 3592.297244] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbat_mv: 4405
[ 3592.297248] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibat_ma: 4434
[ 3592.297252] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_ibus:0
[ 3592.297256] [USBPD-PM]: usbpd_pm_fc2_charge_algo: pdpm->cp.vbat_reg:0, pdpm->cp.ibat_reg:0
[ 3592.297265] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_bat_reg:1
[ 3592.297269] [USBPD-PM]: usbpd_pm_fc2_charge_algo: sw_ctrl_steps:0
[ 3592.297273] [USBPD-PM]: usbpd_pm_fc2_charge_algo: hw_ctrl_steps:1
[ 3592.297515] [USBPD-PM]: usbpd_pm_check_cp_enabled: pdpm->cp.charge_enabled:1
[ 3592.297525] [USBPD-PM]: pd_get_batt_current_thermal_level: pval.intval: 3
[ 3592.299802] [USBPD-PM]: pd_disable_cp_by_jeita_status: batt_temp: 410
[ 3592.299818] [USBPD-PM]: usbpd_pm_fc2_charge_algo: is_temp_out_fc2_range:0
[ 3592.299827] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, sw_ctrl_steps:0, hw_ctrl_steps:1
[ 3592.299847] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, pdpm->request_voltage: 9820
[ 3592.299955] usbpd usbpd0: pd->tx_msgid[sop]:5,hdr:1882
[ 3592.321636] [USBPD-PM]: usbpd_pm_sm: request_voltage:9820, request_current:2350
[ 3592.336849] request pdo: 5, uv: 9840000, ua: 3000000
[ 3592.336867] usbpd usbpd0: PPS is controlled by ourself, return not support

####################################################################
####################################################################
    



####################################################################
########################## Report 7 ################################

Time Passed : 21m
Charge level: 77%
Temp        : 40.4Â°C
Watts       : 16.52w

###########################  DMESG  ################################
[ 3772.570473] ibat_ua =-3917544
[ 3772.574041] ln8000@pri: psy_chg_get_ti_alarm_status: debug adc_vin=9360(th=11000), adc_iin=1956(th=3500), adc_vbat=4430(th=4525), v_offset=500
[ 3772.574354] ln8000@pri: psy_chg_get_ti_alarm_status: adc_vin=9360(th=11000), adc_iin=1956(th=3500), adc_vbat=4430(th=4525), v_offset=500
[ 3772.574359] ln8000@pri: psy_chg_get_ti_alarm_status: st:0x4:0x2:0x0:0x1f alarm=0x0
[ 3772.574971] [USBPD-PM]: usbpd_pm_workfunc: usbpd_pm_workfunc:pd_bat_volt_lp_lmt=4470, vbatt_now=4430
[ 3772.574986] [USBPD-PM]: usbpd_get_effective_fcc_val: effective_fcc_val: 3900
[ 3772.574994] [USBPD-PM]: usbpd_pm_fc2_charge_algo: curr_ibus_limit:2050
[ 3772.575002] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_limit:2050
[ 3772.575009] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibus_total_ma: 1956
[ 3772.575016] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbus_mv: 9360
[ 3772.575022] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbat_mv: 4430
[ 3772.575028] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibat_ma: 3917
[ 3772.575034] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_ibus:1
[ 3772.575041] [USBPD-PM]: usbpd_pm_fc2_charge_algo: pdpm->cp.vbat_reg:0, pdpm->cp.ibat_reg:0
[ 3772.575046] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_bat_reg:1
[ 3772.575052] [USBPD-PM]: usbpd_pm_fc2_charge_algo: sw_ctrl_steps:0
[ 3772.575059] [USBPD-PM]: usbpd_pm_fc2_charge_algo: hw_ctrl_steps:1
[ 3772.575297] [USBPD-PM]: usbpd_pm_check_cp_enabled: pdpm->cp.charge_enabled:1
[ 3772.575309] [USBPD-PM]: pd_get_batt_current_thermal_level: pval.intval: 3
[ 3772.578199] [USBPD-PM]: pd_disable_cp_by_jeita_status: batt_temp: 404
[ 3772.578210] [USBPD-PM]: usbpd_pm_fc2_charge_algo: is_temp_out_fc2_range:0
[ 3772.578222] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, sw_ctrl_steps:0, hw_ctrl_steps:1
[ 3772.578229] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: 0, pdpm->request_voltage: 9700
[ 3772.578575] usbpd usbpd0: pd->tx_msgid[sop]:7,hdr:1c82
[ 3772.601207] [USBPD-PM]: usbpd_pm_sm: request_voltage:9700, request_current:2050

####################################################################
####################################################################
    



####################################################################
########################## Report 8 ################################

Time Passed : 24m
Charge level: 81%
Temp        : 39.5Â°C
Watts       : 14.48w

###########################  DMESG  ################################
[ 3952.361229] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbus_mv: 9344
[ 3952.361247] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbat_mv: 4440
[ 3952.361251] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibat_ma: 3315
[ 3952.361255] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_ibus:-1
[ 3952.361260] [USBPD-PM]: usbpd_pm_fc2_charge_algo: pdpm->cp.vbat_reg:0, pdpm->cp.ibat_reg:0
[ 3952.361263] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_bat_reg:1
[ 3952.361269] [USBPD-PM]: usbpd_pm_fc2_charge_algo: sw_ctrl_steps:-1
[ 3952.361273] [USBPD-PM]: usbpd_pm_fc2_charge_algo: hw_ctrl_steps:1
[ 3952.361521] [USBPD-PM]: usbpd_pm_check_cp_enabled: pdpm->cp.charge_enabled:1
[ 3952.361543] [USBPD-PM]: pd_get_batt_current_thermal_level: pval.intval: 5
[ 3952.363713] [USBPD-PM]: pd_disable_cp_by_jeita_status: batt_temp: 396
[ 3952.363727] [USBPD-PM]: usbpd_pm_fc2_charge_algo: is_temp_out_fc2_range:0
[ 3952.363737] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: -1, sw_ctrl_steps:-1, hw_ctrl_steps:1
[ 3952.363744] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: -1, pdpm->request_voltage: 9680
[ 3952.363800] usbpd usbpd0: pd->tx_msgid[sop]:7,hdr:1c82
[ 3952.367351] pm6150_charger: smblib_usb_pd_adapter_allowance_override: set USBIN_ALLOW_OVERRIDE: 8
[ 3952.367366] pm6150_charger: smblib_set_charge_param: AICL CONT threshold = 8680 (0x1f)
[ 3952.367715] fv calibrate = 0, fv = 4470000
[ 3952.367731] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)
[ 3952.387231] pm6150_charger: smblib_set_charge_param: switching frequency = 1050 (0x08)
[ 3952.387245] pm6150_charger: smblib_usb_pd_adapter_allowance_override: set USBIN_ALLOW_OVERRIDE: 8
[ 3952.387256] pm6150_charger: smblib_set_charge_param: AICL CONT threshold = 8680 (0x1f)
[ 3952.387884] fv calibrate = 0, fv = 4470000
[ 3952.387903] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)
[ 3952.390510] [USBPD-PM]: usbpd_pm_sm: request_voltage:9680, request_current:1950

####################################################################
####################################################################
    



####################################################################
########################## Report 9 ################################

Time Passed : 27m
Charge level: 84%
Temp        : 38.3Â°C
Watts       : 12.93w

###########################  DMESG  ################################
[ 4132.623979] ibat_ua =-3035890
[ 4132.626353] ibat_ua =-3035890
[ 4132.626962] ibat_ua =-3035890
[ 4132.627074] ibat_ua =-3035890
[ 4132.627248] ibat_ua =-3035890
[ 4132.630446] ibat_ua =-3035890
[ 4132.638854] ibat_ua =-3035890
[ 4132.718031] batt power supply prop 124 not supported
[ 4132.718185] ibat_ua =-2915651
[ 4132.718354] ibat_ua =-2915651
[ 4132.718413] QG-K: qg_status_change_work: charge_status=1 charge_done=0
[ 4132.718846] fv calibrate = 0, fv = 4470000
[ 4132.718861] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)
[ 4132.719093] ibat_ua =-2915651
[ 4132.722306] QG-K: qg_charge_full_update: msoc=84 health=1 charge_full=0 charge_done=0 charge_status=1
[ 4132.723554] ibat_ua =-2915651
[ 4132.723611] ibat_ua =-2915651
[ 4132.724999] ibat_ua =-2915651
[ 4132.725083] ibat_ua =-2915651
[ 4132.725185] ibat_ua =-2915651
[ 4132.727614] ibat_ua =-2915651
[ 4132.728100] ibat_ua =-2915651
[ 4132.728178] ibat_ua =-2915651
[ 4132.728318] ibat_ua =-2915651
[ 4132.731289] ibat_ua =-2915651

####################################################################
####################################################################
    



####################################################################
########################## Report 10 ################################

Time Passed : 30m
Charge level: 87%
Temp        : 37.5Â°C
Watts       : 10.4w

###########################  DMESG  ################################
[ 4312.665574] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbus_mv: 9280
[ 4312.665580] [USBPD-PM]: usbpd_pm_fc2_charge_algo: vbat_mv: 4455
[ 4312.665584] [USBPD-PM]: usbpd_pm_fc2_charge_algo: ibat_ma: 2440
[ 4312.665589] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_ibus:-1
[ 4312.665594] [USBPD-PM]: usbpd_pm_fc2_charge_algo: pdpm->cp.vbat_reg:0, pdpm->cp.ibat_reg:0
[ 4312.665598] [USBPD-PM]: usbpd_pm_fc2_charge_algo: step_bat_reg:1
[ 4312.665604] [USBPD-PM]: usbpd_pm_fc2_charge_algo: sw_ctrl_steps:-1
[ 4312.665613] [USBPD-PM]: usbpd_pm_fc2_charge_algo: hw_ctrl_steps:1
[ 4312.665820] [USBPD-PM]: usbpd_pm_check_cp_enabled: pdpm->cp.charge_enabled:1
[ 4312.665829] [USBPD-PM]: pd_get_batt_current_thermal_level: pval.intval: 5
[ 4312.667797] [USBPD-PM]: pd_disable_cp_by_jeita_status: batt_temp: 375
[ 4312.667805] [USBPD-PM]: usbpd_pm_fc2_charge_algo: is_temp_out_fc2_range:0
[ 4312.667812] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: -1, sw_ctrl_steps:-1, hw_ctrl_steps:1
[ 4312.667818] [USBPD-PM]: usbpd_pm_fc2_charge_algo: steps: -1, pdpm->request_voltage: 9520
[ 4312.667872] usbpd usbpd0: pd->tx_msgid[sop]:7,hdr:1c82
[ 4312.671001] pm6150_charger: smblib_usb_pd_adapter_allowance_override: set USBIN_ALLOW_OVERRIDE: 8
[ 4312.671014] pm6150_charger: smblib_set_charge_param: AICL CONT threshold = 8520 (0x1e)
[ 4312.671176] fv calibrate = 0, fv = 4470000
[ 4312.671194] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)
[ 4312.691014] pm6150_charger: smblib_set_charge_param: switching frequency = 1050 (0x08)
[ 4312.691027] pm6150_charger: smblib_usb_pd_adapter_allowance_override: set USBIN_ALLOW_OVERRIDE: 8
[ 4312.691038] pm6150_charger: smblib_set_charge_param: AICL CONT threshold = 8520 (0x1e)
[ 4312.691361] [USBPD-PM]: usbpd_pm_sm: request_voltage:9520, request_current:1550
[ 4312.691370] fv calibrate = 0, fv = 4470000
[ 4312.691391] pm6150_charger: smblib_set_charge_param: float voltage = 4470000 (0x57)

####################################################################
####################################################################
    



####################################################################
########################## Report 11 ################################

Time Passed : 33m
Charge level: 89%
Temp        : 37.1Â°C
Watts       : 5.98w

###########################  DMESG  ################################
[ 4492.266259] ibat_ua =-928040
[ 4492.268364] QG-K: qg_charge_full_update: msoc=89 health=1 charge_full=0 charge_done=0 charge_status=1
[ 4492.269513] ibat_ua =-928040
[ 4492.269572] ibat_ua =-928040
[ 4492.272073] ibat_ua =-928040
[ 4492.272409] ibat_ua =-928040
[ 4492.275023] QG-K: qg_psy_set_property: SOH update: SOH=100 esr_actual=64 esr_nominal=59
[ 4492.275732] ibat_ua =-928040
[ 4492.275899] ibat_ua =-928040
[ 4492.279812] ibat_ua =-928040
[ 4492.279965] ibat_ua =-928040
[ 4492.280171] ibat_ua =-928040
[ 4492.283732] ibat_ua =-928040
[ 4492.283931] ibat_ua =-928040
[ 4492.289100] ibat_ua =-928040
[ 4492.289526] ibat_ua =-928040
[ 4492.289761] ibat_ua =-928040
[ 4492.292641] ibat_ua =-928040
[ 4492.292812] ibat_ua =-928040
[ 4492.298492] ibat_ua =-928040
[ 4492.298703] ibat_ua =-928040
[ 4492.299193] ibat_ua =-928040
[ 4492.304281] ibat_ua =-928040
[ 4492.304458] ibat_ua =-928040
[ 4492.305946] ibat_ua =-928040

####################################################################
####################################################################
    



####################################################################
########################## Report 12 ################################

Time Passed : 36m
Charge level: 91%
Temp        : 36.5Â°C
Watts       : 6.45w

###########################  DMESG  ################################
[ 4671.563370] QCOM-STEPCHG: handle_jeita: BATT_TEMP = 365 FCC = 6000000uA FV = 4470000uV
[ 4671.564161] ibat_ua =-1308289
[ 4671.564216] ibat_ua =-1308289
[ 4671.566672] ibat_ua =-1308289
[ 4671.566768] ibat_ua =-1308289
[ 4671.566912] ibat_ua =-1308289
[ 4671.569215] ibat_ua =-1308289
[ 4671.569387] ibat_ua =-1308289
[ 4671.570592] ibat_ua =-1308289
[ 4671.570730] ibat_ua =-1308289
[ 4671.570933] ibat_ua =-1308289
[ 4671.573255] ibat_ua =-1308289
[ 4671.573386] ibat_ua =-1308289
[ 4671.585140] ibat_ua =-1308289
[ 4671.653610] init: Untracked pid 10411 exited with status 0
[ 4671.653659] init: Untracked pid 10411 did not have an associated service entry and will not be reaped
[ 4671.721863] request pdo: 5, uv: 5020000, ua: 3000000
[ 4671.721876] usbpd usbpd0: PPS is controlled by ourself, return not support
[ 4672.168975] ibat_ua =-1320191
[ 4672.434125] init: Untracked pid 10344 exited with status 0
[ 4672.434142] init: Untracked pid 10344 did not have an associated service entry and will not be reaped
[ 4672.479519] ibat_ua =-1253052
[ 4672.482433] ibat_ua =-1253052
[ 4672.482472] QG-K: qg_battery_soc_smooth_tracking: soc:91, last_soc:91, raw_soc:91, soc_changed:1, update_now:0, charge_status:1, batt_ma:-1253
[ 4672.482478] QG-K: soc_monitor_work: soc:91, raw_soc:91, c:-1253, s:1

####################################################################
####################################################################
```


</p>
</details>
