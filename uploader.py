import re
from paramiko import SSHClient
from scp import SCPClient

class Uploader:
    _ssh_conn = None
    _scp_conn = None

    def __init__(self, keys="~/.ssh/id_rsa"):
        self._ssh_conn = SSHClient()
        self._ssh_conn.load_system_host_keys()
        
    def connect(self, host:str, user:str, port=22):
        self._ssh_conn.connect(host, username=user, port=port)

        self._scp_conn = SCPClient(self._ssh_conn.get_transport())

    def upload(self, files:list, path:str):
        for file_path in files:
            self._scp_conn.put(file_path, remote_path=path)

    def __del__(self):
        self._scp_conn.close()
        self._ssh_conn.close()

