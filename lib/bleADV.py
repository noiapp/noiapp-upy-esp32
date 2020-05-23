from struct import unpack

ADV_TYPES = {
    0x00: "[IND] connectable and scannable undirected advertising",
    0x01: "[DIRECT_IND] connectable directed advertising",
    0x02: "[SCAN_IND] scannable undirected advertising",
    0x03: "[NONCONN_IND] non-connectable undirected advertising",
    0x04: "[SCAN_RSP] scan response"
}

# see https://www.bluetooth.com/specifications/assigned-numbers/generic-access-profile/
ADV_DATA_TYPES = {
    0x01: "Flags",
    0x02: "Incomplete List of 16-bit Serv Class UUIDs",
    0x03: "Complete List of 16-bit Serv Class UUIDs",
    0x04: "Incomplete List of 32-bit Serv Class UUIDs",
    0x05: "Complete List of 32-bit Serv Class UUIDs",
    0x06: "Incomplete List of 128-bit Serv Class UUIDs",
    0x07: "Complete List of 128-bit Serv Class UUIDs",
    0x08: "Shortened Local Name",
    0x09: "Complete Local Name",
    0x0A: "Tx Power Level",
    0x0D: "Class of Device",
    0x0E: "Simple Pairing Hash C-192",
    0x0F: "Simple Pairing Randomizer R-192",
    0x10: "Dev ID/Sec Mngr TK Val",
    0x11: "Security Manager Out of Band Flags",
    0x12: "Slave Connection Interval Range",
    0x14: "List of 16-bit Serv Solicitation UUIDs",
    0x15: "List of 128-bit Serv Solicitation UUIDs",
    0x16: "Serv Data 16-bit UUID",
    0x17: "Public Target Address",
    0x18: "Random Target Address",
    0x19: "Appearance",
    0x1A: "Advertising Interval",
    0x1B: "LE Bluetooth Device Address",
    0x1C: "LE Role",
    0x1D: "Simple Pairing Hash C-256",
    0x1E: "Simple Pairing Randomizer R-256",
    0x1F: "List of 32-bit Serv Solicitation UUIDs",
    0x20: "Serv Data - 32-bit UUID",
    0x21: "Serv Data - 128-bit UUID",
    0x22: "LE Secure Connections Confirmation Value",
    0x23: "LE Secure Connections Random Value",
    0x24: "URI",
    0x25: "Indoor Positioning",
    0x26: "Transport Discovery Data",
    0x27: "LE Supported Features",
    0x28: "Channel Map Update Indication",
    0x29: "PB-ADV",
    0x2A: "Mesh Message",
    0x2B: "Mesh Beacon",
    0x2C: "BIGInfo",
    0x3D: "3D Information Data",
    0xFF: "Manufacturer Specific Data"
}

COMPANY_IDENTIFIER = {
    0x079A: "GuangDong Oppo Mob",
    0x072F: "OnePlus Electronics  Co.",
    0x004C: "Apple",
    0x08A9: "Fraunhofer IIS",
    0x08B7: "ABB",
    0x083F: "D-Link",
    0x0837: "vivo Mobile Comm",
    0x0826: "Hyundai Motor Company",
    0x07FC: "Renault SA",
    0x07A2: "Roku",
    0x038F: "Xiaomi",
    0x0393: "LAVAZZA SpA",
    0x0397: "LEGO System A/S",
    0x0381: "Sharp",
    0x0307: "FUJI INDUSTRIAL CO.",
    0x02FF: "Silicon Laboratories",
    0x02EA: "Fujitsu Limited",
    0x02D0: "3M",
    0x02D5: "OMRON",
    0x02C5: "Lenovo",
    0x02B6: "Schneider Electric",
    0x027D: "HUAWEI Technologies Co.",
    0x022E: "Siemens AG",
    0x022B: "Tesla Motors",
    0x01A9: "Canon",
    0x009F: "Suunto Oy",
    0x009E: "Bose",
    0x0090: "Funai Electric Co.",
    0x0087: "Garmin",
    0x0078: "Nike",
    0x0075: "Samsung Electronics Co.",
    0x005D: "Realtek Semiconductor",
    0x005C: "Belkin International",
    0x0059: "Nordic Semiconductor ASA",
    0x0057: "Harman International Industries",
    0x0056: "Sony Ericsson",
    0x004B: "Continental Automotive Systems",
    0x0040: "Seiko Epson",
    0x003F: "Bluetooth SIG",
    0x003E: "Systems and Chips",
    0x003D: "IPextreme",
    0x003C: "BlackBerry Limited",
    0x003B: "Gennum",
    0x003A: "Panasonic",
    0x0036: "Renesas Electronics",
    0x0031: "Synopsys",
    0x0030: "ST Microelectronics",
    0x002F: "MewTel Technology",
    0x002E: "Norwood Systems",
    0x002D: "GCT Semiconductor",
    0x002C: "Macronix International Co.",
    0x002B: "Tenovis",
    0x002A: "Symbol Technologies",
    0x0029: "Hitachi",
    0x0028: "R F Micro Devices",
    0x0027: "Open Interface",
    0x0026: "C Technologies",
    0x0025: "NXP Semiconductors",
    0x0024: "Alcatel",
    0x0023: "WavePlus Technology Co.",
    0x0022: "NEC",
    0x0021: "Mansella",
    0x0020: "BandSpeed",
    0x001F: "AVM Berlin",
    0x001E: "Inventel",
    0x001D: "Qualcomm",
    0x001C: "Conexant Systems",
    0x001B: "Signia Technologies",
    0x001A: "TTPCom Limited",
    0x0019: "Rohde & Schwarz & Co. KG",
    0x0018: "Transilica",
    0x0017: "Newlogic",
    0x0016: "KC Technology",
    0x0015: "RTX Telecom A/S",
    0x0014: "Mitsubishi Electric",
    0x0013: "Atmel",
    0x0012: "Zeevo",
    0x0011: "Widcomm",
    0x0010: "Mitel Semiconductor",
    0x000F: "Broadcom",
    0x000E: "Parthus Technologies",
    0x000D: "Texas Instruments",
    0x000C: "Digianswer A/S",
    0x000B: "Silicon Wave",
    0x000A: "Qualcomm",
    0x0009: "Infineon Technologies AG",
    0x0008: "Motorola",
    0x0007: "Lucent",
    0x0006: "Microsoft",
    0x0005: "3Com",
    0x0004: "Toshiba",
    0x0003: "IBM",
    0x0002: "Intel",
    0x0001: "Nokia Mobile Phones",
    0x0000: "Ericsson Technology Licensing"
}

def uuidStr(data):
    uuid="_INVALID_"
    if len(data)>=16:
        codes = unpack("<LHHHHL", data)
        uuid = "%08X-%02X-%02X-%02X-%010X" %(codes[5], codes[4], codes[3], codes[2], codes[0]|codes[1]<<32,)
    return uuid

def dumpHex(data):
    return "".join('{:02X} '.format(a) for a in data)

def dumpManufacter(data):
    manCode = data[0] | data[1] << 8
    try:
        manName = COMPANY_IDENTIFIER[manCode]
    except:
        manName = "_UNKNOWN_"
    print("\tMANUFACTER:", manName, "[0x%04X]" %(manCode,))
    print("\t%s" %(dumpHex(data[2:]),) )

def dumpUUID(data):
    print("\t%s" %(uuidStr(data),))

ADV_DISSECTOR_MAP = {
    0x07: dumpUUID,
    0xFF: dumpManufacter
}

def dumpAdvData(data):
    i = 0
    while i < len(data):
        advsize  = data[i]           # adv_size
        advdtype = data[i+1]         # adv data type
        advpdu   = data[i+2:i+advsize+1]
        print("[{:02X}]: ".format(advdtype), ADV_DATA_TYPES[advdtype])
        try:
            ADV_DISSECTOR_MAP[advdtype](advpdu)
        except:
            print("\t%s" %(dumpHex(advpdu),) )
            
        i += advsize+1