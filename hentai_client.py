import socket
from tkinter import *

def but_fow_clicked():
	PWM_r=PWM_R.get()
	PWM_l=PWM_L.get()
	Direc='F_'
	client_sock.send(Direc+str(PWM_r)+'_'+str(PWM_l))

def but_back_clicked():
	PWM_r=PWM_R.get()
	PWM_l=PWM_L.get()
	Direc='B_'
	client_sock.send(Direc+str(PWM_r)+'_'+str(PWM_l))

def but_right_clicked():
	PWM_r=PWM_R.get()
	PWM_l=PWM_L.get()
	Direc='R_'
	client_sock.send(Direc+str(PWM_r)+'_'+str(PWM_l))

def but_left_clicked():
	PWM_r=PWM_R.get()
	PWM_l=PWM_L.get()
	Direc='L_'
	client_sock.send(Direc+str(PWM_r)+'_'+str(PWM_l))

def but_stop_clicked():
	PWM_r=PWM_R.get()
	PWM_l=PWM_L.get()
	Direc='S_'
	client_sock.send(Direc+str(PWM_r)+'_'+str(PWM_l))

def but_play_clicked():
	client_sock.send('P_')

def but_web_clicked():
	Web_ud=servo_up_down.get()
	Web_lr=servo_left_right.get()
	Direc='W_'
	client_sock.send(Direc+str(Web_ud)+'_'+str(Web_lr))

def but_connect_clicked():	
	global client_sock
	client_sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM) 	
	client_sock.connect(('192.168.0.167',8089))
	client_sock.send('pass')#try anything

root = Tk()

root.title("Hentai client")
root.geometry('550x450')

but_fow = Button(root,width=15,height=2,font='arial 14', bg="black",fg='white', text=u"Foward", command=but_fow_clicked)
but_fow.place(x=180,y=1)

but_back = Button(root,width=15,height=2,font='arial 14', bg="black", fg='white',text=u"Back", command=but_back_clicked)
but_back.place(x=180,y=115)

but_right = Button(root,width=15,height=2,font='arial 14', bg="black",fg='white',text=u"Left", command=but_right_clicked)
but_right.place(x=1,y=58)

but_left = Button(root,width=15,height=2,font='arial 14', bg="black",fg='white',text=u"Right", command=but_left_clicked)
but_left.place(x=359,y=58)

but_stop = Button(root,width=15,height=2,font='arial 14', bg="red",fg='black',text=u"Stop", command=but_stop_clicked)
but_stop.place(x=180,y=58)

but_connect = Button(root,width=10,height=1,font='arial 10', bg="blue",fg='black',text=u"Connection", command=but_connect_clicked)
but_connect.place(x=1,y=400)

but_play = Button(root,width=10,height=1,font='arial 10', bg="blue",fg='black',text=u"Play", command=but_play_clicked)
but_play.place(x=100,y=400)

but_web = Button(root,width=10,height=1,font='arial 10', bg="blue",fg='black',text=u"WEB", command=but_web_clicked)
but_web.place(x=200,y=400)


#=================================PWM=========================================
PWM_R = Scale(root,orient=VERTICAL,length=200,from_=100,to=0,tickinterval=10,
resolution=1)
PWM_R.place(x=50,y=180)

PWM_L = Scale(root,orient=VERTICAL,length=200,from_=100,to=0,tickinterval=10,
resolution=1)
PWM_L.place(x=150,y=180)

#===========================Servo_moto====================================
servo_up_down = Scale(root,orient=HORIZONTAL,length=250,from_=-100,to=100,tickinterval=20,
resolution=1)
servo_up_down.place(x=250,y=180)

servo_left_right = Scale(root,orient=HORIZONTAL,length=250,from_=-100,to=100,tickinterval=20,
resolution=1)
servo_left_right.place(x=250,y=250)


root.resizable(False, False)
root.mainloop()
