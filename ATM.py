from tkinter import *
from tkinter import messagebox as msg

# login page 
# ----------------------------------------------------------------
frame=Tk()
l1=Label(frame,text="Pin")
t1=Entry(frame,show="*")
Bal=[10000]


   # Bank menu page 
   # ----------------------------------------------------------------

def Bank():
    pin="123456"
    if (t1.get()==pin):
        # msg.showinfo("Balance",f"Your account balance is: {Bal}")
        frame1=Toplevel()
        frame1.geometry("400x150")
        frame1.title("Main menu")
        L1=Label(frame1,text="Welcome to our Bank")

        # -----------------------------------------------------------------
        def Balance():
                frame2=Toplevel()
                frame2.title("Balance form")
                frame2.geometry("200x200")
                l1=Label(frame2,text="pin")
                t1=Entry(frame2,show="*")    
                
                # Account Balance
                # ----------------------------------------------------------
                def Check_Balance():

                        if (t1.get()==pin):
                                l2.config(text=Bal[0])

                        else:
                                msg.showwarning("warning","Wrong PIN")
                                t1.delete(0,"end")
                l2=Label(frame2,text="")
                l3=Label(frame2,text="Balance: ₹")
                b=Button(frame2,text="Show Balance",command=Check_Balance)
                l1.grid(row=0,column=0)
                t1.grid(row=0,column=1)

                l2.place(x=65,y=150)
                l3.place(x=10,y=150)

                b.grid(row=1,column=1)
                frame2.mainloop()
                #-----------------------------------------------------------


        # Amount withdraw page
        #-------------------------------------------------------------------------
        def Withdraw():
                frame3=Toplevel()
                frame3.title("Withdraw form")
                frame3.geometry("300x200")
                l1=Label(frame3,text="pin")
                l2=Label(frame3,text="Amount: ")
                
                t1=Entry(frame3,show="*")   
                t2=Entry(frame3)

                # withdraw function
                # -------------------------------------------------------------------
                def Withdraw_amount():
                        withdraw=int(t2.get())
                        balance=Bal[0]
                        if (t1.get()==pin):
                                if (withdraw>0) and (withdraw < balance):
                                        Amount=balance-withdraw
                                        Bal[0]=Amount
                                        l3.config(text=Amount)
                                        t2.delete(0,"end")
                                else:
                                        msg.showwarning("Warning","Insufficient Balance ")
                                        t2.delete(0,"end")
                                       
                        else:
                                 msg.showwarning("wrong","Wrong PIN")
                                 t1.delete(0,"end")
                # ------------------------------------------------------------------------


                l3=Label(frame3,text="")
                l4=Label(frame3,text="Balance: ₹")
                b=Button(frame3,text="Withdraw Amount",command=Withdraw_amount)


                l1.grid(row=0,column=0)
                t1.grid(row=0,column=1)
                l2.grid(row=1,column=0)
                t2.grid(row=1,column=1)

                
                b.grid(columnspan=2)
                l3.place(x=65,y=150)
                l4.place(x=10,y=150)
                frame3.mainloop()
                # -----------------------------------------------------------------

        # Deposit page
        #---------------------------------------------------------------------------------

        def Deposit():
                frame4=Toplevel()
                frame4.title("Deposit form")
                frame4.geometry("300x200")
                l1=Label(frame4,text="pin")
                l2=Label(frame4,text="Amount: ")
                t1=Entry(frame4,show="*")   
                t2=Entry(frame4)
                
                # Deposit function
                # ---------------------------------------------------------------------------
                def Deposit_amount():
                        deposit=int(t2.get())
                        balance=Bal[0]
                        if (t1.get()==pin and (deposit>0)):
                                Amount=balance+deposit
                                Bal[0]=Amount
                                l3.config(text=Amount)
                                t2.delete(0,"end")
                        else:
                                msg.showwarning("wrong","Wrong Pin !!!!")
                                t1.delete(0,"end")
                # -----------------------------------------------------------------------------

                l3=Label(frame4,text="")
                l4=Label(frame4,text="Balance: ₹")
                b=Button(frame4,text="Deposit Amount",command=Deposit_amount)

                l1.grid(row=0,column=0)
                t1.grid(row=0,column=1)

                l2.grid(row=1,column=0)
                t2.grid(row=1,column=1)

                b.grid(columnspan=2)

                l3.place(x=65,y=150)
                l4.place(x=10,y=150)

                frame4.mainloop()
                # ---------------------------------------------------------------------------------------
        
        # Cancel page
        # --------------------------------------------------------------------------
        def Destroy():
                frame.destroy()
        # --------------------------------------------------------------------------


        B1=Button(frame1,text="Withdraw",command=Withdraw)
        B2=Button(frame1,text="Deposit",command=Deposit)
        B3=Button(frame1,text="Balance",command=Balance)
        B4=Button(frame1,text="Cancel",command=Destroy)

        L1.place(x=130,y=10)
        B1.place(x=100,y=50)
        B2.place(x=220,y=50)
        B3.place(x=100,y=100)
        B4.place(x=220,y=100)
        frame.mainloop()
        # ---------------------------------------------------------------------------
    else:
        msg.showwarning("warning","Wrong PIN")
        t1.delete(0,"end")

b=Button(frame,text="Enter",command=Bank)
l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
b.grid(row=1,column=1)
frame.title("ATM")
frame.geometry("200x100")
frame.mainloop()

# ------------------------------------------------------------------------------------
