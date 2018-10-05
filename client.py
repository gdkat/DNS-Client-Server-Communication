#Client
import socket as mysoc
import pickle

def client():
    #[ rs socket]
    try:
        ctors=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)

    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))

    #[ts socket]
    try:
        ctots=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)

    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    #load file with hostname information to be resolved
    try:
        #fname = input("Enter file to read (Ex: foo.txt): ")
        fname = "PROJI-HNS.txt"
        fr = open(fname, "r")
    except IOError as err:
        print('{} \n'.format("File Open Error ",err))
        print("Please ensure desired file to reverse exists in source folder and is named HW1test.txt")
        exit()

    #[determine hostname of RS server and port ]
    sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())
    # Define the port on which you want to connect to the server
    port = 50007
    #[bind ctors socket to RS address, RS port]
    try:
        server_binding=(sa_sameas_myaddr,port)
        ctors.connect(server_binding)
    except mysoc.error as err:
        print('{} \n'.format("connect error "), err)
        exit()

    #check rs-server.py for information on how data
    #is being transferred and stored
    #write all resolved IP information to RESOLVED.txt
    with open("RESOLVED.txt", "w") as fw:
        for hostname in fr:
            ctors.send(hostname.strip().encode('utf-8'))
            dataFromRS=ctors.recv(100)
            if not dataFromRS: break
            result=pickle.loads(dataFromRS)
            if 'A' in result[1]:
                fw.write(hostname.strip()+' '+result[0]+' '+result[1]+'\n')
            """ else
                #[connect to TS server]
                if flag-field (dr) == ‘NS’
                    TSname= hostname-field(dr)
                    ctots.send(hostname) #[Determine IP address of TSname, bind ctots socket to TS address, tsport]
                    dr=ctots.recv(…..) #[Connect and send hostname string ]
                    output (dr) """

    # close everything
    fr.close()
    fw.close()
    ctors.close()
    ctots.close()

client()