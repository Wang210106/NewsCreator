import tkinter
import tkinter.messagebox as msg
import tkinter.filedialog as tkfile
import datetime
import os
import shutil
import webbrowser

#js内容
JsonOp = ["var AllTitles = [","var AllNames = [","var AllTimes = [","var AllAuthors = [","var AllImportance = [","var AllContents = ["]#加];\n

#头图
HeadImagePath = ""
HeadImageName = ""

#选择头图
def chooseImg():
    global HeadImageName,HeadImagePath
    HeadImagePath = tkfile.askopenfilename()
    for ch in HeadImagePath.split("/")[-1]:
        if u'\u4e00' <= ch <= u'\u9fff':
            msg.showinfo("Omega提示","图片名中不能包含中文哦")
            return
    HeadImageName = HeadImagePath.split("/")[-1]

#输出
def outputdef():
    filebook = tkfile.askdirectory()
    y = "\",\""

    ImageTitle = HeadImageName.split(".")

    if not ImageTitle[0] or not ImageTitle[1] == "png":
        msg.showinfo("Omega提示", "图片需是PNG格式")
        return
    if not titleinput.get() or not authorinput.get() or not contenttext.get(1.0, tkinter.END):
        msg.showinfo("omega提示", "您有些内容没填哦")
        return

    content = contenttext.get(1.0, tkinter.END).replace("\n", "<br>").replace("\"","'")
    Jsonresult = "[\""+ImageTitle[0]+y+titleinput.get().replace("\"","'")+y+nowtime+y+authorinput.get().replace("\"","'")+y+"common"+y+content+"\"]"

    with open(filebook+"/"+ImageTitle[0]+".json","w+",encoding="utf-8") as f:
        f.write(Jsonresult)

    shutil.copy(HeadImagePath, filebook)

    msg.showinfo("Omega提示","成功生成！")
    window.destroy()

#预览
def viewpage():
    #反复用到的标点
    gn = "];\n"
    po = "\""
    gp = po + gn

    ImageTitle = HeadImageName.split(".")

    if not ImageTitle[0] or not ImageTitle[1] == "png":
        msg.showinfo("Omega提示","图片需是PNG格式")
        return
    if not titleinput.get() or not authorinput.get() or not contenttext.get(1.0,tkinter.END):
        msg.showinfo("omega提示","您有些内容没填哦")
        return

    content = contenttext.get(1.0,tkinter.END).replace("\n","<br>").replace("\"","'")

    Jsonresult = JsonOp[0]+po+ImageTitle[0]+gp+JsonOp[1]+po+titleinput.get().replace("\"","'")+gp+JsonOp[2]+"+"+po+nowtime+gp+JsonOp[3]+\
                 po+authorinput.get().replace("\"","'")+gp+JsonOp[4]+po+"common"+gp+JsonOp[5]+po+content+gp

    with open("Html/order.js","w+",encoding="utf-8") as f:
        f.write(Jsonresult + "\n")

    #清空Img文件夹
    shutil.rmtree("Html/Img")
    os.makedirs("Html\\Img")

    shutil.copy(HeadImagePath,"Html/Img")

    webpath = os.getcwd() + "\Html\ShowNews.html"
    webbrowser.open_new_tab(webpath)

#开启主页面
def start():
    global window

    window = tkinter.Tk()
    window.geometry("1200x800")
    window.title("Omega新闻编辑器")
    window.config(bg="#000")
    window.resizable(0,0)

    global titleinput,authorinput,nowtime,contenttext

    newstitle = tkinter.Label(window,text="标题：",font=("微软雅黑",15),fg="#FFF",bg="#000")
    newstitle.place(x=50,y=30)
    
    titleinput = tkinter.Entry(window,font=("微软雅黑",15),width="30")
    titleinput.place(x=50,y=76)
    
    newsauthor = tkinter.Label(window,text="作者:",font=("微软雅黑",15),fg="#FFF",bg="#000")
    newsauthor.place(x=50,y=120)
    
    authorinput = tkinter.Entry(window,font=("微软雅黑",15),width="30")
    authorinput.place(x=50,y=170)
    
    nowtime = datetime.datetime.now()
    nowtime = str(nowtime.year) + ("0"*(2-len(str(nowtime.month))))+str(nowtime.month)+("0"*(2-len(str(nowtime.day))))+str(nowtime.day)
    
    newstime = tkinter.Label(window,text="时间："+nowtime,font=("微软雅黑",15),fg="#fff",bg="#000")
    newstime.place(x=50,y=220)

    SelImage = tkinter.Button(window,text="选择头图",command=chooseImg,bd="0",bg="#fff",width="10")
    SelImage.place(x=220,y=223)

    contentlebal = tkinter.Label(window,text="内容：",bg="#000",font=("微软雅黑",15),fg="#fff")
    contentlebal.place(x=50,y=265)

    contenttext = tkinter.Text(window,bg="#fff",bd="1",font=("微软雅黑",15),fg="#000",width="80",height="15")
    contenttext.place(x=50,y=310)

    output = tkinter.Button(window,text="直接输出",command=outputdef,bd="0",bg="#fff",width="10")
    output.place(x=460,y=750)

    Pageview = tkinter.Button(window,text="预览页面",command=viewpage,bd="0",bg="#fff",width="10")
    Pageview.place(x=660,y=750)

    root.destroy()

#开始
root = tkinter.Tk()

root.geometry("1200x800")
root.title("Omega新闻编辑器")
root.config(bg="#000")
root.resizable(0,0)

logo = tkinter.PhotoImage(file = "OMEGA.png")
img = tkinter.Label(root,image=logo,bg="#000")
img.place(x=400,y=150)

btn1 = tkinter.Button(root,text="开始编辑新闻",font=("微软雅黑",12),width="20",height="1",bd="0",bg="#f4f3ec",command=start)
btn1.place(x=493,y=430)

btn2 = tkinter.Button(root,text="退出",font=("微软雅黑",12),width="20",height="1",bd="0",bg="#f4f3ec",command=root.destroy)
btn2.place(x=493,y=500)

root.mainloop()