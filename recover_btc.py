from bip_utils import Bip44Changes, Bip84, Bip84Coins

ZPRV = "<INSERT ZPRV HERE>"


# Construct from extended key
bip84_mst_ctx = Bip84.FromExtendedKey(ZPRV, Bip84Coins.BITCOIN)

# Derive BIP84 account keys: m/84'/0'/0'
bip84_acc_ctx = bip84_mst_ctx.Purpose().Coin().Account(0)

# Derive BIP84 chain keys: m/84'/0'/0'/0
bip84_chg_ctx = bip84_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

# Derive the first n addresses of the external chain: m/44'/0'/0'/0/i
for i in range(5):
    bip84_addr_ctx = bip84_chg_ctx.AddressIndex(i)

    # Print extended keys and address
    print(bip84_addr_ctx.PrivateKey().Bip32Key().Raw().ToHex())
    print(bip84_addr_ctx.PublicKey().ToAddress())
    