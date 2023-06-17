from tkinter import * 
from tkinter import ttk

root = Tk()
style = ttk.Style()
root.title("Calculator Hello Kitty")
root.geometry("400x500")
root.resizable(False,False)
root["bg"]="pink" 

def close():root.destroy()
root.protocol("WM_DELETE_WINDOW",close)

frame = LabelFrame(root, width=360, height = 100, bg = "white",fg="#1b181a",text = "0", borderwidth=0, font =("Arial", 20, "bold"))
frame.grid(row=0,column=0,columnspan=4,padx=20,pady = 20)

def action(event):
    try:
        get_text = event.widget.cget("text")
        if frame["text"] == "0":
            frame["text"] = get_text
        else: frame["text"] += get_text
        if get_text == "=":
            frame["text"] = str(eval(frame["text"][:-1]))
        elif get_text == "C":
            frame["text"] = '0'
        elif get_text == "DEL":
            frame["text"] = frame["text"][:-4]
    except:
        frame["text"] = "ERROR!" + "\n (ᕗ ͠° ਊ ͠° )ᕗ"   

btn_object =[]
for r in range(5):
    for c in range(4):
        btn = Button(width=10, bg = "pink", fg ="black",borderwidth=1,relief="solid",highlightcolor="red")
        btn.grid(row=r+1, column=c,ipady=10, padx=5, pady = 10)
        btn.bind("<Button-1>",action)
        btn_object.append(btn)

btn_object[19].destroy()
btn_object[15].grid(row=4, column=3,ipady=50, padx=5, pady = 10, rowspan = 2)

btns_text = ["C","DEL","%","/",
            "7","8","9","*",
            "4","5","6","-",
            "1","2","3","+",
            "0",".","="]
for index,item in enumerate(btns_text): btn_object[index]["text"]=item

root.mainloop()