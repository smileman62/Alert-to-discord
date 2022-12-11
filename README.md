# Gachon University TEAM 1

![](https://gaussian37.github.io/assets/img/vision/opencv/opencv.png)

---
## Refernece
>[Face Recognition](https://github.com/ageitgey/face_recognition)
[Dlib](http://dlib.net/)
[OpenCV2](https://opencv.org/ )
[Discord.py]( https://github.com/Rapptz/discord.py)
[Numpy](https://numpy.org/)

|Author & Collaborator|
|:--:|
|김충영|
|김준혁|
|김진성|
|김태우|
---

## Purpose
- Alert-To-Discord can distinguishes unknowns and registered people for security.
- This project can be used in some private spaces such as workplace

<img src="https://img.insight.co.kr/static/2021/05/31/700/img_20210531205618_23u973gc.webp" width="200" height="200"/>

---

## Feature
(1) It recognizes faces through webcams.<br>
(2) Show "unknown" if you are not registered<br>
(3) If unknown, send alert via discode bot
---
## NOTE
- You must create **Token_discord.py** and put the token value of the discode bot in the token_dis value. For security reasons, **Never expose a bot's token** to the public Internet.
- Although you did not import dlibs from your code, the face_recognition library is a library that uses the features of dlibs. **Therefore, you must have related libraries installed**, such as dlib and Cmake.
- When creating a Discord bot, **PRESENCE INTENT, SERVER MEMBERS INTENT, and MESSAGE CONTENT INTENT** must be enabled. Additional permission assignments can cause security issues.
---
## Known issues
- When the Face detect alert function is running, the record api turns off the gateway at certain times. I think it's to prevent wasting resources when there's no input. However, there seems to be no problem, seeing that the message is sent normally when it occurs.
- If *Face recognition* is not properly performed, an error may occur.
- The stop monitoring function has not yet been implemented because it has an infinite loop in it when entering the start command. Knowledge of asynchronous programming seems to be needed.
--- 
## How To Use
- Create an application, bot, from the Discord Developer Portal at **(https://discord.com/developers/applications)**. Allow certain permissions, such as precautions, and then receive Token.
- Create **token_discord.py** in the project's top-level directory, create the **token_dis variable**, and enter the issued token.
- Put a picture of a known person's face inside the Knows folder. **Only Jpg files** are supported.
- Verify that the webcam is connected, and run record_bot_sender.py. When the Done. message appears in the Console, verify that the bot is online in the discode.
- **!start** command to start webcam monitoring.
