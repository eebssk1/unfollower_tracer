# GitHub username
accountName = "eebssk1"
# Name of follower file
outputFileName = "followerList.md"
# Name of unfollower and new follower file
outputUnfollowerName = "unfollowerList.md"
outputNewFollowerName = "newFollowerList.md"
# Path
outputRawPath = f"./output/{accountName}"
outputFilePath = f"{outputRawPath}/{outputFileName}"
outputUnfollowerPath = f"{outputRawPath}/{outputUnfollowerName}"
outputNewFollowerPath = f"{outputRawPath}/{outputNewFollowerName}"
# Width of avatar
avatarWidth = 75
# Height of avatar
avatarHeight = 75
# Record avatar in the file
# True - Record
# False - Don't record
avatarRecord = True
# How long should crawler sleep until next crawling starts
# Set to 0 if you want it faster
# Not sure if crawler would get blocked for crawling too fast
crawlerSep = 0.5
# Default raw README.md
defaultREADME = "rawIntro/README.md"
