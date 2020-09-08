from PIL import Image
import tkinter,random
from tkinter.messagebox import showinfo,showerror
from AlbumDownloadCmd import find_album
from io import BytesIO

def show_album(datas):
    '''
    top = tkinter.Toplevel()
    top.title('picture')
    '''
    Image.open(BytesIO(datas)).show()

def search():
    sq=query.get() #获取Entry控件内容  
    if sq=="":
        return
    bt['state']= tkinter.DISABLED
    l['text']="搜索中..."
    root.update()
    pic=find_album(sq)
    if pic is not None:
        l['text']="Found"
        show_album(pic)
        bt.update()
    else:
        l['text']="Not Found"
    bt['state']= tkinter.NORMAL
    root.update()

root=tkinter.Tk() #创建Tk对象  
root.resizable(0,0) 
root.title("搜封面") #设置窗口标题  
root.geometry("350x150") #设置窗口尺寸 
query=tkinter.Entry(root,background = 'gainsboro') #创建Entry控件 
query.place(x=60,y=20,width=200) #使用place布局，能够布置具体的坐标位置
tkinter.Label(root,text='关键词').place(x=10,y=20,width=50)#创建Text控件，显示多行文本  
l=tkinter.Label(root,height=5,width=30)#创建Text控件，显示多行文本  
l.place(x=50,y=90)
bt=tkinter.Button(root,bg='yellowgreen',height=1,text="搜索",command=search)#创建Button控件
bt.place(x=280,y=40)


root.mainloop()