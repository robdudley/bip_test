from bip_utils import Bip44Changes, Bip44, Bip44Coins 

XPRV = "<INSERT XPRV HERE>"


# Construct from extended key
bip44_mst_ctx = Bip44.FromExtendedKey(XPRV, Bip44Coins.SOLANA)


# Derive the first n addresses of the external chain: m/501'/0'/0'/0/i
for i in range(5):           
    bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(i)
    bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

    print(bip44_chg_ctx.PrivateKey().Raw().ToHex())
    print(bip44_chg_ctx.PublicKey().ToAddress()) 
