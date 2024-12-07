from writeFollowerList import writeFollower
import re
import config
import os

def writeDiffFollower(newFollowerList):
    matchString = "\| \[(.*?)]\(https://github.com/"
    with open(config.outputFilePath, "r", encoding="utf-8") as f:
        temp = f.read()

    oldFollowerList = re.findall(matchString, temp)
    unfollowerList = list(set(oldFollowerList) - set(newFollowerList))
    followerList = list(set(newFollowerList) - set(oldFollowerList))

    if os.path.exists(config.outputUnfollowerPath):
        with open(config.outputUnfollowerPath, "r", encoding="utf-8") as f:
            temp = f.read()

        oldUnfollowerList = re.findall(matchString, temp)
        unfollowerList.extend(oldUnfollowerList)

    if len(unfollowerList) > 0:
        writeFollower(config.outputUnfollowerPath, unfollowerList)

    if len(followerList) > 0:
        writeFollower(config.outputNewFollowerPath, followerList)