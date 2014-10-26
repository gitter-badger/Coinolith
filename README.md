Coinolith
=========

Coinolith Features:

    Planned Support for the main cryptocurrency exchanges by volume

    Easy to use Api!

    Made with Python!

    Error and exception handling without blowing up the runtime.

    Built for the rapidly advancing Intuition.io trade platform


Planned Exchange Support:
    
    Okcoin, Huobi, BtcChina, LakeBTC, Bitstamp

Eventual Support:
    Bitfinex, itBit, Kraken, BTC38, Bter, Bittrex, Cryptsy

Support The Goals and Pace of this Project:
    1BLPCmwoaCZxWPEJVbqVvhkUbn64Lsm8Qo

Or Contact for Support on this or you own system:

    [Gitter.im](gitter.im/BitTrade)


### Description

The [Intuition trade platform](https://github.com/intuition-io) is a p2p collaborative trade platform in progress.  It provides analysis, backtesting, and execution using python, R, golang.  

Coinolith is a *Work in Progress* of real time cryptocoin exchange apis for the [Intuition trade platform](https://github.com/intuition-io).


Dependencies:
   
    websocket-client:   pip install websocket
    requests:           pip install requests


API Schema:

   exchange/public/client

   exchange/private/client



Python 2.7x Example:

    import okcoin.public.Client

    okcoin = okcoin.public.client()
    okcoin.list_channels()
    okcoin.subscribe('ok_btccny_ticker')

    while 1:
        for msg in okcoin.ws.recv():
            print(msg)
        



    

