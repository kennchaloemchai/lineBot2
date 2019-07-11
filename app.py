from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นายเฉลิมชัย ยงชววงศ์ เลขที่ 2 ม.4/6"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    userText = decoded["events"][0]['message']['text']
    #sendText(user,userText)
    if (userText == 'ลงทะเบียน') :
        sendText(user,'www.xnxxs.com')
    elif (userText == 'เช็คเครดิต') :
        sendText(user,'เว็บไม่เกรียนไม่โกง')
    elif (userText == 'สนใจ') :
        sendText(user,'บอล บาคาร่า ยิงปลาและอีกมากมาย')
    elif (userText == 'วิธีการเล่น') :
        sendText(user,'1.โอนเงิน 2.รอรับเงินได้เลย')
    else :
        sendText(user,'สวัสดีครับ')

    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
