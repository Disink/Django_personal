# Personal website with django
簡單的個人網站

# Project
##  Port1
 - 完整的網頁功能 包含:簡歷. 聯絡方式. 其他連結. 後台管理 ...等
 - 額外功能 在收到來自Contact 時會透過Line Bot通知
   - 在Django admin > Lines 填入 line_id 與 Token 即可
   - 額外得編輯 如訊息格式.內容 在website/lines 內設定

## Port II
如果網頁將部屬到雲端 Google app engine. Heroku ...等. 修改Templates就變得比較麻煩
 - 目標讓Template可以在Django admin 編輯
   - 將Templates 存入DB
 - Page也放入DB 讓Templat自己完成排版 讓Page的建立與編輯可以在後台完成
   - 單純文章形式的狀況很好處理
     - Template完成排版後 將Page從DB載入
   - 但如果內容還必須從資料庫取得 Page的部分就無法得到渲染
     - 使用Vue.js在Template完成前端渲染後填入資料
