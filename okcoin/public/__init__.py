#!/usr/bin/env python
"""
Okcoin public websocket api
"""


__author__ = "james rubino github.com/jcrubino"
__copyright__ = "Copyright 2014, Coinolith for Intution and Insight"
__credits__ = ["james.rubino"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "github.com/bittrade"
__email__ = "github.com/bittrade"
__status__ = "WIP pre-alpha"
__description__ ="Okcoin ws api for the coinolith python library of cryptocoin exchange apis"

# todo
# try namedtuples for error handling and response messages
# add docstring testing
# make main connection and streams cleanup clear

from websocket import create_connection


class Client(object):
    """
    web socket client class to connect to okcoin
    """
    def __init__(self, ):
        """
        initialization of class instance
        automatically connects to okcoin
        does not subscribe to any channel

        class methods return golang style error handling of namedtuples('error', message, 'teturn') tuples

        :type self: object
        """
        self.ws_url = "wss://real.okcoin.com:10440/websocket/okcoinapi"
        self.ws  = create_connection(self.ws_url)
        self.subscribed = []

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


    def subscribe_message(self, channel):
        """
        creates json Subscribe message to send, does not send automatically
        :param channel from list_channels or lookup_channel

        :return (error, json(subscribe_message))  error == None if no errors
        """
        return (None, dumps({'event':'addChannel','channel':channel}))

    def unsubscribe_message(self, channel):
        """
        creates json Unsubscribe message to send, does not send automatically
        Okcoin server does not seem to recognize unsubscribe
        """
        return (None, dumps({'event':'removeChannel','channel':channel}))

    def connect(self, rturn=0):
        """
        without a parameter given creates a main class ws connection to okcoin
        if any parameter is passed returns instance of ws connection
        parameter passing used internally if user wants a ws for every channel

        :optional param rturn
        :return default 'ok', else ws_connection (not set inside class instance)
        """
        if rturn==0:
            self.ws  = create_connection(self.ws_url)
            return (0,'ok')
        return (0, create_connection(self.ws_url))

    def disconnect(self):
        """
        Disconnect main websocket connection
        """
        self.ws.close()


    def open_all_streams(self):
        """
        creates a dict of ws connections, each dedicated to a specific channel
        dict found as Okcoin.public.streams
        premptively closes any open connections in streams
        """
        if self.streams.values() != None:
            self.close_all_streams()
        for ch in self.channels:
            if ch not in self.subscribed:
                self.streams[ch] = self.connect(rturn=1)
                self.streams[ch].send(self.subscribe_message(ch))
                self.subscribed.append(ch)


    def close_all_streams(self):
        """"
        Closes all streams in Okcoin.public.streams

        """"
        [x.close() for x in self.streams.values()]
        self.subscribed = []
