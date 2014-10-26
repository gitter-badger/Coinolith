#!/usr/bin/env python
"""
Okcoin public websocket api
"""

# todo
# try namedtuples for error handling and response messages
# add docstring testing
# make main connection and streams cleanup clear

from websocket import create_connection
from json import dumps
from itertools import chain

class Client(object):
    """
    okcoin web socket client class
    """
    def __init__(self):
        """
        automatically connects to okcoin
        does not subscribe to any channel

        class methods return golang style error handling of namedtuples('error', message, 'teturn') tuples 
        """
        self.ws_url = "wss://real.okcoin.com:10440/websocket/okcoinapi"
        self.ws  = create_connection(self.ws_url)
        self.subscribed = []
        self.streams = {}
        self.lookup_channel = {
              'btc-usd':{"ticker":"ok_btcusd_ticker",
                         "depth":"ok_btcusd_depth",
                         "depth_60":"ok_btcusd_depth60",
                         "trades":"ok_btcusd_trades",
                         "ohlc_1min":"ok_btcusd_kline_1min",
                         "ohlc_3min":"ok_btcusd_kline_3min",
                         "ohlc_5min":"ok_btcusd_kline_5min",
                         "ohlc_30min":"ok_btcusd_kline_30min",
                         "ohlc_1hour":"ok_btcusd_kline_1hour",
                         "ohlc_2hour":"ok_btcusd_kline_2hour",

                         },

              'ltc-usd':{"ticker":"ok_ltcusd_ticker",
                         "depth":"ok_ltcusd_depth",
                         "depth_60":"ok_ltcusd_depth60",
                         "trades":"ok_ltcusd_trades",
                         "ohlc_1min":"ok_ltcusd_kline_1min",
                         "ohlc_3min":"ok_ltcusd_kline_3min",
                         "ohlc_5min":"ok_ltcusd_kline_5min",
                         "ohlc_30min":"ok_ltcusd_kline_30min",
                         "ohlc_1hour":"ok_ltcusd_kline_1hour",
                         "ohlc_2hour":"ok_ltcusd_kline_2hour",
                         },

              'btc-cny':{"ticker":"ok_btccny_ticker",
                         "depth":"ok_btccny_depth",
                         "depth_60":"ok_btccny_depth60",
                         "trades":"ok_btccny_trades",
                         "ohlc_1min":"ok_btccny_kline_1min",
                         "ohlc_3min":"ok_btccny_kline_3min",
                         "ohlc_5min":"ok_btccny_kline_5min",
                         "ohlc_30min":"ok_btccny_kline_30min",
                         "ohlc_1hour":"ok_btccny_kline_1hour",
                         "ohlc_2hour":"ok_btccny_kline_2hour",
                         },

              'ltc-cny':{"ticker":"ok_ltccny_ticker",
                         "depth":"ok_ltccny_depth",
                         "depth_60":"ok_ltccny_depth60",
                         "trades":"ok_ltccny_trades",
                         "ohlc_1min":"ok_ltccny_kline_1min",
                         "ohlc_3min":"ok_ltccny_kline_3min",
                         "ohlc_5min":"ok_ltccny_kline_5min",
                         "ohlc_30min":"ok_ltccny_kline_30min",
                         "ohlc_1hour":"ok_ltccny_kline_1hour",
                         "ohlc_2hour":"ok_ltccny_kline_2hour",

                         },
        }

        self.list_channels = [x[1] for x in self.lookup_channel.items()]
        self.list_channels = list(chain(*[x.items() for x in self.list_channels]))
        self.list_channels = [y[1] for y in self.list_channels]


    def subscribe_message(self, channel):
        """
        creates json Subscribe message to send, does not send automatically
        :param channel from list_channels or lookup_channel

        :return (error, json(subscribe_message))  error == None if no errors
        """
        if channel in self.list_channels:
            return (0, dumps({'event':'addChannel','channel':channel}))
        if channel not in self.list_channels:
            return (1, 'Given channel not in list_channels')

    def unsubscribe_message(self, channel):
        """
        creates json Unsubscribe message to send, does not send automatically
        Okcoin server does not seem to recognize unsubscribe
        """
        if channel in self.list_channels and channel in self.subscribed:
            return (0, dumps({'event':'removeChannel','channel':channel}))
        if channel not in self.list_channels:
            return (1, 'Given channel not in list_channels')
        if channel not in self.subscribed:
            return (0, "channel not already subscribed")

    def connect(self):
        """
        creates a main class instance webssocket connection to okcoin
        
        :return default 'ok', else ws_connection (not set inside class instance)
        """
        try:
            self.ws  = create_connection(self.ws_url)
            return (0,'ok')
        except Exception as e:
            return (1, str(e))


    def disconnect(self):
        """
        Disconnect main websocket connection
        """
        self.ws.close()
        return (0, 'ok')


    def subscribe_to(self, channel):
        """
        Subscribe to a channel
        """
        try:
            if channel not in self.list_channels:
                return (1, "Error: {0} not in list_channels".format(channel))
            err, msg = self.subscribe_message(channel)
            if err in [0, None]:
                self.ws.send(self.subscribe_message(msg))
                return (0, "ok")
            elif err not in [0, None]:
                return (1, str(e))
        except Exception as e:
            return (1, str(e))
