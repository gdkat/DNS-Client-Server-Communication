#TS server
import socket as mysoc
import pickle

def ts():
    try:
        tssd = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)

    except mysoc.error as err:
        print('[TS]: {}\n'.format("socket open error ", err))

    #load table from server
    try:
        #fname = input("Enter file to read (Ex: foo.txt): ")
        fname = "PROJI-DNSTS.txt"
        fr = open(fname, "r")
    except IOError as err:
        print('{} \n'.format("File Open Error ",err))
        print("Please ensure desired file to reverse exists in source folder and is named HW1test.txt")
        exit()

    TS_table = {}

    for line in fr:
        pass#do something with dictionary
 
    #determine local hostname, IP
    #address , select a port number
    server_binding=('',50008)
    tssd.bind(server_binding)
    tssd.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Attempting to connect to client.\n[S]: Server IP address is  ",localhost_ip)
    ctsd,addr=tssd.accept()

    while True:
        hnstring=ctsd.recv(100)
        entry = ''
        if hnstring in TS_table:
            entry = TS_table[hnstring]
        else:
            entry = "hname" + "Error: Host not found"
        ctsd.send(pickle.dump(entry))

    # close everything
    fr.close()
    tssd.close()