import requests


class Bot:
    def __init__(self, sendkey):
        self.sendkey = sendkey

    def send(self, title: str, content: str) -> dict:
        """
        发送消息

        :param title: 通知标题
        :param content: 消息内容
        :return:
        """
        api = "https://sc.ftqq.com/%s.send" % (self.sendkey)
        data = {"text": title, "desp": content}
        return requests.post(api, data=data)