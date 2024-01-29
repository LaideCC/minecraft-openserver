# Laide一键开服器 1.0

import tkinter as tk  # 图形界面
import tkinter.messagebox  # 图形界面
import os  # 因涉及到创建文件夹等操作，才使用os模块！
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


version_list = ['1.20.4', '1.20.3', '1.20.2', '1.20.1', '1.20','1.19.4','1.19.3','1.19.2','1.19.1','1.19']

version_listbox = tk.Listbox(main)
version_listbox.pack()

for i in version_list:
    version_listbox.insert(tk.END, i)

select_button = tk.Button(main, text='下载', command=next_step)
select_button.pack()

main.mainloop()