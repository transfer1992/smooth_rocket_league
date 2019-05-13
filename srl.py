import subprocess
import re
from time import sleep

p = re.compile('[0-9]+')

executable = 'RocketLeague.exe'

while(True):
  pid_result = subprocess.run('wmic process where name="{}" get processid'.format(executable), stdout=subprocess.PIPE)
  pid = p.search(pid_result.stdout.decode())

  if pid is not None:
    pid = pid[0]

    port_result = subprocess.run('netstat -ano', stdout=subprocess.PIPE)
    port_lines = port_result.stdout.decode().split('\r\n  ')

    tcp_lines = []
    udp_lines = []

    for line in port_lines:
      if line.endswith(pid):
        if 'TCP' in line:
          tcp_lines.append(line)
        elif 'UDP' in line:
          udp_lines.append(line)

    tcp_ports = [int(float(line.split(':')[1].split(' ')[0])) for line in tcp_lines]
    udp_ports = [int(float(line.split(':')[1].split(' ')[0])) for line in udp_lines]
    print(tcp_ports, udp_ports)
  else:
    print('Nie ma takiego procesu')

  sleep(1)