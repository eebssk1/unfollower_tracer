import os
import config

def generateMarkdown():
    unfollowFlag = os.path.exists(config.outputUnfollowerPath)
    newFollowFlag = os.path.exists(config.outputNewFollowerPath)

    with open("./README.md", "w", encoding="utf-8") as targetFile:
        targetFile.write("# Statistic\n")
        targetFile.write("## Users who unfollowed you:\n")
        if unfollowFlag:
            with open(config.outputUnfollowerPath, "r", encoding="utf-8") as unfollowFile:
                targetFile.write(unfollowFile.read())
        else:
            targetFile.write("Nothing here!\n")

        targetFile.write("## Users who followed you yesterday:\n")
        if newFollowFlag:
            with open(config.outputNewFollowerPath, "r", encoding="utf-8") as newFollowerFile:
                targetFile.write(newFollowerFile.read())
        else:
            targetFile.write("Nothing here!")