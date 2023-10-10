from typing import List
from instagrapi import Client
from instagrapi.types import Media
from pathlib import Path

#from .medias import get_logger

HASHTAGS = ["instacool"]
IG_USERNAME = "mr.wuhoo"
IG_PASSWORD = "Frb@qdV7U7$haLT"
IG_CREDENTIAL_PATH = "credential.json"

# ... （上面的所有辅助函数和脚本设置保持不变） ...


if __name__ == "__main__":
    import os

    
    cl = Client()
    if os.path.exists(IG_CREDENTIAL_PATH):
        cl.load_settings(IG_CREDENTIAL_PATH)
        #cl.login(IG_USERNAME, IG_PASSWORD)
    else:
        #cl.login(IG_USERNAME, IG_PASSWORD)
        cl.dump_settings(IG_CREDENTIAL_PATH)

   

    # 上传照片
    try:
        caption = "这是我的照片上传测试！"
        photo_path_str = "kanada.jpg"
        photo_path = Path(photo_path_str)
        upload_id, width, height = cl.photo_rupload(photo_path)
        cl.photo_configure(upload_id, width, height, caption)
        print("照片上传成功！")
    except Exception as e:
        print("照片上传失败：{str(e)}")
