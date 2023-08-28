import random
#import matplotlib.pyplot as plt
#import plotly.express as px
import pandas as pd
import numpy as np
import datetime as dt
import schedule
import pandas_datareader.data as web
import time

#======================================================================================================================================
#추가해야 할 매개 변수
#언론
#공급 및  소비
#   자연재해    언론    
#
#======================================================================================================================================

event_bia = 0

stock_default = 5

default_cash = 100000
default_assets = []
default_stock_cost_log = []
default_stock_damand = 0
default_cost = 10000



선동계수 = 1

국민소득지수 = 0

공급지수 = 5

수요지수= 5 

stock_cost_shift_bia = 5 # 1~10 10으로 갈 수록 주가가 상승할 확률이 높아지며 낮아질 수록 변화가 -가 됨.

stock_list = ["삼성","LG","두산","SK텔레콤","대한항공","네이버","카카오","한컴"]
time = [0] # 30s


def get_stock_shift(공급지수,수요지수):

    result = max(공급지수,수요지수) - min(공급지수,수요지수)
    return result

#class news:
    def __init__(self,name,bia):#이름,명사,뉴스의 보도 편향 1:사실적 2:편파 3.가십
        self.name = name
        self.bia = bia
        
#news("Times","Times",1) #세계적인 언론 보도사.모든 사건에 대해 매우 중립적인 태도로 보도
#news("ABC","ABC",2) #ABC 계열 사의 언론 보도사.ABC 그룹 회사의 행보에 대해서 편파적으로 보도
#news("CNN","CNN",3) #잡지 성향이 강한 언론 보도사,가십과 같은 자극적인 보도

def enter_term(term,function): # 기준 : 초
    schedule.every(term).seconds.do(function)

def save_progress_data(): # 현재 시간 시계열 데이터에 입력 및 
    print("현재 진행 상황을 저장합니다.")  
    now = dt.now()
    time.append(now)
    for stock in stock_list:
        stock
    
    
    
def load_before_data():
    print("이전 시간대 데이터를 불러옵니다.")

class user: # 유저 이름,보유 현금,보유 자산
    def __init__(self,name,money,asset) -> None:
        self.name = name # 유저 이름
        self.money = money # 보유 현금
        self.asset = asset # 보유 자산

class stock: # 주식 명칭,주가,주식 수요,주가 로그
    def __init__(self,name,stock_cost,stock_demand,stock_cost_log):
        self.name = name
        self.stock_cost = stock_cost
        self.stock_demand = stock_demand
        self.stock_cost_log = stock_cost_log
        
        
    def stock_cost_change(self):
        print(f"{self.name} 주식의 주가를 변동합니다.")
        
        print(f"현재 주가 : {self.stock_cost}")
        print(f"현재 주식 수요 : {self.stock_demand}")
        #print(f"현재 국민 소득 지수 : {국민소득지수}")
        print(f"현재 선동계수 : {선동계수}")


    def save_stock_cost_progress(self,cost):
        cost_log = self.stock_cost_log
        stock_cost = int(self.stock_cost)
        cost_log.append(stock_cost)
        
    def get_stock_cost(self):
        
        return(self.stock_cost)
    
    def check_stock_element(self):
        self.name = 1
        
    def buy_stock(self,user_self,number):
        cost = int(self.stock_pric) # 주가
        cash = int(user_self.money)
        cash -= cost * int(number) # 구매자 보유 현금 + 주가 * 개수
        user_self.money = cash
        user_self.asset += number # 보유 자산 + 구매 개수
        
    def sell_stock(self,user_self,number):
        
        cost = int(self.stock_pric) # 주가
        cash = int(user_self.money)
        cash += cost * int(number) # 판매자 보유 현금 + 주가 * 개수
        user_self.money = cash
        user_self.asset -= number # 보유 자산 - 판매 개수
        
for stock_name in stock_list:
    stock(stock_name,default_cost,default_stock_damand,default_stock_cost_log)


print("가나다라마바사")
