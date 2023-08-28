from mininet.log import setLogLevel, info
import time, sys, os
from mn_wifi.link import wmediumd
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference
from mininet.term import makeTerm 
'''
os.system ("pip install openpyxl==3.0.10 ")
os.system ("pip install  pyexcel==0.6.7 ") #  --break-system-packages
os.system ("pip install  pyexcel-xlsx==0.6.0 ")
'''
def topology(args):
    print ("args are ", args) 
    'Create a network.'
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    if '-m' in args:
        sta1 = net.addStation('sta1', mac='00:00:00:00:00:01', ip='192.168.0.1/24', min_v=10.0, max_v=15.0, range=5) # min_v=5.0, max_v=10.0,
    else:
        sta1 = net.addStation('sta1', mac='00:00:00:00:00:01', ip='192.168.0.1/24', min_v=10.0, max_v=15.0, range=5) #  position='1,60,0',
    
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:02', ip='192.168.0.2/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:03', ip='192.168.0.3/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:04', ip='192.168.0.4/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    '''
    sta5 = net.addStation('sta5', mac='00:00:00:00:00:05', ip='192.168.0.5/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta6 = net.addStation('sta6', mac='00:00:00:00:00:06', ip='192.168.0.6/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta7 = net.addStation('sta7', mac='00:00:00:00:00:07', ip='192.168.0.7/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    
    sta8 = net.addStation('sta8', mac='00:00:00:00:00:08', ip='192.168.0.8/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta9 = net.addStation('sta9', mac='00:00:00:00:00:09', ip='192.168.0.9/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta10 = net.addStation('sta10', mac='00:00:00:00:00:10', ip='192.168.0.10/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    
    sta11 = net.addStation('sta11', mac='00:00:00:00:00:11', ip='192.168.0.11/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta12 = net.addStation('sta12', mac='00:00:00:00:00:12', ip='192.168.0.12/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta13 = net.addStation('sta13', mac='00:00:00:00:00:13', ip='192.168.0.13/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta14 = net.addStation('sta14', mac='00:00:00:00:00:14', ip='192.168.0.14/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta15 = net.addStation('sta15', mac='00:00:00:00:00:15', ip='192.168.0.15/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5) 
    sta16 = net.addStation('sta16', mac='00:00:00:00:00:16', ip='192.168.0.16/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta17 = net.addStation('sta17', mac='00:00:00:00:00:17', ip='192.168.0.17/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta18 = net.addStation('sta18', mac='00:00:00:00:00:18', ip='192.168.0.18/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta19 = net.addStation('sta19', mac='00:00:00:00:00:19', ip='192.168.0.19/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta20 = net.addStation('sta20', mac='00:00:00:00:00:20', ip='192.168.0.20/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    
    sta21 = net.addStation('sta21', mac='00:00:00:00:00:21', ip='192.168.0.21/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta22 = net.addStation('sta22', mac='00:00:00:00:00:22', ip='192.168.0.22/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta23 = net.addStation('sta23', mac='00:00:00:00:00:23', ip='192.168.0.23/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta24 = net.addStation('sta24', mac='00:00:00:00:00:24', ip='192.168.0.24/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta25 = net.addStation('sta25', mac='00:00:00:00:00:25', ip='192.168.0.25/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta26 = net.addStation('sta26', mac='00:00:00:00:00:26', ip='192.168.0.26/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta27 = net.addStation('sta27', mac='00:00:00:00:00:27', ip='192.168.0.27/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta28 = net.addStation('sta28', mac='00:00:00:00:00:28', ip='192.168.0.28/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta29 = net.addStation('sta29', mac='00:00:00:00:00:29', ip='192.168.0.29/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta30 = net.addStation('sta30', mac='00:00:00:00:00:30', ip='192.168.0.30/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    
    sta31 = net.addStation('sta31', mac='00:00:00:00:00:31', ip='192.168.0.31/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta32 = net.addStation('sta32', mac='00:00:00:00:00:32', ip='192.168.0.32/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta33 = net.addStation('sta33', mac='00:00:00:00:00:33', ip='192.168.0.33/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta34 = net.addStation('sta34', mac='00:00:00:00:00:34', ip='192.168.0.34/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta35 = net.addStation('sta35', mac='00:00:00:00:00:35', ip='192.168.0.35/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta36 = net.addStation('sta36', mac='00:00:00:00:00:36', ip='192.168.0.36/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta37 = net.addStation('sta37', mac='00:00:00:00:00:37', ip='192.168.0.37/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta38 = net.addStation('sta38', mac='00:00:00:00:00:38', ip='192.168.0.38/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta39 = net.addStation('sta39', mac='00:00:00:00:00:39', ip='192.168.0.39/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta40 = net.addStation('sta40', mac='00:00:00:00:00:40', ip='192.168.0.40/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    
    sta41 = net.addStation('sta41', mac='00:00:00:00:00:41', ip='192.168.0.41/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta42 = net.addStation('sta42', mac='00:00:00:00:00:42', ip='192.168.0.42/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta43 = net.addStation('sta43', mac='00:00:00:00:00:43', ip='192.168.0.43/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta44 = net.addStation('sta44', mac='00:00:00:00:00:44', ip='192.168.0.44/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta45 = net.addStation('sta45', mac='00:00:00:00:00:45', ip='192.168.0.45/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta46 = net.addStation('sta46', mac='00:00:00:00:00:46', ip='192.168.0.46/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta47 = net.addStation('sta47', mac='00:00:00:00:00:47', ip='192.168.0.47/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta48 = net.addStation('sta48', mac='00:00:00:00:00:48', ip='192.168.0.48/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta49 = net.addStation('sta49', mac='00:00:00:00:00:49', ip='192.168.0.49/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta50 = net.addStation('sta50', mac='00:00:00:00:00:50', ip='192.168.0.50/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    
    sta51 = net.addStation('sta51', mac='00:00:00:00:00:51', ip='192.168.0.51/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta52 = net.addStation('sta52', mac='00:00:00:00:00:52', ip='192.168.0.52/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta53 = net.addStation('sta53', mac='00:00:00:00:00:53', ip='192.168.0.53/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta54 = net.addStation('sta54', mac='00:00:00:00:00:54', ip='192.168.0.54/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta55 = net.addStation('sta55', mac='00:00:00:00:00:55', ip='192.168.0.55/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta56 = net.addStation('sta56', mac='00:00:00:00:00:56', ip='192.168.0.56/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta57 = net.addStation('sta57', mac='00:00:00:00:00:57', ip='192.168.0.57/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta58 = net.addStation('sta58', mac='00:00:00:00:00:58', ip='192.168.0.58/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta59 = net.addStation('sta59', mac='00:00:00:00:00:59', ip='192.168.0.59/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    sta60 = net.addStation('sta60', mac='00:00:00:00:00:60', ip='192.168.0.60/24', position='90,60,0', min_v=10.0, max_v=15.0, range=5)
    '''
    
    RSU1 = net.addStation('RSU1', mac='02:00:00:00:01:00', ip='192.168.0.100/24', position='35,35,0', color='r')
    RSU2 = net.addStation('RSU2', mac='02:00:00:00:02:00', ip='192.168.1.100/24', position='85,35,0', color='b')

    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring nodes\n")
    net.configureWifiNodes()

    RSU1.setMasterMode(intf='RSU1-wlan0', ssid='RSU1-ssid', channel='4', mode='g', range=30)
    RSU2.setMasterMode(intf='RSU2-wlan0', ssid='RSU2-ssid', channel='4', mode='g', range=30)

    info("*** Adding Link\n")
    net.addLink(RSU1, RSU2)  # wired connection

    if '-p' not in args:
        info("*** Plotting Graph\n")
        net.plotGraph(max_x=135, max_y=70)

    if '-m' not in args:
        print ("Starting Mobility")
        net.startMobility (time=0, seed=1, model='RandomDirection', AC='ssf')

        net.mobility(sta1, 'start', time=10, position='2,40,0')
        net.mobility(sta1, 'stop', time=20, position='120,40,0') # 60
        
        net.mobility(sta2, 'start', time=10, position='2,35,0')
        net.mobility(sta2, 'stop', time=20, position='120,35,0')
        
        net.mobility(sta3, 'start', time=10, position='2,35,0')
        net.mobility(sta3, 'stop', time=20, position='120,35,0')
        
        net.mobility(sta4, 'start', time=20, position='50,35,0')
        net.mobility(sta4, 'stop', time=27, position='120,35,0')
        '''
        net.mobility(sta5, 'start', time=20, position='50,35,0')
        net.mobility(sta5, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta6, 'start', time=20, position='50,35,0')
        net.mobility(sta6, 'stop', time=27, position='120,35,0')

        net.mobility(sta7, 'start', time=20, position='50,35,0')
        net.mobility(sta7, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta8, 'start', time=20, position='50,35,0')
        net.mobility(sta8, 'stop', time=27, position='120,35,0')

        net.mobility(sta9, 'start', time=20, position='50,35,0')
        net.mobility(sta9, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta10, 'start', time=20, position='50,35,0')
        net.mobility(sta10, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta11, 'start', time=20, position='50,35,0')
        net.mobility(sta11, 'stop', time=27, position='120,35,0')

        net.mobility(sta12, 'start', time=20, position='50,35,0')
        net.mobility(sta12, 'stop', time=27, position='120,35,0')

        net.mobility(sta13, 'start', time=20, position='50,35,0')
        net.mobility(sta13, 'stop', time=27, position='120,35,0')

        net.mobility(sta14, 'start', time=20, position='50,35,0')
        net.mobility(sta14, 'stop', time=27, position='120,35,0')

        net.mobility(sta15, 'start', time=20, position='50,35,0')
        net.mobility(sta15, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta16, 'start', time=20, position='50,35,0')
        net.mobility(sta16, 'stop', time=27, position='120,35,0')

        net.mobility(sta17, 'start', time=20, position='50,35,0')
        net.mobility(sta17, 'stop', time=27, position='120,35,0')

        net.mobility(sta18, 'start', time=20, position='50,35,0')
        net.mobility(sta18, 'stop', time=27, position='120,35,0')

        net.mobility(sta19, 'start', time=20, position='50,35,0')
        net.mobility(sta19, 'stop', time=27, position='120,35,0')

        net.mobility(sta20, 'start', time=20, position='50,35,0')
        net.mobility(sta20, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta21, 'start', time=20, position='50,35,0')
        net.mobility(sta21, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta22, 'start', time=20, position='50,35,0')
        net.mobility(sta22, 'stop', time=27, position='120,35,0')

        net.mobility(sta23, 'start', time=20, position='50,35,0')
        net.mobility(sta23, 'stop', time=27, position='120,35,0')

        net.mobility(sta24, 'start', time=20, position='50,35,0')
        net.mobility(sta24, 'stop', time=27, position='120,35,0')

        net.mobility(sta25, 'start', time=20, position='50,35,0')
        net.mobility(sta25, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta26, 'start', time=20, position='50,35,0')
        net.mobility(sta26, 'stop', time=27, position='120,35,0')

        net.mobility(sta27, 'start', time=20, position='50,35,0')
        net.mobility(sta27, 'stop', time=27, position='120,35,0')

        net.mobility(sta28, 'start', time=20, position='50,35,0')
        net.mobility(sta28, 'stop', time=27, position='120,35,0')

        net.mobility(sta29, 'start', time=20, position='50,35,0')
        net.mobility(sta29, 'stop', time=27, position='120,35,0')

        net.mobility(sta30, 'start', time=20, position='50,35,0')
        net.mobility(sta30, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta31, 'start', time=20, position='50,35,0')
        net.mobility(sta31, 'stop', time=27, position='120,35,0')

        net.mobility(sta32, 'start', time=20, position='50,35,0')
        net.mobility(sta32, 'stop', time=27, position='120,35,0')

        net.mobility(sta33, 'start', time=20, position='50,35,0')
        net.mobility(sta33, 'stop', time=27, position='120,35,0')

        net.mobility(sta34, 'start', time=20, position='50,35,0')
        net.mobility(sta34, 'stop', time=30, position='120,35,0')

        net.mobility(sta35, 'start', time=20, position='50,35,0')
        net.mobility(sta35, 'stop', time=27, position='120,35,0')

        net.mobility(sta36, 'start', time=20, position='50,35,0')
        net.mobility(sta36, 'stop', time=27, position='120,35,0')

        net.mobility(sta37, 'start', time=20, position='50,35,0')
        net.mobility(sta37, 'stop', time=27, position='120,35,0')

        net.mobility(sta38, 'start', time=20, position='50,35,0')
        net.mobility(sta38, 'stop', time=27, position='120,35,0')

        net.mobility(sta39, 'start', time=20, position='50,35,0')
        net.mobility(sta39, 'stop', time=27, position='120,35,0')

        net.mobility(sta40, 'start', time=20, position='50,35,0')
        net.mobility(sta40, 'stop', time=27, position='120,35,0')
        
        net.mobility(sta41, 'start', time=30, position='50,35,0')
        net.mobility(sta41, 'stop', time=37, position='120,35,0')
        
        net.mobility(sta42, 'start', time=30, position='50,35,0')
        net.mobility(sta42, 'stop', time=37, position='120,35,0')

        net.mobility(sta43, 'start', time=30, position='50,35,0')
        net.mobility(sta43, 'stop', time=37, position='120,35,0')

        net.mobility(sta44, 'start', time=30, position='50,35,0')
        net.mobility(sta44, 'stop', time=37, position='120,35,0')

        net.mobility(sta45, 'start', time=30, position='50,35,0')
        net.mobility(sta45, 'stop', time=37, position='120,35,0')

        net.mobility(sta46, 'start', time=30, position='50,35,0')
        net.mobility(sta46, 'stop', time=37, position='120,35,0')

        net.mobility(sta47, 'start', time=30, position='50,35,0')
        net.mobility(sta47, 'stop', time=37, position='120,35,0')

        net.mobility(sta48, 'start', time=30, position='50,35,0')
        net.mobility(sta48, 'stop', time=37, position='120,35,0')

        net.mobility(sta49, 'start', time=30, position='50,35,0')
        net.mobility(sta49, 'stop', time=37, position='120,35,0')

        net.mobility(sta49, 'start', time=30, position='50,35,0')
        net.mobility(sta49, 'stop', time=37, position='120,35,0')

        net.mobility(sta50, 'start', time=30, position='50,35,0')
        net.mobility(sta50, 'stop', time=37, position='120,35,0')
        
        net.mobility(sta51, 'start', time=30, position='50,35,0')
        net.mobility(sta51, 'stop', time=37, position='120,35,0')

        net.mobility(sta52, 'start', time=30, position='50,35,0')
        net.mobility(sta52, 'stop', time=37, position='120,35,0')

        net.mobility(sta53, 'start', time=30, position='50,35,0')
        net.mobility(sta53, 'stop', time=37, position='120,35,0')

        net.mobility(sta54, 'start', time=30, position='50,35,0')
        net.mobility(sta54, 'stop', time=37, position='120,35,0')

        net.mobility(sta55, 'start', time=30, position='50,35,0')
        net.mobility(sta55, 'stop', time=37, position='120,35,0')

        net.mobility(sta56, 'start', time=30, position='50,35,0')
        net.mobility(sta56, 'stop', time=37, position='120,35,0')

        net.mobility(sta57, 'start', time=30, position='50,35,0')
        net.mobility(sta57, 'stop', time=37, position='120,35,0')

        net.mobility(sta58, 'start', time=30, position='50,35,0')
        net.mobility(sta58, 'stop', time=37, position='120,35,0')

        net.mobility(sta59, 'start', time=30, position='50,35,0')
        net.mobility(sta59, 'stop', time=37, position='120,35,0')

        net.mobility(sta60, 'start', time=30, position='50,35,0')
        net.mobility(sta60, 'stop', time=37, position='120,35,0')
        '''
        net.stopMobility (time=2000)

    info("*** Starting network\n")
    net.build()

    RSU1.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    RSU2.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

    RSU1.setIP('192.168.0.100/24', intf='RSU1-wlan0')
    RSU1.setIP('192.168.2.1/24', intf='RSU1-eth1')
    RSU2.setIP('192.168.1.100/24', intf='RSU2-wlan0')
    RSU2.setIP('192.168.2.2/24', intf='RSU2-eth1')

    RSU1.cmd('route add -net 192.168.1.0/24 gw 192.168.2.2')
    RSU2.cmd('route add -net 192.168.0.0/24 gw 192.168.2.1')
    
    makeTerm (RSU2, cmd = "bash -c 'python3 Conf_veh_rsu_j.py ;'")
    time.sleep(1)
    makeTerm (RSU1, cmd = "bash -c 'python3 Conf_veh_rsu_i.py ;'")

    veh_rsui_auth_check = {} # for initial auth
    veh_rsuj_hand_auth_check = {}  # for handover to RSU j
    
    #veh_rsu_assoc = {}  # for RSU handover

    ip_ct = 0
    while True :
        for sta in net.stations:
            if str(sta) not in veh_rsui_auth_check and sta.wintfs[0].associatedTo is not None : 
                veh_rsui_auth_check[str(sta)] = 0
                
                apx = sta.wintfs[0].associatedTo.node
                apx = str(apx)
                #veh_rsu_assoc[str(sta)] = apx
                
                print ("---- Associated to RSU1")
                if apx == 'RSU1' and veh_rsui_auth_check[str(sta)] == 0:
                    # send NVID, HPW, p(x), h(x)

                    if str(sta) == 'sta1':
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'Z8CY5IG' 'z8' ;'") # 
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta2':
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'ENUOH84' 'en' ;'") # > auth_sta2.txt
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta4':
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'I1LWWY5' 'i1'  > auth_sta4.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    '''
                    elif str(sta) == 'sta3':
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '0AY7GEV' '0a' ;'") # > auth_sta3.txt
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                                        
                    elif str(sta) == 'sta5':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'GKTDUFU' 'gk'  > auth_sta5.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta6':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '4C1JBT7' '4c'  > auth_sta6.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta7':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'UQE8MVP' 'uq'  > auth_sta7.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta8':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'PBXZGJT' 'pb'  > auth_sta8.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta9':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'IXVS771' 'ix'  > auth_sta9.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta10':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '0FD9CH5' '0f'  > auth_sta10.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta11':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'QVW0N60' 'qv'  > auth_sta11.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta12':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'OTV0P0F' 'ot'  > auth_sta12.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta13':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'HZHVT6L' 'hz'  > auth_sta13.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta14':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '678PYV8' '67'  > auth_sta14.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta15':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '6Z0VS75' '6z'  > auth_sta15.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta16':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '5A8F1JN' '5a'  > auth_sta16.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta17':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'B08IB8J' 'b0'  > auth_sta17.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta18':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'ZFQ1Q5Y' 'zf'  > auth_sta18.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                
                    elif str(sta) == 'sta19':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'RAYI34O' 'ra'  > auth_sta19.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta20':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '5BEC6HJ' '5b'  > auth_sta20.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta21':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'LIO43OG' 'li'  > auth_sta21.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta22':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'GUQLKW4' 'gu'  > auth_sta22.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta23':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'THKUDZB' 'th'  > auth_sta23.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta24':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'I74DJVC' 'i7'  > auth_sta24.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta25':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'HELK5VE' 'he'  > auth_sta25.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta26':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'CQWXGLB' 'cq'  > auth_sta26.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta27':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '5M14AJQ' '5m'  > auth_sta27.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta28':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '0CSPW3E' '0c'  > auth_sta28.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta29':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '11XQNQM' '11'  > auth_sta29.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta30':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'DQSF8E7' 'dq'  > auth_sta30.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta31':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'MP060AW' 'mp'  > auth_sta31.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta32':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'XOQXX1E' 'x0'  > auth_sta32.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta33':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'N6GSKLR' 'n6'  > auth_sta33.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta34':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '387SSD3' '38'  > auth_sta34.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta35':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'P2C3C7G' 'p2'  > auth_sta35.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta36':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '7AH8XOX' '7a'  > auth_sta36.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta37':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'SBU0K8J' 'sb'  > auth_sta37.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta38':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'H9H9KHL' 'h9'  > auth_sta38.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta39':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'TIW1Z0R' 'ti'  > auth_sta39.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta40':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'P9N2VCX' 'p9'  > auth_sta40.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta41':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'DK5ZZTK' 'dk'  > auth_sta41.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta42':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'OR12AQT' 'or'  > auth_sta42.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta43':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'Q9BXMQH' 'q9'  > auth_sta43.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta44':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'VHMQHQT' 'vh'  > auth_sta44.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta45':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'QQ0A6OR' 'qq'  > auth_sta45.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta46':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '29SNDML' '29'  > auth_sta46.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta47':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '00R1J33' '00'  > auth_sta47.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta48':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'GLU7STK' 'gl'  > auth_sta48.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta49':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '21O65D6' '21'  > auth_sta49.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta50':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'P3YE4DG' 'p3'  > auth_sta50.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta51':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'XVLPXH2' 'xv'  > auth_sta51.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta52':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '566ZOQT' '56'  > auth_sta52.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta53':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'TNFN9DW' 'tn'  > auth_sta53.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta54':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'EBUWQMX' 'eb'  > auth_sta54.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta55':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '12P8911' '12'  > auth_sta55.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta56':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py '96Z3E2Q' '96'  > auth_sta56.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta57':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'TW2YE93' 'tw'  > auth_sta57.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta58':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'H7YHMBV' 'h7'  > auth_sta58.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta59':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'ZQQLBMT' 'zq'  > auth_sta59.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta60':
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_auth.py 'HP6E0Q0' 'hp'  > auth_sta60.txt ;'")
                        print ("-------- Auth done for --- ", str(sta))
                        veh_rsui_auth_check[str(sta)] = 1
                    '''
                    
            
            elif str(sta) in veh_rsui_auth_check and sta.wintfs[0].associatedTo is not None:
                #apx = sta.wintfs[0].associatedTo.node
                #apx = str(apx)
                #veh_rsu_assoc[str(sta)] = apx   

                if str(sta) not in veh_rsuj_hand_auth_check and str(sta.wintfs[0].associatedTo.node) == 'RSU2':    
                    ip_ct = ip_ct + 1
                    IP = '192.168.1.' + str(ip_ct)
                    
                    print ("Handover ",str(sta)," associated with RSU2 ", str(sta.wintfs[0].associatedTo.node))
                    
                    if str(sta) == 'sta1':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta1-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'IH8L0G1' '4YGKQXU' '3918' ;'") # VID, session key, auth_suc_r > hand_sta1.txt 
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta2':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta2-wlan0')
                        #x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'KHBC8IH' 'AKUC01Z' '3133' ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta3':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta3-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'O571Q12' 'UTY7519' '8457' ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta4':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta4-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'NZ9DU5V' '19RKCLP' '8347' > hand_sta4.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    '''
                    elif str(sta) == 'sta5':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta5-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'HDA8WAQ' 'UBXR00B' '2035' > hand_sta5.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta6':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta6-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'ENBHPYJ' 'U1HOMAB' '4913' > hand_sta6.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta7':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta7-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'RS7D9J6' 'I51MW2B' '8471' > hand_sta7.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta8':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta8-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'U4HRQ74' 'Q1WO0WQ' '9926' > hand_sta8.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta9':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta9-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '8G0QOZ9' 'AV1R0YT' '4365' > hand_sta9.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta10':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta10-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '4UM0DVV' 'N9TEKZF' '3157' > hand_sta10.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta11':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta11-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'GABJQBR' '9GF349G' '6197' > hand_sta11.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta12':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta12-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'HKOXRUN' '4SAXPSC' '9662' > hand_sta12.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta13':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta13-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'N5YCHD1' '9WZK7BM' '7642' > hand_sta13.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta14':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta14-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'JCS47QQ' 'LGRNZHZ' '2270' > hand_sta14.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta15':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta15-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'XJAPG97' 'ZOFG6C4' '3788' > hand_sta15.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta16':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta16-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'YML40B5' 'OAIRICH' '8783' > hand_sta16.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta17':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta17-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '60P2GX8' 'UY4XX4L' '8283' > hand_sta17.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta18':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta18-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '647TAQO' 'ALGT17L' '4979' > hand_sta18.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta19':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta19-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '7UWL327' 'I0MGVJT' '2143' > hand_sta19.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta20':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta20-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'LDQ27NB' 'VO2FGMS' '7576' > hand_sta20.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta21':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta21-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'W8OJ1FY' '3HVTU5S' '2169' > hand_sta21.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta22':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta22-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'PMTVOO1' 'NAQUWAA' '7832' > hand_sta22.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta23':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta23-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'K8ZG69U' 'E5UA090' '7608' > hand_sta23.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta24':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta24-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'HKBZOZN' 'UPVON8Q' '5081' > hand_sta24.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta25':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta25-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'RDC3BCI' '9XNZC2I' '9851' > hand_sta25.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta26':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta26-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'SW0B7BH' 'U7QR7NN' '6800' > hand_sta26.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta27':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta27-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'FRDJLYV' 'Y16V8WG' '2351' > hand_sta27.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta28':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta28-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '2X9PBHH' 'D3OGPSR' '6628' > hand_sta28.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta29':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta29-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'ES7E6D2' 'VAIDIMM' '8018' > hand_sta29.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta30':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta30-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'I2I8R3W' '3JJ2EIB' '4839' > hand_sta30.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta31':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta31-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'M1LKL6X' 'VGSAZN1' '4278' > hand_sta31.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta32':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta32-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'MNM40J4' '2A1H4D6' '8957' > hand_sta32.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta33':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta33-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'HWB3VNJ' 'RYW25C1' '2646' > hand_sta33.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta34':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta34-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'UQ00RAH' 'SU22HQG' '6557' > hand_sta34.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta35':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta35-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'BGW1I4P' '1OVCANT' '7062' > hand_sta35.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta36':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta36-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '1PBSHCM' 'EV01R2F' '4219' > hand_sta36.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta37':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta37-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'WYONZYR' '9ZIR5B7' '8680' > hand_sta37.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta38':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta38-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '2AOLOBT' 'SOXTK3H' '8373' > hand_sta38.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta39':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta39-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'V7Y0HMH' '06YA9DA' '4621' > hand_sta39.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta40':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta40-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'K2ARSXA' '547OOU7' '3960' > hand_sta40.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta41':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta41-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'BZXBPOU' 'K9SUUKU' '4993' > hand_sta41.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta42':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta42-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'KDTPVDS' 'T4DKUVX' '3200' > hand_sta42.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta43':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta43-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '4E122TR' 'MKIC8IB' '4939' > hand_sta43.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta44':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta44-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '0G2UTPT' 'C9V2DFI' '4678' > hand_sta44.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta45':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta45-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '8SGH426' '23N7YFT' '5945' > hand_sta45.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta46':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta46-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'IPTJIHX' 'DTDDCRS' '2997' > hand_sta46.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta47':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta47-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'KSWQ14U' 'N5ERONC' '5601' > hand_sta47.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta48':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta48-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'GHGTQ3Y' 'AJMEMOO' '2811' > hand_sta48.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta49':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta49-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'NYZU5LT' 'GZRZZUY' '5383' > hand_sta49.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta50':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta50-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'HAS84L0' '6RS4GJE' '3389' > hand_sta50.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    
                    elif str(sta) == 'sta51':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta51-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'MAA4OMT' 'AWTN0AJ' ''7720' > hand_sta51.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta52':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta52-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '1QQQOI1' 'S4C929V' ''6617' > hand_sta52.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta53':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta53-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'FYV1IAV' 'KWTG3V7' ''2655' > hand_sta53.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta54':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta54-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'G828S32' 'XAAF432' ''6861' > hand_sta54.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta55':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta55-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py '7189VJC' 'S624QMP' ''2810' > hand_sta55.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta56':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta56-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'EOSBIUQ' '7EJIIZF' ''3156' > hand_sta56.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta57':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta57-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'M0WQB0Q' 'F8ZCSUT' ''9502' > hand_sta57.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta58':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta58-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'RAW031W' 'ZA8OLH2' ''9202' > hand_sta58.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta59':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta59-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'PAQAKBY' 'FCGTISL' ''4242' > hand_sta59.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1

                    elif str(sta) == 'sta60':
                        print ("IP of ", str(sta), "is ", IP)
                        sta.setIP(IP, intf='sta60-wlan0')
                        x = makeTerm (sta, cmd = "bash -c 'python3 Conf_veh_hand.py 'US6WNH4' 'XRRQZ1M' ''7789' > hand_sta60.txt ;'")
                        print ("Handover done for ",str(sta))
                        veh_rsuj_hand_auth_check[str(sta)] = 1
                    '''                 

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
