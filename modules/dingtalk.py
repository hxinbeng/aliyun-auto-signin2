"""
    @Author: ImYrS Yang
    @Date: 2023/2/11
    @Copyright: ImYrS Yang
    @Description: 
"""

from typing import List, Optional
import logging

import requests
from configobj import ConfigObj


class Pusher:

    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret
        self.access_token = self.get_access_token()

    def get_access_token(self) -> dict:
        """
        获取 access_token

        :return:
        """
        return requests.post(
            'https://api.dingtalk.com/v1.0/oauth2/accessToken',
            json={
                'appKey': self.app_key,
                'appSecret': self.app_secret,
            },
        ).json()['accessToken']

    def send(self, user_ids: List, content: str) -> dict:
        """
        发送消息

        :param user_ids: 用户 ID 列表
        :param content: 消息内容
        :return:
        """
        return requests.post(
            'https://api.dingtalk.com/v1.0/robot/oToMessages/batchSend',
            headers={
                'x-acs-dingtalk-access-token': self.access_token,
            },
            json={
                'robotCode': self.app_key,
                'userIds': user_ids,
                'msgKey': 'sampleText',
                'msgParam': str({
                    'content': content,
                })
            }
        ).json()


def push(
        phone: str,
        signin_result: Optional[str],
        signin_count: Optional[int],
        config: Optional[ConfigObj],
) -> bool:
    """
    签到消息推送

    :param phone: 手机号
    :param signin_result: 签到结果
    :param signin_count: 签到天数
    :param config: 配置文件, ConfigObj 对象
    :return:
    """
    if (
            not config['dingtalk_app_key']
            or not config['dingtalk_app_secret']
            or not config['dingtalk_user_id']
    ):
        logging.error('DingTalk 推送参数配置不完整')
        return False

    try:
        pusher = Pusher(config['dingtalk_app_key'], config['dingtalk_app_secret'])
        pusher.send(
            [config['dingtalk_user_id']],
            f'[{phone}] 阿里云盘签到成功: 本月累计签到 {signin_count} 天. 本次签到 {signin_result}'
            if signin_result and signin_count
            else f'[{phone}] 阿里云盘签到失败: {signin_result}',
        )
        logging.info('DingTalk 推送成功')
    except Exception as e:
        logging.error(f'DingTalk 推送失败, 错误信息: {e}')
        return False

    return True
