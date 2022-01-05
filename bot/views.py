from django.shortcuts import render

# Create your views here.
# import 必要的函式庫
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

import requests
import pandas as pd

# 這邊是Linebot的授權TOKEN(等等註冊LineDeveloper帳號會取得)，我們為DEMO方便暫時存在settings裡面存取，實際上使用的時候記得設成環境變數，不要公開在程式碼裡喔！
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
API_URL = settings.TAIPEI_QA_API_URL
headers = {"Authorization": settings.AUTH_TOKEN}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
            print(events)

        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                question = event.message.text
                output = query({"inputs": question})
                df = pd.DataFrame(output[0])
                # df
                ans = df[df.score == df.score.max()].label.to_string(index=False)
                line_bot_api.reply_message(
                    event.reply_token,
                   TextSendMessage(text=ans)
                   # TextSendMessage(text = event.message.text)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()