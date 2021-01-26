# import the os module
import os
from shutil import copyfile

# assign and create the base directories for TCP Air
rootpath = "/etc/config/tcp_air"
locpeers = "/etc/config/tcp_air/peers"
netpeers = "/etc/config/tcp_air/peers/network_peers"

cwd = os.getcwd()

def main():
    os.makedirs(rootpath)

    # create base folders
    folders = ['scripts','additions','peers']
    for folder in folders: 
        try:
            os.mkdir(os.path.join(rootpath,folder))
        except OSError: 
            print ("Creation of the directory %s failed" % folder)
        else:
            print ("Successfully created the directory %s" % folder)

    # create an additional directory inside /etc/config/tcp_air/peers
    try: 
        os.mkdir(netpeers)
    except OSError:
        print ("Creation of the directory network_peers failed")
    else: 
        print ("Successfully created the directory network_peers")

    # create an empty local peers file to be modified by the user
    try:
        peerfile = open(os.path.join(locpeers, 'local_peers.txt'), 'w')
    except OSError:
        print ("Creation of local_peers file failed")
    else: 
        print ("Successfully created the file local_peers")
        config()

# copy python program files from installer to device folders
def config():
    try: 
        copyfile(os.path.join(cwd, 'network_sync.py'), '/etc/config/tcp_air/scripts/network_sync.py')
    except IOError:
        print ("Creation of network_sync file failed")
    else: 
        print ("Successfully created the file network_sync")
        pass
    
    try: 
        copyfile(os.path.join(cwd, 'update_peering.py'), '/etc/config/tcp_air/scripts/update_peering.py')
    except IOError:
        print ("Creation of update_peering file failed")
    else: 
        print ("Successfully created the file update_peering")
        pass
    
    try: 
        copyfile(os.path.join(cwd, 'update_firewall.py'), '/etc/config/tcp_air/scripts/update_firewall.py')
    except IOError:
        print ("Creation of update_firewall file failed")
    else: 
        print ("Successfully created the file update_firewall")
        pass

# if code is not run my issuing the python interpreter command - start the main() function anyway
if __name__ == '__main__':
    main()