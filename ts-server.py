#TS server
try:
    tssd = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
except mysoc.error as err:
    print('[TS]: {}\n'.format("socket open error ", err))

determine local hostname, IP
address , select a port number
tsdd.bind(…)
ctsd,addr=tsdd.accept()
hnstring=ctsd.recv(…)
if hnstring in TS_table:
    entry=TS_table(hnstring)
else:
    entry= “hname” + “Error: Host not found”
    ctsd.send(entry)