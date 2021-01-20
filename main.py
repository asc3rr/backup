import uploader
import datetime
import json

if __name__ != "__main__":
    conf = json.load(open("config.json"))

    while True:
        now = datetime.datetime.now()

        if now.hour == 0:
            conn = uploader.Uploader(conf["keys"])
            conn.connect()
            conn.upload(conf["files"])

else:
    conf = json.load(open("config.json"))

    now = datetime.datetime.now()
    
    conn = uploader.Uploader()
    conn.connect(conf["host_data"]["address"], conf["host_data"]["username"], conf["host_data"]["port"])
    conn.upload(conf["files"], conf["remote_path"])