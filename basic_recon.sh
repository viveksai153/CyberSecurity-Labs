#!/bin/bash

echo "Basic Recon Script"
echo "=================="

echo "[+] Date & Time:"
date 

echo "[+] Logged in as:"
whoami

echo "[+] System info:"
uname -a

echo "[+] Internal IP:"
ip a | grep inet

echo "[+] Listening Ports:"
netstat -tuln