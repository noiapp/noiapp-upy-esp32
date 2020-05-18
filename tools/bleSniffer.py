from ubluetooth import BLE, UUID, FLAG_NOTIFY, FLAG_READ, FLAG_WRITE
from micropython import const
from bleADV import ADV_TYPES, dumpHex, dumpAdvData

IRQ_SCAN_RESULT = const(1 << 4)
IRQ_SCAN_COMPLETE = const(1 << 5)


def bt_irq(event, data):
    if event == IRQ_SCAN_RESULT:
        # A single scan result.
        addr_type, addr, adv_type, rssi, adv_data = data
        if adv_type in ADV_TYPES:
            print(ADV_TYPES[adv_type])
            print("{addr: ", dumpHex(addr), ", addr_type: ",
                  repr(addr_type), ", rssi:", repr(rssi), "}")
            print("RAW ADV_DATA: %s" %(dumpHex(adv_data),) )
            dumpAdvData(adv_data)
            print("\r\n")

    elif event == IRQ_SCAN_COMPLETE:
        # Scan duration finished or manually stopped.
        print('scan complete')

def main():
    # Scan continuosly
    bt = BLE()
    bt.active(True)
    bt.irq(handler=bt_irq)
    print("Start scanning....", end="")
    bt.gap_scan(0, 10, 10)
    print("DONE!")

if __name__ == '__main__':
    main()
