from bip_utils import Bip44Changes, Bip44, Bip44Coins 

XPRV = "<INSERT XPRV HERE>"


# Construct from extended key
bip44_mst_ctx = Bip44.FromExtendedKey(XPRV, Bip44Coins.ETHEREUM)

# Derive account 0 for Ethereum: m/44'/60'/0'
bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)

# Derive the external chain: m/44'/60'/0'/0
bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

# Derive the first n addresses of the external chain: m/44'/60'/0'/0/i
for i in range(5):
    bip44_addr_ctx = bip44_chg_ctx.AddressIndex(i)

    # Print extended keys and address
    print(bip44_addr_ctx.PrivateKey().Raw().ToHex())
    print(bip44_addr_ctx.PublicKey().ToAddress())

