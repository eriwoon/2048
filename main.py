#! /usr/bin/python
#encoding=UTF-8
'''
Created on 2014-5-15

@author: XIAO Zhen
'''

'''哈哈'''
import Tkinter as tk
import time
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.winfo_toplevel().rowconfigure(0,minsize = 1)
        self.winfo_toplevel().columnconfigure(0,minsize = 1)
        
        self.grid()
        self.createWidgets()
        self.random()
        self.random()
        self.focus_set()
        self.bind("<Up>", self.callback)
        self.bind("<Down>", self.callback)
        self.bind("<Left>", self.callback)
        self.bind("<Right>", self.callback)
        self.pack()
    def createWidgets(self):
        #direction buttons, up down left and right
        self.direction = {}
        self.direction['up'] = tk.Button(self, text = '⇩', height = 2)
        self.direction['up'].configure(command = (lambda dir = 'to_down': self.todirection(dir)))
        self.direction['up'].grid(row = 0,column = 1, columnspan = 4, sticky = tk.W + tk.E)
        
        self.direction['down'] = tk.Button(self, text = '⇧', height = 2)
        self.direction['down'].configure(command = (lambda dir = 'to_up': self.todirection(dir)))
        self.direction['down'].grid(row = 5,column = 1, columnspan = 4, sticky = tk.W + tk.E)
        
        self.direction['left'] = tk.Button(self, text = '⇨', width = 3)
        self.direction['left'].configure(command = (lambda dir = 'to_right': self.todirection(dir)))
        self.direction['left'].grid(row = 1,column = 0, rowspan = 4, sticky = tk.N + tk.S)
        
        self.direction['right'] = tk.Button(self, text = '⇦', width = 3)
        self.direction['right'].configure(command = (lambda dir = 'to_left': self.todirection(dir)))
        self.direction['right'].grid(row = 1,column = 5, rowspan = 4, sticky = tk.N + tk.S)
        
        self.buttons = []
        for i in range(0,16):
            self.buttons.append(tk.Button(self, text = '0', height = 2, width = 5, background = "#FFFFFF", fg = '#FFFFFF'))
            self.buttons[i].configure(command = (lambda b = self.buttons[i]: self.setNumber(b)))
            self.buttons[i].grid(row = i/4 + 1,column=i%4 + 1)
        #self.triggerButton = tk.Button(self, text = 'Print')
        #self.triggerButton.grid(row = 0, column=1,ipadx = 100)
        
        #control buttons, including mainly start and mode selections
        self.controls = {}
        self.controls['startgame'] = tk.Button(self, text = 'Start', height = 2, width = 5, command=self.startgame)
        self.controls['startgame'].grid(row = 6, column = 4)
        
        self.controls['test1'] = tk.Button(self, text = 'Test1', height = 2, width = 5, command=self.random)
        self.controls['test1'].grid(row = 6,column = 1)
        self.controls['test2'] = tk.Button(self, text = 'Test2', height = 2, width = 5, command=self.test2)
        self.controls['test2'].grid(row = 6,column = 2)
        self.controls['test3'] = tk.Button(self, text = 'Test3', height = 2, width = 5, command=self.test3)
        self.controls['test3'].grid(row = 6,column = 3)
        
    def setNumber(self,button):
        pass
        
    def startgame(self):
        print('start game!')
        
    def random(self):
        empty = []
        rand = -1
        for i in range(0,16):
            if self.buttons[i]['text'] == '0':
                empty.append(i)
        if len(empty) != 0:
            rand = random.randrange(0,len(empty))
            self.buttons[empty[rand]]['text'] = str(random.randrange(1,3) * 2)
            self.setColors()
        else:
            print("no more fields")
            
        if rand != -1:
            self.buttons[empty[rand]].configure(background = '#0404B4', fg = '#000000')
        
    def test2(self):
        print('test2')
        self.buttons[0]['text'] = '2'
        self.buttons[1]['text'] = '2'
        self.buttons[2]['text'] = '4'
        self.buttons[3]['text'] = '8'
        self.buttons[4]['text'] = '4'
        self.buttons[5]['text'] = '2'
        self.buttons[6]['text'] = '2'
        self.buttons[7]['text'] = '8'
        self.buttons[8]['text'] = '4'
        self.buttons[9]['text'] = '2'
        self.buttons[10]['text'] = '2'
        self.buttons[11]['text'] = '8'
        self.buttons[12]['text'] = '8'
        self.buttons[13]['text'] = '8'
        self.buttons[14]['text'] = '8'
        self.buttons[15]['text'] = '8'
        
        self.setColors()
    
    def test3(self):
        print('test3')
        
    def callback(self,event):
        if event.keysym == 'Up':
            self.todirection('to_up')
        elif event.keysym == 'Down':
            self.todirection('to_down')
        elif event.keysym == 'Left':
            self.todirection('to_left')
        elif event.keysym == 'Right':
            self.todirection('to_right')
    
    def sum(self,list):
        for i in range (len(list),5):
            list.append(0)
        for i in range(0,3):
            if list[i] == list[i+1] and list[i] != 0:
                list[i] += list[i+1]
                list[i+1] = 0
        re = []
        for i in range(0,4):
            if list[i] != 0:
                re.append(list[i])
        
        for i in range (len(re),5):
            re.append(0)
            
        return re
    
    def todirection(self, direction):
        flag = 0
        if direction == 'to_right':
            #rows
            for i in range(0, 4):
                #columns:
                list = []
                for j in range(3, -1, -1):
                    if self.buttons[i*4 + j] != '0':
                        list.append(int(self.buttons[i*4 + j]['text']))
                re = self.sum(list)
                
                k = 0
                for j in range(3, -1, -1):
                    if self.buttons[i*4 + j]['text'] != str(re[k]):
                        flag = 1
                        self.buttons[i*4 + j]['text'] = str(re[k])
                    k += 1
                     
        elif direction == 'to_left':
            #rows
            for i in range(0, 4):
                #columns:
                list = []
                for j in range(0, 4):
                    if self.buttons[i*4 + j] != '0':
                        list.append(int(self.buttons[i*4 + j]['text']))
                re = self.sum(list)
                k = 0
                for j in range(0, 4):
                    if self.buttons[i*4 + j]['text'] != str(re[k]):
                        flag = 1
                        self.buttons[i*4 + j]['text'] = str(re[k])
                    k += 1
                    
        elif direction == 'to_up':
            #column
            for i in range(0, 4):
                #row:
                list = []
                for j in range(0, 4):
                    if self.buttons[i + j*4] != '0':
                        list.append(int(self.buttons[i + j*4]['text']))
                re = self.sum(list)
                k = 0
                for j in range(0, 4):
                    if self.buttons[i + j*4]['text'] != str(re[k]):
                        flag = 1
                        self.buttons[i + j*4]['text'] = str(re[k])
                    k += 1
                    
        elif direction == 'to_down':
            #column
            for i in range(0, 4):
                #rows:
                list = []
                for j in range(3, -1, -1):
                    if self.buttons[i + j*4] != '0':
                        list.append(int(self.buttons[i + j*4]['text']))
                re = self.sum(list)
                
                k = 0
                for j in range(3, -1, -1):
                    if self.buttons[i + j*4]['text'] != str(re[k]):
                        flag = 1
                        self.buttons[i + j*4]['text'] = str(re[k])
                    k += 1
        
        if flag != 0:
            self.random()
    
    def setColors(self):
        for i in range(0,16):
            self.setColor(self.buttons[i])
            
    def setColor(self,button):
        tmp = button['text']
        if tmp == '0':
            button.configure(background = '#FFFFFF', fg = '#FFFFFF')
        elif tmp == '2':
            button.configure(background = '#F7F2E0', fg = '#000000') 
        elif tmp == '4':
            button.configure(background = '#F3E2A9', fg = '#000000')
        elif tmp == '8':
            button.configure(background = '#F7BE81', fg = '#000000')
        elif tmp == '16':
            button.configure(background = '#FF8000', fg = '#000000')
        elif tmp == '32':
            button.configure(background = '#FF4000', fg = '#000000')
        elif tmp == '64':
            button.configure(background = '#FF0000', fg = '#000000')
        elif tmp == '128':
            button.configure(background = '#B18904', fg = '#000000')
        elif tmp == '256':
            button.configure(background = '#8A4B08', fg = '#000000')
        elif tmp == '512':
            button.configure(background = '#8A0808', fg = '#000000')
        elif tmp == '1024':
            button.configure(background = '#00FFFF', fg = '#000000')
        elif tmp == '2048':
            button.configure(background = '#00FFFF', fg = '#000000')
        elif tmp == '4096':
            button.configure(background = '#01DFD7', fg = '#000000')
        else:
            button.configure(background = '#0404B4', fg = '#000000')
            
         

if __name__ == '__main__':
    print("Hello World!")
    app = Application()
    app.master.title('Sample application')
    app.mainloop()
    pass


