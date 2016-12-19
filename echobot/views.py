from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import urllib
from urllib.request import urlopen
import requests
import re
from xml.etree.ElementTree import parse
from xml.dom import minidom
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
def get_weather(city):
    k = "http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=CWB-E2BF5AB5-CB0D-4434-ABD8-1A1C7AF82F3D"
    c = urlopen(k).read()
    tree = minidom.parseString(c)
    obs_values = tree.getElementsByTagName('locationName')
    location = obs_values[0].firstChild.nodeValue
    obs_values2 = tree.getElementsByTagName('parameterName')
    weather = obs_values2[0].firstChild.nodeValue
    return location + weather

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        weather = "天氣1"
        

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    if "臺南" in event.message.text :
                        reply = get_weather("臺南市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    else:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="其他")
                        )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
