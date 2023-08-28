import socket
import string
import random # import randint
import time, os
import numpy as np
from math import floor 
# import pandas as pd
from hashlib import sha256 
'''
os.system ("pip install openpyxl==3.0.10 ")
os.system ("pip install  pyexcel==0.6.7 ") # --break-system-packages
os.system ("pip install  pyexcel-xlsx==0.6.0 ")
'''
import pyexcel as pe

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += str(ele)
        str1 += ","
    str1 = str1[:len(str1)-1]
    # return string
    return str1

def multiply(A, B, m, n):
 
    prod = [0] * (m + n - 1);
     
    # Multiply two polynomials term by term
     
    # Take ever term of first polynomial
    for i in range(m):
         
        # Multiply the current term of first
        # polynomial with every term of
        # second polynomial.
        for j in range(n):
            prod[i + j] += A[i] * B[j];
 
    return prod
 
# A utility function to print a polynomial
def printPoly(poly, n):
 
    for i in range(n):
        print(poly[i], " ")
        if (i != 0):
            print("x^", i, " ")
        if (i != n - 1):
            print(" + ", " ")

host = "localhost" # socket.gethostname() 
port = 6002  # socket server port number
veh_socket = socket.socket()  # instantiate
veh_socket.connect((host, port))  # connect to the TA

N = 7
veh_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))

veh_pswd = input("Enter password for veh_ID '{0}': ".format(veh_id))
#print("Veh pswd is ", veh_pswd)

reg1_comp_start_time = time.time ()

IPW = sha256(veh_id.encode('utf-8') + veh_pswd.encode('utf-8')).hexdigest()
print ("IPW is ", IPW)

msg1 = veh_id+ ','+ IPW+ ",01R"
#print ("Message being sent to TA is ", msg1)
reg1_comp_end_time = time.time ()

veh_reg_comp_time = reg1_comp_end_time - reg1_comp_start_time
veh_socket.send(msg1.encode('utf'))  # send VID, IPW, 01R

msg2 = veh_socket.recv(1024).decode() # NVID, VID

reg2_comp_start_time = time.time ()

msg2 = [str(i) for i in msg2.split(',')]

#print ("NVID and VID is ", msg2)

if msg2[1] == veh_id:

    poly_deg = random.randint(3, 7)
    #print("Degree is ", poly_deg)
    if poly_deg % 2 == 0:
        t_deg = int(poly_deg/2)
    else:
        t_deg = int(floor(poly_deg/2))
    h_deg = poly_deg - t_deg
    #print("t_deg is ", t_deg)
    #print("h_deg is ", h_deg)

    t_list = []
    h_list = []

    for i in range(0, t_deg+1):
        t_list.append(random.randint(-100, 100))
    for i in range(0, h_deg+1):
        h_list.append(random.randint(-100, 100))
    #print("t_list is ", t_list)
    #print("h_list is ", h_list)

    t_len = len(t_list)
    h_len = len(h_list)
    #print("Polynomial t(x)= ")
    #printPoly(t_list, t_len)
    #print("\n Polynomial h(x)= ")
    #printPoly(h_list, h_len) 
 
    prod = multiply(t_list, h_list, t_len, h_len) 

    #print ("Product of poly is ", prod)

    #print ("\nProduct polynomial is ")
    #printPoly(prod, t_len + h_len-1)

    msg3 = msg2[0]+ "&"+ listToString(t_list)+ "&"+ str(poly_deg)

    #print ("NVID, t(x), d are ", msg3)

    reg2_comp_end_time = time.time ()

    veh_reg_comp_time += reg2_comp_end_time - reg2_comp_start_time

    veh_socket.send(msg3.encode('utf')) # NVID, t(x), d 

    reg_status = veh_socket.recv(1024).decode()  # NVIDnew, IPW, Reg_status
    reg3_comp_start_time = time.time ()
    

    reg_status = [str(i) for i in reg_status.split(',')]
    NVIDnew = reg_status[0]

    print ("Reg status is ", reg_status)

    if reg_status[1] == IPW and reg_status[2] == "Reg_suc" :
        print ("Reg successful")
        reg3_comp_end_time = time.time ()

        veh_reg_comp_time += reg3_comp_end_time - reg3_comp_start_time
        
        '''
        print ("veh_id is ", veh_id)
        print ("NVIDnew is ", NVIDnew)
        print ("hlist is ", listToString(h_list))
        print ("prod p(x) is ", listToString(prod))
        print ("poly deg is ", poly_deg )
        print ("veh reg comp time is ", veh_reg_comp_time )
        '''
        sheet = pe.get_sheet (file_name= "Conf_Reg_veh_time.xlsx")
        sheet.row += [veh_id, veh_pswd, NVIDnew, listToString(h_list), listToString(prod), str(poly_deg), veh_reg_comp_time]
        sheet.save_as ("Conf_Reg_veh_time.xlsx")

        print ("******* Veh Registration Done **********")



