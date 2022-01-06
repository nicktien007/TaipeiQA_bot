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
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
API_URL = settings.TAIPEI_QA_API_URL
headers = {"Authorization": settings.AUTH_TOKEN}


def query(payload):
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS", "POST"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    response = http.post(API_URL, headers=headers, json=payload,)

    # response = requests.post(API_URL, headers=headers, json=payload, timeout=20)
    print("query res:")
    print(response)
    # print(response.json())
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
                answer = df[df.score == df.score.max()].label.to_string(index=False)
                replay_msg = f"你好😊\n關於您的提問，太Q已為您查詢到服務的局處💪💪\n歡迎聯繫「{answer}」，由專人來為您解答😀\n還有其他可以協助您的地方嗎？\n請將問題輸入對話框👇\n太Q將為您查詢服務的局處唷😃"
                line_bot_api.reply_message(
                    event.reply_token,
                   TextSendMessage(text=replay_msg)
                   # TextSendMessage(text = event.message.text)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()