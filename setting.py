  # Laide一键开服器 1.0

numbers = ['1','2','3','4','5','6','7','8','9','0']

def setting():
    import tkinter as tk  # 图形界面

    main = tk.Tk()
    main.title('设置')
    main.geometry('900x600')

    info1 = tk.Label(main, text="第一个文本框为Java最低运行内存（以MB为单位，只填数字！），留空为1024MB。")
    Xms = tk.Entry(main)
    info2 = tk.Label(main, text="第二个文本框为Java最高运行内存（以MB为单位，只填数字！），留空为1024MB。")
    Xmx = tk.Entry(main)
    info3 = tk.Label(main, text="第三个文本框为服务端游戏模式（填入对应的英文），留空为survival（生存）。\ncreative：创造模式\nsurvival：生存模式\nadventure：冒险模式\nspectator：旁观模式")
    MODE = tk.Entry(main)
    info4 = tk.Label(main, text="第四个文本框为服务端世界种子，留空为随机。")
    SEED = tk.Entry(main)
    info5 = tk.Label(main, text="第五个文本框为服务端端口，留空为25565。")
    PORT = tk.Entry(main)
    OKbtn = tk.Button(main,text="创建服务器",command=lambda: iferr(PORT,SEED,Xms,Xmx,MODE))

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
    OKbtn.pack()

    main.mainloop()

def iferr(PORT,SEED,Xms,Xmx,MODE):
    import tkinter.messagebox  # 图形界面
    portvalue = PORT.get()
    seedvalue = SEED.get()
    xmsvalue = Xms.get()
    xmxvalue = Xmx.get()
    modevalue = MODE.get()
    error = 0

    if portvalue != '':
        if not portvalue.isdecimal():
            tkinter.messagebox.showerror(title="出现问题", message="端口号内含有不正确的字符！")
            error = 1
        else:
            if int(portvalue) >= 1 and int(portvalue) <= 65535:
                tkinter.messagebox.showerror(title="出现问题", message="端口号范围错误！（只能在1-65535的范围内）")
                error = 1
    else:
        portvalue = '25565'
    
    if seedvalue != '':
        if not seedvalue.isdecimal():
            tkinter.messagebox.showerror(title="出现问题", message="种子内含有不正确的字符！")
            error = 1

    if xmsvalue != '':
        if xmsvalue.isdecimal():
            tkinter.messagebox.showerror(title="出现问题", message="Xms值不正确！（请填入数字）")
            error = 1
    else:
        xmsvalue = '1024'

    if xmxvalue != '':
        if xmxvalue.isdecimal():
            tkinter.messagebox.showerror(title="出现问题", message="Xmx值不正确！（请填入数字）")
            error = 1
    else:
        xmxvalue = '1024'

    if modevalue != '':
        if not modevalue in ['creative','survival','adventure','spectator']:
            tkinter.messagebox.showerror(title="出现问题", message="游戏模式英文名不正确！")
            error = 1
    else:
        modevalue = 'survival'

    if error == 0:
        download(xmsvalue,xmxvalue)

def download(Xms,Xmx):
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
        building(Xms,Xmx)

def building(Xms,Xmx):
    import os  # 因涉及到运行命令操作，才使用os模块
    os.system("java -Xms"+Xms+"M -Xmx"+Xmx+"M -jar server.jar")
    read_eula = open('eula.txt','r')
    eula = read_eula.read()
    read_eula.close()
    edit_eula = open('eula.txt','w')
    edit_eula.write(eula.replace('false','true'))
    edit_eula.close()
    os.system("java -Xms"+Xms+"M -Xmx"+Xmx+"M -jar server.jar")


if __name__ == '__main__':
    setting()
