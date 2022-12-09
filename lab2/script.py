#!/usr/bin/env python3

import glog as log
import argparse
import subprocess
import platform


# @TODO if os == 'linux':
def check(host, MTU, os):
    """ping with don't fragment flag, -c count -W timeout
    """
    if os == 'darwin': # mac-os
        cmd = f'ping -D -s {MTU} {host} -c 1 -W 3000'
    else:
        cmd = f'ping -M do -s {MTU} {host} -c 1 -W 3'
    cmd = cmd.split(' ')
    res = subprocess.run(cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, universal_newlines=True)
    return res.returncode == 0



parser = argparse.ArgumentParser()
parser.add_argument(
    '--host',
    required=True,
    help='host for which the minimal MTU is searched for'
)
parser.add_argument(
    '--loglevel',
    default='WARN',
    help='glog loglevel. Possible options: INFO WARN. Useless options: CRITICAL FATAL ERROR NOTSET WARNING DEBUG'
)


args = parser.parse_args()
host = args.host
loglevel = args.loglevel

log.setLevel(loglevel)

current_os = platform.system().lower()

if not check(host, MTU=0, os=current_os):
    print(f'host {host} is unavailable')
    exit(0)

left, right = 0, 1502 - 28
while left + 1 < right:
    mid = (left + right) // 2
    if check(host, MTU=mid, os=current_os):
        log.info(f'MTU {mid} is ok')
        left = mid
    else:
        log.info(f'MTU {mid} bad')
        right = mid

print(f'minimal MTU for {host} = {left}')
