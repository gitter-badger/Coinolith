Coinolith
=========
The [Intuition trade platform](https://github.com/intuition-io) is a p2p collaborative trade platform in progress.  It provides analysis and backtesting with python and R and execution apis in python and golang.

Coinolith is a *Work in Progress* of Realtime Cryptocoin Exchange Apis for the [Intuition trade platform](https://github.com/intuition-io).  Not production ready or tested for real transactions at this time.  In fact only the public apis are being made available at this time. So socket bash and crash away.  

Exchanges with websocket api are being given priority.  RESTful Exchanges will follow and welcomed as contributions at anytime.  See the Api schema and example for uniform api structure for coinolith if you are interested in contributing.


Coinolith is a real time exchange library in python.  Realtime in python?  If you have a need for speed and quick development cycles and zero cost json deserializtion python is tough to beat and there is always pypy.  

Planned Exchange Support:
    
    Okcoin, Huobi, BtcChina, LakeBTC, Bitstamp




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
        



    

