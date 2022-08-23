import socket
def connect(host:str,port:int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        res = s.connect_ex((host,port))
        return res
