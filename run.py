from slacker import Slacker
import json
import requests
import datetime
import time



slack = Slacker("<YOUR-SLACK-TOKEN>")


def message():
    json_data = json.loads(str(slack.channels.list()))
    channels = json_data['channels']
    res = requests.get("./index.php")
    info = json.loads(str(res.text))
    post_list = str()
    for channel in channels:
        if channel["is_member"]:
            post_list = post_list+"{0}".format(channel["name"])+","
            slack.chat.post_message(
                "#{0}".format(channel["name"]),
                username="鉄道運行情報bot",
                icon_url="./icon.php",
                attachments=[{
                    "pretext":"北海道",
                    "text":"{}".format(info["Hokaido"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/2/"),
                    "color":"FF9900",
                },{
                    "pretext":"東北",
                    "text":"{}".format(info["Tohoku"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/3/"),
                    "color":"FF9900",
                },{
                    "pretext":"関東",
                    "text":"{}".format(info["Kanto"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/4/"),
                    "color":"FF9900",
                },{
                    "pretext":"中部",
                    "text":"{}".format(info["Chubu"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/5/"),
                    "color":"FF9900",
                },{
                    "pretext":"近畿",
                    "text":"{}".format(info["Kinki"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/6/"),
                    "color":"FF9900",
                },{
                    "pretext":"中国",
                    "text":"{}".format(info["Chugoku"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/8/"),
                    "color":"FF9900",
                },{
                    "pretext":"四国",
                    "text":"{}".format(info["Shikoku"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/9/"),
                    "color":"FF9900",
                },{
                    "pretext":"九州",
                    "text":"{}".format(info["Kyushu"].replace(",","\n")+"\nhttps://transit.yahoo.co.jp/traininfo/area/7/"),
                    "color":"FF9900",
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
        print(57000)

    print("29秒後にもう一度ループします。"+str(date))
    time.sleep(29)