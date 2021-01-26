import sqlite3
import subprocess

from network_chain import fun

class Update_Firewall(object):
    #def add_device(mac):        
        #src_mac = new_transaction(mac)
        #add_mac = "uci set firewall.@rule[-1].src_mac=" + src_mac
        new = 'hello'

        subprocess.call('uci add firewall rule', shell=True)
        subprocess.call("uci set firewall.@rule[-1].target='ACCEPT'", shell=True)
        subprocess.call("uci set firewall.@rule[-1].proto='tcp udp icmp'", shell=True)
        subprocess.call("uci set firewall.@rule[-1].src='lan'", shell=True)
        print(new)
        print(fun)
        subprocess.call(['uci set firewall.@rule[-1].src_mac=', new], shell=True)
        subprocess.call('uci commit && service firewall reload', shell=True)

"""     def remove_device():
        subprocess.call('uci delete firewall rule {}', shell=True)
    
    def update_db():
    
    def network_broadcast(): """

""" if __name__ == '__main__':
    Update_Firewall() """