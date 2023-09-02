import random


def random_ssd():
    with open('ssd_250_nvme.txt', 'r') as ssd:
        lines = ssd.readlines()
        productID = []
        vendorID = []
        d = {}
        for line in lines:
            if "productID" in line:
                productID.append(line.strip())
            if "vendorID" in line:
                vendorID.append(line.strip())
        for i in range(len(productID)):
            d[i] = {productID[i]: vendorID[i]}
        r = random.choice(d)
    return r


def random_proc():
    with open('lga_1200.txt', 'r') as proc:
        proc = random.choice(proc.readlines())
    return proc


def random_uuid_bios():
    uuid1: int = f'{random.randint(0, 9)}{random.randint(0, 9)}'
    uuid2: int = random.randint(0, 9)
    uuid3: int = f'{random.randint(0, 9)}{random.randint(0, 9)}'
    uuid4: int = f'{random.randint(0, 9)}{random.randint(0, 9)}'
    uuid6: int = random.randint(0, 9)
    uuid7: int = f'{random.randint(0, 9)}{random.randint(0, 9)}'
    uuid8: int = f'{random.randint(0, 9)}{random.randint(0, 9)}'
    uuid9: int = random.randint(0, 9)
    uuid10: int = f'{random.randint(0, 9)}{random.randint(0, 9)}'
    uuid11: int = random.randint(0, 9)
    uuid12: int = random.randint(0, 9)
    uuid13: int = f'{random.randint(0, 9)}{random.randint(0, 9)}'
    uuid14: int = f'{random.randint(0, 9)}{random.randint(0, 9)}'
    uuid15: int = f'{random.randint(0, 9)}{random.randint(0, 9)}'
    uuid16: int = random.randint(0, 9)
    uuid = (
        f'{uuid1} {uuid2}d {uuid3} {uuid4} fe {uuid6}d {uuid7} {uuid8}-'
        f'f{uuid9} {uuid10} d{uuid11} {uuid12}c {uuid13} {uuid14} {uuid15} '
        f'{uuid16}b'
    )
    return uuid


def random_hdd_serial():
    hdd1: int = random.randint(0, 9)
    hdd2: int = random.randint(0, 9)
    hdd3: int = random.randint(0, 9)
    hdd4: int = random.randint(0, 9)
    hdd5: int = random.randint(0, 9)
    hdd6: int = random.randint(0, 9)
    hdd7: int = random.randint(0, 9)
    hdd8: int = random.randint(0, 9)
    hdd9: int = random.randint(0, 9)
    hdd10: int = 'D'
    hdd11: int = random.randint(0, 9)
    hdd12: int = random.randint(0, 9)
    hdd = (
        f'{hdd1}{hdd2}{hdd3}{hdd4}'
        f'{hdd5}{hdd6}{hdd7}{hdd8}'
        f'{hdd9}{hdd10}{hdd11}{hdd12}'
    )
    return hdd


def random_ethernet_address():
    mac = 'ABCDEF1234567890'
    address1: str = 'B4'
    address2: str = f'{random.choice(mac)}{random.choice(mac)}'
    address3: str = f'{random.choice(mac)}{random.choice(mac)}'
    address4: str = f'{random.choice(mac)}{random.choice(mac)}'
    address5: str = f'{random.choice(mac)}{random.choice(mac)}'
    address6: str = f'{random.choice(mac)}{random.choice(mac)}'
    address = (
        f'{address1}:{address2}:{address3}:'
        f'{address4}:{address5}:{address6}'
    )
    return address


def start_count_vm():
    with open('how_much_vm.txt', 'r') as f:
        start = f.readline()
    return start


def count_vm(count):
    with open('how_much_vm.txt', 'w') as f:
        f.write(f'{count + 1:04}')


if __name__ == '__main__':
    vm_dir = 'vm_today'
    n = int(input())
    if n == 0:
        with open('how_much_vm.txt', 'w') as f:
            f.write('0')
    start = int(start_count_vm())
    for x in range(start, start + n):
        with open(
            'config_for_mod.vmx', 'r'
        ) as f1, open(
            f'{vm_dir}\{x + 1:04}.vmx', 'w'
        ) as f2:
            r = random_ssd()
            product = list(r.keys())
            vendor = list(r.values())
            proc = random_proc()
            uuid = random_uuid_bios()
            hdd = random_hdd_serial()
            ethernet = random_ethernet_address()
            lines = f1.readlines()
            lines[11] = f'{product[0]}\n'
            lines[12] = f'{vendor[0]}\n'
            lines[21] = f'{proc.strip()}\n'
            lines[49] = f'uuid.bios = "{uuid}"\n'
            lines[50] = f'uuid.location = "{uuid}"\n'
            lines[51] = f'hdd.serial = "{hdd}"\n'
            lines[130] = f'ethernet1.address = "{ethernet}"\n'
            lines[189] = f'ethernet0.address = "{ethernet}"\n'

            for line in lines:
                f2.write(line.replace('qwe', f'{x + 1:04}'))
        count_vm(x)
