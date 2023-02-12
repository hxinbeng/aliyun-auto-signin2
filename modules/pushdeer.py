"""
    @Author: ImYrS Yang
    @Date: 2023/2/12
    @Copyright: ImYrS Yang
    @Description: 
"""

from typing import Optional
import logging

import requests
from configobj import ConfigObj


class Pusher:

    def __init__(self, endpoint: str, push_key: str):
        self.endpoint = endpoint
        self.push_key = push_key

    def send(self, title: str, content: str) -> dict:
        """
        发送消息

        :param title: 通知标题
        :param content: 消息内容
        :return:
        """
        return requests.post(
            self.endpoint + '/message/push',
            json={
                'pushkey': self.push_key,
                'type': 'markdown',
                'text': title,
                'desp': content,
            }
        ).json()


def push(
        signin_result: Optional[str],
        signin_count: Optional[int],
        config: Optional[ConfigObj],
) -> bool:
    """
    签到消息推送

    :param signin_result: 签到结果
    :param signin_count: 签到天数
    :param config: 配置文件, ConfigObj 对象
    :return:
    """
    if (
            not config['pushdeer_endpoint']
            or not config['pushdeer_send_key']
    ):
        logging.error('PushDeer 推送参数配置不完整')
        return False

    try:
        pusher = Pusher(config['pushdeer_endpoint'], config['pushdeer_send_key'])
        pusher.send(
            '阿里云盘自动签到',
            f'签到成功: 本月累计签到 {signin_count} 天. 本次签到 {signin_result}'
            if signin_result and signin_count
            else f'签到失败: {signin_result}',
        )
        logging.info('PushDeer 推送成功')
    except Exception as e:
        logging.error(f'PushDeer 推送失败, 错误信息: {e}')
        return False

    return True
