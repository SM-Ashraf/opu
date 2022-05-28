from tkinter import *
import sqlite3

root=Tk()
root.title("Find Your Docter ")
## root.geometry("400*600")
root.config(background="#12a4d9")
##root.resizable(0,0)



def neuro():





    msg=Message(root,text="neuro doctors are : "+" "+"\n"
                          "1.Dr.Pradip Kumar Kayasthagir"+" "+"\n"
                          "MBBS ,MD(NeuroMedicine)"+" "+"\n"
                          "Brain,Stroke,Nerve,Medicine&NeuroMedicine"+" "+"\n"
                          "Chittagong Medical College"+" "+"\n"
                                    "Chember & appointment"+" "+"\n"
                                    "Epic HealthCare,Chittagong"+" "+"\n"
                                    "Visiting hour:6pm to 8pm(closed:friday)"+" "+"\n"
                                    "Mobile No:01984499600"+" "+"\n",
                font=("Comic sans MS",20,"bold"),
                fg="#e75874",
                bg="#be1558"

                )
    msg.pack()
def medicine():
    msg=Message(root,
                text="Medicine Docter Are:"+" ""\n"
                     "1.Dr.Syed Selim Sarwar"+" ""\n"
                     "MBBS,FCPS(Medicine)"+" ""\n"
                     "Chamber 1:CSCR,CTG(Friday Closed)"+" ""\n"
                     "Mobile no:01819045535"+" ""\n"
                     "Chamber2:New star lab limited ,GEC"+" ""\n"
                     "Mobile no:01819045535"+" ""\n"
                     "Chamber3:Alfa lab,Chadgaon(closed friday)"+" ""\n"
                     "Mobile No:01779393371"+" ""\n",
                font=("Comic sans MS", 20, "bold"),
                fg="#e75874",
                bg="#be1558",


                )
    msg.pack()
def startIspressed():
    Labeltext.destroy()
    Labeltext2.destroy()
    btn_enter.destroy()
    lbl_instruction.destroy()
    lbl_rules.destroy()
    btn_neuro= Button(root, text="Neuro docter ",fg="white",bg="#1e3d59",font=("Comic sans MS",17,"bold"), command=neuro)
    btn_neuro.pack()
    btn_medicine = Button(root, text="Medicine docter",fg="white",bg="#1e3d59",font=("Comic sans MS",17,"bold"),command=medicine)
    btn_medicine.pack()

    startIspressed.close()









Labeltext=Label(
    root,
    text="Welcome To Find Your Docter App",
    font=("Comic sans MS",24,"bold")
)
Labeltext.pack(pady=40)



Labeltext2=Label(
    root,
    text="Here You can find Docter number &Address in Chittagong.You Can also find blood Doner number in Chittagong and Rangamaty area",
    font=("Comic sans MS",18,"bold"),
    fg="Navyblue",
    bg="#e52165"
)
Labeltext2.pack(pady=(0,50))

btn_enter=Button(
    root,
    text="Enter",
    font=("Comic Sans MS",50,"bold"),
    bg="#e75874",
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btn_enter.pack(pady=80)


lbl_instruction=Label(
    root,
    text="Read The Rules And Regulation\nclick start once You are ready",
    background="#ffffff",
    font=("Consolas",14),

)
lbl_instruction.pack(pady=(10,100))
lbl_rules=Label(
    root,
    text="Don't Call Docter&Blood Doner Without any reason",
    width=100,
    font=("Times",14),
    background="#000000",
    fg="#FACA2F"
)

lbl_rules.pack()











root.mainloop()