from time import sleep
from lib.rl_ports_api import get_rl_ports
from lib.router_api import perform_login, clear_rule, add_tcp_rule, add_udp_rule
from lib.utils import rl_ports_changed

old_rl_ports = {
    'success': False,
    'tcp': [],
    'udp': []
}

print('Performing initial clean...')
for i in range(1, 17):
    clear_rule(i)

while(True):
    new_rl_ports = get_rl_ports()
    # print(new_rl_ports)

    if len(new_rl_ports['udp']) + len(new_rl_ports['tcp']) <= 16:
        if rl_ports_changed(old_rl_ports, new_rl_ports):
            print('Ports changed, proceeding with update...')
            perform_login()

            old_ports_count = len(old_rl_ports['tcp']) + len(old_rl_ports['udp'])
            new_ports_count = len(new_rl_ports['tcp']) + len(new_rl_ports['udp'])

            if old_ports_count > new_ports_count:
                for i in range(new_ports_count, old_ports_count):
                    print('Clearing rule {}...'.format(i + 1))
                    clear_rule(i + 1)

            for i in range(len(new_rl_ports['tcp'])):
                print('Adding rule {} for TCP port {}...'.format(i + 1, new_rl_ports['tcp'][i]))
                add_tcp_rule(i + 1, new_rl_ports['tcp'][i], new_rl_ports['tcp'][i])

            for i in range(len(new_rl_ports['udp'])):
                print('Adding rule {} for UDP port {}...'.format(i + 1 + len(new_rl_ports['tcp']), new_rl_ports['udp'][i]))
                add_udp_rule(i + 1 + len(new_rl_ports['tcp']), new_rl_ports['udp'][i], new_rl_ports['udp'][i])

            old_rl_ports = new_rl_ports
            print('QoS rules updated successfully!')
    sleep(2)
