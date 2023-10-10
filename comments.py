from instagrapi import Client
import os

HASHTAGS = ["instacool"]
IG_USERNAME = "mr.wuhoo"
IG_PASSWORD = "Frb@qdV7U7$haLT"
IG_CREDENTIAL_PATH = "credential.json"


# 登录到Instagram
#log into instagram

if __name__ == "__main__":
    cl = Client()
    if os.path.exists(IG_CREDENTIAL_PATH):
        cl.load_settings(IG_CREDENTIAL_PATH)

    try:
    # 从URL获取媒体ID
        media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/Cx9ReVkMv4f/'))

    # 获取所有评论
        comments = cl.media_comments(media_id)

    # 将所有评论保存到文件中
        with open("comments.txt", "w", encoding="utf-8") as f:
            for comment in comments:
                username = comment.user.username
                text = comment.text
                created_at = comment.created_at_utc.strftime('%Y-%m-%d %H:%M:%S')  # Format datetime to string
                f.write(f"Username: {username}, Date: {created_at}, Comment: {text}\n")

        print("All comments saved to comments.txt!")
    except Exception as e:
        print(f"comments saved fall：{str(e)}")