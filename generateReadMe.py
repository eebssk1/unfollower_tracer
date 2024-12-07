import os
import config

def generateMarkdown():
    unfollowFlag = os.path.exists(config.outputUnfollowerPath)
    newFollowFlag = os.path.exists(config.outputNewFollowerPath)

    with open("./README.md", "w", encoding="utf-8") as targetFile:
        with open(config.defaultREADME, "r", encoding="utf-8") as sourceFile:
            targetFile.write(sourceFile.read())
            targetFile.write("\n")

        targetFile.write(f"# Statistic of {config.accountName} || {config.accountName} 的数据\n")
        targetFile.write("## Users who unfollowed you || 取关列表\n")
        if unfollowFlag:
            with open(config.outputUnfollowerPath, "r", encoding="utf-8") as unfollowFile:
                targetFile.write(unfollowFile.read())
                targetFile.write("\n")
        else:
            targetFile.write("Nothing here! || 啥也没有！\n")

        targetFile.write("## Users who followed you yesterday || 昨日新增\n")
        if newFollowFlag:
            with open(config.outputNewFollowerPath, "r", encoding="utf-8") as newFollowerFile:
                targetFile.write(newFollowerFile.read())
                targetFile.write("\n")
        else:
            targetFile.write("Nothing here! || 啥也木有！\n")