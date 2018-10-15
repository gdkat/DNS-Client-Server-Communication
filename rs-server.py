#RS server
import socket as mysoc
import pickle

def rs():
    #initialize RS socket
    try:
        rssd = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)

    except mysoc.error as err:
        print('[RS]{} \n'.format("RS server socket open error ", err))

    #load file with table information
    try:
        fname = "PROJI-DNSRS.txt"
        fr = open(fname, "r")
    except IOError as err:
        print('{} \n'.format("File Open Error ",err))
        print("Please ensure desired file to reverse exists in source folder and is named PROJI-DNSRS.txt")
        exit()

    #using dictionary structure to store table information
    #each key holds one list value with relevant information to key
    #format dictionary[hostname]: [host_ip,Flag]
    RS_table = {}
    #List of information for TS Server in format [TS Host Name, TS_IP, Flag]
    TS = {}
    # {hostname: {ip: x , flag: y}}
    name = ""
    for line in fr:
        #Per entry, use split to create list of words
        #format = {host : {'ip': ip, 'flag': flag}
        tokenize = line.split()
        #Using strip a lot here
        #gets rid of trailing/preceding spaces and '\n' for proper strcomparisons
        if tokenize[1].strip() == '-':
            pass
        # RS_table[tokenize[0].strip()] = [tokenize[1].strip(),tokenize[2].strip()]
        RS_table[tokenize[0].strip()] = {'ip': tokenize[1].strip(), 'flag':tokenize[2].strip()}
        # if 'NS' in (RS_table[tokenize[0]])[1]:
        if RS_table[tokenize[0].strip()]['flag'] == 'NS':
            name = tokenize[0].strip()
            TS[name] = {'ip': mysoc.gethostbyname(tokenize[0].strip()), 'flag': RS_table[tokenize[0].strip()]['flag']}
            #TS = [tokenize[0].strip(), (mysoc.gethostbyname(tokenize[0].strip())), (RS_table[tokenize[0].strip()])[1]]
    if not TS:
        print("Warning, no TS server to redirect miss\n")
    """ else:
        print("TS Server: ", TS) """ #testing

    #doing server binding stuff here
    #listen for and accept client connection
    server_binding = ('',50008)
    rssd.bind(server_binding)
    rssd.listen(1)
    host=mysoc.gethostname()
    # host = 'grep.cs.rutgers.edu'
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Attempting to connect to client.\n[S]: Server IP address is  ",localhost_ip)
    crsd,addr=rssd.accept()
    print ("[S]: Got a connection request from a client at", addr)

    while True:
        #receive hostname string for resolution request
        data=crsd.recv(100)
        # print('test')
        hnstring=data.decode('utf-8')
        if not hnstring: break
        #check if hnstring is in dictionary and return relevant info list if found
        if hnstring in RS_table:
            entry={hnstring:RS_table[hnstring]}
        #else send TS server info list if TS existed in file
        else:
            if not TS:
                entry=[hnstring,'Error: Host not found','NS']
            else:
                entry={hnstring:TS[name]}
        #using pickle here to convert list into
        #pickle data and send data over socket, since can't just send a list
        crsd.send(pickle.dumps(entry))

    # close everything
    fr.close()
    rssd.close()

rs()