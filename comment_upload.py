from instagrapi import Client
from pathlib import Path
import os

HASHTAGS = ["instacool"]
IG_USERNAME = "mr.wuhoo"
IG_PASSWORD = "Frb@qdV7U7$haLT"
IG_CREDENTIAL_PATH = "credential.json"
ffmpeg_path = "/Users/lizhuolun/Downloads/ffmpeg"

# 设置环境变量
os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

# def comment_on_media(cl: Client, media_url: str, text: str) -> None:
#     media_id = cl.media_id_from_url(media_url)
#     cl.media_comment(media_id, text)

if __name__ == "__main__":
    cl = Client()
    if os.path.exists(IG_CREDENTIAL_PATH):
        cl.load_settings(IG_CREDENTIAL_PATH)
        #cl.login(IG_USERNAME, IG_PASSWORD)
    else:
       # cl.login(IG_USERNAME, IG_PASSWORD)
        cl.dump_settings(IG_CREDENTIAL_PATH)

    # 发表评论
    try:
        media_url = "https://www.instagram.com/p/Cx9ReVkMv4f/"
        media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/Cx9ReVkMv4f/'))
        comment = cl.media_comment(media_id, "This car is cool")
        comments = cl.media_comments(media_id)
        #comments[0].dict()
        comment.dict()
        print("成功发表评论！")
    except Exception as e:
        print(f"发表评论失败：{str(e)}")
