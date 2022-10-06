import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import socket
import threading
from tkinter import *
from PIL import ImageTk,Image
from time import sleep

#���ο� ������ ����
def openFrame(frame):
    frame.tkraise()

#�г��� �Է� �Ϸ� ��ư ������ ��->�г��� ������ ������ ���ϱ�
def click_entrancebutton():
    openFrame(frame3)


def name_select():
    result = tkinter.simpledialog.askstring("����", "�г����� �Է��ϼ���")
    # ��Ī �Ϸ� �� ����->�Լ� ����ؼ� ��Ī�� �����Ѵٸ� ���� ���������� ��ȯ
    openFrame(frame2)
    print(result)

#������ ����
def cham_start():
    pass

#�̹�������
a = None
def character_select1(e):
    global a
    a = image1

def character_select2(e):
    global a
    a = image2

def character_select3(e):
    global a
    a = image3

def character_select4(e):
    global a
    a = image4

def select_ok(e):
    select_char_can.configure(image = a)

#ä�� �Է��� �� ȭ�鿡 ���̰� (���ͳ� �����ؼ� ����)
def chat_send():
    message = chat_input.get()
    chat_space.insert(END, '\n' + message)
    chat_input.delete(0, 'end')


#����â ����
window=tkinter.Tk()
window.title("������ ����")
window.geometry("700x700")

frame1=tkinter.Frame(window) #�⺻ ������
frame2=tkinter.Frame(window) #�ι�° ������(�г��� ���ϰ� ��Ī ������ �� ���� ȭ��)
frame3=tkinter.Frame(window,bg="yellow") #����° ������(����)

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")
frame3.grid(row=0, column=0, sticky="nsew")

#ĳ���� �̹���
image1=Image.open("image/image1.jpg")
image1=image1.resize((200,200))
image1=ImageTk.PhotoImage(image1)
image2=Image.open("image/image2.jpg")
image2=image2.resize((200,200))
image2=ImageTk.PhotoImage(image2)
image3=Image.open("image/image3.jpg")
image3=image3.resize((200,200))
image3=ImageTk.PhotoImage(image3)
image4=Image.open("image/image4.jpg")
image4=image4.resize((200,200))
image4=ImageTk.PhotoImage(image4)
playbt=Image.open("image/playbt.png")
playbt=playbt.resize((150,100))
playbt=ImageTk.PhotoImage(playbt)

#frame1(���� ù ȭ��)
game_st=tkinter.Button(frame1,image=playbt,command = name_select)
game_st.pack(padx=300,pady=500)

#frame2(��Ī��)
input_nickname_bt=tkinter.Button(frame2,bg="white",text="�� ����",command=click_entrancebutton)
input_nickname_bt.place(x = 315, y= 350)

#frame3(����)

#���� �̹��� ǥ��
select_char_can = tkinter.Label(frame3, width =150, height = 150,bg= 'yellow')
select_char_can.place(x=50, y=50)
select_char_user=tkinter.Label(frame3,text="�� �Է� �г��� ���̰�")
select_char_user.place(x=70,y=10)
select_anchar_user=tkinter.Label(frame3,text="��� �Է� �г��� ���̰�")
select_anchar_user.place(x= 250,y=10)

#ĳ���� ���� ��ư
char_select_br = tkinter.Button(frame3, text = "ĳ���� ����")
char_select_br.place(x =200,y=660)
#ĳ���� ��ư ��ġ
char_image1 = tkinter.Button(frame3,image=image1, width = 200, height = 200)
char_image2 = tkinter.Button(frame3,image=image2, width = 200, height = 200)
char_image3 = tkinter.Button(frame3,image=image3, width = 200, height = 200)
char_image4 = tkinter.Button(frame3,image=image4, width = 200, height = 200)
char_image1.place(x=25,y=240)
char_image2.place(x=235,y=440)
char_image3.place(x=25,y=440)
char_image4.place(x=235,y=240)

char_image1.bind('<Button>', character_select1)
char_image2.bind('<Button>', character_select2)
char_image3.bind('<Button>', character_select3)
char_image4.bind('<Button>', character_select4)
char_select_br.bind('<Button>', select_ok)



#ä�� ������ ���� (Label���� Text�� ����)
chat_space = tkinter.Text(frame3, width = 30, height =35)
chat_space.place(x= 460, y=30)

#ä���Է� �ϴ°�
chat_input = tkinter.Entry(frame3)
# chat_input.bind("<Return>",chat_send)
chat_input.place(x = 460, y = 500,width=155,height=22)

#���� ��ư
chat_br = tkinter.Button(frame3, text = " ���� ", command = chat_send)
chat_br.place(x =630,y=495)

#���ӽ��� ��ư
chamcham_st_bt= tkinter.Button(frame3,image=playbt,command= cham_start)
chamcham_st_bt.place(x=500,y=550)

openFrame(frame1)
window.mainloop()