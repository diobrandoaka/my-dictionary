import urllib.request as r
import bs4
import tkinter as tk
import sqlite3
conn=sqlite3.connect("data.db")
cursor=conn.cursor()
def show():
    inp=test.get()
    if len(inp)<=15:
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
        com="SELECT chinese\nFROM voc\nWHERE english='{}';".format(inp)
        inp=inp.replace(" ","%20")
        cursor.execute(com)
        record=cursor.fetchall()
        if record==[]:
            try:
                url="http://www.iciba.com/word?w="+inp
                inp=inp.replace("%20"," ")
                request=r.Request(url,headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'})
                with r.urlopen(request) as f:
                    data=f.read().decode("utf-8")
                soup=bs4.BeautifulSoup(data,"html.parser")
                titles=soup.find_all("ul",class_="Mean_part__UI9M6")
                if titles!=[]:
                    for i in titles:
                        print(i.text)
                        print("=========================================================================================")
                        g=i.text
                        if len(inp)<15:
                            com2="INSERT INTO voc(english)\nVALUES('{}');".format(inp)
                            cursor.execute(com2)
                            conn.commit()
                            for j in range(len(inp)):
                                com2="UPDATE voc\nSET {}='{}'\nWHERE english='{}';".format(l[j],inp[j],inp)
                                cursor.execute(com2)
                                conn.commit()
                            com2="UPDATE voc\nSET chinese='{}'\nWHERE english='{}';".format(g,inp)
                            cursor.execute(com2)
                            conn.commit()
                else:
                    print("查無結果")
                    print("=========================================================================================")
            except:
                print("*詞庫沒有此字相關資料,請接上網路讓我們能獲取資料*")
        else:
            if record[0][0]==None:
                try:
                    url="http://www.iciba.com/word?w="+inp
                    inp=inp.replace("%20"," ")
                    request=r.Request(url,headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'})
                    with r.urlopen(request) as f:
                        data=f.read().decode("utf-8")
                    soup=bs4.BeautifulSoup(data,"html.parser")
                    titles=soup.find_all("ul",class_="Mean_part__UI9M6")
                    if titles!=[]:
                        for i in titles:
                            print(i.text)
                            print("=========================================================================================")
                            g=i.text
                            com2="UPDATE voc\nSET chinese='{}'\nWHERE english='{}';".format(g,inp)
                            cursor.execute(com2)
                            conn.commit()
                    else:
                        print("查無結果")
                        print("=========================================================================================")
                except:
                    print("*詞庫沒有此字相關資料,請接上網路讓我們能獲取資料*")
            else:
                print(record[0][0])
                print("=========================================================================================")
    else:
        print("*字長請在15字以下*")
def show2():
    l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    inp=test.get()
    if len(inp)<=15:
        s=""
        for i in range(len(inp)):
            if i==0:
                s=s+l[i]+"='"+inp[i]+"'"
            else:
                s=s+" and "+l[i]+"='"+inp[i]+"'"
        com="SELECT english\nFROM voc\nWHERE {}\nLIMIT 5;".format(s)
        cursor.execute(com)
        record=cursor.fetchall()
        print("建議搜尋選項：")
        if record !=[]:
            for i in record:
                for j in i:
                    print(j)
        else:
            print("無")
        print("=========================================================================================")
    else:
        print("建議搜尋選項：")
        print("無")
        print("=========================================================================================")
window = tk.Tk()
window.title('英漢字典')
window.geometry('380x400')
test=tk.Entry()
test.pack()
testButton = tk.Button(text="搜尋",command=show)
testButton2 = tk.Button(text="建議搜尋選項",command=show2)
testButton.pack()
testButton2.pack()
window.mainloop()