## 展示影片
https://github.com/kce4981/donut/assets/55190549/ba4f0a94-0ebc-44b0-b076-68d15efe1710
## 程式碼結構
```
│   實驗用，物體頂點等資料匯出資料夾。
├── dumps
│   外部模型，包含物體中心，點和邊等資料。只有torus.csv有被使用到
├── models
│   ├── torus.csv
│   └── ..
│   匯出Blender模型成此程式可用型態的腳本，很粗糙所以不會匯出物體大小，位置資訊等
├── scripts
│   └── blender_export.py
│   程式碼本體
├── src
│   │   場景等
│   ├── scenes
│   │   用來載入外部模型，torus是基於此class
│   │   ├── external.py
│   │   └── ..
│   │   渲染器
│   ├── renderer.py
│   │   旋轉矩陣生產等函式
│   └── transformations.py
│   程式 entry point
├── main.py
│   Dependencies
├── requirements.txt
│   實驗用 Jupyter Notebook，對於測試物體投影點和座標頗有幫助
└── test.ipynb
```
## 運行方法
1. 右上角 Code 選單內下載 zip 檔
2. 解壓縮後進入資料夾
3. 開啟命令視窗並安裝dependencies `pip install -r requirements.txt`
4. 執行main.py `python main.py` or `python3 main.py`
5. 輸入欲選擇場景代碼

指令視窗建議以全螢幕運行，避免繪製圖形超出範圍 \
建議 Python 版本 3.11
