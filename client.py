#Client
#[ first socket]
try:
    ctors=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)

except mysoc.error as err:
    print('{} \n'.format("socket open error ",err))

#[second socket]
try:
    ctots=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)

except mysoc.error as err:
    print('{} \n'.format("socket open error ", err))

[determine hostname of RS server and port ]
[bind ctors socket to RS address, rsport]

#First Connect to RS server
ctors.send(“hostname”,RSserver )
dr=ctors.recv(…..)
if flag field(dr) == ‘A’
    output(dr)
else
    #[connect to TS server]
    if flag-field (dr) == ‘NS’
        TSname= hostname-field(dr)
        ctots.send(hostname) #[Determine IP address of TSname, bind ctots socket to TS address, tsport]
        dr=ctots.recv(…..) #[Connect and send hostname string ]
        output (dr)