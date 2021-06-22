# fruit_price

## Introduction
用於查詢本月水果市價資料視覺化軟體

讓有購買大量水果的商家，可以一目了然該水果在本月的價格
可以省錢買下大量便宜的水果，商家用心 顧客安心

## Build process
軟體安裝的套件有:
* requests (2.25.1) : 用於要求API回應資料
* matplotlib (3.4.1) : 製作Line Chart
```
import json
import tkinter
import datetime
```
* json : 處理API回傳的json 型態資料
* tkinter : 製作python GUi
* datetime : 獲得今日日期

## Details of the approach
先利用農委會API要求資料
需要傳遞以下參數 : 
* **Start_time** 資料開始時間
* **End_time**  資料結束時間
* **CropCode**  品項號碼
* **CropName**  品項名稱
* **MarketName**  市場名稱
```
url = "https://agridata.coa.gov.tw/api/v1/AgriProductsTransType/?Start_time=110."+month+".01&End_time=110."+month+"."+day+"&CropCode="+CropCodes[numc]+"&CropName="+CropNames[numc]+"&MarketName="+MarketNames[numm]
r = requests.get(url)
```
回傳資料型態如下面
```python
 data:{
     "TransDate": "110.06.09",
     "CropCode": "R1",
     "CropName": "芒果-愛文",
     "MarketCode": "104",
     "MarketName": "台北二",
     "Upper_Price": 91.5,
     "Middle_Price": 49.3,
     "Lower_Price": 26,
     "Avg_Price": 53.1,
     "Trans_Quantity": 53711
}
```
抓去data中的Avg_Price ,TransDate
放入matplotlib的[x,y]軸

## Results
最初程式會有兩個下拉式選單可以做選取

![image](https://github.com/yachen9991/fruit_price/blob/main/img/combobox.jpg)

* **水果** : 百香果-改良種 ,香蕉 ,鳳梨-金鑽鳳梨 ,芒果-愛文 ,西瓜-大西瓜 ,葡萄-巨峰
* **市場** : 台北二 ,台北一 ,板橋區 ,三重區

選擇後並按下Show Chart 按鈕
顯示本月初到今日，所選擇的水果及市場平均價格折線圖

![image](https://github.com/yachen9991/fruit_price/blob/main/img/result2.jpg)

PS.日期通常不會是連續的，市場會休市。
## References
[農委會 - 農業開放資料服務平台](https://agridata.coa.gov.tw/api.aspx#operations-tag-%E4%BA%A4%E6%98%93%E8%A1%8C%E6%83%85).

