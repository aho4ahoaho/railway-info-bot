from slackclient import SlackClient
import json
import requests
import datetime
import time
import os

client=SlackClient(os.environ["SLACK_TOKEN"])

def channels_list():
    global channels
    json_data = client.api_call("channels.list")
    channels = json_data['channels']

def railinfo():
    global info
    res = requests.get("http://aho4ahoaho.main.jp/railway-info/index.php")
    info = json.loads(str(res.text))

def message():
    channels_list()
    railinfo()
    post_list=str()
    for channel in channels:
        if channel["is_member"]:
            send="#"+channel["name"]
            post_list = post_list+"{0}".format(channel["name"])+","
            client.api_call("chat.postMessage",
            channel="#"+channel["name"],
            username="鉄道運行情報bot",
            icon_url="http://aho4ahoaho.main.jp/railway-info/icon",
            text="{0}時{1}分現在の運行情報です。".format(datetime.datetime.now().hour,datetime.datetime.now().minute),
            attachments=[{
                    "pretext":"北海道",
                    "text":"{}".format(info["Hokaido"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/2/"),
                    "color":"fc6efd",
                },{
                    "pretext":"東北",
                    "text":"{}".format(info["Tohoku"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/3/"),
                    "color":"a54ec9",
                },{
                    "pretext":"関東",
                    "text":"{}".format(info["Kanto"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/4/"),
                    "color":"e472b0",
                },{
                    "pretext":"中部",
                    "text":"{}".format(info["Chubu"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/5/"),
                    "color":"541cbd",
                },{
                    "pretext":"近畿",
                    "text":"{}".format(info["Kinki"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/6/"),
                    "color":"ee25cb",
                },{
                    "pretext":"中国",
                    "text":"{}".format(info["Chugoku"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/8/"),
                    "color":"fa5b00",
                },{
                    "pretext":"四国",
                    "text":"{}".format(info["Shikoku"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/9/"),
                    "color":"5a8d02",
                },{
                    "pretext":"九州",
                    "text":"{}".format(info["Kyushu"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/7/"),
                    "color":"81b040",
                }]
            )

    print(post_list)

while True:
    date = datetime.datetime.now()
    if date.hour == 8 and date.minute == 00 :
        message()
        print("8時間のスリープに入ります")
        time.sleep(28200)
    
    if date.hour == 16 and date.minute == 00 :
        message()
        print("16時間のスリープに入ります")
        time.sleep(57000)

    print("29秒後にもう一度ループします。"+str(date))
    time.sleep(29)