import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import sys
import threading
from tkinter import simpledialog
from tkinter import *
from win11toast import toast
import smtplib
if 1 == 0: #headers设置,似乎暂时用不着
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    r = requests.get("http://www.bing.com",headers = headers)
    print(r.text)

def combine_function():
    save_the_password()
    save_the_browser()
    save_the_course()
    window_thread = threading.Thread(target=open_a_window_to_show)
    window_thread.start()
    ISP_login()
    mode0()
def send_notification_vacant(thein1):
    toast1 = toast('{}有剩余容量'.format(thein1))
def send_notification_full(thein2):
    toast2 = toast('{}课程满了'.format(thein2))
def send_notification_by_IFTTT(event_name, key, text1,text2,text3):
    url = "https://maker.ifttt.com/trigger/" + event_name + "/with/key/" + key + ""
    payload = {
        "value1": text1,
        "value2": text2,
        "value3": text3
    }
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a9477d0f-08ee-4960-b6f8-9fd85dc0d5cc,d376ec80-54e1-450a-8215-952ea91b01dd",
        'Host': "maker.ifttt.com",
        'accept-encoding': "gzip, deflate",
        'content-length': "63",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
def input_or_update_showlist(lst,colour):
    if showlist.size() == 0:
        showlist.insert(END, lst)
        showlist.itemconfig(END, bg=colour)
        return 0
    for i in range(showlist.size()):
        item = showlist.get(i)
        if item[0] == lst[0]:
            showlist.delete(i)
            showlist.insert(i, lst)
            showlist.itemconfig(i, bg=colour)
            return 0
    showlist.insert(END, lst)
    showlist.itemconfig(END, bg=colour)
    return 0
def init_email(): #发邮件通知方法，用来发通知给微信的
    mailhost = 'smtp.163.com'
    mailuser = 'zdc6651'
    mailpass = '98765FourThree'
    sender = 'zdc6651@163.com'
    receivers = ['2915903089@qq.com']
def save_the_password():
    theusername = username_entry.get()
    thepassword = password_entry.get()
    f1 = open("THE account.txt", 'w')
    f1.write(theusername)
    f1.write("\n")
    f1.write(thepassword)
    f1.closed
def save_the_browser():
    choosethebrowser = rd_var.get()
    f2 = open("THE browser chosen.txt", 'w')
    f2.write(choosethebrowser)
    f2.closed
def save_the_course():
    class_numbers = value1.get()
    teacher_numbers = value2.get()
    f3 = open("THE course number.txt",'w')
    f3.write(class_numbers)
    f4 = open("THE teacher number.txt",'w')
    f4.write(teacher_numbers)
    f3.closed
    f4.closed
def ISP_login(): #core code
    global browser
    the_browser = rd_var.get()
    if the_browser == "Firefox":
        browser = webdriver.Firefox()
    if the_browser == 'Edge':
        browser = webdriver.Edge()
    browser.get("http://xk.autoisp.shu.edu.cn/Home/TermSelect")
    username_ = browser.find_element(By.ID,'username')
    username_.send_keys(username_entry.get())
    password_ = browser.find_element(By.ID,"password")
    password_.send_keys(password_entry.get())
    time.sleep(1)
    the_button = browser.find_element(By.ID,'submit-button')
    #the_button = browser.find_element(By.XPATH,".//button[@type='submit' and @class='auth_login_btn primary full_width']")
    time.sleep(1)
    the_button.click()
    the_button2 = browser.find_element(By.NAME,"rowterm")
    the_button2.click()
    time.sleep(1)
    the_button3 = browser.find_element(By.XPATH,"//button[contains(., '确定')]")
    the_button3.click()
def open_a_window_to_show():
    global showlist
    mainwindow2 = Tk()
    mainwindow2.title("课程状态监视界面")
    mainwindow2.geometry("550x500")
    mainwindow2.resizable(0,0)
    showlist = Listbox(mainwindow2,width=550,height=500)
    showlist.pack()
    mainwindow2.mainloop()
def modify_selected_items_of_a_list(event): #由GPT生成，懒得自己做了
    selected_index = lst.curselection()
    for index in selected_index:# 获取当前选中项目的值
        current_value = lst.get(index)# 弹出对话框，让用户输入新的数值
        new_value = simpledialog.askstring("输入", "请输入新的数值", initialvalue=current_value)
        if new_value is not None:# 删除选中的项目
            lst.delete(index)# 插入新的数值
            lst.insert(index, new_value)
def modify_selected_items_of_a_list2(event):#和上面一样
    selected_index2 = lst2.curselection()
    for index in selected_index2:
        # 获取当前选中项目的值
        current_value = lst2.get(index)
        # 弹出对话框，让用户输入新的数值
        new_value = simpledialog.askstring("输入", "请输入新的数值", initialvalue=current_value)
        if new_value is not None:
            # 删除选中的项目
            lst2.delete(index)
            # 插入新的数值
            lst2.insert(index, new_value)
def mode0(): #查询课程
    browser.get("http://xk.autoisp.shu.edu.cn/StudentQuery/QueryCourse")
    time.sleep(1)
    pattern = r"\b\w+\b"
    with open("THE course number.txt",'r') as f3:
        classlist = f3.read().strip("()")
        classlist1 = re.findall(pattern,classlist)
        classlist2 = []
        for each in classlist1:
            if each != '0':
                classlist2.append(each)
        print(classlist2)
    with open("THE teacher number.txt",'r') as f4:
        teacherlist = f4.read().strip("()")
        teacherlist1 = re.findall(pattern,teacherlist)
        teacherlist2 = []
        for every in teacherlist1:
            if every != '0' :
                teacherlist2.append(every)
        print(teacherlist2)
        while (1 == 1):
            for i in range(len(teacherlist2)):
                time.sleep(3)
                toinputclasscode = browser.find_element(By.NAME,"CID")
                toinputclasscode.send_keys(classlist2[i])
                toinputteachercode = browser.find_element(By.NAME,"TeachNo")
                toinputteachercode.send_keys(teacherlist2[i])
                the_button4 = browser.find_element(By.XPATH, "//button[contains(.,'查询')]")
                the_button4.click()
                the_row = browser.find_element(By.NAME,"rowclass")
                lst = []
                lst = the_row.text.split(" ")  #将获得的数据通过空格分隔开来
                volumn = lst[9] #这两个数据是数出来的
                peoplenum = lst[10]
                if volumn>peoplenum:
                    print("{}有空闲！快进入！".format(lst[1])) #输出在控制台，不在图形化界面
                    input_or_update_showlist(lst,"green")
                    send_notification_vacant(lst[1])
                    send_notification_by_IFTTT(IFTTT_Event,IFTTT_Key,lst[1],lst[0],lst[3])
                else:
                    print(""""{}"满了""".format(lst[1]))#输出在控制台，不在图形化界面
                    input_or_update_showlist(lst,"red")
                    #send_notification_full(lst[1])  #一般不会有人想收到满了的通知吧
                    send_notification_by_IFTTT(IFTTT_Event, IFTTT_Key, "满了，不如玩一把原神", lst[0], lst[3])
                time.sleep(3)
                browser.refresh()
            time.sleep(5)
#########################################__main__#################################################################
#开发者专属捏
IFTTT_Event = ""
IFTTT_Key = ""
mainwindow = Tk()
mainwindow.title("上大选课捡漏工具")
mainwindow.geometry('600x600')
mainwindow.resizable(0, 0)
lable1 = Label(text='用户名')
lable1.place(x=0, y=10)
lable2 = Label(text='密码')
lable2.place(x=0, y=40)
username_entry = Entry()
username_entry.place(x=40, y=10)
password_entry = Entry(show='*')
password_entry.place(x=40, y=40)
if os.path.exists("THE account.txt"):
    with open("THE account.txt") as f1:
            therealusername, therealpassword = f1.read().split("\n")
            username_entry.insert(0, therealusername)
            password_entry.insert(0, therealpassword)
rd_var = StringVar()  # 创建一个Tkinter变量用于关联Radiobutton
if os.path.exists("THE browser chosen.txt"):
    with open("THE browser chosen.txt") as f2:
        browser111 = f2.read()
        rd_var.set(browser111)
else:
    rd_var.set("Firefox")  # 设置默认选中的选项为"Firefox"
rd1 = Radiobutton(mainwindow, text="Firefox", variable=rd_var,value="Firefox")
rd2 = Radiobutton(mainwindow, text="Edge", variable=rd_var,value="Edge")
lable3 = Label(text="请选择浏览器")
lable3.place(x=250, y=10)
lable4 = Label(text="课程号")
lable4.place(x=10, y=100)
lable5 = Label(text='教师号')
lable5.place(x=180, y=100)
rd1.place(x=330, y=10)
rd2.place(x=330, y=40)
startbutton = Button(mainwindow, text="开始", bg="white", width=5, height=1, font=('Times', 15, 'bold'),command=combine_function)
startbutton.place(x=260, y=550)
value1 = StringVar()
lst = Listbox(mainwindow,listvariable=value1)
lst.bind("<ButtonRelease-1>", modify_selected_items_of_a_list)
value2 = StringVar()
lst2 = Listbox(mainwindow,listvariable=value2)
lst2.bind("<ButtonRelease-1>", modify_selected_items_of_a_list2)
pattern = r"\b\w+\b"
f5 = open("THE course number.txt",'r')
content1 = f5.read().strip("()")
content11 = re.findall(pattern,content1)
for _ in range(len(content11)):
    lst.insert(0,content11[_])
f5.closed
f6 = open("THE teacher number.txt",'r')
content2 = f6.read().strip("()")
content22 = re.findall(pattern,content2)
for _ in range(len(content22)):
    lst2.insert(0,content22[_])
f6.closed
lst.place(x=10, y=120)
lst2.place(x=180, y=120)
mainwindow.mainloop()