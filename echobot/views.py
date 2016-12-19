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
    for i in range(0,22):
        if obs_values[i].firstChild.nodeValue == city:
            j=i*15
            location = obs_values[i].firstChild.nodeValue
            obs_values2 = tree.getElementsByTagName('parameterName')
            weather = obs_values2[j].firstChild.nodeValue
    return city + weather

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

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    if "臺南" in event.message.text :
                        reply = get_weather("臺南市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "臺北" in event.message.text :
                        reply = get_weather("臺北市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "新北" in event.message.text :
                        reply = get_weather("新北市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "桃園" in event.message.text :
                        reply = get_weather("桃園市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "臺中" in event.message.text :
                        reply = get_weather("臺中市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "高雄" in event.message.text :
                        reply = get_weather("高雄市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "基隆" in event.message.text :
                        reply = get_weather("基隆市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "新竹縣" in event.message.text :
                        reply = get_weather("新竹縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "新竹市" in event.message.text :
                        reply = get_weather("新竹市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "苗栗" in event.message.text :
                        reply = get_weather("苗栗縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "彰化" in event.message.text :
                        reply = get_weather("彰化縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "南投" in event.message.text :
                        reply = get_weather("南投縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "雲林" in event.message.text :
                        reply = get_weather("雲林縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "嘉義縣" in event.message.text :
                        reply = get_weather("嘉義縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "嘉義市" in event.message.text :
                        reply = get_weather("嘉義市")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "屏東" in event.message.text :
                        reply = get_weather("屏東縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "宜蘭" in event.message.text :
                        reply = get_weather("宜蘭縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "花蓮" in event.message.text :
                        reply = get_weather("花蓮縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "臺東" in event.message.text :
                        reply = get_weather("臺東縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "澎湖" in event.message.text :
                        reply = get_weather("澎湖縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "金門" in event.message.text :
                        reply = get_weather("金門縣")
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    elif "連江" in event.message.text :
                        reply = get_weather("連江縣")
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
