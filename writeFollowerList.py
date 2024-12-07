from tabulate import tabulate
import config

def writeFollower(path, followerList):
    listToWrite = []

    for follower in followerList:
        followerURL = f"https://github.com/{follower}"
        avatarURL = f"{followerURL}.png"
        currFollower = {
            "GitHub Account": f"[{follower}]({followerURL})",
            "Avatar": f"<a href=\"{followerURL}\"><img src=\"{avatarURL}\" width={config.avatarWidth}px height={config.avatarHeight}px></a>",
            "Remark": ""
        }
        if not config.avatarRecord:
            currFollower.pop("Avatar")
        listToWrite.append(currFollower)

    finalList = tabulate(listToWrite, tablefmt="github", headers="keys")
    with open(path, "w", encoding="utf-8") as f:
        f.write(finalList)