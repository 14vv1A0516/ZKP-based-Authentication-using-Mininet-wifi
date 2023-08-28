import socket
import time
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode, b64decode
import hashlib
import pyexcel as pe
import ast

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

VID =  sys.argv[1] #"7HW4L3N"
'''
auth_suc_r = '7878'
session_key = "LHZCL1H"
hand_req = "03H"
'''

session_key = sys.argv[2]
auth_suc_r = sys.argv[3]

print ("auth_suc r is ", auth_suc_r )
send1 = encrypt (VID + "&"+ auth_suc_r, session_key) # Data: VID, rand r and password: session key

host = "192.168.1.100" # socket.gethostname()
port = 6017  # socket server port number
veh_socket = socket.socket()  # instantiate
flag = 0

while flag == 0 :
    try : 
        veh_socket.connect((host, port))  # connect to the server
        flag = 1
    except :
        print ("fail") # ("Failed ... Trying to connect again")

#print ("conn with RSU j done ----------")
sheet = pe.get_sheet(file_name="Conf_veh_hand_time.xlsx")

hand_start_lat = time.time ()
send1 = str(send1) + '$$' + VID+ "$$"+ "03H"

veh_socket.send(send1.encode('utf')) # send enc

hand_res = veh_socket.recv(1024).decode() # enc, vid

veh_start1_comp_time = time.time()

hand_res = [str(i) for i in hand_res.split('&')] 
# print ("Recvd key after hand auth is ", hand_res)


if hand_res[1] == auth_suc_r : # sys.argv[3] :
    print ("auth_suc_r matched")
    enc_val = ast.literal_eval(hand_res[0]) # str to dict conversion 
    dec_key = decrypt(enc_val, session_key) # sys.argv[1]) # enc and VID

    #print ("dec new VID data is ", dec_key)

    veh_end1_comp_time = time.time()
    veh_hand_comp_time = veh_end1_comp_time - veh_start1_comp_time
    hand_end_lat = time.time ()

    hand_latency = hand_end_lat - hand_start_lat

    sheet.row += [hand_latency, veh_hand_comp_time]
    sheet.save_as ("Conf_veh_hand_time.xlsx")

    print ("Comp time for hand is ", veh_hand_comp_time)

    print ("======== Veh Handover Auth Done ====================\n")

else :
    print ("Issue in Hand auth request")

veh_socket.close()

