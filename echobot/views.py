from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import urllib

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


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


		k = "http://opendata.cwb.gov.tw/datadownload?dataid=F-C0032-001"
		c = urllib.urlopen(k).read()
		c1 = c.split('<locationName>臺南市</locationName>')
		c2 = c1[1].split('<parameterName>')
		c3 = c2[1].split('</parameterName>')
'''m = 1
try:
    while c1[m] != None:
        c2 = c1[m].split('","tag"')
        c2[0] = re.sub("(<[^>]+>)", "", c2[0])
        if c2[0] != None:
            print c2[0]
            print "--------------------------------------------------"
            m = m+1
except:
    pass'''
        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    line_bot_api.reply_message(
                        event.reply_token,
                        #TextSendMessage(text=event.message.text)
                        TextSendMessage(text=c3[0])
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
