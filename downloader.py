import urllib.request
import tkinter
from os.path import splitext
from urllib.parse import urlparse
import time
import os
import _thread
import posixpath
import urllib.parse

def downloadfile(url,name,extension):
    downloadname = name + extension
    info = urllib.request.urlopen(url)
    size = int(info.info()['Content-Length'])
    filesize = size/(1024.0*1024.0)
    popup = tkinter.Tk()
    popup.minsize(200,100)
    okbtn = tkinter.Button(popup, text="OK",command = lambda:downloading(popup,downloadname,filesize,url))
    sizelbl = tkinter.Label(popup, text="Download size: %f MB"%(filesize))
    sizelbl.pack()
    okbtn.pack()


def downloading(popup,filename,filesize,url):

    popup.destroy()

    _thread.start_new_thread(down,(url,filename))
    print ('\n\n\t downloading started\n\n')
    time.sleep(5)
    _thread.start_new_thread(updatestring,(filename,filesize))


def down(url,filename):
    urllib.request.urlretrieve(url,filename)

def updatestring(filename,filesize):

    downloadingrate = r"0% downloaded"
    downloadingframe = tkinter.Tk()

    downloadingframe.wm_title(filename)
    downloadingframe.minsize(250,40)
    while True:
        temp = os.stat(filename)
        tempsize = (temp.st_size/(1024*1024))
        time.sleep(1)
        downloadingrate = str((tempsize/filesize)*100) + r"% out of 100% downloaded"
        lbl = tkinter.Label(downloadingframe, text = downloadingrate)
        lbl.update()
        lbl.pack()
        downloadingframe.update()
        lbl.destroy()
        print (downloadingrate)



    downloadingframe.mainloop()

def autofetcher(url,filetext,exttext):
    path = urlparse(url).path
    ext = splitext(path)[1]
    path = urllib.parse.urlsplit(url).path
    filename = str(posixpath.basename(path))
    if '.' in filename:
        filename = filename.replace('.','_',5)

    deleteext = '_' + ext[1:]


    filetext.delete(0,200)
    exttext.delete(0,200)
    if deleteext in filename:
        filename = filename.replace(deleteext,'')
    filetext.insert(0,filename)
    exttext.insert(0,ext)
