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
    url = "http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=CWB-E2BF5AB5-CB0D-4434-ABD8-1A1C7AF82F3D"
    c = urlopen(url).read()
    tree = minidom.parseString(c)
    obs_values = tree.getElementsByTagName("locationName")
    for i in range(0,22):
        if obs_values[i].firstChild.nodeValue == city:      #從最上面的locationName開始找,直到找到使用者輸入的city為止,i為city的index
            j=i*15                                          #因為除了"天氣"有parameterName這個tag,其他也有用到(EX最高溫.最低溫等),一個縣市共有15個parameterName,所以i*15
            obs_values2 = tree.getElementsByTagName("parameterName")
            weather = obs_values2[j].firstChild.nodeValue
    return city + weather


@csrf_exempt
def callback(request):
    
    if request.method == "POST":
        signature = request.META["HTTP_X_LINE_SIGNATURE"]
        body = request.body.decode("utf-8")

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        
        Hello = ["Hello", "哈囉", "嗨"]
        Confirm = ["有", "有喔", "有阿", "好", "好喔", "好阿", "可", "可以"]


        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    uid = event.source.user_id
                    if event.message.text in Hello:
                        reply = uid+" 您好，手環資料顯示您的體溫似乎比較高，請問您有咳嗽情形嗎？"
                        
                        line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=reply)
                            )
                    elif "天氣" in event.message.text :               
                        if "臺南" in event.message.text :
                            reply = get_weather("臺南市")
                        elif "臺北" in event.message.text :
                            reply = get_weather("臺北市")
                        elif "新北" in event.message.text :
                            reply = get_weather("新北市")
                        elif "桃園" in event.message.text :
                            reply = get_weather("桃園市")
                        elif "臺中" in event.message.text :
                            reply = get_weather("臺中市")
                        elif "高雄" in event.message.text :
                            reply = get_weather("高雄市")
                        elif "基隆" in event.message.text :
                            reply = get_weather("基隆市")
                        elif "新竹縣" in event.message.text :
                            reply = get_weather("新竹縣")
                        elif "新竹市" in event.message.text :
                            reply = get_weather("新竹市")
                        elif "苗栗" in event.message.text :
                            reply = get_weather("苗栗縣")
                        elif "彰化" in event.message.text :
                            reply = get_weather("彰化縣")
                        elif "南投" in event.message.text :
                            reply = get_weather("南投縣")
                        elif "雲林" in event.message.text :
                            reply = get_weather("雲林縣")
                        elif "嘉義縣" in event.message.text :
                            reply = get_weather("嘉義縣")
                        elif "嘉義市" in event.message.text :
                            reply = get_weather("嘉義市")
                        elif "屏東" in event.message.text :
                            reply = get_weather("屏東縣")
                        elif "宜蘭" in event.message.text :
                            reply = get_weather("宜蘭縣")
                        elif "花蓮" in event.message.text :
                            reply = get_weather("花蓮縣")
                        elif "臺東" in event.message.text :
                            reply = get_weather("臺東縣")
                        elif "澎湖" in event.message.text :
                            reply = get_weather("澎湖縣")
                        elif "金門" in event.message.text :
                            reply = get_weather("金門縣")
                        elif "連江" in event.message.text :
                            reply = get_weather("連江縣")
                        else:
                            reply = get_weather("臺南市")  #如果只有輸入天氣,沒有輸入地點,會假設成要找臺南市的天氣
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=reply)
                        )
                    else:
                        line_bot_api.reply_message(    #如果沒提到天氣,就重複使用者說的話
                            event.reply_token,
                            TextSendMessage(text=str(did)+event.message.text)
                        )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
