import sys
import os
import os.path
sys.path.append("../")
sys.path.append("../dgt_signing")


from dgt_signing import create_context
from dgt_signing import CryptoFactory
from dgt_sdk.protobuf.transaction_pb2 import TransactionHeader
from dgt_sdk.protobuf.transaction_pb2 import Transaction
from dgt_sdk.protobuf.transaction_pb2 import TransactionList
from dgt_sdk.protobuf.batch_pb2 import BatchList
from dgt_sdk.protobuf.batch_pb2 import BatchHeader
from dgt_sdk.protobuf.batch_pb2 import Batch

import json
import cbor
from hashlib import sha512
import random
import time
import requests
import ipaddress as ip
import base64

import configparser

import client

def valIP(nodeIP: str):
    try:
        nodeIP = nodeIP.replace("http://","")
        nodeIP= nodeIP.split(":",1)[0]
        ip_obj = ip.ip_address(nodeIP)
    except ValueError:
        print("Invalid IP")
        sys.exit()

def valPort(port: str) -> None:
    try:
        port = int(port)
        if port < 0 or port > 65535: raise ValueError
    except ValueError:
        print("Invalid Port. Please enter IP:PORT")
        sys.exit()

def valArgs(args:list) -> None:
    try:
        valid_commands = [ "version" , "connect" , "set" , "inc" ,"dec" , "trans"
                "show", "list" "execute" , "exit" ]
        if sys.argv[1].lower() not in valid_commands : raise NameError

        if len(args) < 3 : raise IndexError
        if sys.argv[1] == "connect" and len(sys.argv) != 3:
            raise IndexError
    except IndexError:
        print("Invalid number of arguments.")
        sys.exit()
    except NameError:
        print("Invalid Command")
        sys.exit()
def initIP():
    try:
       connect = sys.argv[1]
       if connect != "connect" : raise NameError
       if len(sys.argv) > 3  : raise IndexError
       
       valIP(sys.argv[2])
       
       if ":" not in sys.argv[2]:
           print("Please provide Port")
           sys.exit()

       valPort(sys.argv[2].split(":",1)[1])

       config.add_section("user_info")
       config.set("user_info", "node_ip" , sys.argv[2])
       
       if not os.path.isdir("config"): os.makedirs("config") 
       with open("config/config.ini","w") as file:
           config.write(file)
   
    except IndexError:
        print("Invalid number of arguments")
    except NameError:
        print('Not connected to any Node, run "bgtc connect"')
        sys.exit()
    except OSError:
        print("Something went wrong when writing the config file")

def updateIP(socket:str) -> None:
    config.read("config/config.ini")
    user_info = config["user_info"]
    
    ip_port=socket.split(":",1)
    valIP(ip_port[0])
    valPort(ip_port[1])

    user_info["node_ip"] = socket
    try:
        with open("config/config.ini","w") as cf:
            config.write(cf)
    except OSError:
        print("Someting went wrong modifing the config file")
        sys.exit()

def main():
    global config
    config = configparser.ConfigParser()
    
    valArgs(sys.argv)

    if not os.path.isfile("config/config.ini"): initIP()
    
    if sys.argv[1] == "connect" : 
        updateIP(sys.argv[2])
        nodeIP=sys.argv[2].split(":",1)
        errno=client.connect(nodeIP[0], int(nodeIP[1]))
        if errno != 0 : 
            print(f"Something went wrong. Errno:{errno}")
            sys.exit()
        print("Sucessfully connected.")



if __name__ == '__main__':
    main()


