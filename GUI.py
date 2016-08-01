import tkinter
import downloader

top = tkinter.Tk()

top.wm_title("Buggy downloader")
top.config(background = 'lightyellow')

def downloadbtncmd():
    url = str(urltext.get())
    filename = filetext.get()
    ext = exttext.get()
    downloader.downloadfile(url,filename,ext)




downloadbtn = tkinter.Button(top, text="download",command=downloadbtncmd,bg = "yellow")
fetchurl = tkinter.Button(top, text="fetchurl",command=lambda:urltext.insert(0,urltext.clipboard_get()),bg = 'grey')
fetchdata = tkinter.Button(top,text="fetchdata from URL", command=lambda:downloader.autofetcher(urltext.get(),filetext,exttext),bg = 'grey')
urltext = tkinter.Entry(top,width = 30)
urllbl = tkinter.Label(top, text="URL:")
filetext = tkinter.Entry(top,width = 20)
filelbl = tkinter.Label(top,text="Filename")
extlbl = tkinter.Label(top, text="Extension")
exttext = tkinter.Entry(top,text = 15)



urllbl.pack()
urltext.pack()
fetchurl.pack()
fetchdata.pack()
filelbl.pack()
filetext.pack()
extlbl.pack()
exttext.pack()
downloadbtn.pack()

top.minsize(300,250)

top.mainloop()
