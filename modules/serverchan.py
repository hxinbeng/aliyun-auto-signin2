from typing import Optional
import logging

import requests
from configobj import ConfigObj


class Pusher:
    def __init__(self, send_key):
        self.send_key = send_key

    def send(self, title: str, content: str) -> dict:
        """
        发送消息

        :param title: 通知标题
        :param content: 消息内容
        :return:
        """
        api = "https://sc.ftqq.com/%s.send" % self.send_key
        data = {"text": title, "desp": content}
        return requests.post(api, data=data).json()


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
    if not config['serverchan_send_key']:
        logging.error('ServerChan 推送参数配置不完整')
        return False

    try:
        pusher = Pusher(config['serverchan_send_key'])
        pusher.send(
            '阿里云盘自动签到',
            f'签到成功: 本月累计签到 {signin_count} 天. 本次签到 {signin_result}'
            if signin_result and signin_count
            else f'签到失败: {signin_result}',
        )
        logging.info('ServerChan 推送成功')
    except Exception as e:
        logging.error(f'ServerChan 推送失败, 错误信息: {e}')
        return False

    return True
