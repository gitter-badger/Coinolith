Coinolith
=========
Work in Progress of Realtime Cryptocoin Exchange Apis for the [Intuition trade platform](https://github.com/intuition-io).  Not production ready or tested for real transactions at this time.  Infact only the public apis are being made available at this time. So socket bash and crash away.

Exchanges with websocket api wre being given priority

Planned Exchange Support:
    
    Okcoin, Huobi, BtcChina, LakeBTC, Bitstamp

Coinolith is a real time exchange library in python.  Realtime in python?  If you have a need for speed and quick development cycles use PyPy and leverage cpython used in the insight package for intuition.


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
        



    

