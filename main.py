from followerList import getFollowerList
from writeFollowerList import writeFollower
from writeDiffFollowerList import writeDiffFollower
from generateReadMe import generateMarkdown
import config
import os

def main():
    uid = config.accountName
    # get follower list (username)
    newFollowerList = getFollowerList(uid)
    if len(newFollowerList) == 0:
        print("无法访问 GitHub 用户关注者列表")
        exit(1)

    os.makedirs(config.outputRawPath, exist_ok=True)
    # check if file exists
    if os.path.exists(config.outputFilePath):
        writeDiffFollower(newFollowerList)

    writeFollower(config.outputFilePath, newFollowerList)

    # generate README.md
    generateMarkdown()


if __name__ == '__main__':
    main()