from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"
            
      row = i//3
      col = i%3
      
      #가로줄에서 게임을 이기는 조건을 확인함
      if list[row*3]["text"] == list[row*3+1]["text"] == list[row*3+2]["text"] :
            winner(row)
      #세로줄에서 게임을 이기는 조건을 확인함
      elif list[col]["text"] == list[col+3]["text"] == list[col+6]["text"] :
            winner(col)
      #대각선에서 게임을 이기는 조건을 확인함
      elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     " or list[2]["text"] == list[4]["text"] == list[6]["text"] !="     " :
            winner(4)

#승자를 출력하는 
def winner(i) :
      msg = Label(window, text = "winner is " + list[i]["text"])
      msg.grid(row=3, column=1)

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


