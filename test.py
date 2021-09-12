import math
import random
import calendar
import time
import collections
import matplotlib.pyplot as plt# python3 -m pip install matplotlib
from numpy import i0, right_shift, triu_indices
import numpy as np
from swampy.Gui import *
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from csv import reader
import tkinter as tk
from tkinter import ttk as tktw
import pandas as pd
from tkinter import colorchooser
import os.path
from os import path
import csv
from urllib.request import urlopen
#import time
#import socket

from tkinter import *
# https://realpython.com/python-gui-tkinter/ 
# https://tkdocs.com/tutorial/grid.html 
# https://docs.huihoo.com/tkinter/an-introduction-to-tkinter-1997/intro06.htm
import torch 
class GUIntf:
  def __init__(self):
      self.widthForm=425
      self.heightForm=300
      self.heightTools=30
      self.heightDlg=125
      self.xLeftY=-1
      self.xRightY=-1
      self.widthDlg=1300
      self.heightList=5
      self.showDlg="No"
      self.showForm="Yes"
      self.expandList="expand"
      self.dictExpand={"shrink":15,"expand":5}
      self.nGlobalShift = 0 #indexDailyFromDate(Y + "-" + M + "-" + D)
      self.dict_o={}
      self.dict_h={}
      self.dict_l={}
      self.dict_c={}
      self.dict_v={}
      self.dict_list_of_rows={}
      #self.getData("AAPL")
      self.symbols=['AAPL']#[]
      #self.names=[]
      #self.formulas=[]
      self.dict_name={}
      self.symbolExamples=['AAPL', 'ABT', 'AEP', 'AXP', 'BA', 'BK', 'BMY', 'C', 'CI', 'CL', 'CLX', 'CRM', 'CSCO', 'CVX', 'DD', 'DIS', 'ED', 'F', 'GE', 'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MCK', 'MCO', 'MET', 'MMM', 'MO', 'MRK', 'MS', 'MSFT', 'MSI', 'NEE', 'NKE', 'NTRS', 'OMC', 'OXY', 'PCAR', 'PEG', 'PEP', 'PFE', 'PG', 'SEE', 'SO', 'TGT', 'TRV', 'TXT', 'UNH', 'UNP', 'V', 'VZ', 'WBA', 'WFC', 'WMB', 'XOM']
      self.visibility=["Yes","No"]
      self.pane=['1','2','3','4','5','6','7','8','9']
      self.yaxis=["Right","None","Left"]
      self.type=["Line","Bar", "Hstgm", "Edge"]
      self.width=['1','2','3','4','5','6','7','8','9']
      self.style=["Solid","Dot","Dash"]
      self.legend=["Short","Long","None"]
      self.symbolPresentation=[['Yes', '1', 'Right', 'Line', '1', 'Solid', 'Short', 'blue']]#[]
      self.formulaPresentation=[]
      self.curSelSymb=-1
      self.nGlobalShift = 0 #indexDailyFromDate(Y + "-" + M + "-" + D)
      self.selectedSymbol=-1
      self.selectedFormula=-1
      self.comboInd=-1
      self.xHeight=18
      self.gap=2
      self.yMargin=3
      self.xMargin=3
      self.widthY=60
      self.paneWeights=[]
      self.unzoomList=[[self.indexDailyFromDate(2009,3,23),self.indexDailyFromDate(2009,5,10)]]#[]
      self.dictCoordsLegS={} #coords: idx
      self.dictCoordsLeg={} #coords: idx
      self.leftInd=-1
      self.rightInd=-1
      self.traceOn=0
      self.traceInd=-1
      self.yCursor=-1
      self.xCursor=-1
      self.listMsg=[]
      self.paneLeft=-1
      self.paneRight=-1
      self.unzoomOn=-1
      self.down=0
      self.downX=-1
      self.downY=-1
      self.upX=-1
      self.sumadxady=0
      self.idToDelete=-1
      self.pairToDelete=[-1,Listbox(window)]
      self.listToDelete=[]
      self.liliLeg=[[]]
      self.listFormulas=[]#[["SMA","sma(c)"],["R","ref(c,-10)"]]
      self.prevListFormulas=[]
      self.formulaExamples=["c","open","h","low","v","volume"]
      self.dictSv2i={}
      self.error=""
      self.keyToMove=""
      self.dPane=0
      self.dictLegs={}
      #self.wrongFormula=-1
      self.lstBadNames=[]
      self.lstBadSymbols=[]
  def changeListMsg(self):
    dateCursor=G.dateDailyFromIndex(G.traceInd,"/")
    self.listMsg=[dateCursor]
    for symb in self.symbols:
      c=self.dict_c[symb]
      if G.traceInd-c[0]+1>=0 and G.traceInd-c[0]+1<len(c):
        line=symb+":"+str(c[G.traceInd-c[0]+1])
        self.listMsg.append(line) 
    for key in self.dict_name:
      ser=self.dict_name[key]
      if len(ser)==1:
        line=key+":"+str(ser[0])
        self.listMsg.append(line)
      else:
        if G.traceInd-ser[0]+1>=0 and G.traceInd-ser[0]+1<len(ser):
          line=key+":"+str(ser[G.traceInd-c[0]+1])
          self.listMsg.append(line) 
  def indexDailyFromDate(self,year,month,day):#sYmd
    cum = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    j = day - 1 #	 // jan 1
    if month > 1: j += cum[month - 2]
    if year % 4 == 0 and month > 2: j += 1
    y4 = math.floor((year - 1901) / 4)
    j += 1461 * y4
    for i in range(1901 + 4 * y4, year):
        j += 365;
        if i % 4 == 0: j += 1;
    return -1 + 5 * math.floor((j + 1) / 7) + (j + 1) % 7 - self.nGlobalShift
  def dateDailyFromIndex(self, nIndex,sep):
    nIndex = nIndex + self.nGlobalShift #3/17/2017
    if nIndex==None: return "0"   #if (nIndex == undefined || isNaN(nIndex) ) return "0";
    col = nIndex;
    j = -1 + 7 * math.floor((col + 1) / 5) + (col + 1) % 5
    i = 1900;
    i = 1900 + 4 * math.floor(j / 1461);
    j = j % 1461 + 1  #	// 1 jan
    while j > 0:
        i+=1
        j -= 365
        if (i % 4 == 0): j -= 1
    j += 365
    if i % 4 == 0: j += 1;
    days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];
    if i % 4 == 0: days[1] = 29;
    else: days[1] = 28;
    m = -1;
    while True:
        m+=1;
        j -= days[m];
        if j <= 0:
            j += days[m];
            break;
    year = i;
    m1 = m + 1;
    if sep=="-":
      if m1 < 10: m1 = "0" + str(m1);
      if j < 10: j = "0" + str(j);
      return str(year)+"-"+str(m1)+ "-" + str(j);
    else:
      return str(m1)+"/"+str(j)+"/"+str(year)
  def transformFile(self, oldPath, newPath):
    df=pd.read_csv(oldPath)# "DOW//IBM.csv"
    df1 = df[['Date', 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
    d={'Adj. Open':'Open','Adj. High':'High','Adj. Low':'Low','Adj. Close':'Close','Adj. Volume':'Volume'}
    df1=df1.rename(columns = d, inplace = False)
    lines=[]
    nTomorrow=0
    for row in df1.iterrows():
      o = "{:.2f}".format(row['Open'])
      h = "{:.2f}".format(row['High'])
      l = "{:.2f}".format(row['Low'])
      c = "{:.2f}".format(row['Close'])
      v = str(int(row['Volume']))
      date=row['Date']
      year=0
      month=0
      day=0
      sep='/'
      if not date[4]=="-":
        lst=date.split('/')
        month=int(lst[0])
        day=int(lst[1])
        year=int(lst[2])
      else:
        sep="-"
        year=int(date[0:4])
        month=int(date[5:7])
        day=int(date[8:])
      nToday= G.indexDailyFromDate(year,month,day)
      s1=str(row['Date'])+","+o+","+h+","+l+","+c+","+v+"\n"
      dif=nTomorrow-nToday
      if not dif<=1:
        for i in range(dif-1):
          date=G.dateDailyFromIndex(nToday+dif-i-1,sep)
          s=date+","+c+","+c+","+c+","+c+","+"0\n"
          lines.append(s)
      lines.append(s1)  
      nTomorrow=nToday

    with open(newPath,"w") as fn:# "DOW//IBM.csv"
      fn.write("date, open, high, low,  close,  volume\n")
      for l in lines:
        fn.write(l)   
  
  def parseData(self,symb,list_of_rows):
    self.dict_list_of_rows[symb]=list_of_rows
    o=[]
    h=[]
    l=[]
    c=[]
    v=[]
    lst=list_of_rows[1:][::-1]
    flag=0
    for dohlcv in lst:       
      if flag==0:
        date=dohlcv[0]
        ymd=date.split("/")#3/19/2018
        index=0
        if len(ymd)==3:
          index=self.indexDailyFromDate(int(ymd[2]),int(ymd[0]),int(ymd[1]))
        else:
          ymd=date.split("-")#2017-07-17,
          index=self.indexDailyFromDate(int(ymd[0]),int(ymd[1]),int(ymd[2]))
        date=self.dateDailyFromIndex(index,"/")
        o.append(index)
        h.append(index)
        l.append(index)
        c.append(index)
        v.append(index)
        flag=1
      o.append(float(dohlcv[1]))
      h.append(float(dohlcv[2]))
      l.append(float(dohlcv[3]))
      c.append(float(dohlcv[4]))
      v.append(float(dohlcv[5]))
    self.dict_o[symb]=o
    self.dict_h[symb]=h
    self.dict_l[symb]=l
    self.dict_c[symb]=c
    self.dict_v[symb]=v
    """
    ['date', 'open', 'high', 'low', 'close', 'volume']
    ['3/27/2018', '331.51', '334.88', '319.00', '321.12', '5296793']
    ['1/2/1962', '0.89', '0.89', '0.87', '0.87', '352198']
    """
  def howManyPanes(self):
    n=1
    for pres in self.symbolPresentation:
      k=int(pres[1])
      if n<k: n=k
    for pres in self.formulaPresentation:
      k=int(pres[1])
      if n<k: n=k
    return n
  def hasLeftY(self):
    for pres in self.symbolPresentation:
      if pres[2]=="Left":
        return 1
    for pres in self.formulaPresentation:
      if pres[2]=="Left":
        return 1
    return 0
  def hasRightY(self):
    for pres in self.symbolPresentation:
      if pres[2]=="Right":
        return 1
    for pres in self.formulaPresentation:
      if pres[2]=="Right":
        return 1
    return 0
  def getData(self, symb):
    list_of_rows=[]
    if symb=="": print("get empty")
    print("symb=",symb)
    #print(self.symbolExample)
    #if not symb.upper() in self.symbolExamples: return []
    if symb=="": return []
    list_of_rows.append("Date, Open, High, Low, Close, Volume")
    df = pd.DataFrame()
    oldPath="DOw/"+symb+".csv"
    newPath="DATA/"+symb+".csv"
    if not path.exists(oldPath): 
      if not symb=="":
        url = "https://www.quandl.com/api/v3/datasets/WIKI/"+ symb +".csv"
        try:
          df=pd.read_csv(url, index_col=None)
          for index, row in df.iterrows():
            s=row["Date"]+","+str(row["Adj. Open"])+","+str(row["Adj. High"])+","+str(row["Adj. Low"])+","+str(row["Adj. Close"])+","+str(row["Adj. Volume"])
            list_of_rows.append(s)
        except:
          list_of_rows.append("No Data")
      else: return[]
    else:
      if not path.exists(newPath):
        f=open(newPath,"x")
        self.transformFile(oldPath,newPath)
        f.close()
      with open(newPath,'r') as read_obj:
          csv_reader = reader(read_obj)
          list_of_rows = list(csv_reader)
          if not symb in self.dict_list_of_rows.keys():
            self.parseData(symb,list_of_rows)
    return list_of_rows
  def setLRMM(self):
      #Left, Rigth
      leftInd=0
      rightInd=1
      if len(self.symbols)==0:
        leftInd=0
        rightInd=1
      elif len(self.unzoomList)==0:
        symb=self.symbols[0]
        leftInd=self.dict_c[symb][0]
        rightInd=leftInd
        for i in range(len(self.symbolPresentation)):
          if self.symbolPresentation[i][0]=="No": continue#invisible
          symb=self.symbols[i]
          symb=symb.strip()
          if symb=="":continue # empty
          start=int(self.dict_c[symb][0])
          length=len(self.dict_c[symb])
          end=int(start+length-2)
          if leftInd>start: leftInd=start
          if rightInd<end: rightInd=end
        for i in range(len(self.formulaPresentation)):
          """
           if i== self.wrongFormula: 
            self.showDlg="Error"
            continue         
          """
          name=self.listFormulas[i][0]
          if name in self.lstBadNames: continue
          if self.formulaPresentation[i][0]=="No": continue#invisible
          name=self.listFormulas[i][0]
          name=name.strip()
          if name=="":continue # empty
          ser=G.dict_name[name]
          if len(ser)>1:
            start=ser[0]
            length=len(ser)
            end=int(start+length-2)
            if leftInd>start: leftInd=start
            if rightInd<end: rightInd=end
      else:
        if len(self.unzoomList)>0 and len(self.unzoomList[0])>0 and len(self.unzoomList[-1])>0:
          leftInd=self.unzoomList[-1][0]
          rightInd=self.unzoomList[-1][1]
      self.leftInd=leftInd
      self.rightInd=rightInd 
      #List leftYMax,rightYMax,leftYMin,rightYMin
      n=self.howManyPanes()
      listLeftYMin=[float("inf")]*n
      listRightYMin=[float("inf")]*n
      listLeftYMax=[float("-inf")]*n
      listRightYMax=[float("-inf")]*n
      #print("len(listRightYMax)=",len(listRightYMax))
      for idx,pres in enumerate(self.symbolPresentation):
        """
        if idx== self.wrongFormula: 
          self.showDlg="Error"
          continue        
        """
        if self.symbols[idx] in self.lstBadNames: continue
        if pres[0]=="No": continue#invisible
        symb=self.symbols[idx]
        symb=symb.strip()
        if symb=="":continue # empty
        pane=int(pres[1])
        yaxis=pres[2]
        c=self.dict_c[symb] 
        i1=self.leftInd-c[0]+1
        i2=self.rightInd-c[0]+2  
        if i1<0 and i2<0: continue        
        if i1<0: i1=1
        if i2> len(c) -1: i2=len(c) -1  
        if pres[3] =="Hstgm" or pres[3]=="Edge":
          yMax=np.max(c[i1:i2])
          yMin=0
        elif pres[3]=="Bar":
          h=self.dict_h[symb]
          yMax=np.max(h[i1:i2])
          l=self.dict_l[symb]
          yMin=np.min(l[i1:i2])
        else:#Line
          c=self.dict_c[symb]
          yMin=np.min(c[i1:i2])  
          yMax=np.max(c[i1:i2])
          #print("yMax=",yMax)
        if yMax>listLeftYMax[pane-1] and  yaxis=="Left":listLeftYMax[pane-1]=yMax
        if yMax>listRightYMax[pane-1] and  yaxis=="Right":listRightYMax[pane-1]=yMax
        if yMin<listLeftYMin[pane-1] and  yaxis=="Left":listLeftYMin[pane-1]=yMin
        if yMin<listRightYMin[pane-1] and  yaxis=="Right":listRightYMin[pane-1]=yMin
      for i in range(len(self.formulaPresentation)):
        """
        if i== self.wrongFormula: 
          self.showDlg="Error"
          continue        
        """
        name=self.listFormulas[i][0]
        if name in self.lstBadNames: continue
        pres=self.formulaPresentation[i]
        if pres[0]=="No": continue#invisible
        pane=int(pres[1])
        yaxis=pres[2]
        name=self.listFormulas[i][0]
        name=name.strip()
        if name=="" or not self.error=="":continue # empty
        print("len(self.dict_name)=",len(self.dict_name))
        c=self.dict_name[name] 
        i1=self.leftInd-c[0]+1
        i2=self.rightInd-c[0]+2 
        if i1<0 and i2<0: continue         
        if i1<0: i1=1
        if i2> len(c) -1: i2=len(c) -1 
        yMax=c[0]
        yMin=c[0]
        if len(c)>1:
          yMax=np.max(c[i1:i2])
          if pres[3] =="Hstgm" or pres[3]=="Edge":yMin=0
          else:  yMin=np.min(c[i1:i2])
        if yMax>listLeftYMax[pane-1] and  yaxis=="Left":listLeftYMax[pane-1]=yMax
        if yMax>listRightYMax[pane-1] and  yaxis=="Right":listRightYMax[pane-1]=yMax
        if yMin<listLeftYMin[pane-1] and  yaxis=="Left":listLeftYMin[pane-1]=yMin
        if yMin<listRightYMin[pane-1] and  yaxis=="Right":listRightYMin[pane-1]=yMin

      self.listLeftYMax=listLeftYMax
      self.listRightYMax=listRightYMax
      self.listLeftYMin=listLeftYMin
      self.listRightYMin=listRightYMin
      #print("listRightYMax=",listRightYMax,"listRightYMin=",listRightYMin)
  def replace(self,oldSymb,symb):
    oldInd=self.symbols.index(oldSymb)
    ind=self.symbols.index(symb)
  def findLiliLeg(self):     
    n=self.howManyPanes()
    #print("n=",n)
    self.liliLeg=[[] for x in range(n)]
    #print("self.liliLeg=",self.liliLeg,"self.symbolPresentation=",self.symbolPresentation)
    for idx,pres in enumerate(self.symbolPresentation):
      #print("G:",idx,pres)
      symb=self.symbols[idx]
      pane=int(pres[1])
      #print(self.liliLeg[pane-1])
      self.liliLeg[pane-1].append(symb)
      #print(self.liliLeg[0])
    return self.liliLeg
  def makeList(self,c):
    #print("in makeList: len(self.dict_name=",len(self.dict_name))
    L=["date______value"]
    if len(c)==1:
      return [c[0]]
    for i in range(len(c)-1):
      L.append([self.dateDailyFromIndex(c[0]+i,"-"),c[i]])
    return L
  def calculate(self,f):
    if f.isnumeric(): return [float(f)]
    else:
      if f=="c":return self.dict_c[self.symbols[0]]
      if f=="h":return self.dict_h[self.symbols[0]]
      if f=="c1":return self.dict_c[self.symbols[1]]
      if f=="h1":return self.dict_h[self.symbols[1]]
      if f=='':return "empty"
      return "error"
  def sameFormulas(self):
    b=True
    n=len(self.listFormulas)
    if not n==len(self.prevListFormulas): return False
    for i in range(n):
      if not self.listFormulas[i]==self.prevListFormulas[i]: return False
    return triu_indices
  def calc(self):
    self.dict_name.clear()
    self.lstBadNames.clear()
    self.lstBadSymbols.clear()
    self.showDlg="No"
    self.error=""
    for i,p in enumerate(self.listFormulas):
      ser=self.calculate(p[1])
      if ser=="error": 
        if not p[0] in self.lstBadNames: 
          self.lstBadNames.append(p[0])
          #del self.dict_name[p[0]]
        self.error="Error in the formula "+p[0]
        return "Error in the formula "+p[0]
      else:
        self.dict_name[p[0]]=ser
    return ""
  def clearErrors(self):
    self.lstBadNames=[]
    self.lstBadSymbols=[]
    self.error=""
    self.dict_name.clear()
  
    
def out():
  star1(window)
  #print("out") 

def draw(cnv,w,h,G,fr_dlg,fr_tools,fr_form, fr_graph):
  G.error=""
  #print("in draw: len G.listFormulas=",G.listFormulas,"G.formulaPresentation=",G.formulaPresentation,"len(G.dict_name)=",len(G.dict_name))
  def motion(event): 

    if G.traceOn:
      cnv.delete(G.listToDelete[0])
      cnv.delete(G.listToDelete[1])
      cnv.delete(G.listToDelete[2])       
      if G.upX<=0:
        G.upX=event.x      
      else:
        cnv.delete(G.listToDelete[0])
        cnv.delete(G.listToDelete[1])
        cnv.delete(G.listToDelete[2]) 
        x=event.x
        G.yCursor=event.y    
        G.traceInd=math.floor((x-xLeftY)*(G.rightInd-G.leftInd)/(G.xRightY-G.xLeftY))+G.leftInd
        if G.traceInd<G.leftInd:G.traceInd=G.leftInd
        if G.traceInd>G.rightInd:G.traceInd=G.rightInd
        G.changeListMsg()   

        id1=cnv.create_line(x,0,x,h-G.xHeight)
        s=""
        longest=G.listMsg[0]
        for line in G.listMsg:
          if len(longest)<len(G.listMsg):longest=line 
          s+=line+"\n"
        width=len(longest)*10
        if x>(G.xRightY+G.xLeftY):x-=width
        hh=G.xHeight*(len(G.listMsg)+0.5)
        id3=cnv.create_rectangle(x, G.yCursor-hh, x+width, G.yCursor, fill='white')
        id2=cnv.create_text(0,0,text=s,font="Times 12 ")
        move_item(cnv,id2,x,G.yCursor-hh,0,0)
        G.listToDelete=[id1,id2,id3]    

    if G.downX==-1:
      G.downX=event.x
      G.downY=event.y
    for key, value in G.dictCoordsLeg.items():
      if event.x>value[0] and event.x<value[2]+value[0] and event.y>value[1] and event.y<value[3]:
        G.keyToMove=key
        break
    if G.keyToMove=="":
      if G.traceOn==1:
        pass
      else:  
        x1=G.downX
        x2=xLeftY
        x2=event.x
        
        if x2>xRightY: x2=xRightY
        if x2<xLeftY: x2=xLeftY
        if x1>x2:
          x1,x2=x2,x1    
                       
        if G.upX<=0: 
          G.upX=event.x
          cnv.delete(G.pairToDelete[0])
          G.pairToDelete[1].place_forget()     
          G.downX=x2
          G.downY=event.y
          G.unzoomList.append([])
          cnv.create_line(x2,0,x2,h-G.xHeight, fill="red")
        else:
          cnv.delete(G.idToDelete)
          G.idToDelete=cnv.create_line(event.x,0,event.x,h-G.xHeight, fill="red")  
          lInd=math.floor(G.leftInd+(G.rightInd-G.leftInd)*(x1-G.paneLeft)/(G.paneRight-G.paneLeft))
          rInd=math.ceil(G.leftInd+(G.rightInd-G.leftInd)*(x2-G.paneLeft)/(G.paneRight-G.paneLeft))
          G.unzoomList[-1]=[lInd,rInd]      
    else:
      cnv.delete(G.idToDelete)
      G.idToDelete=cnv.create_text(event.x,event.y,text=G.keyToMove,font="Times 12 ")
      dx=event.x-G.downX
      dy=event.y-G.downY    
      adx=abs(dx)
      ady=abs(dy)
      G.sumadxady=adx+ady
      ids=-1
      idf=-1
      if G.keyToMove in G.symbols:ids=G.symbols.index(G.keyToMove)
      else:
        for i in range(len(G.listFormulas)):
          if G.keyToMove==G.listFormulas[i][0]:
            idf=i
            break   
      if ady<adx:
        G.dPane=0
        if dx>0:
          if G.keyToMove in G.symbols: 
            G.symbolPresentation[ids][2]="Right"
          else: 
            G.formulaPresentation[idf][2]="Right"
        else:
          if G.keyToMove in G.symbols:
            G.symbolPresentation[ids][2]="Left"
          else: 
            G.formulaPresentation[idf][2]="Left"
      else:#ady>adx
        if dy>0:
          G.dPane=1
        if dy<=0:
          G.dPane=-1
    
  cnv.bind("<B1-Motion>", motion)
  def move_item(cnv,item, x,y,dx,dy):
    coords=cnv.bbox(item)
    cnv.move(item,x+(coords[2]-coords[0])*(0.5+dx),y+(coords[3]-coords[1])*(0.5+dy))   
    return coords 
  def callback(event):
    G.downX=-1
    G.upX=-1
    #print("G.keyToMove=",G.keyToMove)
    keyToMove=""
    for key, value in G.dictCoordsLeg.items():
      if event.x>value[0] and event.x<value[2]+value[0] and event.y>value[1] and event.y<value[3]:
        keyToMove=key
        break
    #print("keyToMove=",keyToMove)

    
    if G.keyToMove in G.symbols:
      idx=G.symbols.index(G.keyToMove)
      pane=int(G.symbolPresentation[idx][1])+G.dPane
      if pane<1: pane=1
      G.symbolPresentation[idx][1] =str(pane)
    elif not G.keyToMove=="": 
      for i in range(len(G.listFormulas)):
        if G.listFormulas[i][0]==G.keyToMove:
          pane=int(G.formulaPresentation[i][1])+G.dPane
          if pane<1: pane=1
          G.formulaPresentation[i][1] =str(pane)
          break
    G.keyToMove="" 
    
    G.dPane=0
    if G.traceOn==0:
      #print("G.keyToMove=",G.keyToMove, "keyToMove=",keyToMove)
      if G.keyToMove=="" and not keyToMove=="" and G.sumadxady==0:
        if keyToMove in G.symbols:  
          G.showDlg="Edit Symbol"   
          G.selectedSymbol=G.symbols.index(keyToMove)
        else:
          G.showDlg="Edit Formula"   
          for i in range(len(G.listFormulas)):
            if G.listFormulas[i][0]==G.keyToMove:
              G.selectedFormula=i
              break
     
    
    else:
      x=event.x
      y=event.y
      G.xCursor=x
      G.yCursor=y
      G.traceInd=math.floor(G.leftInd+(G.rightInd-G.leftInd)*(x-G.paneLeft)/(G.paneRight-G.paneLeft))         
      G.changeListMsg()
    G.sumadxady=0
    fr_dlg.pack_forget()
    fr_tools.pack_forget()
    fr_form.pack_forget()
    fr_graph.pack_forget()    
    out()
  cnv.bind("<ButtonRelease-1>", callback)#    
  #print("DRAW")

  #print(G.unzoomList,G.leftInd,G.rightInd)
  cnv.delete("all") 
  nPanes=G.howManyPanes()
  cnv.create_rectangle(0,0,w,h-G.xHeight, fill="white smoke")

  # Draw x-Axis
  yXaxis=h-G.xHeight
  bLeftY=G.hasLeftY()
  bRightY=G.hasRightY()
  xLeftY=0
  xRightY=w
  if bLeftY==True: xLeftY=G.widthY
  if bRightY==True: xRightY=w-G.widthY
  G.xLeftY=xLeftY
  G.xRightY=xRightY
  G.setLRMM()##########
  leftInd=G.leftInd
  rightInd=G.rightInd
  start=G.dateDailyFromIndex(leftInd,"/")
  item=cnv.create_text(0,0,text=start,font="Times 12 ")
  move_item(cnv,item,xLeftY,yXaxis,0,0)#xLeftY
  end=G.dateDailyFromIndex(rightInd,"/")
  item=cnv.create_text(0,0,text=end,font="Times 12 ")
  move_item(cnv,item, xRightY,yXaxis,-1,0)

  # Draw Panes 
  if not nPanes==G.paneWeights:
    G.paneWeights=[]
    for n in range(nPanes): G.paneWeights.append(1/nPanes)
  paneTops=[0]
  for n in range(1,nPanes):
    paneTops.append(paneTops[n-1]+yXaxis*G.paneWeights[n-1])
  paneTops.append(yXaxis)
  paneLeft=bLeftY*xLeftY
  paneRight=w-bRightY*G.widthY
  G.paneLeft=paneLeft
  G.paneRight=paneRight
  for n in range(nPanes):  
    hPane=paneTops[n+1]-paneTops[n]
    if bLeftY==1:
      cnv.create_rectangle(0,paneTops[n],xLeftY,paneTops[n+1], fill="white smoke") 
    if bRightY==1:
      cnv.create_rectangle(w-G.widthY,paneTops[n],w,paneTops[n+1], fill="white smoke")     
    cnv.create_rectangle(paneLeft,paneTops[n],paneRight,paneTops[n+1], fill="white smoke")
  
  #put yMax and yMin
  for n in range(nPanes):
    leftMax=G.listLeftYMax[n]
    if not abs(leftMax)==float("inf"):
      leftMax=cnv.create_text(0,0,text=str(leftMax),font="Times 12 ")
      move_item(cnv,leftMax, xLeftY,paneTops[n],-1,1)
    leftMin=G.listLeftYMin[n]
    if not abs(leftMax)==float("inf"):
      leftMin=cnv.create_text(0,0,text=str(leftMin),font="Times 12 ")
      move_item(cnv,leftMin, xLeftY,paneTops[n+1],-1,-1)
    rightMax=G.listRightYMax[n]
    if not abs(rightMax)==float("inf"):
      rightMax=cnv.create_text(0,0,text=str(rightMax),font="Times 12 ")
      move_item(cnv,rightMax, xRightY,paneTops[n],0,1)
    rightMin=G.listRightYMin[n]
    if not abs(rightMax)==float("inf"):
      rightMin=cnv.create_text(0,0,text=str(rightMin),font="Times 12 ")
      move_item(cnv,rightMin, xRightY,paneTops[n+1],0,-1)

  #graphs
  G.listXLegend=[xLeftY]*nPanes
  for idx,pres in enumerate(G.symbolPresentation):
    if pres[0]=="No": continue# invisible
    symb=G.symbols[idx]
    symb=symb.strip()
    if symb=="":continue # empty
    pane=int(pres[1])
    yaxis=pres[2]
    type=pres[3]
    width=pres[4]
    style=pres[5]
    legend=pres[6]
    color=pres[7]    
    #put legend
    start=int(G.dict_c[symb][0])
    length=len(G.dict_c[symb])
    end=int(start+length-2)
    if start<leftInd and end<leftInd: continue    
    c=G.dict_c[symb]   
    if start<leftInd:start=leftInd
    if end>rightInd:end=rightInd
    #legends
    leg=symb
    if yaxis=="Left":leg='<'+symb
    if yaxis=="Right": leg='>'+symb
    if legend=="None":leg=""
    if legend=="Long":leg+=" "+str(c[end-c[0]+1])
    leg=cnv.create_text(0,0,text=leg,font="Times 12 ",fill=color)
    G.dictLegs[symb]=leg
    coords=move_item(cnv,leg, G.listXLegend[pane-1],paneTops[pane-1],0,0)
    G.dictCoordsLeg[symb]=(G.listXLegend[pane-1],paneTops[pane-1],coords[2]-coords[0],paneTops[pane-1]+coords[3]-coords[1])
    G.listXLegend[pane-1]+=coords[2]-coords[0]+5
    minY=G.listLeftYMin[pane-1]
    if yaxis=="Right":minY=G.listRightYMin[pane-1]
    maxY=G.listLeftYMax[pane-1]
    if yaxis=="Right":maxY=G.listRightYMax[pane-1]
    paneTop=paneTops[pane-1]
    paneTopForMax= paneTop+G.xHeight+G.gap
    paneBottom=paneTops[pane]
    paneBottomForMin=paneBottom-G.gap
    points=[] 
    d=0.5*(paneRight-paneLeft)/(rightInd-leftInd)
    dd=0
    widthX=paneRight-dd-paneLeft
    xprev=-1
    if type=="Bar" and widthX<rightInd-leftInd:type="Line"
    if type=="Line":
      for i in range(start,end+1):
        x=paneLeft+(i-leftInd)*widthX/(rightInd-leftInd)
        if int(x)==int(xprev): continue
        xprev=x
        points.append(x)
        y=(paneTopForMax+paneBottomForMin)/2
        #print(minY,maxY)
        if yaxis=="None":
          minY=np.min(c[start-c[0]+1:end-c[0]+1])
          maxY=np.max(c[start-c[0]+1:end-c[0]+1])
        if not maxY==minY: y=paneBottomForMin+(c[i-c[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
        points.append(y)
      if len(points)==0: continue
      i=len(points)-4
      while i>=0:
        points.append(points[i])
        points.append(points[i+1])
        i-=2
      #print("len(points)=",len(points))
      if style=="Solid": cnv.create_polygon(points,outline=color,width=width)
      elif style=="Dash":  cnv.create_polygon(points,outline=color,width=width, dash=(6,4))
      else: cnv.create_polygon(points,outline=color,width=width, dash=(2,4))
    elif type=="Hstgm":
      for i in range(start,end+1):
        x=paneLeft+(i-leftInd)*(paneRight-paneLeft)/(rightInd-leftInd)
        if int(x)==int(xprev): continue
        xprev=x
        points.append(x)
        c=G.dict_c[symb]
        if yaxis=="None":
          minY=0
          maxY=np.max(c[start-c[0]+1:end-c[0]+1])
        yc=(paneTopForMax+paneBottomForMin)/2
        if not maxY==minY: yc=paneBottomForMin+(c[i-c[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
        if style=="Solid": cnv.create_line(x, yc, x, paneBottomForMin, fill=color,width=width)
        elif style=="Dash":  cnv.create_line(x, yc, x, paneBottomForMin, fill=color,width=width, dash=(6,4))
        else: cnv.create_line(x, yc, x, paneBottomForMin, fill=color,width=width,dash=(2,4))
    elif type=="Bar":#"Bar"
      for i in range(start,end+1):
        x=paneLeft+(i-leftInd)*(paneRight-paneLeft)/(rightInd-leftInd)
        points.append(x)
        hh=G.dict_h[symb]
        l=G.dict_l[symb]
        c=G.dict_c[symb]
        if yaxis=="None":
          minY=np.min(l[start-c[0]+1:end-c[0]+1])
          maxY=np.max(hh[start-c[0]+1:end-c[0]+1])
        yh=(paneTopForMax+paneBottomForMin)/2
        yl=(paneTopForMax+paneBottomForMin)/2
        yc=(paneTopForMax+paneBottomForMin)/2
        if not maxY==minY: 
          yh=paneBottomForMin+(hh[i-hh[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
          yl=paneBottomForMin+(l[i-l[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
          yc=paneBottomForMin+(c[i-c[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
        if style=="Solid": 
          cnv.create_line(x, yh, x, yl, fill=color,width=width)
          cnv.create_line(x, yc, x+d, yc, fill=color,width=width)
        elif style=="Dash":  
          cnv.create_line(x, yh, x, yl, fill=color,width=width, dash=(6, 4))
          cnv.create_line(x, yc, x+d, yc, fill=color,width=width, dash=(6, 4))
        else: #cnv.create_line(x, yc, x, paneBottomForMin, fill=color,width=width,dash=(2,4))
          cnv.create_line(x, yh, x, yl, fill=color,width=width, dash=(2, 4))
          cnv.create_line(x, yc, x+d, yc, fill=color,width=width, dash=(2, 4))
    else:#Edge
      for i in range(start,end+1):
        x=paneLeft+(i-leftInd)*(paneRight-paneLeft)/(rightInd-leftInd)
        if int(x)==int(xprev): continue
        xprev=x
        points.append(x)
        c=G.dict_c[symb]
        if yaxis=="None":
          minY=0
          maxY=np.max(c[start-c[0]+1:end-c[0]+1])
        y=(paneTopForMax+paneBottomForMin)/2
        if not maxY==minY: y=paneBottomForMin+(c[i-c[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
        points.append(y)
      n=len(points)
      points.append(points[n-2])
      points.append(paneBottomForMin)
      points.append(points[0])
      points.append(paneBottomForMin)
      points.append(points[0])
      points.append(points[1])
      #cnv.create_polygon(points,outline=color,width=width,fill=color)
      if style=="Solid": cnv.create_polygon(points,outline=color,width=width,fill=color)
      elif style=="Dash":  cnv.create_polygon(points,outline=color,width=width,fill=color, dash=(6,4))
      else: cnv.create_polygon(points,outline=color,width=width,fill=color, dash=(2,4))
  #trace
  for idx,pres in enumerate(G.formulaPresentation):
    """
    print('G.wrongFormula=',G.wrongFormula,idx,G.listFormulas[idx])
    if idx== G.wrongFormula: 
      G.showDlg="Error"
      continue    
    """
    name=G.listFormulas[idx][0]
    if name in G.lstBadNames: continue
    if pres[0]=="No": continue# invisible
    name=name.strip()
    if name=="":continue # empty
    pane=int(pres[1])
    yaxis=pres[2]
    type=pres[3]
    width=pres[4]
    style=pres[5]
    legend=pres[6]
    color=pres[7]    
    #put legend
    #print("name=",name,"G.wrongFormula=",G.wrongFormula)
    start=int(G.dict_name[name][0])
    length=len(G.dict_name[name])
    end=int(start+length-2)
    c=G.dict_name[name]    
    if start<leftInd and end<leftInd and not len(c)==1: continue    
    if start<leftInd:start=leftInd
    if end>rightInd:end=rightInd
    #legends
    legN=name
    if yaxis=="Left":legN='<'+name
    if yaxis=="Right": legN='>'+name
    if legend=="None":legN=""
    if legend=="Long":legN+=" "+str(c[end-c[0]+1])
    legN=cnv.create_text(0,0,text=legN,font="Times 12 ",fill=color)
    G.dictLegs[name]=legN
    coords=move_item(cnv,legN, G.listXLegend[pane-1],paneTops[pane-1],0,0)
    G.dictCoordsLeg[name]=(G.listXLegend[pane-1],paneTops[pane-1],coords[2]-coords[0],paneTops[pane-1]+coords[3]-coords[1])
    G.listXLegend[pane-1]+=coords[2]-coords[0]+5
    minY=G.listLeftYMin[pane-1]
    if yaxis=="Right":minY=G.listRightYMin[pane-1]
    maxY=G.listLeftYMax[pane-1]
    if yaxis=="Right":maxY=G.listRightYMax[pane-1]
    paneTop=paneTops[pane-1]
    paneTopForMax= paneTop+G.xHeight+G.gap
    paneBottom=paneTops[pane]
    paneBottomForMin=paneBottom-G.gap
    points=[] 
    d=0.5*(paneRight-paneLeft)/(rightInd-leftInd)
    dd=0
    widthX=paneRight-dd-paneLeft
    xprev=-1
    if len(c)==1:
      if yaxis=="Left":
        minY= G.listLeftYMin[pane-1]
        maxY=G.listLeftYMax[pane-1]
      if yaxis=="Right":
        minY= G.listRightYMin[pane-1]
        maxY=G.listRightYMax[pane-1]
      if minY==maxY: 
        y=(paneTopForMax+paneBottomForMin)/2
      else:          
        y=paneBottomForMin+(c[0]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
      if style=="Solid": cnv.create_line(paneLeft,y,paneRight,y, fill=color,width=width)
      elif style=="Dash":  cnv.create_line(paneLeft,y,paneRight,y, fill=color,width=width, dash=(6,4))
      else: cnv.create_line(paneLeft,y,paneRight,y, fill=color,width=width,dash=(2,4))
    else:
      #print("LOST PATR")
      if type=="Bar" and widthX<rightInd-leftInd:type="Line"
      if type=="Line":
        for i in range(start,end+1):
          x=paneLeft+(i-leftInd)*widthX/(rightInd-leftInd)
          if int(x)==int(xprev): continue
          xprev=x
          points.append(x)
          y=(paneTopForMax+paneBottomForMin)/2
          #print(minY,maxY)
          if yaxis=="None":
            minY=np.min(c[start-c[0]+1:end-c[0]+1])
            maxY=np.max(c[start-c[0]+1:end-c[0]+1])
          if not maxY==minY: y=paneBottomForMin+(c[i-c[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
          points.append(y)
        if len(points)==0: continue
        i=len(points)-4
        while i>=0:
          points.append(points[i])
          points.append(points[i+1])
          i-=2
        #print("len(points)=",len(points))
        if style=="Solid": cnv.create_polygon(points,outline=color,width=width)
        elif style=="Dash":  cnv.create_polygon(points,outline=color,width=width, dash=(6,4))
        else: cnv.create_polygon(points,outline=color,width=width, dash=(2,4))
      elif type=="Hstgm":
        for i in range(start,end+1):
          x=paneLeft+(i-leftInd)*(paneRight-paneLeft)/(rightInd-leftInd)
          if int(x)==int(xprev): continue
          xprev=x
          points.append(x)
          #c=G.dict_c[symb]#############
          if yaxis=="None":
            minY=0
            maxY=np.max(c[start-c[0]+1:end-c[0]+1])
          yc=(paneTopForMax+paneBottomForMin)/2
          if not maxY==minY: yc=paneBottomForMin+(c[i-c[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
          if style=="Solid": cnv.create_line(x, yc, x, paneBottomForMin, fill=color,width=width)
          elif style=="Dash":  cnv.create_line(x, yc, x, paneBottomForMin, fill=color,width=width, dash=(6,4))
          else: cnv.create_line(x, yc, x, paneBottomForMin, fill=color,width=width,dash=(2,4))
      elif type=="Bar":#"Bar"
        for i in range(start,end+1):
          x=paneLeft+(i-leftInd)*(paneRight-paneLeft)/(rightInd-leftInd)
          points.append(x)
          #hh=G.dict_h[symb]
          #l=G.dict_l[symb]
          #c=G.dict_c[symb]
          if yaxis=="None":
            minY=np.min(l[start-c[0]+1:end-c[0]+1])
            maxY=np.max(hh[start-c[0]+1:end-c[0]+1])
          yh=(paneTopForMax+paneBottomForMin)/2
          yl=(paneTopForMax+paneBottomForMin)/2
          yc=(paneTopForMax+paneBottomForMin)/2
          if not maxY==minY: 
            #yh=paneBottomForMin+(hh[i-hh[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
            #yl=paneBottomForMin+(l[i-l[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
            yc=paneBottomForMin+(c[i-c[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
            yh=yc
            yl=yc
          if style=="Solid": 
            cnv.create_line(x, yh, x, yl, fill=color,width=width)
            cnv.create_line(x, yc, x+d, yc, fill=color,width=width)
          elif style=="Dash":  
            cnv.create_line(x, yh, x, yl, fill=color,width=width, dash=(6, 4))
            cnv.create_line(x, yc, x+d, yc, fill=color,width=width, dash=(6, 4))
          else: #cnv.create_line(x, yc, x, paneBottomForMin, fill=color,width=width,dash=(2,4))
            cnv.create_line(x, yh, x, yl, fill=color,width=width, dash=(2, 4))
            cnv.create_line(x, yc, x+d, yc, fill=color,width=width, dash=(2, 4))
      else:#Edge
        for i in range(start,end+1):
          x=paneLeft+(i-leftInd)*(paneRight-paneLeft)/(rightInd-leftInd)
          if int(x)==int(xprev): continue
          xprev=x
          points.append(x)
          #c=G.dict_c[symb]
          if yaxis=="None":
            minY=0
            maxY=np.max(c[start-c[0]+1:end-c[0]+1])
          y=(paneTopForMax+paneBottomForMin)/2
          if not maxY==minY: y=paneBottomForMin+(c[i-c[0]+1]-minY)*(paneTopForMax-paneBottomForMin)/(maxY-minY)
          points.append(y)
        n=len(points)
        points.append(points[n-2])
        points.append(paneBottomForMin)
        points.append(points[0])
        points.append(paneBottomForMin)
        points.append(points[0])
        points.append(points[1])
        #cnv.create_polygon(points,outline=color,width=width,fill=color)
        if style=="Solid": cnv.create_polygon(points,outline=color,width=width,fill=color)
        elif style=="Dash":  cnv.create_polygon(points,outline=color,width=width,fill=color, dash=(6,4))
        else: cnv.create_polygon(points,outline=color,width=width,fill=color, dash=(2,4))
 
    
  def showMsgList():
    if G.traceOn==1:
      G.changeListMsg()
      if G.traceInd>=0:
        x=G.xLeftY+(G.traceInd-G.leftInd)*(G.xRightY-G.xLeftY)/(G.rightInd-G.leftInd) 
      else:
        x=(G.xRightY+G.xLeftY)/2    
      id1=cnv.create_line(x,0,x,h-G.xHeight)
 
      s=""
      longest=G.listMsg[0]
      for line in G.listMsg:
        if len(longest)<len(G.listMsg):longest=line 
        s+=line+"\n"
      width=len(longest)*10

      if x>(G.xRightY+G.xLeftY):x-=width
      hh=+G.xHeight*(len(G.listMsg)+0.5)
      id3=cnv.create_rectangle(x, G.yCursor-hh, x+width, G.yCursor, fill='white')
      id2=cnv.create_text(0,0,text=s,font="Times 12 ")
      move_item(cnv,id2,x,G.yCursor-hh,0,0)
      return [id1,id2,id3]
  G.listToDelete = showMsgList()
def star1(window):###################################################
  STATE=NORMAL
  if not G.showDlg=="No": 
    STATE=DISABLED
    STATE=NORMAL
  def right(wid):
        wid.update()
        return wid.winfo_x()+wid.winfo_width()
  def forget():
    #if not G.error=="":  return
    fr_dlg.pack_forget()
    fr_tools.pack_forget()
    fr_form.pack_forget()
    fr_graph.pack_forget()
    star1(window)
  def on_enter(e):
    e.widget['background'] = 'light blue'
  def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'
  def blink(wid):
    wid.bind("<Enter>", on_enter)
    wid.bind("<Leave>", on_leave)
  def newselectionS(event):
    fr_dlg.focus() 
  def hide_dlg():
    G.showDlg="No"
    forget()
  def acceptSymbol(): 
    #print(G.selectedSymbol,G.symbols)
    symb= cbx_Symbol.get()  
    if symb in G.symbolExamples:
      G.getData(cbx_Symbol.get())
      G.symbols.append(symb) 
      pres=[]
      pres.append(cbx_Visibility.get())
      pres.append(cbx_Pane.get())
      pres.append(cbx_Yaxis.get())
      pres.append(cbx_Type.get())
      pres.append(cbx_Width.get())
      pres.append(cbx_Style.get())
      pres.append(cbx_Legend.get())
      pres.append(cnv_Color["bg"])
      G.symbolPresentation.append(pres)
      G.showDlg="No"
      if G.traceInd>0: G.changeListMsg() 
    #elif symb.strip=='':     
    else:
      cbx_Symbol["text"]=""
      #cbx_Symbol["bg"]="red"
    forget()
  

  #G.error=G.calc()   

  fr_dlg=tk.Frame(window, width=G.widthDlg,  bg='yellow',highlightbackground="blue",highlightthickness=1)
  if G.showDlg=="Edit Symbol": # Edit Symbol # Edit Symbol # Edit Symbol # Edit Symbol
    # https://www.geeksforgeeks.org/python-tkinter-scrolledtext-widget/ 
    fr_dlg.pack(side=TOP)
    fr_dlg["height"]=90
    fr_dlg.update()
    def change_list_height():
      s=str(btn_expand['text'])
      if s=="expand": 
        G.expandList="shrink"
      else: 
        G.expandList="expand"
      forget()
    btn_expand=Button(fr_dlg,text=G.expandList,height=1,command=change_list_height)
    yh=0
    n=G.selectedSymbol
    btn_expand.place(x=0,y=yh) 
    lbl_Symbol=Label(fr_dlg,text="Symbol #"+str(n)+":",bg="yellow")
    lbl_Symbol.place(x=right(btn_expand),y=yh)
    ent_n=Entry(fr_dlg,width=5)#,state=STATE
    ent_n.delete(0,"end")
    ent_n.insert(0,G.symbols[n])
    xL=150
    
    ent_n.place(x=right(lbl_Symbol),y=yh)
    lbl_Visibility=Label(fr_dlg,text="Visibility:",bg="yellow")
    lbl_Visibility.place(x=xL+100,y=yh)
    cbx_Visibility=ttk.Combobox(fr_dlg,values=G.visibility,width=3,state="read only") 
    cbx_Visibility.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Visibility.place(x=right(lbl_Visibility),y=yh)
    cbx_Visibility["state"]="readonly"
    viz=G.symbolPresentation[n][0]
    lst=list(cbx_Visibility["values"])
    k=lst.index(viz)
    cbx_Visibility.current(k)   #visibility
        
    lbl_Pane=Label(fr_dlg,text="Pane:",bg="yellow")
    lbl_Pane.place(x=right(cbx_Visibility),y=yh)
    cbx_Pane=ttk.Combobox(fr_dlg,values=G.pane,width=2,state="read only") 
    cbx_Pane.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Pane.place(x=right(lbl_Pane),y=yh)
    cbx_Pane["state"]="readonly"
    pane=G.symbolPresentation[n][1]
    lst=list(cbx_Pane["values"])
    k=lst.index(pane)
    cbx_Pane.current(k)

    lbl_Yaxis=Label(fr_dlg,text="Yaxis:",bg="yellow")
    lbl_Yaxis.place(x=right(cbx_Pane),y=yh)
    cbx_Yaxis=ttk.Combobox(fr_dlg,values=G.yaxis,width=5,state="read only") 
    cbx_Yaxis.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Yaxis.place(x=right(lbl_Yaxis),y=yh)
    cbx_Yaxis["state"]="readonly"
    yaxis=G.symbolPresentation[n][2]
    lst=list(cbx_Yaxis["values"])
    k=lst.index(yaxis)
    cbx_Yaxis.current(k)

    lbl_Type=Label(fr_dlg,text="Type:",bg="yellow")
    lbl_Type.place(x=right(cbx_Yaxis),y=yh)
    cbx_Type=ttk.Combobox(fr_dlg,values=G.type,width=6,state="read only") 
    cbx_Type.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Type.place(x=right(lbl_Type),y=yh)
    cbx_Type["state"]="readonly"
    type=G.symbolPresentation[n][3]
    lst=list(cbx_Type["values"])
    k=lst.index(type)
    cbx_Type.current(k)

    lbl_Width=Label(fr_dlg,text="Width:",bg="yellow")
    lbl_Width.place(x=right(cbx_Type),y=yh)
    cbx_Width=ttk.Combobox(fr_dlg,values=G.width,width=2,state="read only") 
    cbx_Width.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Width.place(x=right(lbl_Width),y=yh)
    cbx_Width["state"]="readonly"
    width=G.symbolPresentation[n][4]
    lst=list(cbx_Width["values"])
    k=lst.index(width)
    cbx_Width.current(k)

    lbl_Style=Label(fr_dlg,text="Style:",bg="yellow")
    lbl_Style.place(x=right(cbx_Width),y=yh)
    cbx_Style=ttk.Combobox(fr_dlg,values=G.style,width=6,state="read only") 
    cbx_Style.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Style.place(x=right(lbl_Style),y=yh)
    cbx_Style["state"]="readonly"    
    style=G.symbolPresentation[n][5]
    lst=list(cbx_Style["values"])
    k=lst.index(style)
    cbx_Style.current(k)
    
    lbl_Legend=Label(fr_dlg,text="Legend:",bg="yellow")
    lbl_Legend.place(x=right(cbx_Style),y=yh)
    cbx_Legend=ttk.Combobox(fr_dlg,values=G.legend,width=6,state="read only") 
    cbx_Legend.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Legend.place(x=right(lbl_Legend),y=yh)
    cbx_Legend["state"]="readonly"   
    legend=G.symbolPresentation[n][6]
    lst=list(cbx_Legend["values"])
    k=lst.index(legend)
    cbx_Legend.current(k)

    lbl_Color=Label(fr_dlg,text="Color:",width=6,bg="yellow")
    lbl_Color.place(x=right(cbx_Legend),y=yh)
    lbl_Color1=Label(fr_dlg,width=5)
    lbl_Color1.place(x=right(lbl_Color),y=yh)
    blink(lbl_Color1)
    cnv_Color=Canvas(fr_dlg,width=25,height=10,bg=G.symbolPresentation[n][7])
    cnv_Color.place(x=right(lbl_Color)+5,y=5+yh)

    def choose_color(event):
      color_code = colorchooser.askcolor(title ="Choose color")
      cnv_Color.configure(bg =color_code[1]) 
    cnv_Color.bind("<Button-1>",choose_color) 
    lbl_Color1.bind("<Button-1>",choose_color)

    btn_Cancel=Button(fr_dlg,text="Cancel",width=6,command=lambda:hide_dlg())
    btn_Cancel.place(x=right(cnv_Color)+9,y=0)
    blink(btn_Cancel)
    def replaceSymbol():
      k=int(lbl_Symbol["text"][:-1].split("#")[1])
      G.dictCoordsLeg.pop(G.symbols[k],None)
      G.symbols[k]=ent_n.get()
      G.getData(ent_n.get())
      G.symbolPresentation[k][0]=cbx_Visibility.get()
      G.symbolPresentation[k][1]=cbx_Pane.get()
      G.symbolPresentation[k][2]=cbx_Yaxis.get()
      G.symbolPresentation[k][3]=cbx_Type.get()
      G.symbolPresentation[k][4]=cbx_Width.get()
      G.symbolPresentation[k][5]=cbx_Style.get()
      G.symbolPresentation[k][6]=cbx_Legend.get()
      G.symbolPresentation[k][7]=cnv_Color["bg"]
      G.showDlg="No"
      forget()


    btn_OK=Button(fr_dlg,text="OK",width=3,command=lambda:replaceSymbol() )
    btn_OK.place(x=right(btn_Cancel),y=0)
    blink(btn_OK)
    
    #######################
    cnv_list=Canvas(fr_dlg,bg="blue", height=fr_dlg["height"] -yh-btn_expand.winfo_height() )#
    cnv_list.place(x=0,y=yh+btn_expand.winfo_height())
    
  
    scroll_bar = Scrollbar(cnv_list)
    scroll_bar.pack( side = RIGHT, fill=Y)  
    mylist = Listbox(cnv_list,yscrollcommand = scroll_bar.set,width=123,height=G.dictExpand[G.expandList],font=('Arial', '11'))
        
    if G.expandList=="expand":
      fr_dlg["height"]=G.dictExpand[G.expandList]*26
    else:
      fr_dlg["height"]=G.dictExpand[G.expandList]*26
      mylist["height"]+=4    
    cnv_list["height"]=fr_dlg["height"]
    cnv_list.update()
    mylist.update()
    fr_dlg.update()
    list_of_rows=G.getData(G.symbols[G.selectedSymbol])
    mylist.insert(END, *list_of_rows)
    mylist.pack( side = LEFT, fill = BOTH )
    scroll_bar.config( command = mylist.yview )       
  if G.showDlg=="Add Symbol": # Add Symbol # Add Symbol# Add Symbol# Add Symbol# Add Symbol
    fr_dlg.pack(side=TOP)
    fr_dlg["height"]=30
    fr_dlg.update()
    lbl_SymbolNumber=Label(fr_dlg,text="Add Symbol # "+str(len(G.symbols))+":",bg="yellow")
    yh=3
    lbl_SymbolNumber.place(x=0,y=yh)
    cbx_Symbol=ttk.Combobox(fr_dlg,values=G.symbolExamples,width=6)  
    cbx_Symbol.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Symbol.place(x=right(lbl_SymbolNumber),y=yh)
    cbx_Symbol.current(0)

    def Return(event):
      print(1277)
      symb= cbx_Symbol.get()  
      print("Return: symb=",symb)
      #if symb.upper() in G.symbolExamples and not symb.upper()==oldSymb.upper():
      if symb.upper() in G.symbolExamples:
        acceptSymbol()
      else:
        cbx_Symbol["values"]=G.symbols
        cbx_Symbol.current(G.selectedSymbol)
        forget()
    #def presSf(xL,):
    cbx_Symbol.bind('<Return>', Return) 
    xL=right(cbx_Symbol)

    lbl_Visibility=Label(fr_dlg,text="Visibility:",bg="yellow")
    lbl_Visibility.place(x=xL+100,y=yh)
    cbx_Visibility=ttk.Combobox(fr_dlg,values=G.visibility,width=3) 
    cbx_Visibility.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Visibility.place(x=right(lbl_Visibility),y=yh)
    cbx_Visibility.current(0)
    cbx_Visibility["state"]="readonly"

    lbl_Pane=Label(fr_dlg,text="Pane:",bg="yellow")
    lbl_Pane.place(x=right(cbx_Visibility),y=yh)
    cbx_Pane=ttk.Combobox(fr_dlg,values=G.pane,width=2,state="readonly") 
    cbx_Pane.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Pane.place(x=right(lbl_Pane),y=yh)
    cbx_Pane.current(0)
    #cbx_Pane["state"]="readonly"

    lbl_Yaxis=Label(fr_dlg,text="Yaxis:",bg="yellow")
    lbl_Yaxis.place(x=right(cbx_Pane),y=yh)
    cbx_Yaxis=ttk.Combobox(fr_dlg,values=G.yaxis,width=5,state="readonly") 
    cbx_Yaxis.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Yaxis.place(x=right(lbl_Yaxis),y=yh)
    cbx_Yaxis.current(0)

    lbl_Type=Label(fr_dlg,text="Type:",bg="yellow")
    lbl_Type.place(x=right(cbx_Yaxis),y=yh)
    cbx_Type=ttk.Combobox(fr_dlg,values=G.type,width=6,state="readonly") 
    cbx_Type.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Type.place(x=right(lbl_Type),y=yh)
    cbx_Type.current(0)
 
    lbl_Width=Label(fr_dlg,text="Width:",bg="yellow")
    lbl_Width.place(x=right(cbx_Type),y=yh)
    cbx_Width=ttk.Combobox(fr_dlg,values=G.width,width=2,state="readonly") 
    cbx_Width.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Width.place(x=right(lbl_Width),y=yh)
    cbx_Width.current(0)

    lbl_Style=Label(fr_dlg,text="Style:",bg="yellow")
    lbl_Style.place(x=right(cbx_Width),y=yh)
    cbx_Style=ttk.Combobox(fr_dlg,values=G.style,width=6,state="readonly") 
    cbx_Style.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Style.place(x=right(lbl_Style),y=yh)
    cbx_Style.current(0)

    lbl_Legend=Label(fr_dlg,text="Legend:",bg="yellow")
    lbl_Legend.place(x=right(cbx_Style),y=yh)
    cbx_Legend=ttk.Combobox(fr_dlg,values=G.legend,width=6,state="readonly") 
    cbx_Legend.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Legend.place(x=right(lbl_Legend),y=yh)
    cbx_Legend.current(0)

    lbl_Color=Label(fr_dlg,text="Color:",width=6,bg="yellow")
    lbl_Color.place(x=right(cbx_Legend),y=yh)
    lbl_Color1=Label(fr_dlg,width=5)
    lbl_Color1.place(x=right(lbl_Color),y=yh)
    blink(lbl_Color1)
    cnv_Color=Canvas(fr_dlg,width=25,height=10,bg="blue")
    cnv_Color.place(x=right(lbl_Color)+5,y=5+yh)
    def choose_color(event):
      color_code = colorchooser.askcolor(title ="Choose color")
      cnv_Color.configure(bg =color_code[1]) 
    cnv_Color.bind("<Button-1>",choose_color) 
    lbl_Color1.bind("<Button-1>",choose_color) 
    btn_Cancel=Button(fr_dlg,text="Cancel",width=6,command=lambda:hide_dlg())
    btn_Cancel.place(x=right(cnv_Color)+9,y=0)
    blink(btn_Cancel)
    btn_OK=Button(fr_dlg,text="OK",width=3,command=lambda: acceptSymbol())
    btn_OK.place(x=right(btn_Cancel),y=0)
    blink(btn_OK)
  # draw tools######draw tools
  if G.showDlg=="Add Formula":
    fr_dlg.pack(side=TOP)
    fr_dlg["height"]=60
    fr_dlg["width"]=790
    fr_dlg.update()
    nF=len(G.listFormulas)
    G.selectedFormula=nF
    lbl_Formula=Label(fr_dlg,text="Formula # "+str(nF)+":",bg="yellow")
    yh=3
    lbl_Formula.place(x=0,y=yh)
    sv_name=Entry(fr_dlg,width=10)
    sv_name.insert(0,"F"+str(nF))
    sv_name.place(x=right(lbl_Formula),y=yh)
 
    lbl_eq=Label(fr_dlg,text="=")
    lbl_eq.place(x=right(sv_name),y=yh)
    cbx_Formula=ttk.Combobox(fr_dlg,values=G.formulaExamples,width=90)  
    cbx_Formula.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Formula.place(x=right(lbl_eq),y=yh)
    cbx_Formula.focus()
    def acceptFormula(): 
      print("G.listFormulas=",G.listFormulas)
      print("G.prevListFormulas=",G.prevListFormulas)
      if G.sameFormulas(): return
      if not G.error=="": 
        G.showDlg="No"
        print("forget")
        forget()
      name=sv_name.get()
      f=cbx_Formula.get()
      print("f=",f)
      f=f.strip()
      if f=="": return
      G.listFormulas.append([name,cbx_Formula.get()])
      print("G.listFormulas=",G.listFormulas)
      print("G.prevListFormulas=",G.prevListFormulas)
      if G.sameFormulas(): return

      pres=[]   
      pres.append(cbx_Visibility.get())
      pres.append(cbx_Pane.get())
      pres.append(cbx_Yaxis.get())
      pres.append(cbx_Type.get())
      pres.append(cbx_Width.get())
      pres.append(cbx_Style.get())
      pres.append(cbx_Legend.get())
      pres.append(cnv_Color["bg"])
      G.formulaPresentation.append(pres)
      G.error=G.calc()
      if not  G.error=="": G.showDlg="Error"
      else: G.showDlg="No"
      forget()
     
    def enter(event=None):
      print(1407)
      acceptFormula()
    cbx_Formula.bind("<Return>",enter)
    sv_name.bind("<Return>",enter)
    yh+=25
    lbl_Visibility=Label(fr_dlg,text="Visibility:",bg="yellow")
    lbl_Visibility.place(x=0,y=yh)
    cbx_Visibility=ttk.Combobox(fr_dlg,values=G.visibility,width=3,state="read only") 
    cbx_Visibility.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Visibility.place(x=right(lbl_Visibility),y=yh)
    cbx_Visibility["state"]="readonly"
    cbx_Visibility.current(0)
    lbl_Pane=Label(fr_dlg,text="Pane:",bg="yellow")
    lbl_Pane.place(x=right(cbx_Visibility),y=yh)
    cbx_Pane=ttk.Combobox(fr_dlg,values=G.pane,width=2,state="read only") 
    cbx_Pane.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Pane.place(x=right(lbl_Pane),y=yh)
    cbx_Pane["state"]="readonly"
    pane=G.howManyPanes()
    cbx_Pane.current(pane)

    lbl_Yaxis=Label(fr_dlg,text="Yaxis:",bg="yellow")
    lbl_Yaxis.place(x=right(cbx_Pane),y=yh)
    cbx_Yaxis=ttk.Combobox(fr_dlg,values=G.yaxis,width=5,state="read only") 
    cbx_Yaxis.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Yaxis.place(x=right(lbl_Yaxis),y=yh)
    cbx_Yaxis["state"]="readonly"
    cbx_Yaxis.current(0)

    lbl_Type=Label(fr_dlg,text="Type:",bg="yellow")
    lbl_Type.place(x=right(cbx_Yaxis),y=yh)
    cbx_Type=ttk.Combobox(fr_dlg,values=G.type,width=6,state="read only") 
    cbx_Type.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Type.place(x=right(lbl_Type),y=yh)
    cbx_Type["state"]="readonly"
    cbx_Type.current(0)

    lbl_Width=Label(fr_dlg,text="Width:",bg="yellow")
    lbl_Width.place(x=right(cbx_Type),y=yh)
    cbx_Width=ttk.Combobox(fr_dlg,values=G.width,width=2,state="read only") 
    cbx_Width.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Width.place(x=right(lbl_Width),y=yh)
    cbx_Width["state"]="readonly"
    cbx_Width.current(0)

    lbl_Style=Label(fr_dlg,text="Style:",bg="yellow")
    lbl_Style.place(x=right(cbx_Width),y=yh)
    cbx_Style=ttk.Combobox(fr_dlg,values=G.style,width=6,state="read only") 
    cbx_Style.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Style.place(x=right(lbl_Style),y=yh)
    cbx_Style["state"]="readonly"    
    cbx_Style.current(0)
    
    lbl_Legend=Label(fr_dlg,text="Legend:",bg="yellow")
    lbl_Legend.place(x=right(cbx_Style),y=yh)
    cbx_Legend=ttk.Combobox(fr_dlg,values=G.legend,width=6,state="read only") 
    cbx_Legend.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Legend.place(x=right(lbl_Legend),y=yh)
    cbx_Legend["state"]="readonly"   
    cbx_Legend.current(0)

    lbl_Color=Label(fr_dlg,text="Color:",width=6,bg="yellow")
    lbl_Color.place(x=right(cbx_Legend),y=yh)
    lbl_Color1=Label(fr_dlg,width=5)
    lbl_Color1.place(x=right(lbl_Color),y=yh)
    blink(lbl_Color1)
    cnv_Color=Canvas(fr_dlg,width=25,height=10,bg="blue")
    cnv_Color.place(x=right(lbl_Color)+5,y=5+yh)

    def choose_color(event):
      color_code = colorchooser.askcolor(title ="Choose color")
      cnv_Color.configure(bg =color_code[1]) 
    cnv_Color.bind("<Button-1>",choose_color) 
    lbl_Color1.bind("<Button-1>",choose_color)

    btn_Cancel=Button(fr_dlg,text="Cancel",width=6,command=lambda:hide_dlg())
    btn_Cancel.place(x=right(cnv_Color)+9,y=yh)
    blink(btn_Cancel)

    
    btn_OK=Button(fr_dlg,text="OK",width=3,command=lambda: acceptFormula())
    btn_OK.place(x=right(cnv_Color)+29,y=0)
    blink(btn_OK)

  if G.showDlg=="Edit Formula": # Edit Symbol # Edit Symbol # Edit Symbol # Edit Symbol
    # https://www.geeksforgeeks.org/python-tkinter-scrolledtext-widget/ 
    fr_dlg.pack(side=TOP)
    fr_dlg["height"]=90
    fr_dlg.update()
    def change_list_height():
      s=str(btn_expand['text'])
      if s=="expand": 
        G.expandList="shrink"
      else: 
        G.expandList="expand"
      forget()
    
    yh=0
    n=G.selectedFormula
    lbl_Formula=Label(fr_dlg,text="Formula #"+str(n)+":",bg="yellow")
    lbl_Formula.place(x=0,y=yh)

    ent_nn=Entry(fr_dlg,width=10)
    ent_nn.insert(0,G.listFormulas[n][0])
    ent_nn.place(x=right(lbl_Formula),y=yh)
    lbl_eq=Label(fr_dlg,text="=")
    lbl_eq.place(x=right(ent_nn),y=yh)
    ent_ff=Entry(fr_dlg,width=45)
    ent_ff.insert(0,G.listFormulas[n][1])
    ent_ff.place(x=right(lbl_eq),y=yh)
    
    def replaceFormula():
      nn=ent_nn.get()
      ff=ent_ff.get()   
      k=int(lbl_Formula["text"][:-1].split("#")[1])
      G.dictCoordsLeg.pop(G.listFormulas[k][0],None)
      G.listFormulas[k]=[nn,ff]
      G.formulaPresentation[k][0]=cbx_Visibility.get()
      G.formulaPresentation[k][1]=cbx_Pane.get()
      G.formulaPresentation[k][2]=cbx_Yaxis.get()
      G.formulaPresentation[k][3]=cbx_Type.get()
      G.formulaPresentation[k][4]=cbx_Width.get()
      G.formulaPresentation[k][5]=cbx_Style.get()
      G.formulaPresentation[k][6]=cbx_Legend.get()
      G.formulaPresentation[k][7]=cnv_Color["bg"]
      G.showDlg="No"
      G.error=G.calc()
      if not  G.error=="": G.showDlg="Error"
      else: G.showDlg="No"
      forget()

    def retn(event=None):
      print(1539)
      replaceFormula()
    ent_nn.bind("<Return>", retn)
    ent_ff.bind("<Return>", retn)
    xL=0
    yh+=G.xHeight +3
    btn_expand=Button(fr_dlg,text=G.expandList,height=1,command=change_list_height)
    btn_expand.place(x=0,y=yh) 
       

    lbl_Visibility=Label(fr_dlg,text="Visibility:",bg="yellow")
    lbl_Visibility.place(x=right(btn_expand),y=yh)
    cbx_Visibility=ttk.Combobox(fr_dlg,values=G.visibility,width=3,state="read only") 
    cbx_Visibility.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Visibility.place(x=right(lbl_Visibility),y=yh)
    cbx_Visibility["state"]="readonly"
    viz=G.formulaPresentation[n][0]
    lst=list(cbx_Visibility["values"])
    kk=lst.index(viz)
    cbx_Visibility.current(kk)   #visibility
        
    lbl_Pane=Label(fr_dlg,text="Pane:",bg="yellow")
    lbl_Pane.place(x=right(cbx_Visibility),y=yh)
    cbx_Pane=ttk.Combobox(fr_dlg,values=G.pane,width=2,state="read only") 
    cbx_Pane.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Pane.place(x=right(lbl_Pane),y=yh)
    cbx_Pane["state"]="readonly"
    pane=G.formulaPresentation[n][1]
    lst=list(cbx_Pane["values"])
    kk=lst.index(pane)
    cbx_Pane.current(kk)

    lbl_Yaxis=Label(fr_dlg,text="Yaxis:",bg="yellow")
    lbl_Yaxis.place(x=right(cbx_Pane),y=yh)
    cbx_Yaxis=ttk.Combobox(fr_dlg,values=G.yaxis,width=5,state="read only") 
    cbx_Yaxis.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Yaxis.place(x=right(lbl_Yaxis),y=yh)
    cbx_Yaxis["state"]="readonly"
    yaxis=G.formulaPresentation[n][2]
    lst=list(cbx_Yaxis["values"])
    kk=lst.index(yaxis)
    cbx_Yaxis.current(kk)

    lbl_Type=Label(fr_dlg,text="Type:",bg="yellow")
    lbl_Type.place(x=right(cbx_Yaxis),y=yh)
    cbx_Type=ttk.Combobox(fr_dlg,values=G.type,width=6,state="read only") 
    cbx_Type.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Type.place(x=right(lbl_Type),y=yh)
    cbx_Type["state"]="readonly"
    type=G.formulaPresentation[n][3]
    lst=list(cbx_Type["values"])
    kk=lst.index(type)
    cbx_Type.current(kk)

    lbl_Width=Label(fr_dlg,text="Width:",bg="yellow")
    lbl_Width.place(x=right(cbx_Type),y=yh)
    cbx_Width=ttk.Combobox(fr_dlg,values=G.width,width=2,state="read only") 
    cbx_Width.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Width.place(x=right(lbl_Width),y=yh)
    cbx_Width["state"]="readonly"
    width=G.formulaPresentation[n][4]
    lst=list(cbx_Width["values"])
    kk=lst.index(width)
    cbx_Width.current(kk)

    lbl_Style=Label(fr_dlg,text="Style:",bg="yellow")
    lbl_Style.place(x=right(cbx_Width),y=yh)
    cbx_Style=ttk.Combobox(fr_dlg,values=G.style,width=6,state="read only") 
    cbx_Style.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Style.place(x=right(lbl_Style),y=yh)
    cbx_Style["state"]="readonly"    
    style=G.formulaPresentation[n][5]
    lst=list(cbx_Style["values"])
    kk=lst.index(style)
    cbx_Style.current(kk)
    
    lbl_Legend=Label(fr_dlg,text="Legend:",bg="yellow")
    lbl_Legend.place(x=right(cbx_Style),y=yh)
    cbx_Legend=ttk.Combobox(fr_dlg,values=G.legend,width=6,state="read only") 
    cbx_Legend.bind("<<ComboboxSelected>>", newselectionS)    
    cbx_Legend.place(x=right(lbl_Legend),y=yh)
    cbx_Legend["state"]="readonly"   
    legend=G.formulaPresentation[n][6]
    lst=list(cbx_Legend["values"])
    kk=lst.index(legend)
    cbx_Legend.current(kk)

    lbl_Color=Label(fr_dlg,text="Color:",width=6,bg="yellow")
    lbl_Color.place(x=right(cbx_Legend),y=yh)
    lbl_Color1=Label(fr_dlg,width=5)
    lbl_Color1.place(x=right(lbl_Color),y=yh)
    blink(lbl_Color1)
    cnv_Color=Canvas(fr_dlg,width=25,height=10,bg=G.formulaPresentation[n][7])
    cnv_Color.place(x=right(lbl_Color)+5,y=5+yh)

    def choose_color(event):
      color_code = colorchooser.askcolor(title ="Choose color")
      cnv_Color.configure(bg =color_code[1]) 
    cnv_Color.bind("<Button-1>",choose_color) 
    lbl_Color1.bind("<Button-1>",choose_color)

    btn_Cancel=Button(fr_dlg,text="Cancel",width=6,command=lambda:hide_dlg())
    btn_Cancel.place(x=right(cnv_Color)+9,y=yh)
    blink(btn_Cancel)
    

    btn_OK=Button(fr_dlg,text="OK",width=3,command=lambda:replaceFormula() )
    btn_OK.place(x=right(btn_Cancel),y=yh)
    blink(btn_OK)
    
    #######################
    cnv_list=Canvas(fr_dlg,bg="blue", height=fr_dlg["height"] -yh-btn_expand.winfo_height() )#
    cnv_list.place(x=0,y=yh+btn_expand.winfo_height())
    
  
    scroll_bar = Scrollbar(cnv_list)
    scroll_bar.pack( side = RIGHT, fill=Y)  
    mylist = Listbox(cnv_list,yscrollcommand = scroll_bar.set,width=123,height=G.dictExpand[G.expandList],font=('Arial', '10'))
        
    if G.expandList=="expand":
      fr_dlg["height"]=G.dictExpand[G.expandList]*26
    else:
      fr_dlg["height"]=G.dictExpand[G.expandList]*26
      mylist["height"]+=4    
    cnv_list["height"]=fr_dlg["height"]
    cnv_list.update()
    mylist.update()
    fr_dlg.update()
    name=G.listFormulas[n][0]
    if not name in G.lstBadNames: list_of_rows=G.makeList(G.dict_name[name])
    mylist.insert(END, *list_of_rows)
    mylist.pack( side = LEFT, fill = BOTH )
    scroll_bar.config( command = mylist.yview )  

  if G.showDlg=="Error":
    fr_dlg.pack(side=TOP)
    fr_dlg["height"]=60
    fr_dlg["width"]=790
    fr_dlg.update()
    lbl_error=Label(fr_dlg,text=G.error,fg="red")
    lbl_error.place(x=10,y=10)
     
  

  #print("Tools")
  fr_tools=tk.Frame(window, height=G.heightTools, bg="green")
  fr_tools.pack(side=TOP,fill=X)
  def hideshow():
    s = str(btn_hideshow['text'])
    if s=="<<":G.showForm="No"
    else:G.showForm="Yes"
    forget()
  btn_hideshow=Button(fr_tools,state=STATE,command=hideshow)
  blink(btn_hideshow)
  if G.showForm=="Yes":btn_hideshow['text']='<<'
  else:btn_hideshow['text']='>>'
  btn_hideshow.pack(side=LEFT)
  yh=3 

  btn_ClearAll=Button(fr_tools,state=STATE,text="Clear All")
  btn_ClearAll.pack(side=LEFT)
  blink(btn_ClearAll)

  lbl_Data=Label(fr_tools,state=STATE,text="Data:")
  lbl_Data.pack(side=LEFT)
  cmb_Data=ttk.Combobox(fr_tools,state="readonly", values=["canned","daily"],width=len("canned"))
  if not G.showDlg=="No": cmb_Data["state"]=DISABLED
  cmb_Data.pack(side=LEFT)
  cmb_Data.current(0)
  def newselection(event):
    fr_tools.focus()
  cmb_Data.bind("<<ComboboxSelected>>", newselection)

  def add_symbol():
    G.showDlg="Add Symbol"
    forget()
  btn_AddSymbol=Button(fr_tools,text="Add Symbol",state=STATE,command=add_symbol)
  btn_AddSymbol.pack(side=LEFT)
  blink(btn_AddSymbol)
  
  def edit_symbol(event):
    #widget=event.widget
    G.showDlg="Edit Symbol"   
    G.selectedSymbol=int(event.widget["text"][:-1])
    forget()
  

  n=len(G.symbols)
  yh=4
  if n>0:
    btn_s0=Button(fr_tools,text="0:",state=STATE,fg=G.symbolPresentation[0][7])
    btn_s0.bind("<Button>",edit_symbol)
    blink(btn_s0)
    btn_s0.place(x=right(btn_AddSymbol),y=0)
    ent_0=Entry(fr_tools,width=5)#,fg=G.symbolPresentation[0][7]

    def func0(event):
      oldSymb=G.symbols[0] 
      symb=str(ent_0.get())
      if symb.upper() in G.symbolExamples or symb=="":
        G.dictCoordsLeg.pop(oldSymb,None)       
        G.getData(symb)
        G.symbols[0]=symb 
        G.getData(symb)  
        G.showDlg="No"
        G.selectedSymbol=0
        forget()
      else:
        G.symbols[0]=symb
        G.error=" Wrong symb 0"
        G.showDlg="Error"
        forget()
    def func1(event):
      print(1752)
      oldSymb=G.symbols[1]   
      symb=ent_1.get()
      if symb.upper() in G.symbolExamples or symb=="":
        G.dictCoordsLeg.pop(oldSymb,None)         
        G.getData(symb)
        G.symbols[1]=symb     
        G.getData(symb)  
        G.showDlg="No"
        G.selectedSymbol=1
        forget()
      else:
        G.symbols[1]=symb
        G.error=" Wrong symb 1"
        G.showDlg="Error"
        forget()
    def func2(event,oldSymb): 
      print(1769)
      symb=cbx_2.get() 
      m=int(btn_s2["text"].split(":")[0])
      G.symbols[m]=symb
      k=G.symbols.index(symb)
      if symb.upper() in G.symbolExamples or symb=="":
        G.dictCoordsLeg.pop(oldSymb,None)     
        G.symbols[m]=symb
        G.getData(symb)  
        G.showDlg="No"
        k=G.symbols.index(symb)
        G.selectedSymbol=k
        G.comboInd=k
        forget()
      else:
        G.symbols[k]=""
        cbx_2.current(k)
        G.comboInd=k
        #print(G.symbols)
        G.error=" Wrong symb "+str(k)+": "+symb
        G.showDlg="Error"
        forget()
   
    ent_0.bind('<Return>', func0)
    ent_0.delete(0,"end")
    ent_0.insert(0,G.symbols[0])
    ent_0["state"]=STATE
    ent_0.place(x=right(btn_s0),y=yh)
    blink(ent_0)
  if n>1: 
    btn_s1=Button(fr_tools,text="1:",state=STATE,fg=G.symbolPresentation[1][7])
    btn_s1.bind("<Button>",edit_symbol)#send old symg
    blink(btn_s1)
    btn_s1.place(x=right(ent_0),y=0)  

    ent_1=Entry(fr_tools,width=5)#,fg=G.symbolPresentation[1][7]
    ent_1.bind('<Return>', func1)    
    ent_1.delete(1,"end")
    ent_1.insert(0,G.symbols[1])
    ent_1["state"]=STATE
    ent_1.place(x=right(btn_s1),y=yh)
    blink(ent_1)
  if n>2:
    sn=str(n-1) +":"
    if G.comboInd>-1: sn= str(G.comboInd)+":"
    btn_s2=Button(fr_tools,text=sn,state=STATE, fg=G.symbolPresentation[n-1][7])#
    btn_s2.bind("<Button>",edit_symbol)
    blink(btn_s2)
    btn_s2.place(x=right(ent_1),y=0)  
    vs=[str(index)+": "+s for index,s in enumerate(G.symbols)]
    cbx_2=tktw.Combobox(fr_tools,width=6,values=vs)
    oldSymb=G.symbols[n-1]
    if G.comboInd>-1: cbx_2.set(G.symbols[G.comboInd])
    cbx_2.bind('<Return>', lambda event: func2(event, oldSymb)) 
    cbx_2["state"]=STATE
    cbx_2.place(x=right(btn_s2),y=yh)
    def selectionN(event): 
      pair=str(cbx_2.get()).split(" ")
      btn_s2["state"]="normal"
      btn_s2["text"]=pair[0]   
      k=int(pair[0][:-1])
      #G.selectedSymbol=k
      G.comboInd=k
      cbx_2.set(pair[1])
      btn_s2["fg"]=G.symbolPresentation[k][7]
      fr_tools.focus()
     # forget()
     
    cbx_2.bind("<<ComboboxSelected>>", selectionN)#redraw
    cbx_2.current(n-1)
    cbx_2.set(G.symbols[n-1])
  def trace(event):
    if G.traceInd==-1: 
      G.traceInd=math.floor((G.leftInd+G.rightInd)/2)
      G.yCursor=G.heightDlg/2
    if G.traceOn==0 :
      G.traceOn=1     
    else:      
      G.traceOn=0   
    forget()
  btn_trace=Button(fr_tools,width=5)
  btn_trace.bind('<Button-1>',trace)
  btn_trace.place(x=right(btn_AddSymbol)+220,y=0)
  def up():
    if G.traceInd<G.rightInd: 
      G.traceInd+=1
      G.changeListMsg()
    else:
      pass
    forget()
  def left():
    if G.traceInd>G.leftInd: 
      G.traceInd-=1
      G.changeListMsg()
    else:
      pass
    forget() 
  
  btn_left=Button(fr_tools,text="<",command=left)
  btn_left.place(x=right(btn_trace),y=0)
  btn_right=Button(fr_tools,text=">",command=up)
  btn_right.place(x=right(btn_left),y=0)  
  if G.traceOn==0:
    btn_trace["text"]='Trace'
    btn_left["state"]= DISABLED
    btn_right["state"]= DISABLED
  else:
    btn_trace["text"]=' Hide'
    btn_left["state"]= NORMAL
    btn_right["state"]= NORMAL

  def unzoom():
    if G.unzoomOn==1:
      G.unzoomList.pop()
      if len(G.unzoomList)==0:
        btn_unzoom["state"]=DISABLED
        G.unzoomOn=0
    #G.setLRMM()
    forget()

  btn_unzoom=Button(fr_tools,text="UnZoom",command=unzoom)
  if len(G.unzoomList)==0:
    btn_unzoom["state"]=DISABLED
    G.unzoomOn=0
  else:
    btn_unzoom["state"]=NORMAL
    G.unzoomOn=1
  btn_unzoom.place(x=right(btn_right),y=0)

  if n==0:# n==0
    pass

  # draw form
  wForm=0
  if G.showForm=="Yes": 
    wForm=G.widthForm
  fr_form=tk.Frame(window,width=wForm, height=G.heightForm,bg ="blue")
  fr_form.pack(side=LEFT,fill=Y)
  cnv_formulas = Canvas(fr_form,width=fr_form["width"], height=G.heightForm, bg="white smoke", highlightthickness=1, highlightbackground="light grey")
  cnv_formulas.place(x=0,y=0)
  cnv_formulas.pack(fill=BOTH,side=LEFT, expand=YES)
  def addFormula():
    G.showDlg="Add Formula"
    forget()

  btn_AddFormula=Button(cnv_formulas,text="Add Formula",command=addFormula)
  btn_AddFormula.place(x=10,y=30)
  lbl_MyAlgorithm=Label(cnv_formulas,text="My Algorithm:")
  lbl_MyAlgorithm.place(x=170,y=30)
  btn_SaveAs=Button(cnv_formulas,text="Save As")
  btn_SaveAs.place(x=350,y=30)
  x=10
  yprev=60
  def edit_formula(event):
    G.showDlg="Edit Formula"  
    G.selectedFormula=int(event.widget["text"])
    forget()
  for i,p in enumerate(G.listFormulas):
    btn_n=Button(cnv_formulas,height=1,text=str(i),fg=G.formulaPresentation[i][7])
    btn_n.bind("<Button>",edit_formula)
    btn_n.place(x=x,y=yprev)

    def callbackN(svN):
      i=G.dictSv2i[str(svN)]
      G.listFormulas[i][0]=svN.get()
    svN = StringVar()
    G.dictSv2i[str(svN)]=i
    svN.trace("w", lambda name, index, mode, svN=svN: callbackN(svN))
    ent_name = Entry(cnv_formulas,  width=10,textvariable=svN)

    #ent_name=Entry(cnv_formulas,width=10)
    ent_name.insert(0,p[0])
    ent_name.place(x=right(btn_n),y=yprev)
    lbl_eq=Label(cnv_formulas,text="=")
    lbl_eq.place(x=right(ent_name),y=yprev)
   
    def callbackF(sv):
      i=G.dictSv2i[str(sv)]
      G.listFormulas[i][1]=sv.get()
    sv = StringVar()
    G.dictSv2i[str(sv)]=i
    sv.trace("w", lambda name, index, mode, sv=sv: callbackF(sv))
    ent_f = Entry(cnv_formulas, width=50, textvariable=sv)
    #ent_f=Entry(cnv_formulas,width=45)
    ent_f.delete(0,"end")
    ent_f.insert(0,p[1])
    ent_f.place(x=right(lbl_eq),y=yprev)
    
    print("p=",p,"G.error=",G.error)
    if G.error==p[0]:
      if not G.error == "":G.showDlg="Error"
      
    

    #print("p=",p,"G.error=",G.error,"ent_name['fg']=", ent_name["fg"])
    def enter(a):   
      print("a=",a)
      if a==1 or a==2:
        G.error=G.calc()
        if not  G.error=="": G.showDlg="Error"
        else: G.showDlg="No"
        forget()
      else: return
    ent_f.bind("<Return>",lambda event, a=1: enter(a))
    ent_name.bind("<Return>",lambda event, a=2: enter(a))
    yprev+=btn_n.winfo_height()

  # draw graph
  fr_graph=tk.Frame(window,height=G.heightForm,bg="blue")
  fr_graph.pack(side=TOP,fill=BOTH,expand=True)
  cnv_graph=Canvas(fr_graph,width=fr_graph["width"],height=fr_graph["height"],bg="light blue")

  cnv_graph.place(x=G.widthForm,y=0)
  cnv_graph.pack(fill=BOTH,side=LEFT, expand=YES)       
  cnv_graph.pack(fill=BOTH,expand=True)
  cnv_graph.update()
    
  #G.error=G.calc()

  print("drawing...")
  print("G.lstBadNames=",G.lstBadNames)
  draw(cnv_graph,cnv_graph.winfo_width(),cnv_graph.winfo_height(),G,fr_dlg,fr_tools,fr_form, fr_graph)
  def on_resize(e): 
    forget()
    draw(cnv_graph,e.width,e.height,G,fr_dlg,fr_tools,fr_form, fr_graph) 
  cnv_graph.bind("<Configure>", on_resize)
  #print("end of draw",G.downX,G.upX)
  G.downX=-1
  

######################################################
window = tk.Tk()
#setting tkinter window size
widthW= window.winfo_screenwidth()/1.3
heightW= window.winfo_screenheight()/2
window.geometry("%dx%d" % (widthW, heightW))

G=GUIntf()
G.getData(G.symbols[0])
window.title("Lemcat calculator")
star1(window)

#G.clearErrors()

window.mainloop()






