from ubluetooth import BLE, UUID, FLAG_NOTIFY, FLAG_READ, FLAG_WRITE
from micropython import const
from bleADV import ADV_TYPES, ADV, ADVData, buildAdvDataTypes

IRQ_SCAN_RESULT = const(1 << 4)
IRQ_SCAN_COMPLETE = const(1 << 5)

def bt_irq(event, data):
    if event == IRQ_SCAN_RESULT:
        # A single scan result.
        addr_type, addr, adv_type, rssi, adv_data = data
        if adv_type in ADV_TYPES:
            
            advs = buildAdvDataTypes(adv_data)

            adv = ADV(adv_type, rssi, addr, addr_type, advs)
            
            print("\r\n%s" %(repr(adv),))
            for it in advs:
                print("\r\n%s" %(str(it)))

    elif event == IRQ_SCAN_COMPLETE:
        # Scan duration finished or manually stopped.
        print('scan complete')

def sniffer(time):
    # Scan continuosly
    bt = BLE()
    bt.active(True)
    bt.irq(handler=bt_irq)
    print("Scanning for %dms..." % time, end="")
    bt.gap_scan(time, 10, 10)
    print("DONE!")

if __name__ == '__main__':
    print(args)
    if len(args) > 1:
        time = int(args[1])
    else:
        time = 0
    print(time)
    sniffer(time)
