#!/bin/python3
import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AD_INET = IPV4, SOCK_STREAM = PORT
s.connect((HOST,PORT))
