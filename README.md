Coinolith
=========
The [Intuition trade platform](https://github.com/intuition-io) is an open source python and golang based p2p collaborate trade system in progress.  It provides analysis and backtesting with python and R and execution apis in python and golang.  As of now there is no cryptocurrency support for the quickly refined intution.io trade platform and Coinolith is the first package to get it there.

Coinolith is a *Work in Progress* of Real-time Cryptocoin Exchange Apis for the [Intuition trade platform](https://github.com/intuition-io) useable in your own project.


Features:

    Planned Support for the main cryptocurrency exchanges

    Easy to use Api!

    Made with Python!

    Ajax like Error and Exception Handling 

    Built for the rapidly improving Intuition.io trade platform



Planned Exchange Support:
    
    Okcoin, Huobi, BtcChina, LakeBTC, Bitstamp

Eventual Support:
    Bitfinex, itBit, Kraken, BTC38, Bter, Bittrex, Cryptsy

Support The Goals and Pace of this Project:
    1BLPCmwoaCZxWPEJVbqVvhkUbn64Lsm8Qo

Or Contact for Support on this or you own system:
    [Gitter.im](gitter.im/BitTrade)


Dependencies:
   
    websocket-client:   pip install websocket
    requests:          pip install requests


Api Schema:

   exchange/public/client

   exchange/private/client

Python 2.7x Example:

    import okcoin.public.client

    okcoin = okcoin.public.client()
    okcoin.list_channels()
    okcoin.subscribe('ok_btccny_ticker')

    while 1:
        for msg in okcoin.ws.recv():
            print(msg)
        



    

