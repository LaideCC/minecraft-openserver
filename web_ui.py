from pywebio import *
from pywebio.input import *
import requests
import json
import time
import webbrowser
import random
import os

if not os.path.isdir("server"):
    os.mkdir("server")

yes_or_no_list = ["是","否"]

online_mode_replace = {"是":"true","否":"false"}

gamemode_list = ["生存模式","创造模式","冒险模式","旁观模式"]

gamemode_replace = {"生存模式":"survival","创造模式":"creative","冒险模式":"adventure","旁观模式":"spectator"}

config(title='Minecraft-Open Server')

def index():
    version_list = requests.get("http://res.laide.fun/resources/minecraft_server/version_list.json")
    version_list = str(version_list.content)
    version_list = version_list.replace("b", "")
    version_list = version_list.replace("'", "")
    version_list = json.loads(version_list)

    version = select(
        label="服务端版本：",
        options=version_list
    )

    settings = input_group(
        "服务端配置：",
        [
            input('Java最低运行内存（MB）', name='xms', min=1, value=1024, type=NUMBER, required=True),
            input('Java最高运行内存（MB）', name='xmx', min=1, value=1024, type=NUMBER, required=True),
            select(
                label="游戏模式：",
                name='gamemode',
                options=gamemode_list
            ),
            input("世界种子", name="seed", type=NUMBER),
            input("服务器端口", name="port",min=1,max=25565,type=NUMBER),
            input("服务器简介",name="motd",value="A Minecraft Server. Powered by Minecraft-Open Server"),
            select(
                label="是否开启正版验证",
                name="online_mode",
                options=yes_or_no_list
            )
        ]
    )

    gamemode = gamemode_replace[settings["gamemode"]]
    online_mode = online_mode_replace[settings["online_mode"]]
    level_seed = str(settings["seed"])
    server_port = str(settings["port"])
    motd = settings["motd"]
    xms = str(settings["xms"])
    xmx = str(settings["xmx"])

    setting = "gamemode="+gamemode+"\nlevel-seed="+level_seed+"\nserver-port="+server_port+"\nmotd="+motd+"\nonline-mode="+online_mode

    server_name = str(random.randint(10000000, 99999999))

    url = "http://res.laide.fun/resources/minecraft_server/server_"+version+".jar"
    os.chdir('server')
    os.mkdir(server_name)
    os.chdir(server_name)
    download_request = requests.get(url)
    with open('server.jar', 'wb') as download_file:
        download_file.write(download_request.content)

    os.system("java -Xms"+xms+"M -Xmx"+xmx+"M -jar server.jar")
    read_eula = open('eula.txt','r')
    eula = read_eula.read()
    read_eula.close()
    edit_eula = open('eula.txt','w')
    edit_eula.write(eula.replace('false','true'))
    edit_eula.close()
    edit_setting = open('server.properties','w')
    edit_setting.write(setting)
    edit_setting.close()
    os.system("java -Xms"+xms+"M -Xmx"+xmx+"M -jar server.jar")

start_server(index,port=80,auto_open_webbrowser=True)
