#請將底線部分，修改為可正確運行的程式碼 :)

import ________________ 

def draw(deck,hand): #抽牌函式:...
  ________________

def Have11(hand): #11轉換成1判斷函式:內包含in運算子語法、...
  ________________

def separator(): #輸出分隔線函式:...
  ________________


start=True
print("歡迎進入21點遊戲!")


while(start ________________ ):

  card_list = [ ________________ ] * ________________ #建立牌組
  player_cards = ________________
  dealer_cards = ________________


  print("<遊戲開始>")

  i=0 #初始發牌
  while(i<________________): 
    ________________ 
    ________________


  print(f"玩家的牌: { ________________ }") #輸出玩家明牌
  print("莊家的明牌:"+str(dealer_cards[ ________________ ])) #輸出莊家明牌

  while True: #玩家計算點數
    ________________ 
    if(sum(player_cards)>21): #判斷是否大於21點
      ________________

    print("是否加牌?(y:是;n:否)") #判斷玩家是否加牌
    add_card = ________________ 
    if(add_card == "n"):
      break
    elif(add_card == "y"):
      ________________ 
    else:
      print("輸入格式不符，請重新輸入")



  ________________ 
  print("<遊戲結算>")

  player_points = sum( ________________ )
  print(f"玩家的牌:{ ________________ }") #輸出玩家牌和總和
  print(f"玩家點數總和:{ ________________ }")

  while True: #莊家計算點數(函數)
    ________________
    if(sum(dealer_cards)<17): #判斷是否小於17點
      ________________
    else:
      ________________ 

  dealer_points = sum(dealer_cards)
  print(f"莊家的牌:{ ________________ }") #輸出莊家牌和總和
  print(f"莊家點數總和:{ ________________ }")


  win = "y"  #判斷輸贏條件
  if(player_points>21):
    print("你爆了!")
    win = ________________
  elif(dealer_points > 21):
    print("莊家爆了!")
  elif(player_points > dealer_points):
    print("你的點數大於莊家")
  elif(player_points == dealer_points):
    print("平手")
    win = ________________
  else:
    print("你的點數小於莊家")
    win = ________________

  if(win == "y"): #判斷輸贏
    print("result:你贏了!")
  elif(win == "n"):
    print("result:你輸了!")
  ________________

  start=False
