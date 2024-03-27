from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi('i4ZV7mSCtpfIO6xE8/ZPiHHOfXQno2Z268zK81DIpvu76Qv3S43d4aQlQSate5BOeC9P2CzVXXrf0uZlbNwwDCQ7R99mUy7hIlsoJ+hTlqxMR2PgVzUKCPVloNciurR2L4+0ux7UrYGgZPtCyqrjPAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b98b6c80e3d4367d53a78d8c68bf6104')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
