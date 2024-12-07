import requests
import re
import time
import config

def getFollowerList(uid):
    url = f"https://github.com/{uid}"
    param = {
        "page": 1,
        "tab": "followers"
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    # 关注者列表
    followerList = []
    matchString = "<span class=\"Link--secondary.*\">(.*?)</span>"

    currPage = 0
    # 获取当前时刻的关注者列表
    while True:
        currPage += 1
        param["page"] = currPage
        response = requests.get(url, params=param, headers=header)
        time.sleep(config.crawlerSep)
        originalHTML = response.text
        if response.status_code != 200:
            followerList = []
            break
        result = re.findall(matchString, originalHTML)
        if len(result) == 0:
            break
        followerList.extend(result)

    return followerList
