import tkinter as tk  # 图形界面
import tkinter.messagebox  # 图形界面
import os  # 因涉及到创建文件夹等操作，才使用os模块！
import requests # 获取版本列表
import json
import setting

main = tk.Tk()
main.title('选取原版服务端版本')
main.geometry('900x600')

if not os.path.isdir("server"):
    os.mkdir("server")

def next_step():
    if not version_listbox.curselection() == ():
        open("cache.tmp", "a", encoding="utf-8").write(
            version_listbox.get(version_listbox.curselection()))
        setting.setting()
    else:
        tkinter.messagebox.showerror(title="出现问题", message="请选择一个服务端版本！")


version_list = requests.get("http://res.laide.fun/resources/minecraft_server/version_list.json")
version_list = str(version_list.content)
version_list = version_list.replace("b", "")
version_list = version_list.replace("'", "")
version_list = json.loads(version_list)

version_listbox = tk.Listbox(main)
version_listbox.pack()

for i in version_list:
    version_listbox.insert(tk.END, i)

select_button = tk.Button(main, text='下载', command=next_step)
select_button.pack()

main.mainloop()
