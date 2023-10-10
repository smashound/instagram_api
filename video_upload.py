from typing import List
from instagrapi import Client
from instagrapi.types import Media
from pathlib import Path

#from .medias import get_logger

HASHTAGS = ["instacool"]
IG_USERNAME = "mr.wuhoo"
IG_PASSWORD = "Frb@qdV7U7$haLT"
IG_CREDENTIAL_PATH = "credential.json"
ffmpeg_path = "/Users/lizhuolun/Downloads/ffmpeg"

# ... （上面的所有辅助函数和脚本设置保持不变） ...


if __name__ == "__main__":
    import os

    os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path
    
    cl = Client()
    if os.path.exists(IG_CREDENTIAL_PATH):
        cl.load_settings(IG_CREDENTIAL_PATH)
        cl.login(IG_USERNAME, IG_PASSWORD)
    else:
        cl.login(IG_USERNAME, IG_PASSWORD)
        cl.dump_settings(IG_CREDENTIAL_PATH)

   

    # 上传照片
    try:
        caption = "这是我的video上传测试！"
        video_path_str = "car.mp4"
        video_path = Path(video_path_str)
        cl.video_upload(video_path, caption = "这是我的video上传测试！")
        #cl.video_configure(upload_id, width, height, caption)
        print("veido上传成功！")
    except Exception as e:
        print(f"video上传失败：{str(e)}")
