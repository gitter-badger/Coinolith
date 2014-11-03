<head>
<meta name="google-translate-customization" content="f31da71bc0931632-6ef0cdc90c75472e-g1b3e94b8cfb8c5f4-13"></meta>
</head>

Coinolith
=========
<div id="google_translate_element"></div><script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.FloatPosition.TOP_LEFT}, 'google_translate_element');
}
</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>


**Coinolith Features:**

    Planned Support for the main cryptocurrency exchanges

    Easy to use Api!

    Made with Python so you can optimize however you want!

    Error and exception handling without blowing up the runtime.

    Built for the advanced Intuition.io trade platform made for hackers


**Planned Exchange Support:**
    
    Okcoin, Huobi, BtcChina, LakeBTC, Bitstamp, Anx

**Eventual Support:**
    
    Bitfinex, itBit, Kraken, BTC38, Bter, Bittrex, Cryptsy

**Support The Goals and Pace of this Project:**

    1BLPCmwoaCZxWPEJVbqVvhkUbn64Lsm8Qo

**Contact**

   [Gitter](gitter.im/BitTrade)
 



##Description

The [Intuition.io trade platform](https://github.com/intuition-io) provides a distributed self hosted p2p collaborative trade platform for hackers and centrally hosted platform for users who want a web app interface.   Intuition.io provides analysis, backtesting, and execution using Python, R, and Golang and now  with **Coinolith** support for virtual currency exchanges.

Coinolith is a *Work in Progress* of real time cryptocoin exchange apis for the [Intuition trade platform](https://github.com/intuition-io).


Dependencies:
   
    websocket-client   pip install websocket
    requests           pip install requests


API Schema:

   exchange/public/client

   exchange/private/client



Python 2.7x Example:

    import okcoin.public

    okcoin = okcoin.public.Client()
    okcoin.list_channels()
    okcoin.subscribe('ok_btccny_ticker')

    while 1:
        messages = okcoin.ws.recv():
        for msg in messages:
            print(msg)
        



    

