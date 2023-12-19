import base58


XPRV = "<INSERT XPRV HERE>"'

zp_header = b'\x04\xb2\x43\x0c'

ZPRV = base58.b58encode_check(zp_header + base58.b58decode_check(XPRV)[4:]).decode('ascii')

print(ZPRV)