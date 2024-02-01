def setting():
    import tkinter as tk  # 图形界面
    from tkinter import ttk  # 图形界面

    main = tk.Tk()
    main.title('设置')
    main.geometry('900x600')

    info1 = tk.Label(main, text="下面的文本框为Java最低运行内存（以MB为单位，只填数字！），留空为1024MB。")
    Xms = tk.Entry(main)
    info2 = tk.Label(main, text="下面的文本框为Java最高运行内存（以MB为单位，只填数字！），留空为1024MB。")
    Xmx = tk.Entry(main)
    info3 = tk.Label(main, text="下面的下拉框为服务端游戏模式")
    MODE = ttk.Combobox(main)
    MODE["value"] = ("生存","创造","冒险","旁观")
    MODE.current(0)
    MODE["state"] = "readonly"
    info4 = tk.Label(main, text="下面的文本框为服务端世界种子，留空为随机。")
    SEED = tk.Entry(main)
    info5 = tk.Label(main, text="下面的文本框为服务器端口，留空为25565。")
    PORT = tk.Entry(main)
    info6 = tk.Label(main, text="下面的文本框为服务器简介，留空为默认信息。\n（A Minecraft Server. Powered by Minecraft-Open Server）。")
    MOTD = tk.Entry(main)
    info7 = tk.Label(main, text="下面的下拉框为是否开启正版验证（开启会禁止离线模式玩家加入游戏）")
    onlinemode = ttk.Combobox(main)
    onlinemode["value"] = ("是","否")
    onlinemode.current(0)
    onlinemode["state"] = "readonly"
    OKbtn = tk.Button(main, text="创建服务器", command=lambda: iferr(PORT,SEED,Xms,Xmx,MODE,MOTD,onlinemode))

    info1.pack()
    Xms.pack()
    info2.pack()
    Xmx.pack()
    info3.pack()
    MODE.pack()
    info4.pack()
    SEED.pack()
    info5.pack()
    PORT.pack()
    info6.pack()
    MOTD.pack()
    info7.pack()
    onlinemode.pack()
    OKbtn.pack()

    main.mainloop()

def iferr(PORT,SEED,Xms,Xmx,MODE,MOTD,onlinemode):
    import tkinter.messagebox  # 图形界面

    valuelist = {"是":"true","否":"false","生存":"survival","创造":"creative","冒险":"adventure","旁观":"spectator"}
    portvalue = PORT.get()
    seedvalue = SEED.get()
    xmsvalue = Xms.get()
    xmxvalue = Xmx.get()
    modevalue = valuelist[MODE.get()]
    motdvalue = MOTD.get()
    online = valuelist[onlinemode.get()]
    error = 0

    if portvalue != '':
        if not portvalue.isdecimal():
            tkinter.messagebox.showerror(title="出现问题", message="端口号内含有不正确的字符！")
            error = 1
        else:
            if not int(portvalue) >= 1 and int(portvalue) <= 65535:
                tkinter.messagebox.showerror(title="出现问题", message="端口号范围错误！（只能在1-65535的范围内）")
                error = 1
    else:
        portvalue = '25565'
    
    if seedvalue != '':
        if not seedvalue.isdecimal():
            tkinter.messagebox.showerror(title="出现问题", message="种子内含有不正确的字符！")
            error = 1

    if xmsvalue != '':
        if xmsvalue.isdecimal() or xmsvalue == '0':
            tkinter.messagebox.showerror(title="出现问题", message="Xms值不正确！（请填入数字，至少>=1）")
            error = 1
    else:
        xmsvalue = '1024'

    if xmxvalue != '':
        if xmxvalue.isdecimal() or xmxvalue == '0':
            tkinter.messagebox.showerror(title="出现问题", message="Xmx值不正确！（请填入数字，至少>=1）")
            error = 1
    else: 
        xmxvalue = '1024'

    if modevalue != '':
        if not modevalue in ['creative','survival','adventure','spectator']:
            tkinter.messagebox.showerror(title="出现问题", message="游戏模式英文名不正确！")
            error = 1
    else:
        modevalue = 'survival'

    if motdvalue == '':
        motdvalue = 'A Minecraft Server. Powered by Laide-Open Server'

    old_setting = "gamemode="+modevalue+"|level-seed="+seedvalue+"|server-port="+portvalue+"|motd="+motdvalue+"|online-mode="+online
    setting = old_setting.replace("|","\n")

    if error == 0:
        download(xmsvalue,xmxvalue,setting)

def download(Xms,Xmx,setting):
    import os  # 因涉及到读取文件等操作，才使用os模块！
    import requests  # 用于下载文件
    import random  # 随机服务器文件夹名称

    server_name = str(random.randint(10000000, 99999999))

    if os.path.isfile("cache.tmp"):
        cache = open('cache.tmp', 'r')
        url = "http://res.laide.fun/resources/minecraft_server/server_"+cache.read()+".jar"
        os.remove('cache.tmp')
        os.chdir('server')
        os.mkdir(server_name)
        os.chdir(server_name)
        download_request = requests.get(url)
        with open('server.jar', 'wb') as download_file:
            download_file.write(download_request.content)
        building(Xms,Xmx,setting)

def building(Xms,Xmx,setting):
    import os  # 因涉及到运行命令操作，才使用os模块
    os.system("java -Xms"+Xms+"M -Xmx"+Xmx+"M -jar server.jar")
    read_eula = open('eula.txt','r')
    eula = read_eula.read()
    read_eula.close()
    edit_eula = open('eula.txt','w')
    edit_eula.write(eula.replace('false','true'))
    edit_eula.close()
    edit_setting = open('server.properties','w')
    edit_setting.write(setting)
    edit_setting.close()
    os.system("java -Xms"+Xms+"M -Xmx"+Xmx+"M -jar server.jar")

if __name__ == '__main__':
    setting()
