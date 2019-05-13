import requests

login_data = {
    'tipsFlag': '0',
    'timevalue': '0',
    'Login_Name': 'admin',
    'Login_Pwd': 'Ha2S+eOKqmzA6nrlmTeh7w==',
    'uiWebLoginhiddenUsername': '21232f297a57a5a743894a0e4a801fc3',
    'uiWebLoginhiddenPassword': 'eecc235be523f6bdc99e86716b1376a2'
}

headers = {
    'Host': '192.168.0.2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'pl,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://192.168.0.2/login_security.html',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '196',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


def delete_qos_rule_data(rule_no):
    return {'Qos_active': '1',
            'QosRuleIndex': str(rule_no),
            'QOS_Flag': '2',
            'QosRuleActive': '1',
            'QosApp': '',
            'QosPhyPortWLAN': 'on',
            'QosPhyPortEnet1': 'on',
            'QosPhyPortEnet2': 'on',
            'QosPhyPortEnet3': 'on',
            'QosPhyPortEnet4': 'on',
            'QosDestMacValue': '',
            'QosDestIpValue': '',
            'QosDestMaskValue': '',
            'QosDestPortValue1': '7899',
            'QosDestPortValue2': '7900',
            'QosSrcMacValue': '',
            'QosSrcIpValue': '',
            'QosSrcMaskValue': '',
            'QosSrcPortValue1': '',
            'QosSrcPortValue2': '',
            'QosProtocol': 'UDP',
            'QosVIDValue1': '',
            'QosVIDValue2': '',
            'Qos_IPP_DSCP1': '0',
            'QosDSCPValue1': '0',
            'QosDSCPValue2': '63',
            'Qos8021pValue1': '',
            'Qos8021pValue2': '',
            'Qos_IPP_DSCP2': '0',
            'QosReDSCPValue': '46',
            'Qos8021pReValue': '',
            'Qos8021pReApp': '',
            'QosConfigPriority': 'Highest',
            'QoS_Del': 'DELETE',
            'QosMBSSIDNumberFlag': '1'
            }


def add_rule_data(rule_no, protocol, port_min, port_max):
    return {'Qos_active': '1',
            'QosRuleIndex': str(rule_no),
            'QOS_Flag': '0',
            'QosRuleActive': '1',
            'QosApp': '',
            'QosPhyPortWLAN': 'on',
            'QosPhyPortEnet1': 'on',
            'QosPhyPortEnet2': 'on',
            'QosPhyPortEnet3': 'on',
            'QosPhyPortEnet4': 'on',
            'QosDestMacValue': '',
            'QosDestIpValue': '',
            'QosDestMaskValue': '',
            'QosDestPortValue1': str(port_min),
            'QosDestPortValue2': str(port_max),
            'QosSrcMacValue': '',
            'QosSrcIpValue': '',
            'QosSrcMaskValue': '',
            'QosSrcPortValue1': '',
            'QosSrcPortValue2': '',
            'QosProtocol': protocol,
            'QosVIDValue1': '',
            'QosVIDValue2': '',
            'Qos_IPP_DSCP1': '0',
            'QosDSCPValue1': '0',
            'QosDSCPValue2': '63',
            'Qos8021pValue1': '',
            'Qos8021pValue2': '',
            'Qos_IPP_DSCP2': '0',
            'QosReDSCPValue': '46',
            'Qos8021pReValue': '',
            'Qos8021pReApp': '',
            'QosConfigPriority': 'Highest',
            'QoS_Add': 'ADD',
            'QosMBSSIDNumberFlag': '1'}


session = requests.session()

def perform_login():
    session.post("http://192.168.0.2/Forms/login_security_1",
                 data=login_data, headers=headers)


def clear_rule(rule_no):
    if rule_no is not None:
        session.post("http://192.168.0.2/Forms/adv_qos_1",
                     data=delete_qos_rule_data(rule_no), headers=headers)


def add_tcp_rule(rule_no, port_min, port_max):
    if rule_no is not None:
        session.post("http://192.168.0.2/Forms/adv_qos_1",
                     data=add_rule_data(rule_no, 'TCP', port_min, port_max), headers=headers)


def add_udp_rule(rule_no, port_min, port_max):
    if rule_no is not None:
        session.post("http://192.168.0.2/Forms/adv_qos_1",
                     data=add_rule_data(rule_no, 'UDP', port_min, port_max), headers=headers)
