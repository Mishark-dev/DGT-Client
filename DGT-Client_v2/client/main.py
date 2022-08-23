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


def valIP(nodeIP: str):
    try:
        nodeIP = nodeIP.replace("http://","")
        nodeIP= nodeIP.split(":",1)[0]
        ip_obj = ip.ip_address(nodeIP)
    except ValueError:
        print("Invalid IP")
        sys.exit()


def connect():
    try:
       connect = sys.argv[1]
       if connect != "connect" : raise NameError
       if len(sys.argv) > 3  : raise IndexError
       
       valIP(sys.argv[2])
       
       config = configparser.ConfigParser()
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
   
#    except OSError:
#        print("Something went wrong when trying to write to the config file")
#        sys.exit()
#
def main():
    if not os.path.isfile("config/config.ini"):
        connect()

if __name__ == '__main__':
    main()


