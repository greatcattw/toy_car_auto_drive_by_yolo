# toy_car_auto_drive_by_yolo
Using yolo 8  for toy car auto drive  
使用yolo實作玩具車自動行駛  
這個版本主要是為了  
### 容易學習  容易學習  容易學習  
<br>
<br>
PC由WiFi讀取玩具車上的樹莓3B/Webcam取得影像  
PC由藍芽操作玩具車的動力系統  

使用直排輪的迷你三角錐當作引導物件  
玩具車只有四個動作,直行,往左前,往右前,停止.  

可分成4個單元  
1.圖片取得 get picture  
2.物件偵測 detect object  
3.決策 decision  
4.執行  execution  

## 1.圖片取得
使用樹莓3B架設webcam,這是很成熟的技術了.  
架設流程請參考這邊.  
greatcattw/webcam_rasp_for_auto_drive 
<br>
## 2.物件偵測
本案使用ubuntu22  


## 3.決策
使用python  
為了容易學習,basic1.py,處理的邏輯為  
最下方的角錐,位於圖片水平中央區域,直行  
最下方的角錐,位於圖片水平左側區域,往右前  
最下方的角錐,位於圖片水平右側區域,往左前  
沒有偵測到角錐,停止  
<br>
basic2.py,加入手勢啟動與停止  


## 4.執行
藍芽 + arduino控制馬達,這是很成熟的技術了.  
架設流程請參考這邊.  
greatcattw/control_toy_car_over_bluetooth  
<br>
# In progress
