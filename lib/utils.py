def rl_ports_changed(obj1, obj2):
    if obj1['tcp'] == obj2['tcp'] and obj1['udp'] == obj2['udp']:
        return False
    return True
