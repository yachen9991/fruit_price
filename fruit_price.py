# -*- coding: utf-8 -*-
import requests
import json
import tkinter as tk
import tkinter.ttk as ttk
import datetime

from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

#get date
today = str(datetime.date.today())
day = today.split('-')[2]
month = today.split('-')[1]

CropChNames = ['百香果-改良種','香蕉','鳳梨-金鑽鳳梨','芒果-愛文','西瓜-大西瓜','葡萄-巨峰']
CropCodes = ['51','A1','B2','R1','T1','S1']
CropNames = ['%E7%99%BE%E9%A6%99%E6%9E%9C','%E9%A6%99%E8%95%89','%E9%B3%B3%E6%A2%A8','%E8%8A%92%E6%9E%9C','%E8%A5%BF%E7%93%9C','%E8%91%A1%E8%90%84']

MarketChNames = ['台北二','台北一','板橋區','三重區']
MarketCodes = [104,109,220,241]
MarketNames = ['%E5%8F%B0%E5%8C%97%E4%BA%8C','%E5%8F%B0%E5%8C%97%E4%B8%80','%E6%9D%BF%E6%A9%8B%E5%8D%80','%E4%B8%89%E9%87%8D%E5%8D%80']

#json data 
'''  "TransDate": "110.06.09",
      "CropCode": "R1",
      "CropName": "芒果-愛文",
      "MarketCode": "104",
      "MarketName": "台北二",
      "Upper_Price": 91.5,
      "Middle_Price": 49.3,
      "Lower_Price": 26,
      "Avg_Price": 53.1,
      "Trans_Quantity": 53711
'''
#---------------GUI--------------------
def callbackFunc(event):
     print(Crop_cb.get())
     print(Market_cb.get())

window = tk.Tk()
window.title('剉冰今天加甚麼')
window.geometry("600x500+250+150")

#new combobox
text1 = tk.Label(window,text="請選擇水果")
text1.pack()
Crop_cb = ttk.Combobox(window,value=CropChNames)
Crop_cb.pack()
text2 = tk.Label(window,text="請選擇市場")
text2.pack()
Market_cb = ttk.Combobox(window,value=MarketChNames)
Market_cb.pack()

Crop_cb.bind("<<ComboboxSelected>>", callbackFunc)
Market_cb.bind("<<ComboboxSelected>>", callbackFunc)

#------------------------chart------------------------
def plot():


    #def which data we need
    if Crop_cb.get() == '百香果-改良種':
        numc = 0
    elif Crop_cb.get() == '香蕉':
        numc = 1
    elif Crop_cb.get() == '鳳梨-金鑽鳳梨':
        numc = 2
    elif Crop_cb.get() == '芒果-愛文':
        numc = 3
    elif Crop_cb.get() == '西瓜-大西瓜':
        numc = 4
    elif Crop_cb.get() == '葡萄-巨峰':
        numc = 5
    

    if Market_cb.get() == '台北二':
        numm = 0
    elif Market_cb.get() == '台北一':
        numm = 1
    elif Market_cb.get() == '板橋區':
        numm = 2
    elif Market_cb.get() == '三重區':
        numm = 3
    
    url = "https://agridata.coa.gov.tw/api/v1/AgriProductsTransType/?Start_time=110."+month+".01&End_time=110."+month+"."+day+"&CropCode="+CropCodes[numc]+"&CropName="+CropNames[numc]+"&MarketName="+MarketNames[numm]
    r = requests.get(url)

    #display response data
    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj,sort_keys=True, indent=4)
        print(text)
    
    r.encoding = 'UTF-8'
    pass_times = r.json()['Data']

    #get avgprice list
    avgprice = []
    for d in pass_times:
        time = d['Avg_Price']
        avgprice.append(time)

    #get dates list
    dates = []
    for d in pass_times:
        tmpd = d['TransDate'].split('.')[2]
        dates.append(tmpd)

    avgprice.reverse()
    dates.reverse()

    #print(avgprice)
    #print(dates)

    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),dpi = 100)
    # adding the subplot
    plot1 = fig.add_subplot(111)
    
    # plotting the graph
    plot1.plot(dates,avgprice)
    
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

plot_button = Button(master = window,command = plot,height = 2,width = 10,text = "Show Chart")
#plot_button2 = Button(master = window,command = clear,height = 2,width = 10,text = "Clear")
  
# place the button 
# in main window
plot_button.pack()
#plot_button2.pack()

window.mainloop()
