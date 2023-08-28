import socket
import threading
import random # import randint
import time, os
from hashlib import sha256  
import datetime
import numpy as np
'''
os.system ("pip install openpyxl==3.0.10 ")
os.system ("pip install  pyexcel==0.6.7 ") #  --break-system-packages
os.system ("pip install  pyexcel-xlsx==0.6.0 ")
'''
import pyexcel as pe

def get_timestamp() :
    # ct stores current time
    ct = datetime.datetime.now()
    # ts store timestamp of current time
    ts = ct.timestamp()
    return ts

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += str(ele)
        str1 += ","
    str1 = str1[:len(str1)-1]
    # print ("str returning is ", str1)
    # return string
    return str1

def xor_sha_strings(s,t):
    s = bytes.fromhex(s)
    t = bytes.fromhex(t)

    res_bytes = bytes(a^b for a,b in zip(s,t))
    return res_bytes.hex()

'''
def gcdExtended(a, b):
    global x, y
 
    # Base Case
    if (a == 0):
        x = 0
        y = 1
        return b
 
    # To store results of recursive call
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd

def modInverse(A, M):
 
    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
    else:
        # m is added to handle negative x
        res = (x % M + M) % M
        print("Modular multiplicative inverse is ", res)
        return res
'''

def horner(poly, n, x): # poly list(coeff), len(poly), x value to substitute
 
    # Initialize result
    result = poly[0]
 
    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, n):
 
        result = result*x + poly[i]
 
    return result

g = 29
h = 53
n = 103

host = "localhost" # socket.gethostname()
print("Host IP is ", host)
port = 6002  # initiate port no above 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
server_socket.bind((host, port))  # bind host address and port together

server_socket.listen(60)

def handle_client(client_socket):
    
    msg1 = client_socket.recv(1024).decode() # veh_id, IPW, 01R
    reg_start_latency = time.time ()
    reg1_comp_start_time = time.time ()

    msg1 = [str(i) for i in msg1.split(',')]

    print ("Recvd ID, IPW is ", msg1)

    if msg1[2] == "01R":
        
        x = random.randint(2, 1000)
        y = random.randint(2, 1000)
        Tc = get_timestamp ()

        hxTc = sha256(str(x).encode('utf-8') + str(Tc).encode('utf-8')).hexdigest()
        hyTc = sha256(str(y).encode('utf-8') + str(Tc).encode('utf-8')).hexdigest()

        NVID_temp = xor_sha_strings (msg1[1], hxTc) 
        NVID = xor_sha_strings ( NVID_temp, hyTc)

        msg2 = NVID+ ","+ msg1[0]
        reg1_comp_end_time = time.time ()

        TA_reg_comp_time = reg1_comp_end_time - reg1_comp_start_time 

        client_socket.send(msg2.encode('utf'))  # send NVID, veh_ID

        msg3 = client_socket.recv(1024).decode() # NVID, t(x), d

        reg2_comp_start_time = time.time ()

        msg3 = [str(i) for i in msg3.split('&')]

        #print ("t(x) and poly degree is ", msg3)
        poly_deg = int(msg3[2])

        if msg3[0] == NVID:
            print ("NVID matched ")

            Tc = get_timestamp ()
            hkTc = sha256(str(random.randint(10, 1000)).encode('utf-8') + str(Tc).encode('utf-8')).hexdigest()
            hxTc = sha256(str(x).encode('utf-8') + str(Tc).encode('utf-8')).hexdigest()

            NVIDnew_temp = xor_sha_strings (NVID, hkTc, )
            NVIDnew = xor_sha_strings (hxTc, NVIDnew_temp)

            msg4 = NVIDnew+ ","+ msg1[1]+ ","+ "Reg_suc" 

            reg2_comp_end_time = time.time ()
            TA_reg_comp_time += reg2_comp_end_time - reg2_comp_start_time

            client_socket.send(msg4.encode('utf'))  # NVIDnew, IPW, Reg_status

            reg3_comp_start_time = time.time ()

            s =  random.randint(2, 100)
            alpha = random.randint(2, 100)

            g_alpha_s_i = []
            g_s_i = []
            #print ("s is ", s)
            #print ("alpha is ", alpha)
            g_alpha = int(pow(g, alpha, n)) # g^alpha (mod n)

            #print("g^alpha is ", g_alpha)

            for  i in range(0, poly_deg+1) :
                g_s_i.append(int(pow(g, (s**i), n)))
                g_alpha_s_i.append( int(pow(g, alpha *(s**i), n)))
            #print ("g_s_i is ", g_s_i)
            #print ("g_alpha_s_i is ", g_alpha_s_i)

            t_x2 = [int(i) for i in msg3[1].split(',')]  # const first
            t_x1 = t_x2[::-1]
            #print ("tx_2 is ", t_x2)

            #print ("tx_1 is ", t_x1)
            
            # print ("tx is ", tx)
            t_s_np = np.poly1d(t_x1) # reverse()) 
            tx_val_on_s = horner (t_x1, len(t_x1), s)

            #print ("t_x is \n", t_s_np)
            #print ("tx_val on subst s is ", tx_val_on_s)

            '''
            g_t_s_val = 1
            for i in range(len(t_x2)):
                if t_x2[i] < 0 :
                    x = modInverse(g_s_i[i], n)
                    g_t_s_val *= int(pow(g_s_i[i], t_x2[i], n))
                else :
                    g_t_s_val *= int(pow(g_s_i[i], t_x2[i], n))

            g_t_s_val = g_t_s_val % n
            '''

            print ("Prover key is ", g_s_i, g_alpha_s_i)

            print ("SDN Verifier key [ g_alpha, g_t_s_val ] = [ ", alpha, tx_val_on_s, " ]")

            reg3_comp_end_time = time.time ()

            TA_reg_comp_time += reg3_comp_end_time - reg3_comp_start_time
            reg_end_latency = time.time ()

            TA_reg_latency = reg_end_latency - reg_start_latency
            sheet = pe.get_sheet (file_name= "Conf_ZKP_Reg_TA_details.xlsx")

            # values[0] = new_NVID
            # values[1] = Tx_ID
            # Saving cofficients in reverse order
            proving_key =  listToString(g_s_i)+ "&"+ listToString(g_alpha_s_i)

            sheet.row += [ msg1[1], NVIDnew, proving_key, alpha, tx_val_on_s, poly_deg, TA_reg_latency, TA_reg_comp_time]
            sheet.save_as ("Conf_ZKP_Reg_TA_details.xlsx")
            print ("Reg successful and stored in xlsx \n************************")
        else :
            print ("NVIDs mismatched")
    else :
        print ("Invalid Registration Request")
    client_socket.close()

            
   

while True :
    client_socket, client_address = server_socket.accept()

    client_thread = threading.Thread (target=handle_client, args= (client_socket,))
    client_thread.start()

