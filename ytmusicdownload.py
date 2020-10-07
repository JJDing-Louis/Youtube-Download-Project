from pytube import YouTube
import os
from tkinter import *
from tkinter import ttk


class App():
    def __init__(self, window):
        # 建立變數
        self.urlStr = StringVar()
        self.data = self.urlStr
        # self.video = YouTube(self.data)

        # 建立window  and Layout
        urlLbl = Label(root, text="網址:", width=8)
        urlLbl.place(x=0, y=5)
        runBtn = Button(root, width=10, text='下載', command=self.download)
        runBtn.place(x=417, y=5)
        self.urlE = Entry(root, width=50, textvariable=self.urlStr)
        self.urlE.place(x=60, y=5)
        self.progressbar = ttk.Progressbar(orient="horizontal", length=350, mode="determinate")
        self.progressbar.place(x=60, y=30)
        self.stateLbl = Label(root, text="等待下載!", width=49,
                              anchor="w", wraplength="350", justify="left",bg="white")
        self.stateLbl.place(x=60, y=60)

    def download(self):
        self.video = YouTube(self.urlStr.get(), on_progress_callback=self.onProgress)
        print('開始下載影片，請稍候!')
        self.stateLbl.config(text=str("開始下載影片，請稍候!"), bg="white")
        # 建立判斷是確認下載地址是否存在，若不存在則建立資料夾

        if not os.path.isdir('.\\Youtube影片'):
            os.mkdir('.\\Youtube影片')
            # 影片下載至所屬的資料夾
            self.video.streams.filter(only_audio = True).first().download('.\\Youtube影片')
        else:
            self.video.streams.filter(only_audio = True).first().download('.\\Youtube影片')
        self.stateLbl.config(text=str("下載完成, 音樂名稱: " + self.video.title), bg="yellow")
        print('音樂下載開始')
        print("----------------------------------")
        print("下載音樂名稱:" + self.video.title)
        print("下載完成")

    def onProgress(self, stream, chunk, file_handle, bytes_remaining=0):
        # 以下是Terminal進度條設定
        contentSize = self.video.streams.first().filesize
        process = (contentSize - file_handle) / contentSize * 100
        size = int(process)
        print('\r' + '[Download progress]:[%s%s]%.2f%% ' % (
            '█' * int(size / 100 * 20), ' ' * (20 - int(size / 100 * 20)), size), end='')

        # 以下是GUI進度條設定
        self.progressbar["value"] = size  # 設定目前所得到的數值
        self.progressbar["maximum"] = 100  # 設定最大值
        self.progressbar.update()  # 更新GUI介面

    '''測試用程式碼'''
    # def getV(self):
    # print(self.data.get())
    # print(type(self.data))


if __name__ == '__main__':
    root = Tk()
    root.title('Youtube音樂下載App')
    root.geometry("500x150")
    root.resizable(FALSE, FALSE)
    app = App(root)
    root.mainloop()
