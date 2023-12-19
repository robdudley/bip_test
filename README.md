# Bip Test

Testing BIP44 and BIP84 hierarchical deterministic wallet derivation from extended master keys

## Installation

Tested against Python 3.11

```pip install bip_utils base58```

## Usage

For each script, enter the XPRV or ZPRV as required into the relevent variable and run.

DO NOT COMMIT XPRV or ZPRV to source control.

### XPRV to ZPRV conversion

Where needed, XPRV can be converted to ZPRV using xprv_to_zprv.py

## Credits

* BIP Utils: https://github.com/ebellocchia/bip_utils/blob/master/examples/bip44.py
* XPrv ZPrv conversion: https://gist.github.com/openoms/4e8a527e4c9757162a53f2dc96e3d229
* Solana Derivation: https://nick.af/articles/derive-solana-addresses