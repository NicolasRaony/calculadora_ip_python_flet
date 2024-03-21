print("-_-_-_--_-_-_--_-_-_--_-_-_--_-_-_--_-_-_-IP ADDRESSES-_-_-_--_-_-_--_-_-_--_-_-_--_-_-_--_-_-_-\n")
print(
    "Starting IP Address	   Ending IP Address     	Subnet Mask   \n Class A 10.0.0.0	    10.255.255.255	         255.0.0.0 \n Class B 172.16.0.0	    172.31.255.255	         255.255.0.0 \n Class C 192.168.0.0	192.168.255.255	         255.255.255.0\n")
while True:
    try:
        while True:
            oct1, oct2, oct3, oct4 = input("Digite o endereço ip: ").split('.')
            ip = [0, 0, 0, 0]
            ip[0] = oct1 = int(oct1)
            ip[1] = oct2 = int(oct2)
            ip[2] = oct3 = int(oct3)
            ip[3] = oct4 = int(oct4)
            if ip[0] >= 0 and ip[0] <= 255 and ip[1] >= 0 and ip[1] <= 255 and ip[2] >= 0 and ip[2] <= 255 and ip[3] >= 0 and ip[3] <= 255:
                break
            else:
                print('Valor inválido\n')
                continue
        break
    except ValueError:
        print("Valor inválido\n")
        continue
while True:
    mask = input("\nDigite o valor da máscara: ")
    if mask == '/8' or mask =='/9' or mask == '/10' or mask == '/11' or mask == '/12' or mask == '/13' or mask == '/14' or mask == '/15' or mask == '/16' or mask == '/17' or mask == '/18' or mask == '/19' or mask == '/20' or mask == '/21' \
        or mask == '/22' or mask == '/23' or mask == '/24' or mask == '/25' or mask == '/26' or mask == '/27' or mask == '/28' or mask == '/29' or mask == '/30' or mask == '/31' or mask == '/32':
        break
    else:
        print('Valor inválido')
        continue

print('\n-_-_-_--_-_-_--_-_-_--_-_-_--_-_-_--_-_-_-ADDRESS RESULTS-_-_-_--_-_-_--_-_-_--_-_-_--_-_-_--_-_-_-')
print('')

class_ = 0
if oct1 >= 1 and oct1 < 10:
    class_ = 'Class A - Public'
if oct1 > 10 and oct1 < 128:
    class_ = 'Class A - Public'
if oct1 > 127 and oct1 < 172:
    class_ = 'Class B - Public'
if oct1 == 172:
    if oct2 > 31:
        class_ = 'Class B - Public'
if oct1 > 172 and oct1 < 192:
    class_ = 'class B - Público'
if oct1 == 192:
    if oct2 < 168:
        class_ = 'Class C - Public'
if oct1 == 192:
    if oct2 > 168:
        class_ = 'Class C - Public'
if oct1 > 192 and oct1 < 224:
    class_ = 'Class C - Public'
if oct1 > 223 and oct1 < 240:
    class_ = 'Class D - Public'
if oct1 > 239 and oct1 < 256:
    class_ = 'Class E - Public'
if oct1 == 10:
    class_ = 'Class A - Private'
if oct1 == 172:
    if oct2 > 15 and oct2 < 32:
        class_ = 'Class B - Private'
if oct1 == 192:
    if oct2 == 168:
        class_ = 'Class C - Private'

print('Address: {}.{}.{}.{} - {}'.format(ip[0], ip[1], ip[2], ip[3], class_))

def mask8():
    print('\nNetwork: {}.{}.{}.{}'.format(ip[0], 0, 0, 0))
    print(' Broadcast: {}.{}.{}.{}'.format(ip[0], 255, 255, 255))
    print(' Firsthost: {}.{}.{}.{}'.format(ip[0], 0, 0, 1))
    print(' Lasthost: {}.{}.{}.{}'.format(ip[0], 255, 255, 254))
    print('\nNetmask: 255.0.0.0 = 8')
    print('\nSubnets:')
    print(' {}.{}.{}.{}'.format(ip[0], 0, 0, 0))
    print('\nHosts/Net: {}'.format(2**24 - 2))

def mask9():
    jumps = []
    jumps2 = []
    for i in range(0, 129, 128):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[1] >= jumps[j] and ip[1] < jumps2[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], 255, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], 255, 255, 254))
    print('\nNetmask: 255.128.0.0 = 9')
    print('\nSubnets:')
    for i in range(0, 129, 128):
        ip[1] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print('\nHosts/Net: {}'.format(2 ** 23 - 2))

def mask10():
    jumps = []
    jumps2 = []
    for i in range(0, 193, 64):
        jumps.append(i)
        jumps2.append(i)

    del(jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[1] >= jumps[j] and ip[1] < jumps2[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 254))
    print('\nNetmask: 255.192.0.0 = 10')
    print('\nSubnets:')
    for i in range(0, 193, 64):
        ip[1] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print('\nHosts/Net: {}'.format(2 ** 22 - 2))

def mask11():
    jumps = []
    jumps2 = []
    for i in range(0, 225, 32):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[1] >= jumps[j] and ip[1] < jumps2[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 254))
    print('\nNetmask: 255.224.0.0 = 11')
    for i in range(0, 225, 32):
        ip[1] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print('\nHosts/Net: {}'.format(2 ** 21 - 2))
def mask12():
    jumps = []
    jumps2 = []
    for i in range(0, 241, 16):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[1] >= jumps[j] and ip[1] < jumps2[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 254))
    print('\nNetmask: 255.240.0.0 = 12')
    print('\nSubnets:')
    for i in range(0, 241, 16):
        ip[1] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print('\nHosts/Net: {}'.format(2 ** 20 - 2))

def mask13():
    jumps = []
    jumps2 = []
    for i in range(0, 249, 8):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[1] >= jumps[j] and ip[1] < jumps2[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 254))
    print('\nNetmask: 255.248.0.0 = 13')
    print('\nSubnets:')
    for i in range(0, 249, 8):
        ip[1] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print('\nHosts/Net: {}'.format(2 ** 19 - 2))

def mask14():
    jumps = []
    jumps2 = []
    for i in range(0, 253, 4):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[1] >= jumps[j] and ip[1] < jumps2[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 254))
    print('\nNetmask: 255.252.0.0 = 14')
    print('\nSubnets:')
    for i in range(0, 253, 4):
        ip[1] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print('\nHosts/Net: {}'.format(2 ** 18 - 2))

def mask15():
    jumps = []
    jumps2 = []
    for i in range(0, 255, 2):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[1] >= jumps[j] and ip[1] < jumps2[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, 255, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], 0, 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps[j] - 1, 255, 254))
    print('\nNetmask: 255.254.0.0 = 15')
    print('\nSubnets:')
    for i in range(0, 255, 2):
        ip[1] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print('\nHosts/Net: {}'.format(2 ** 17 - 2))

def mask16():
    print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print(' Broadcast: {}.{}.{}.{}'.format(ip[0], 255, 255, 255))
    print(' Firsthost: {}.{}.{}.{}'.format(ip[0], 0, 0, 1))
    print(' Lasthost: {}.{}.{}.{}'.format(ip[0], 255, 255, 254))
    print('\nNetmask: 255.255.0.0 = 16')
    print('\nSubnets:')
    print(' {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print('\nHosts/Net: {}'.format(2 ** 16 - 2))

def mask17():
    jumps = []
    jumps2 = []
    for i in range(0, 129, 128):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[2] >= jumps[j] and ip[2] < jumps2[j]:
                ip[2] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 254))
        else:
            if ip[2] >= jumps[j]:
                ip[2] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 254))
    print('\nNetmask: 255.255.128.0 = 17')
    print('\nSubnets:')
    for i in range(0, 129, 128):
        ip[2] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
    print('\nHosts/Net: {}'.format(2 ** 15 - 2))

def mask18():
    jumps = []
    jumps2 = []
    for i in range(0, 193, 64):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[2] >= jumps[j] and ip[2] < jumps2[j]:
                ip[2] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 254))
        else:
            if ip[2] >= jumps[j]:
                ip[2] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 254))
    print('\nNetmask: 255.255.192.0 = 18')
    print('\nSubnets:')
    for i in range(0, 193, 64):
        ip[2] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
    print('\nHosts/Net: {}'.format(2 ** 14 - 2))

def mask19():
    jumps = []
    jumps2 = []
    for i in range(0, 225, 32):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[2] >= jumps[j] and ip[2] < jumps2[j]:
                ip[2] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 254))
    print('\nNetmask: 255.255.224.0 = 19')
    print('\nSubnets:')
    for i in range(0, 225, 32):
        ip[2] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
    print('\nHosts/Net: {}'.format(2 ** 13 - 2))

def mask20():
    jumps = []
    jumps2 = []
    for i in range(0, 241, 16):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[2] >= jumps[j] and ip[2] < jumps2[j]:
                ip[2] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 254))
    print('\nNetmask: 255.255.240.0 = 20')
    print('\nSubnets:')
    for i in range(0, 241, 16):
        ip[2] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
    print('\nHosts/Net: {}'.format(2 ** 12 - 2))

def mask21():
    jumps = []
    jumps2 = []
    for i in range(0, 249, 8):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[2] >= jumps[j] and ip[2] < jumps2[j]:
                ip[2] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 254))
    print('\nNetmask: 255.255.248.0 = 21')
    print('\nSubnets:')
    for i in range(0, 249, 8):
        ip[2] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
    print('\nHosts/Net: {}'.format(2 ** 11 - 2))

def mask22():
    jumps = []
    jumps2 = []
    for i in range(0, 253, 4):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[2] >= jumps[j] and ip[2] < jumps2[j]:
                ip[2] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1],jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 254))
    print('\nNetmask: 255.255.252.0 = 22')
    print('\nSubnets:')
    for i in range(0, 252, 4):
        ip[2] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
    print('\nHosts/Net: {}'.format(2 ** 10 - 2))

def mask23():
    jumps = []
    jumps2 = []
    for i in range(0, 255, 2):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[2] >= jumps[j] and ip[2] < jumps2[j]:
                ip[2] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps2[j] - 1, 254))
        else:
            if ip[1] >= jumps[j]:
                ip[1] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 255))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j], 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], jumps[j] - 1, 254))
    print('\nNetmask: 255.255.254.0 = 23')
    print('\nSubnets:')
    for i in range(0, 255, 2):
        ip[2] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 0))
    print('\nHosts/Net: {}'.format(2 ** 9 - 2))

def mask24():
    print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
    print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 255))
    print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 1))
    print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], 254))
    print('\nNetmask: 255.255.255.0 = 24')
    print('\nSubnets:')
    print(' {}.{}.{}.{}'.format(ip[0], ip[1], 0, 0))
    print('\nHosts/Net: {}'.format(2 ** 8 - 2))
def mask25():
    jumps = []
    jumps2 = []
    for i in range(0, ):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[3] >= jumps[j] and ip[3] < jumps2[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 2))
        else:
            if ip[3] >= jumps[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 2))
    print('\nNetmask: 255.255.255.128 = 25')
    print('\nSubnets:')
    for i in range(0, 129, 128):
        ip[3] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
    print('\nHosts/Net: {}'.format(2 ** 7 - 2))
def mask26():
    jumps = []
    jumps2 = []
    for i in range(0, 193, 64):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[3] >= jumps[j] and ip[3] < jumps2[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 2))
        else:
            if ip[3] >= jumps[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 2))
    print('\nNetmask: 255.255.255.192 = 26')
    print('\nSubnets:')
    for i in range(0, 193, 64):
        ip[3] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
    print('\nHosts/Net: {}'.format(2 ** 6 - 2))
def mask27():
    jumps = []
    jumps2 = []
    for i in range(0, 225, 32):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[3] >= jumps[j] and ip[3] < jumps2[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 2))
        else:
            if ip[3] >= jumps[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 2))
    print('\nNetmask: 255.255.255.224 = 27')
    print('\nSubnets:')
    for i in range(0, 225, 32):
        ip[3] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
    print('\nHosts/Net: {}'.format(2 ** 5 - 2))

def mask28():
    jumps = []
    jumps2 = []
    for i in range(0, 241, 16):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[3] >= jumps[j] and ip[3] < jumps2[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 2))
        else:
            if ip[3] >= jumps[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 2))
    print('\nNetmask: 255.255.255.241 = 28')
    print('\nSubnets:')
    for i in range(0, 241, 16):
        ip[3] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
    print('\nHosts/Net: {}'.format(2 ** 4 - 2))
def mask29():
    jumps = []
    jumps2 = []
    for i in range(0, 249, 8):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[3] >= jumps[j] and ip[3] < jumps2[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 2))
        else:
            if ip[3] >= jumps[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 2))
    print('\nNetmask: 255.255.255.248 = 29')
    print('\nSubnets:')
    for i in range(0, 249, 8):
        ip[3] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
    print('\nHosts/Net: {}'.format(2 ** 3 - 2))
def mask30():
    jumps = []
    jumps2 = []
    for i in range(0, 253, 4):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[3] >= jumps[j] and ip[3] < jumps2[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps2[j] - 2))
        else:
            if ip[3] >= jumps[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 1))
                print(' Firsthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] + 1))
                print(' Lasthost: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], jumps[j] - 2))
    print('\nNetmask: 255.255.255.252 = 30')
    print('\nSubnets:')
    for i in range(0, 253, 4):
        ip[3] = i
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
    print('\nHosts/Net: {}'.format(2 ** 2 - 2))
def mask31():
    jumps = []
    jumps2 = []
    for i in range(0, 255, 2):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[3] >= jumps[j] and ip[3] < jumps2[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: N/A')
                print(' Firsthost: N/A')
                print(' Lasthost: N/A')
        else:
            if ip[3] >= jumps[j]:
                ip[3] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
                print(' Broadcast: N/A')
                print(' Firsthost: N/A')
                print(' Lasthost: N/A')
    print('\nNetmask: 255.255.255.254 = 31')
    print('\nSubnets: N/A')
    print('\nHosts/Net: N/A')
def mask32():
    jumps = []
    jumps2 = []
    for i in range(0, 256, 255):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])
    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[3] >= jumps[j] and ip[3] < jumps2[j]:
                ip[3] = jumps[j]
                print('\nNetwork: N/A')
                print(' Broadcast: N/A')
                print(' Firsthost: N/A')
                print(' Lasthost: N/A')
        else:
            if ip[3] >= jumps[j]:
                ip[3] = jumps[j]
                print('\nNetwork: N/A')
                print(' Broadcast: N/A')
                print(' Firsthost: N/A')
                print(' Lasthost: N/A')
    print('\nNetmask: 255.255.255.255 = 32')
    print('\nSubnets: N/A')

    print('\nHosts/Net: N/A')

if mask == '/8':
    mask8()
elif mask == '/9':
    mask9()
elif mask == '/10':
    mask10()
elif mask == '/11':
    mask11()
elif mask == '/12':
    mask12()
elif mask == '/13':
    mask13()
elif mask == '/14':
    mask14()
elif mask == '/15':
    mask15()
elif mask == '/16':
    mask16()
elif mask == '/17':
    mask17()
elif mask == '/18':
    mask18()
elif mask == '/19':
    mask19()
elif mask == '/20':
    mask20()
elif mask == '/21':
    mask21()
elif mask == '/22':
    mask22()
elif mask == '/23':
    mask23()
elif mask == '/24':
    mask24()
elif mask == '/25':
    mask25()
elif mask == '/26':
    mask26()
elif mask == '/27':
    mask27()
elif mask == '/28':
    mask28()
elif mask == '/29':
    mask29()
elif mask == '/30':
    mask30()
elif mask == '/31':
    mask31()
elif mask == '/32':
    mask32()