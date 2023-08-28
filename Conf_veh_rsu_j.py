
import socket
import random # import randint
import time
import threading
import ast
import string

from base64 import b64encode, b64decode 
import hashlib

import pyexcel as pe

# from collections import OrderedDict

from Cryptodome.Cipher import AES 
from Cryptodome.Random import get_random_bytes


def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])
    

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted

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

def handle_client_veh(client_socket):
    
    auth_enc = client_socket.recv(1024).decode() # enc
    sheet1 = pe.get_sheet(file_name="Conf_RSU_j.xlsx")
    sheet2 = pe.get_sheet(file_name="Conf_RSU_hand_time.xlsx")
    #auth_req = client_socket.recv(1024).decode()  # receive VID, handover_auth_req
    rsu_start_lat = time.time ()
    rsu_start1_comp_time = time.time ()

    values = [str(i) for i in auth_enc.split('$$')] # vid, 03H 
    
    row_flag = 0
    if values[2] == '03H' :
        print ("Received Handover Authentication request ")
        for row in sheet1 :
            if row[0] == values[1] : # matching VIDs
                row_flag = 1
                #print ("row is ", row) # VIDnew, Session key, auth_suc_r
                break

        if row_flag == 1 :

            print ("Matched with row ", row) # vid , session key ,  auth_suc_rfrom sheet
            enc_val_from_veh = ast.literal_eval(values[0])
            dec = decrypt (enc_val_from_veh, row[1]) 
            dec = dec.decode()
            #print ("dec is ", dec)
            dec = [str(i) for i in dec.split('&')]  # VID, r
            #print("dec after split VID and r is ", dec)
            if dec[0] == row[0] and dec[1] == str(row[2]) : # if VID and r macthes after dec
                print ("Matched for Handover ===")
                hand_suc_r = random.randint(2, 10000)
                VIDnew = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(7))
                send1 = VIDnew+ "&"+ str(hand_suc_r) 
                enc_send1 = encrypt (send1, row[1]) 
                enc_send1 = str(enc_send1)+ "&"+ row[2] 

                rsu_end1_comp_time = time.time ()

                client_socket.send(enc_send1.encode()) # enc (r, x), VID
                send_k = row[0]+ ","+ str(hand_suc_r)+ ","+ dec[0] #  session key, new r, VID

                rsu_end_lat = time.time ()
                rsu_hand_latency = rsu_end_lat - rsu_start_lat
                #print ("rsu hand latency is ", rsu_hand_latency)
                
                
                #print ("RSU comp time is ", rsu_comp_time)
                sheet2.row += [rsu_hand_latency, rsu_end1_comp_time - rsu_start1_comp_time ]
                sheet2.save_as ("Conf_RSU_hand_time.xlsx")

                #print ("New r in details is ", send_k)
                # rsuk_conn.send(send1.encode()) # enc (r, x), VID
                print ("======== Handover Done ====================\n")
            else :
                print ("VID or auth_suc_r does not match")
        else :
            print ("Not found in excel sheet")
    else :
        print ("Invalid Handover authentication request")
        

def handle_rsu_i(rsui_conn) :
    while(1) :
        print ("Trying to recv keys from RSU i")
        veh_keys = rsui_conn.recv(1024).decode() # recv VID, auth_suc_r, session key from RSU_i
        print ("Recd veh keys from RSU_i is ", veh_keys)
        print ("\n")
        sheet = pe.get_sheet(file_name="Conf_RSU_j.xlsx")

        sheet.row += [str(i) for i in veh_keys.split('&')]
        sheet.save_as ("Conf_RSU_j.xlsx")
    
'''
def handle_rsu_k(rsuk_conn) :
    veh_keys = rsuk_conn.recv(1024).decode()
    print ("Recd veh keys from RSU_k is ", veh_keys)
    sheet = pe.get_sheet(file_name="rsu_auth_sheet_j.xlsx")

    sheet.row += [str(i) for i in veh_keys.split(',')]
    sheet.save_as ("rsu_auth_sheet_j.xlsx")
'''

host =  "192.168.1.100" # socket.gethostname()

print("RSU j IP is ", host)
port_i = 8010  # RSU_i connection & initiate port no above 1024
rsui_socket = socket.socket()  # get instance
rsui_socket.bind((host, port_i))  # bind host address and port together
rsui_socket.listen(4) 
rsui_conn, rsui_address = rsui_socket.accept()
print ("COnn with RSU i done")
'''

port_k = 8030  # RSU_k connection & initiate port no above 1024
rsuk_socket = socket.socket()  # get instance
rsuk_socket.bind((host, port_k))  # bind host address and port together
rsuk_socket.listen(2) 
rsuk_conn, rsuk_address = rsuk_socket.accept()
'''

print ("-------------------")
port = 6017  # initiate port no above 1024
server_socket = socket.socket()  # get instance
server_socket.bind((host, port))  # bind host address and port together
server_socket.listen(4) 

i = 0
rsu_j = 0
hand_ct = 0

veh_threads = []

while True :
    #print ("For loop i = ", i)
    
    if rsu_j == 0:
        print ("Thread for RSU i started ...")
        client_thread1 = threading.Thread (target=handle_rsu_i, args= (rsui_conn,)) # rsui_conn, rsuk_conn))
        #client_thread2 = threading.Thread (target=handle_client_veh, args= (rsuk_conn,)) # rsui_conn, rsuk_conn))
        client_thread1.start()
        
        #client_thread2.start() 
        rsu_j = 1
    
    #print ("Trying to connect with veh ...")
    
    veh_conn, veh_address = server_socket.accept()  
    
    #print ("\nRecvd conn from veh ", veh_conn, veh_address)  
    
    client_thread3 = threading.Thread (target=handle_client_veh, args= (veh_conn,)) # , rsui_conn, rsuk_conn)) 
    client_thread3.start()
    client_thread3.join()
    #print ("hand_ct is ", hand_ct)
    #veh_threads.append(client_thread3)
    

    #print ("Thread  ", i ,"started")
    '''
    if hand_ct == 10 :
        
        for each in veh_threads :
            each.join()
        
        end = time.time()
        print ("booooooo------------------------ooooom")
        print ("Total time for hand latency is ", (end-start)*10**3, " m.sec")
        print ("Breaking ")
        break
    
    i = i + 1
    '''