#!/LouisDing/bin/python3.7
from tkinter.ttk import Notebook
from pytube import YouTube
import os
from tkinter import *
from tkinter import ttk
from pytube import Playlist
#以下是爬蟲package
import urllib.request as req
import bs4


class App():
    def __init__(self, window):
        # 建立變數
        self.urlStr = StringVar()
        self.data = self.urlStr

        # 建立網址輸入位置
        urlLbl = Label(root, text="網址:", width=8)
        urlLbl.place(x=0, y=5)
        self.urlE = Entry(root, width=50, textvariable=self.urlStr)
        self.urlE.place(x=60, y=5)
        # 建立notebook layout
        notebook = Notebook(root, width=8)
        frame1 = Frame()
        frame2 = Frame()
        notebook.add(frame1, text="單檔下載")
        notebook.add(frame2, text="播放清單下載")
        notebook.place(x=5, y=30, width=480, height=150)

        # 建立frame1 的 Layout
        runBtn1 = Button(frame1, width=10, text='下載', command=self.download)
        runBtn1.place(x=360, y=5)
        self.progressbar1 = ttk.Progressbar(frame1, orient="horizontal", length=350, mode="determinate")
        self.progressbar1.place(x=5, y=5)
        self.stateLbl1 = Label(frame1, text="等待下載!", width=49,
                               anchor="w", wraplength="350", justify="left", bg="white")
        self.stateLbl1.place(x=5, y=30)

        # 建立frame2 的 Layout
        runBtn2 = Button(frame2, width=10, text='下載', command=self.palylistget)
        runBtn2.place(x=360, y=5)
        self.progressbar2 = ttk.Progressbar(frame2, orient="horizontal", length=350, mode="determinate")
        self.progressbar2.place(x=5, y=5)
        self.stateLbl2 = Label(frame2, text="等待下載!", width=49,
                               anchor="w", wraplength="350", justify="left", bg="white")
        self.stateLbl2.place(x=5, y=30)

    '''以下是frame1的function'''
    def download(self):
        self.video = YouTube(self.urlStr.get(), on_progress_callback=self.onProgress1)
        print('開始下載音樂，請稍候!')
        self.stateLbl1.config(text=str("開始下載音樂，請稍候!"), bg="white")
        # 建立判斷是確認下載地址是否存在，若不存在則建立資料夾
        if not os.path.isdir('.\\Youtube影片'):
            os.mkdir('.\\Youtube影片')
            # 影片下載至所屬的資料夾
            self.video.streams.filter(only_audio=True).first().download('.\\Youtube音樂')
        else:
            self.video.streams.filter(only_audio=True).first().download('.\\Youtube音樂')
        self.stateLbl1.config(text=str("下載完成, 音樂名稱: " + self.video.title), bg="yellow")
        print('音樂下載開始')
        print("----------------------------------")
        print("下載音樂名稱:" + self.video.title)
        print("下載完成")

    def onProgress1(self, stream, chunk, file_handle, bytes_remaining=0):
        # 以下是Terminal進度條設定
        contentSize = self.video.streams.first().filesize
        process = (contentSize - file_handle) / contentSize * 100
        size = int(process)
        print('\r' + '[Download progress]:[%s%s]%.2f%% ' % (
            '█' * int(size / 100 * 20), ' ' * (20 - int(size / 100 * 20)), size), end='')

        # 以下是GUI進度條設定
        self.progressbar1["value"] = size  # 設定目前所得到的數值
        self.progressbar1["maximum"] = 100  # 設定最大值
        self.progressbar1.update()  # 更新GUI介面

    '''測試用程式碼'''

    # def getV(self):
    # print(self.data.get())
    # print(type(self.data))

    '''以下是frame2的function'''
    def palylistget(self):
        playlist = []
        pl = Playlist(self.urlStr.get())
        links=pl.parse_links()
        for link in links:
            playlist.append(link)
        self.playlistdownload(playlist)

    def playlistdownload(self,items):
        for item in items:
            self.video2=YouTube(item, on_progress_callback=self.onProgress2)    #設定重置?
            print('開始下載音樂，請稍候!')
            self.stateLbl2.config(text=str("開始下載音樂，請稍候!"), bg="white")
            self.stateLbl2.update()
            fileTitle=self.crawlTitle() #抓取播放清單名稱
            if not os.path.isdir('.\\Youtube影片\\'+fileTitle):
                os.mkdir('.\\Youtube影片\\'+fileTitle)
                # 影片下載至所屬的資料夾
                self.video2.streams.filter(only_audio=True).first().download('.\\Youtube音樂\\'+fileTitle)
            else:
                self.video2.streams.filter(only_audio=True).first().download('.\\Youtube音樂\\'+fileTitle)
            self.stateLbl2.config(text=str("下載完成, 播放清單名稱: " + fileTitle), bg="yellow")
            print('音樂下載開始')
            print("----------------------------------")
            print("下載音樂名稱:" + self.video2.title)
            print("下載完成")

    def onProgress2(self, stream, chunk, file_handle, bytes_remaining=0):
        # 以下是Terminal進度條設定
        contentSize = self.video2.streams.first().filesize
        process = (contentSize - file_handle) / contentSize * 100
        size = int(process)
        print('\r' + '[Download progress]:[%s%s]%.2f%% ' % (
            '█' * int(size / 100 * 20), ' ' * (20 - int(size / 100 * 20)), size), end='')

        # 以下是GUI進度條設定
        self.progressbar2["value"] = size  # 設定目前所得到的數值
        self.progressbar2["maximum"] = 100  # 設定最大值
        self.progressbar2.update()  # 更新GUI介面
        self.stateLbl2.config(text=str("下載中, 音樂名稱: " + self.video2.title), bg="yellow")
        self.stateLbl2.update()

        '''以下使抓取標題'''
    def crawlTitle(self):
        request = req.Request(self.urlStr.get(), headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(data, "html.parser")
        title = root.select('title')[1].text
        return title

if __name__ == '__main__':
    root = Tk()
    root.title('Youtube音樂下載App')
    root.geometry("500x150")
    root.resizable(FALSE, FALSE)
    app = App(root)
    root.mainloop()
