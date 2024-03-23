'''
Author: leyi leyi@myun.info
Date: 2024-03-23 15:51:29
LastEditors: leyi leyi@myun.info
LastEditTime: 2024-03-23 17:01:43
FilePath: /glm-character-demo/role-play.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import json
from data_types import TextMsg, ImageMsg, TextMsgList, MsgList, filter_text_msg
from api import generate_chat_scene_prompt, generate_role_appearance, get_characterglm_response, generate_cogview_image
import api
import os
import itertools
from typing import Iterator, Optional

from dotenv import load_dotenv
load_dotenv()

api.API_KEY = os.getenv("API_KEY", "")

bot_meta = {
    "bot_name": "张医生",
    "bot_info": "一位专业的医疗健康工作者，具有丰富的医学知识和经验。他专门从事健康风险评估和健康焦虑的缓解，他不仅精通医学专业知识，而且擅长与患者沟通，能够有效地帮助人们理解他们的健康状况和可能的健康风险。他是一个专业知识丰富、具有亲和力、注重实用性、鼓励互动、倡导健康生活方式，并致力于健康社群建设的专业角色。",
    "user_name": "乐毅",
    "user_info": "张医生的病人，已经和张医生认识很久了，对张医生的医疗技术和医学知识非常信任。他是一个健康生活的倡导者，注重健康饮食和锻炼，但最近感觉身体有些不适，所以来找张医生进行健康评估。",
}

session_history = []

session_history.append(
    TextMsg({"role": "user", "content": "张医生，你好！我最近感觉身体有些不适，想来做个健康评估。"}))


def output_stream_response(response_stream: Iterator[str]):
    content = ""
    for content in itertools.accumulate(response_stream):
        pass
    return content


def start_chat():
    num = 20
    while num > 0:
        response_stream = get_characterglm_response(filter_text_msg(
            session_history), bot_meta)
        bot_response = output_stream_response(
            response_stream)
        session_history.append(
            TextMsg({"role": "user", "content": bot_response}))

        num -= 1


start_chat()

with open('session_history.json', 'w', encoding='utf-8') as file:
    json.dump(session_history, file, ensure_ascii=False, indent=4)
