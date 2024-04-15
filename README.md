## Preparies

```
pip install python-dotenv pyautogui pywinauto uiautomation logging
(如果 python 安裝版本內已包含 logging 就不須另外安裝了)
```

computer:

1. 安裝 python, git, vscode
2. Chrome, Skype, Spotify

cellphone:

1. 安裝 Skype, Chrome, Spotify, 雲端硬碟, Gmail
2. 開發者模式 關閉手機休眠

## ENVIROMENT

- GOOGLE_MEET_ROOM
- SPOTIFY_PLAYLIST: 4bfj9Go9YnSq7L4YeWTWeY

## INSPECT UI automation Control Pattern

```
cd .\Python-UIAutomation-for-Windows

# 滑鼠指標目前指的元件
python .\automation.py -t3 -c

# 目前最上層視窗的所有元件
python .\automation.py -t3 > log.txt
```

## Description

| File             | Dir                            | Description                            |
| ---------------- | ------------------------------ | -------------------------------------- |
| adb.exe          | (root)                         | Android 手機 command line 執行應用程式 |
| AdbWinApi.dll    | (root)                         | Android 手機 command line 所需檔案     |
| AdbWinUsbApi.dll | (root)                         | Android 手機 command line 所需檔案     |
| main.py          | center controller 主要執行程式 |
| url_list.json    | (root)                         | 包含腳本內所有 URL 的 JSON 檔案        |

每次執行前，須執行動作

1. 開啟 google meet 並建立會議，將會議設定為允許外部人員參加，並更新 .env 中的會議代碼

### IP table

| MAC addr.            | NAME              | IP addr.       |
| -------------------- | ----------------- | -------------- |
| 331 DESKTOP          | 50:EB:F6:B8:FB:EF | 192.168.50.170 |
| IPhone-SE2 CELLPHONE | 62:02:B7:F7:A3:C4 | 192.168.50.171 |
| OPPO-Reno7 CELLPHONE | 22:D0:61:A8:5E:8E | 192.168.50.172 |
| ACER T9300 LAPTOP    | 4C:03:4F:E4:EF:71 | 192.168.50.173 |
| ASUS A550V LAPTOP    | A8:42:A1:0E:7F:B2 | 192.168.50.174 |
| SAMSUNG S20 FE CELLPHONE | BA:72:0D:6F:14:30 | 192.168.50.175 |
| MSI M16 LAPTOP       | F0:D4:15:7F:4C:07 | 192.168.50.176 |
| MY LAPTOP (CENTER)   | 20:16:B9:44:7A:7D | 192.168.50.177 |
| 
