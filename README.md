# My Dictionary
## 作品說明
有感於上大學後課本大多轉為原文書,網上資料也大多變為英文,搜索英文單字譯意的需求也隨之提升,我撰寫了一個屬於自己的字典,在學習上有所幫助
## 使用技術
* python(爬蟲)
* SQL(使用SQLite)
## 檔案說明
* main.py為主程式
* data.db為記錄單字的資料庫(辭庫)
* 執行影片展示程式運行狀況,附有txt檔說明
## 運用資源網站
* [https://www.merriam-webster.com/browse/thesaurus](https://www.merriam-webster.com/browse/thesaurus)(基礎辭庫來源)
* [http://www.iciba.com/](http://www.iciba.com/)(中文譯意來源)
## 功能介紹
執行程式會出現GUI介面,上頭有打字的欄位,另有兩種按鍵選擇:搜尋跟建議搜尋選項(詳可見執行影片),點擊按鈕便會根據當前字欄內的字去執行功能
### 搜尋功能
一般來說輸入有四種情況:
* **有網路連接且辭庫存有譯意:** 程式直接給出辭庫中的譯意(較快)
* **有網路連接且辭庫沒有譯意:** 程式會至我們的[中文譯意來源](http://www.iciba.com/)爬取譯意(較慢),爬取完後會將單字和譯意存入辭庫<br>
下次有同樣的查詢就能直接從辭庫取出,加快速度<br>
當然,查無結果的單字不會被記錄<br>
這也是My Dictionary名稱的由來,程式會特別記住使用者查詢過的字,提供更快的查詢速度及線下查詢功能<br>
久而久之,這個字典所記錄的單字也會越來越貼近使用者<br>
個人覺得這樣的設計對看原文書時對於那幾個重複出現的關鍵字反覆查詢的學生應該會有所幫助(就是我)
* **無網路連接且辭庫存有譯意:** 程式直接給出辭庫中的譯意(較快),即線下查詢
* **無網路連接且辭庫沒有譯意:** 程式會要求使用者連上網路供其查詢譯意再查詢此字
### 建議搜尋選項功能
辭庫事先從[基礎辭庫來源](https://www.merriam-webster.com/browse/thesaurus)寫入了約五萬多筆沒有對應譯意的單字以運行這個功能<br>
這項功能會給出辭庫內開頭為字欄內字串的單字(最多五個),ex:字欄:apple,列出:apple,applesauce<br>
在使用者僅依稀記得單字的時候能派上用場
## 注意事項
* 程式支援查詢單字及片語,不過查詢內容請不要包含英文和空白以外的字元,以免出錯
* 輸入字元長度不可超過20
* 資料庫和程式請放在同一個資料夾
## 作者的話
感謝各位看到這裡,我知道這個程式還有不少可以加強的地方,腦中也有一些想法想加入<br>
像是建議搜尋選項功能,現在只會列出前五個找到的單字,一成不變<br>
我想在資料庫再新增一個欄位儲存一個單字被查詢的次數<br>
列出建議搜尋選項時是列出查詢次數前五高的選項,有點模擬熱門搜尋的感覺<br>
還有其他諸如此類的想法想加在這個字典中,讓它功能更多樣化更完善<br>
有空的話看能不能做個更新之類的,搞不好以後會有My Dictionary2.0,3.0之類的XD<br>
想說的話大概就這樣吧,這是我的第一個專案,也希望未來會有更多更多,感謝各位又看我的廢話看到這裡,掰掰<br>
