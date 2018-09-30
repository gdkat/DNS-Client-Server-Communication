#RS server
try:
    rssd = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)

except mysoc.error as err:
    print('[RS]{} \n'.format("RS server socket open error ", err))

determine local hostname, IP
address , select a port number
rssd.bind(…)
crsd,addr=rsdd.accept()
hnstring=crsd.recv(…)
if hnstring in RS_table:
    entry=TS_table(hnstring)
else:
    entry= TS-tablerow(Flag=’NS’)
    crsd.send(entry)
