# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 19:14:58 2025

@author: USER
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#%%

#分析台灣國民平均所得

taiwan_economy = pd.read_csv('taiwan_economy.csv', encoding='big5')
taiwan_economy.info()
print(list(taiwan_economy.columns))
taiwan_economy = taiwan_economy.iloc[:-4]


# taiwan_economy["經濟成長率(%)"] = taiwan_economy["經濟成長率(%)"].astype(str)

import matplotlib
matplotlib.rc('font', family='Microsoft JhengHei')


plt.figure(figsize=(14,8),facecolor="cyan")    #要放plot前
plt.plot(taiwan_economy["統計期"], taiwan_economy["平均每人所得(元)"],"r-*", label="平均每人所得(元)")
plt.xlabel("年份")
plt.ylabel("國人平均所得（年薪）")
plt.title("台灣近十年國民平均所得")
plt.rcParams.update({'font.size': 20})  #調整字體大小
ax = plt.gca()
ax.set_facecolor("lightyellow")
plt.grid()
plt.legend()
plt.show()



#%%

#日本平均年齡

world_age = pd.read_csv('world_age.csv')
world_age.info()

world_age[["男性零歲平均餘命(歲)","女性零歲平均餘命(歲)"]] = world_age[["男性零歲平均餘命(歲)","女性零歲平均餘命(歲)"]].apply(lambda x:pd.to_numeric(x,errors="coerce").fillna(0))
print(world_age)    #轉成float


japan_age = world_age[world_age["國別"] == "日本"]
japan_age.info()
print(japan_age)


plt.figure(figsize=(14,8),facecolor="cyan")    #要放plot前
plt.plot(japan_age[japan_age["西元年"] <= 2020]["西元年"], japan_age[japan_age["西元年"] <= 2020]["男性零歲平均餘命(歲)"], "b-o", label="男性平均年紀 實際值")
plt.plot(japan_age[japan_age["西元年"] >= 2020]["西元年"], japan_age[japan_age["西元年"] >= 2020]["男性零歲平均餘命(歲)"], "b--o", label="男性平均年紀 推估值")
plt.plot(japan_age[japan_age["西元年"] <= 2020]["西元年"], japan_age[japan_age["西元年"] <= 2020]["女性零歲平均餘命(歲)"], "r-o", label="女性平均年紀 實際值")
plt.plot(japan_age[japan_age["西元年"] >= 2020]["西元年"], japan_age[japan_age["西元年"] >= 2020]["女性零歲平均餘命(歲)"], "r--o", label="女性平均年紀 推估值")
plt.xlabel("年份")
plt.ylabel("平均年紀（歲）")
plt.title("日本國民平均歲數")
plt.rcParams.update({'font.size': 20})  #調整字體大小
ax = plt.gca()
ax.set_facecolor("lightyellow") #表底顏色
plt.xlim(1960,2080) #設定範圍
plt.ylim(55,100)
plt.xticks(np.arange(1960,2080,10)) #細分x軸顯示數值
plt.grid()
plt.legend()
plt.show()


#%%

#韓國平均年齡

korea_age = world_age[world_age["國別"] == "韓國"]
korea_age.info()
print(korea_age)


plt.figure(figsize=(14,8),facecolor="cyan")    #要放plot前
plt.plot(korea_age[korea_age["西元年"] <= 2020]["西元年"], korea_age[korea_age["西元年"] <= 2020]["男性零歲平均餘命(歲)"], "b-o", label="男性平均年紀 實際值")
plt.plot(korea_age[korea_age["西元年"] >= 2020]["西元年"], korea_age[korea_age["西元年"] >= 2020]["男性零歲平均餘命(歲)"], "b--o", label="男性平均年紀 推估值")
plt.plot(korea_age[korea_age["西元年"] <= 2020]["西元年"], korea_age[korea_age["西元年"] <= 2020]["女性零歲平均餘命(歲)"], "r-o", label="女性平均年紀 實際值")
plt.plot(korea_age[korea_age["西元年"] >= 2020]["西元年"], korea_age[korea_age["西元年"] >= 2020]["女性零歲平均餘命(歲)"], "r--o", label="女性平均年紀 推估值")
plt.xlabel("年份")
plt.ylabel("平均年紀（歲）")
plt.title("韓國國民平均歲數")
plt.rcParams.update({'font.size': 20})  #調整字體大小
ax = plt.gca()
ax.set_facecolor("lightyellow") #表底顏色
plt.xlim(1960,2080) #設定範圍
plt.ylim(55,100)
plt.xticks(np.arange(1960,2080,10)) #細分x軸顯示數值
plt.grid()
plt.legend()
plt.show()


#%%

#美國平均年齡

usa_age = world_age[world_age["國別"] == "美國"]
usa_age.info()
print(usa_age)


plt.figure(figsize=(14,8),facecolor="cyan")    #要放plot前
plt.plot(usa_age[usa_age["西元年"] <= 2020]["西元年"], usa_age[usa_age["西元年"] <= 2020]["男性零歲平均餘命(歲)"], "b-o", label="男性平均年紀 實際值")
plt.plot(usa_age[usa_age["西元年"] >= 2020]["西元年"], usa_age[usa_age["西元年"] >= 2020]["男性零歲平均餘命(歲)"], "b--o", label="男性平均年紀 推估值")
plt.plot(usa_age[usa_age["西元年"] <= 2020]["西元年"], usa_age[usa_age["西元年"] <= 2020]["女性零歲平均餘命(歲)"], "r-o", label="女性平均年紀 實際值")
plt.plot(usa_age[usa_age["西元年"] >= 2020]["西元年"], usa_age[usa_age["西元年"] >= 2020]["女性零歲平均餘命(歲)"], "r--o", label="女性平均年紀 推估值")
plt.xlabel("年份")
plt.ylabel("平均年紀（歲）")
plt.title("美國國民平均歲數")
plt.rcParams.update({'font.size': 20})  #調整字體大小
ax = plt.gca()
ax.set_facecolor("lightyellow") #表底顏色
plt.xlim(1960,2080) #設定範圍
plt.ylim(55,100)
plt.xticks(np.arange(1960,2080,10)) #細分x軸顯示數值
plt.grid()
plt.legend()
plt.show()


#%%

#英國平均年齡

uk_age = world_age[world_age["國別"] == "英國"]
uk_age.info()
uk_age = uk_age.iloc[2:]    #前兩列為non
print(uk_age)


plt.figure(figsize=(14,8),facecolor="cyan")    #要放plot前
plt.plot(uk_age[uk_age["西元年"] <= 2020]["西元年"], uk_age[uk_age["西元年"] <= 2020]["男性零歲平均餘命(歲)"], "b-o", label="男性平均年紀 實際值")
plt.plot(uk_age[uk_age["西元年"] >= 2020]["西元年"], uk_age[uk_age["西元年"] >= 2020]["男性零歲平均餘命(歲)"], "b--o", label="男性平均年紀 推估值")
plt.plot(uk_age[uk_age["西元年"] <= 2020]["西元年"], uk_age[uk_age["西元年"] <= 2020]["女性零歲平均餘命(歲)"], "r-o", label="女性平均年紀 實際值")
plt.plot(uk_age[uk_age["西元年"] >= 2020]["西元年"], uk_age[uk_age["西元年"] >= 2020]["女性零歲平均餘命(歲)"], "r--o", label="女性平均年紀 推估值")
plt.xlabel("年份")
plt.ylabel("平均年紀（歲）")
plt.title("英國國民平均歲數")
plt.rcParams.update({'font.size': 20})  #調整字體大小
ax = plt.gca()
ax.set_facecolor("lightyellow") #表底顏色
plt.xlim(1960,2080) #設定範圍
plt.ylim(55,100)
plt.xticks(np.arange(1960,2080,10)) #細分x軸顯示數值
plt.grid()
plt.legend()
plt.show()


#%%

#西班牙平均年齡

spain_age = world_age[world_age["國別"] == "西班牙"]
spain_age.info()
spain_age = spain_age.iloc[1:]    #前兩列為non
print(spain_age)


plt.figure(figsize=(14,8),facecolor="cyan")    #要放plot前
plt.plot(spain_age[spain_age["西元年"] <= 2020]["西元年"], spain_age[spain_age["西元年"] <= 2020]["男性零歲平均餘命(歲)"], "b-o", label="男性平均年紀 實際值")
plt.plot(spain_age[spain_age["西元年"] >= 2020]["西元年"], spain_age[spain_age["西元年"] >= 2020]["男性零歲平均餘命(歲)"], "b--o", label="男性平均年紀 推估值")
plt.plot(spain_age[spain_age["西元年"] <= 2020]["西元年"], spain_age[spain_age["西元年"] <= 2020]["女性零歲平均餘命(歲)"], "r-o", label="女性平均年紀 實際值")
plt.plot(spain_age[spain_age["西元年"] >= 2020]["西元年"], spain_age[spain_age["西元年"] >= 2020]["女性零歲平均餘命(歲)"], "r--o", label="女性平均年紀 推估值")
plt.xlabel("年份")
plt.ylabel("平均年紀（歲）")
plt.title("西班牙國民平均歲數")
plt.rcParams.update({'font.size': 20})  #調整字體大小
ax = plt.gca()
ax.set_facecolor("lightyellow") #表底顏色
plt.xlim(1960,2080) #設定範圍
plt.ylim(55,100)
plt.xticks(np.arange(1960,2080,10)) #細分x軸顯示數值
plt.grid()
plt.legend()
plt.show()


#%%

#挪威平均年齡

norway_age = world_age[world_age["國別"] == "挪威"]
norway_age.info()
# norway_age = norway_age.iloc[1:]    #前兩列為non
print(norway_age)


plt.figure(figsize=(14,8),facecolor="cyan")    #要放plot前
plt.plot(norway_age[norway_age["西元年"] <= 2020]["西元年"], norway_age[norway_age["西元年"] <= 2020]["男性零歲平均餘命(歲)"], "b-o", label="男性平均年紀 實際值")
plt.plot(norway_age[norway_age["西元年"] >= 2020]["西元年"], norway_age[norway_age["西元年"] >= 2020]["男性零歲平均餘命(歲)"], "b--o", label="男性平均年紀 推估值")
plt.plot(norway_age[norway_age["西元年"] <= 2020]["西元年"], norway_age[norway_age["西元年"] <= 2020]["女性零歲平均餘命(歲)"], "r-o", label="女性平均年紀 實際值")
plt.plot(norway_age[norway_age["西元年"] >= 2020]["西元年"], norway_age[norway_age["西元年"] >= 2020]["女性零歲平均餘命(歲)"], "r--o", label="女性平均年紀 推估值")
plt.xlabel("年份")
plt.ylabel("平均年紀（歲）")
plt.title("挪威國民平均歲數")
plt.rcParams.update({'font.size': 20})  #調整字體大小
ax = plt.gca()
ax.set_facecolor("lightyellow") #表底顏色
plt.xlim(1960,2080) #設定範圍
plt.ylim(55,100)
plt.xticks(np.arange(1960,2080,10)) #細分x軸顯示數值
plt.grid()
plt.legend()
plt.show()


#%%

#台灣平均年齡

taiwan_age = world_age[world_age["國別"] == "中華民國"]
taiwan_age.info()
# taiwan_age = taiwan_age.iloc[1:]    #前兩列為non
print(taiwan_age)


plt.figure(figsize=(14,8),facecolor="cyan")    #設定圖表大小和背景顏色要放plot前
plt.plot(taiwan_age[taiwan_age["西元年"] <= 2020]["西元年"], taiwan_age[taiwan_age["西元年"] <= 2020]["男性零歲平均餘命(歲)"], "b-o", label="男性平均年紀 實際值")
plt.plot(taiwan_age[taiwan_age["西元年"] >= 2020]["西元年"], taiwan_age[taiwan_age["西元年"] >= 2020]["男性零歲平均餘命(歲)"], "b--o", label="男性平均年紀 推估值")
plt.plot(taiwan_age[taiwan_age["西元年"] <= 2020]["西元年"], taiwan_age[taiwan_age["西元年"] <= 2020]["女性零歲平均餘命(歲)"], "r-o", label="女性平均年紀 實際值")
plt.plot(taiwan_age[taiwan_age["西元年"] >= 2020]["西元年"], taiwan_age[taiwan_age["西元年"] >= 2020]["女性零歲平均餘命(歲)"], "r--o", label="女性平均年紀 推估值")
plt.xlabel("年份")
plt.ylabel("平均年紀（歲）")
plt.title("台灣國民平均歲數")
plt.rcParams.update({'font.size': 20})  #調整字體大小
ax = plt.gca()
ax.set_facecolor("lightyellow") #表底顏色
# ax1 = ax.twinx()
# ax1.set_ylabel("平均年紀（歲）")  # 右側 y 軸
# ax1.tick_params(axis='y')  # 設定右側 y 軸
# ax1.set_ylim(55,100)
plt.xlim(1960,2080) #設定範圍
plt.ylim(55,100)
plt.xticks(np.arange(1960,2080,10))
plt.grid()
plt.legend()
plt.show()


#%%

taiwan_life = pd.read_csv('taiwan_life.csv')
# taiwan_life.info()
taiwan_life_25 = taiwan_life[taiwan_life["西元年"] == 2025]
# taiwan_life_25.info()

taiwan_life_25["年齡"] = taiwan_life_25["年齡"]. str.replace("歲及以上","")
taiwan_life_25["年齡"] = taiwan_life_25["年齡"]. str.replace("歲","")
taiwan_life_25["性別"] = taiwan_life_25["性別"]. str.replace("性","")
taiwan_life_25["年齡"] = pd.to_numeric(taiwan_life_25["年齡"])
# taiwan_life_25.info()

age = int(input("請輸入您的年紀 : "))
if age < 0 or age > 100:
    print("請輸入正確年紀,0~100的整數")
else:
    sex = input("請選擇您的性別(男 / 女): ")
    sex = sex.lower()
    if sex == "男":
        print("您輸入的是男性 ," , age ,"歲")
    elif sex == "女":
        print("您輸入的是女性 ," , age ,"歲")
    else:print("請輸入正確性別")
    
filtered_taiwan_life_25 = taiwan_life_25[(taiwan_life_25["年齡"] == age) & (taiwan_life_25["性別"] == sex)]
if filtered_taiwan_life_25.empty:
    print("沒有找到符合條件的數據")
else:pass
    # print("找到的數據：")
    # print(filtered_taiwan_life_25["預期壽命"])
       
result = (filtered_taiwan_life_25.iloc[0]["預期壽命"])
# print(result)
    
h = int(input("請輸入您的身高cm : "))
w = int(input("請輸入您的體重kg : "))
bmi = w/(h/100)**2
if bmi < 18.5:
    result = result-4.3
elif 18.5 <= bmi <24:
    result = result+1
elif 24 <= bmi <27:result = result-3.8
else:result = result-10

smoke = str(input("您是否吸菸(Y/N) : "))
smoke = smoke.upper()
if smoke == "Y":result = result-10
else:pass

emo = str(input("您是樂觀的人嗎?(Y/N) : "))
emo = emo.upper()
if emo == "N":result = result-2   
else:result = result+2

sport = str(input("您是否有運動的習慣?(Y/N) : "))
sport = sport.upper()
if sport == "N":result = result-1   
else:result = result+2

print(f"您的生命剩餘:{result:.2f}年")
    
    
    
    