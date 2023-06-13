
#final
from tkinter import *
from tkinter import ttk
import datetime
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
from tkcalendar import *
now = datetime.datetime.now()

#sqlite connection
con = sqlite3.Connection('hm_proj.db')
cur = con.cursor()
cur.execute("create table if not exists roomd(rn number primary key,beds number,ac varchar(10),tv varchar(10),internet varchar(10),price number(10))")
cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar,checkindate varchar, checkoutdate varchar)")
con.commit()


def mainroot():

	root = Tk()
	root.geometry('1080x500')
	root.minsize(width=1080,height=550)
	root.maxsize(width=1080,height=550)
	root.configure(bg='white')
	root.title("Hotel Mangement System")


	#Main frame

	top_frame = Frame(root,height=70,width=1080,bg='gray89')
	top_frame.place(x=0,y=0)
	tf_label = Label(top_frame,text='Hotel Management System',font='msserif 33',fg='black',bg='gray89',height=70)
	tf_label.pack(anchor='center')
	top_frame.pack_propagate(False)



	#Hotel status page

	def hotel_status():
		global b_frame
		b_frame = Frame(root,height=400,width=1080,bg='gray91')
		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		cur.execute("select count(rn) from roomd")
		x = cur.fetchone()
		cur.execute("select count(rn) from roomd where rstatus = 'Reserved'")
		y = cur.fetchone()
		tor = x[0]
		rer = y[0]
		tos = 21
		avr = int(tor)-int(rer)
		avr = str(avr)
		hts = Label(b_frame,text='Hotel Status',font='msserif 15',fg='black',bg='gray91',height=1)

	#inner frames of bottom frame

		smf1 = Frame(b_frame,height=150,width=175,bg='white')
		tr = Label(smf1,text='Total Rooms:',fg='white',bg='cyan4',width=100,height=2,font='helvetica 15')
		tr.pack(side='top')
		smf1.pack_propagate(False)
		smf1.place(x=30,y=30)
		Label(smf1,text=tor,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

		smf2 = Frame(b_frame,height=150,width=175,bg='white')
		ar = Label(smf2,text='Available Rooms:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		ar.pack(side='top')
		smf2.pack_propagate(False)
		smf2.place(x=440+4,y=30)
		Label(smf2,text=avr,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

		smf3 = Frame(b_frame,height=150,width=175,bg='white')
		tre = Label(smf3,text='Total reservations:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		tre.pack(side='top')
		smf3.pack_propagate(False)
		smf3.place(x=860+6,y=30)
		Label(smf3,text=rer,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')


		redf1 = Frame(b_frame,height=8,width=1080,bg='cyan4')




		redf1.place(x=0,y=22)
		Label(b_frame,text='Hotel Status',font='msserif 12',bg='cyan4',fg='white').pack(anchor='center')
		redf1.pack_propagate(False)



	#records page

	def records():
		b_frame = Frame(root,height=300,width=1080,bg='white')

		# Frame(b_frame,height=13,width=250,bg='white').place(x=410,y=2)
		# Frame(b_frame,height=13,width=250,bg='white').place(x=410,y=153)

		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()
		db_frame = Frame(root, height=100, width=1080, bg='white')
		db_frame.place(x=0,y = 120+6+20+60+11+300)
		db_frame.pack_propagate(False)
		db_frame.tkraise()

		tv = ttk.Treeview(b_frame)
		tv['columns'] = ('SR', 'firstName', 'lastName','Contact','Email','roomNo','checkindate','checkoutdate')

		tv.column('#0', width=0, stretch=NO)
		tv.column('SR', anchor = CENTER , width = 50)
		tv.column('firstName', anchor='w', width=135)
		tv.column('lastName', anchor='e', width=135)
		tv.column('Contact', anchor='w', width=135)
		tv.column('roomNo', anchor=CENTER, width=135)
		tv.column('checkindate', anchor=CENTER, width=135)
		tv.column('checkoutdate', anchor=CENTER, width=135)
		tv.column('Email', anchor='w', width=220)

		tv.heading('#0', text='', anchor=CENTER)
		tv.heading('SR', anchor=CENTER, text = 'SR')
		tv.heading('firstName', anchor=CENTER, text= 'First Name')
		tv.heading('lastName', anchor=CENTER, text='Last Name')
		tv.heading('Contact', anchor=CENTER, text='Contact')
		tv.heading('roomNo', anchor=CENTER, text = 'Room No.')
		tv.heading('checkindate', anchor=CENTER, text = 'Check In')
		tv.heading('checkoutdate', anchor=CENTER, text = 'Check Out')
		tv.heading('Email', anchor=CENTER, text = 'Email')

		tv.place(x=0 , y = 0 , height = 300 ,width = 1080)

		cur.execute("SELECT id,f_name,l_name,c_number,email,r_n,check_in_date,check_out_date FROM paymentsf")

		data = cur.fetchall()

		for d in data :
			tv.insert('','end', values = (d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]))


		def delete_record():
			try:
				for item in tv.selection():
					item_text = tv.item(item,option = 'values')
				cur.execute("delete from paymentsf where id = '"+item_text[0]+"' ")
				con.commit()
				records()
			except:
				messagebox.showinfo("","Select a Record!")
				records()

		dbutton = Button(db_frame,width = 20,text = 'Delete',font=('Bold',10),bg = 'red',command = lambda : delete_record())
		dbutton.place(x = 500 , y = 2)


	#rooms page
	def rooms():
		b_frame = Frame(root,height=400,width=1080,bg='gray91')
		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()

		sidebuttons = Text(b_frame,width=1,height=19)
		sc = Scrollbar(b_frame,command=sidebuttons.yview,width=10,bg='lightsteelblue3')
		sidebuttons.configure(yscrollcommand=sc.set)
		sc.pack(side='left',fill=Y)
		sidebuttons.place(x=10,y=0)
		def roomdet(rno):
			Label(b_frame,text='Room %s'% rno,font='msserif 15',fg='white',bg='cyan4',width=10).place(x=535,y=0)
			cur.execute("select * from roomd where rn = ?",(rno,))
			rdata=cur.fetchall()
			smf1 = Frame(b_frame,height=120,width=145,bg='white')
			hline = Frame(b_frame,height=10,width=960,bg='cyan4')
			hline.place(x=122,y=27)
			vline = Frame(b_frame,height=400,width=7,bg='lightsteelblue3')
			vline.place(x=122,y=0) 
			tr = Label(smf1,text='Total Bed(s):',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			smf1.pack_propagate(False)
			smf1.place(x=129+3,y=30)
			Label(smf1,text=str(rdata[0][1]),fg='cyan4',bg='white',font='msserif 35').pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text='AC Available?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			smf2.pack_propagate(False)
			smf2.place(x=140*2+5+3*2,y=30)
			Label(smf2,text=str(rdata[0][2]),fg='cyan4',bg='white',font='msserif 35').pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text='TV Available?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			smf2.pack_propagate(False)
			smf2.place(x=140*3+12+5*2+3*3,y=30)
			Label(smf2,text=str(rdata[0][3]),fg='cyan4',bg='white',font='msserif 35').pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text='  Wifi ?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			smf2.pack_propagate(False)
			smf2.place(x=140*4+12*2+5*3+3*4,y=30)
			Label(smf2,text=str(rdata[0][4]),fg='cyan4',bg='white',font='msserif 35').pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text=' Price ?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			smf2.pack_propagate(False)
			smf2.place(x=140*5+12*3+5*4+3*5,y=30)
			Label(smf2,text=str(rdata[0][5]),fg='cyan4',bg='white',font='msserif 35').pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text='Reserved ?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')

			smf2.pack_propagate(False)
			smf2.place(x=140*6+12*4+5*5+3*6,y=30)
			p=''
			if rdata[0][6]=='Unreserved':
				p = 'No'
				Label(smf2, text=p, fg='cyan4', bg='red', font='msserif 35').pack()
			else :
				p = 'Yes'
				Label(smf2, text=p, fg='cyan4', bg='green', font='msserif 35').pack()

		roomdet(1)

		sidebuttons.configure(state='disabled')

		b1  = Button(b_frame,font='mssherif 10', text="Room 1", bg='white',fg='cyan4',width=10,command=lambda:roomdet(1))
		b2  = Button(b_frame,font='mssherif 10', text="Room 2", bg='white',fg='cyan4',width=10,command=lambda:roomdet(2))
		b3  = Button(b_frame,font='mssherif 10', text="Room 3", bg='white',fg='cyan4',width=10,command=lambda:roomdet(3))
		b4  = Button(b_frame,font='mssherif 10', text="Room 4", bg='white',fg='cyan4',width=10,command=lambda:roomdet(4))
		b5  = Button(b_frame,font='mssherif 10', text="Room 5", bg='white',fg='cyan4',width=10,command=lambda:roomdet(5))
		b6  = Button(b_frame,font='mssherif 10', text="Room 6", bg='white',fg='cyan4',width=10,command=lambda:roomdet(6))
		b7  = Button(b_frame,font='mssherif 10', text="Room 7", bg='white',fg='cyan4',width=10,command=lambda:roomdet(7))
		b8  = Button(b_frame,font='mssherif 10', text="Room 8", bg='white',fg='cyan4',width=10,command=lambda:roomdet(8))
		b9  = Button(b_frame,font='mssherif 10', text="Room 9", bg='white',fg='cyan4',width=10,command=lambda:roomdet(9))
		b10 = Button(b_frame,font='mssherif 10', text="Room 10",bg='white',fg='cyan4',width=10,command=lambda:roomdet(10))
		b11 = Button(b_frame,font='mssherif 10', text="Room 11",bg='white',fg='cyan4',width=10,command=lambda:roomdet(11))
		b12 = Button(b_frame,font='mssherif 10', text="Room 12",bg='white',fg='cyan4',width=10,command=lambda:roomdet(12))
		b13 = Button(b_frame,font='mssherif 10', text="Room 13",bg='white',fg='cyan4',width=10,command=lambda:roomdet(13))
		b14 = Button(b_frame,font='mssherif 10', text="Room 14",bg='white',fg='cyan4',width=10,command=lambda:roomdet(14))
		b15 = Button(b_frame,font='mssherif 10', text="Room 15",bg='white',fg='cyan4',width=10,command=lambda:roomdet(15))
		b16 = Button(b_frame,font='mssherif 10', text="Room 16",bg='white',fg='cyan4',width=10,command=lambda:roomdet(16))
		b17 = Button(b_frame,font='mssherif 10', text="Room 17",bg='white',fg='cyan4',width=10,command=lambda:roomdet(17))
		b18 = Button(b_frame,font='mssherif 10', text="Room 18",bg='white',fg='cyan4',width=10,command=lambda:roomdet(18))
		b19 = Button(b_frame,font='mssherif 10', text="Room 19",bg='white',fg='cyan4',width=10,command=lambda:roomdet(19))
		b20 = Button(b_frame,font='mssherif 10', text="Room 20",bg='white',fg='cyan4',width=10,command=lambda:roomdet(20))
		sidebuttons.window_create("end",window=b1)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b2)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b3)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b4)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b5)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b6)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b7)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b8)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b9)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b10)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b11)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b12)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b13)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b14)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b15)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b16)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b17)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b18)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b19)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b20)

	#room unreserve page

	def unres():
		b_frame = Frame(root,height=400,width=1080,bg='gray89')

		unrf = Frame(b_frame,width = 2, height = 2)
		unre = Entry(b_frame,width=35, bd =5)
		unre.place(x= 500, y = 100)
		unrel = Label(b_frame,text = 'Room Number:',font = ('bold',14))
		unrel.place(x = 350, y = 100)
		unrf.pack(ipady=4,ipadx=15)
		Label(b_frame,text = 'Enter the room number to be unreserved',font =('Bold',24)).place(x=250,y=30)

		def unreserve():
			if unre.get()=='':
				messagebox.showerror('Entries not filled','Kindly Enter room Number')
			else :
				cur.execute("update roomd set rstatus='Unreserved' where rn = ? ",(unre.get(),))
				messagebox.showinfo("Successful","Room Unreserved successfully")
				reserve()
				con.commit()

		unres = Button(b_frame,text='Unreserve',bg='white',fg='Black',font='timenewroman 14',activebackground='green',command=unreserve).place(x=460,y=170)


		b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()

	#room reservation page

	def reserve():
		b_frame = Frame(root,height=420,width=1080,bg='gray89')

		label = Label(b_frame,height=420,width=1080)
		label.image=img
		label.place(x=0,y=0)
		

		vline = Frame(b_frame,height=400,width=7,bg='lightsteelblue3')
		vline.place(x=700,y=0) 

		Label(b_frame,text='Personal Information',font='msserif 15',bg='gray93').place(x=225,y=0)

		fnf = Frame(b_frame,height=1,width=1)
		fn = Entry(fnf)

		fnl = Label(b_frame,text = "First:").place(x=1,y=42)

		
		mnf = Frame(b_frame,height=1,width=1)
		mn = Entry(mnf)
		mnl = Label(b_frame, text="Middle:").place(x=220, y=42)

		lnf = Frame(b_frame,height=1,width=1)
		ln = Entry(lnf)
		lnl = Label(b_frame, text="Last:").place(x=450, y=42)

		fn.pack(ipady=4,ipadx=15)
		mn.pack(ipady=4,ipadx=15)
		ln.pack(ipady=4,ipadx=15)
		fnf.place(x=60,y=42)
		mnf.place(x=275,y=42)
		lnf.place(x=520,y=42)



		cnf = Frame(b_frame,height=1,width=1)
		cn = Entry(cnf)
		cnl = Label(b_frame,text = "Contact:").place(x=1,y=80)

		
		emf = Frame(b_frame,height=1,width=1)
		em = Entry(emf)
		eml = Label(b_frame,text = "Email:").place(x=220,y=80)

		adf = Frame(b_frame,height=1,width=1)
		ad = Entry(adf)
		adl = Label(b_frame,text = "Address:").place(x=450,y=80)



		cn.pack(ipady=4,ipadx=15)
		em.pack(ipady=4,ipadx=15)
		ad.pack(ipady=4,ipadx=15)
		cnf.place(x=60,y=80)
		emf.place(x=275,y=80)
		adf.place(x=520,y=80)


		Label(b_frame,text='Reservation Information',font='msserif 15',bg='gray93').place(x=220,y=130)
		
		nocf = Frame(b_frame,height=0,width=1)
		noc = Entry(nocf)
		nocl = Label(b_frame, text="No. of Children:").place(x=5, y=170)
		
		noaf = Frame(b_frame,height=0,width=1)
		noa = Entry(noaf)
		noal = Label(b_frame, text="No. of Adults:").place(x=5, y=200)

		number_days = StringVar()

		nodf = Frame(b_frame,height=0,width=1)
		nod = Entry(nodf,textvariable = number_days)
		nodl = Label(b_frame, text="No. of days:").place(x=300, y=230)

		check_in_date = StringVar()
		check_out_date = StringVar()
		checkinl = Label(b_frame, text="Check In:").place(x=300, y=170)
		checkindate = DateEntry(b_frame,date_pattern ='dd-mm-yyyy')
		checkindate.place(x=400,y=170)

		checkoutdate = DateEntry(b_frame, date_pattern='dd-mm-yyyy')
		checkoutdate.place(x=400, y=200)
		checkoutl = Label(b_frame, text="Check Out:").place(x=300, y=200)


		noc.pack(ipady=2,ipadx=15)
		noa.pack(ipady=2,ipadx=15)
		nod.pack(ipady=2,ipadx=15)
		nocf.place(x=100,y=170)
		noaf.place(x=100,y=200)
		nodf.place(x=400,y=230)
		
		roomnf = Frame(b_frame,height=1,width=1)
		roomn = Entry(roomnf)
		roomnl = Label(b_frame,text = 'Room Number: ').place(x=5, y =230)

		roomn.pack(ipady=4,ipadx=15)
		roomnf.place(x=100,y=230)

		pmethod = IntVar()
		def booking():

			#Validating Entries
			if fn.get() == '' or ln.get() == '' or cn.get() == '' or cn.get() == '' or em.get() == '' or ad.get() == "" or noc.get() == '' or noa.get() == '' or nod.get() == '' or roomn.get() == '':
				messagebox.showinfo('Incomplete','Fill All the Fields')
			#Validating phone no.
			elif len(cn.get()) != 10:
				messagebox.showwarning('Warning','Contact no is not 10 digit')

			elif em.get()[-4:] != '.com':
				messagebox.showinfo('Warning','Please Enter a Valid Email ID')
			else :
				cur.execute("select rstatus from roomd where rn = ?",(roomn.get(),))
				temp = cur.fetchone()
				if temp[0] == 'Reserved':
					messagebox.showwarning('Room is Reserved','Room number '+str(roomn.get())+' is Reserved')
				else:
					payroot = Tk()
					payroot.title("Payment")
					payroot.minsize(height=236,width=302)
					payroot.configure(bg='White')

					cur.execute("select price from roomd where rn = (?)",(roomn.get(),))
					rp = cur.fetchone()
					amtpd = str(int(rp[0])*int(nod.get()))
					Label(payroot,text='Select an option to pay '+str(int(rp[0])*int(nod.get())),font='msserif 14 bold',bg='White').place(x=0,y=0)
					Frame(payroot,height=4,width=300,bg='cyan4').place(x=0,y=39)
					Radiobutton(payroot,text='Cash  ',bg='White',variable=pmethod,value=1,font='helvetica 15',width=5).place(x=0,y=43+10)
					Radiobutton(payroot,text='Card   ',bg='White',variable=pmethod,value=2,font='helvetica 15',width=5).place(x=0,y=80+10)
					Radiobutton(payroot,text='UPI     ',bg='White',variable=pmethod,value=3,font='helvetica 15',width=5).place(x=0,y=115+10)
					Radiobutton(payroot,text='Paytm ',bg='White',variable=pmethod,value=4,font='helvetica 15',width=5).place(x=0,y=150+10)

					def f():
						if pmethod != '':
							print (pmethod.get())
							print ('pmethod value')
							cur.execute("select id from paymentsf order by id desc")
							x = cur.fetchone()
							cid = int(x[0])
							cid+=1
							print (cid)
							print (pmethod.get())
							checkin = checkindate.get_date()
							checkout = checkoutdate.get_date()
							cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar,checkindate varchar, checkoutdate varchar)")
							cur.execute("insert into paymentsf values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(cid,fn.get(),ln.get(),cn.get(),em.get(),roomn.get(),str(now.strftime("%d")),str(now.strftime("%b")),str(now.strftime("%Y")),str(now.strftime("%H:%M")),str(pmethod.get()),amtpd,checkin,checkout))
							cur.execute("update roomd set rstatus='Reserved' where rn = ? ",(roomn.get(),))
							messagebox.showinfo("Successful","Room Booked successfully")
							con.commit()
							ask = messagebox.showinfo("Successful","Payment Successful")
							reserve()
							payroot.destroy()
						else :
							messagebox.showwarning("Not selected","Please Select the payment method")
					Button(payroot,text='Pay',font='msserif 12',bg='Green',fg='White',width=28,command=f).place(x=0,y=200)




		#filter page
		Label(b_frame,text='Filter',font='msserif 20',bg='gray93').place(x=850,y=0)

		nbb = IntVar()
		acb = IntVar()
		tvb = IntVar()
		wifib = IntVar()

		style = ttk.Style()
		style.map('TCombobox', fieldbackground=[('readonly','white')])
		Label(b_frame,text='Bed(s) :',bg='gray93',font='17').place(x=730,y=50)

		nb = ttk.Combobox(b_frame,values=['please select...','1','2','3'],state='readonly',width=22)
		nb.place(x=830,y=50)
		nb.current(0)

		Label(b_frame,text='AC :',font='17',bg='gray93').place(x=732,y=75)

		ac = ttk.Combobox(b_frame,values=['please select...','Yes','No'],state='readonly',width=22)
		ac.place(x=830,y=75)
		ac.current(0)


		Label(b_frame,text='TV :',font='17',bg='gray93').place(x=732,y=100)

		tv = ttk.Combobox(b_frame,values=['please select...','Yes','No'],state='readonly',width=22)
		tv.place(x=830,y=100)
		tv.current(0)

		Label(b_frame,text='Wifi :',font='17',bg='gray93').place(x=732,y=125)

		wifi = ttk.Combobox(b_frame,values=['please select...','Yes','No'],state='readonly',width=22)
		wifi.place(x=830,y=125)
		wifi.current(0)

		listofrooms = Listbox(b_frame,height=6,width=36)
		listofrooms.place(x=735,y=190)
		listofrooms.insert(END,'Rooms of Your Choice will appear Here')
		listofrooms.insert(END,'once you apply filter')
		def findrooms():
			cur.execute('select rn,price,rstatus from roomd where beds = ? and ac = ? and tv = ? and internet = ? order by price asc',((nb.get()),ac.get(),tv.get(),wifi.get()) )
			x = cur.fetchall()
			#print (x)
			listofrooms.delete(0,END)
			if x == []:
				listofrooms.insert(END,'No Matching Found')
			for i in x :
				listofrooms.insert(END,'Room Number '+str(i[0])+' - Price - '+str(i[1]))

		Res = Button(b_frame,text='Reserve',bg='white',fg='black',font='timenewroman 14',activebackground='green',command=booking).place(x=250,y=270)

		findrooms = Button(b_frame,text='Find Rooms',bg='white',fg='black',font='timenewroman 9',activebackground='green',command = findrooms).place(x=830,y=155)
		
		scrollbar = Scrollbar(b_frame, orient="vertical")
		scrollbar.config(command=listofrooms.yview)
		scrollbar.place(x=1014,y=191,height=111)
		listofrooms.config(yscrollcommand=scrollbar.set)



		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()



	def Exitmod():
		q = messagebox.askyesno("Exit","Do you really want to exit ?")
		if(q):
			root.destroy()
	#---------------2nd top frame-----------------------------------------------------------------------------------------------------------------

	sl_frame = Frame(root,height=130,width=1080,bg='white')
	sl_frame.place(x=0,y=70+6)
	path = "images/rooms.png"
	img = ImageTk.PhotoImage(Image.open(path))
	b1 = Button(sl_frame,image=img,text='Rooms',bg='white',width=180,command=rooms)
	b1.image = img
	b1.place(x=180,y=0)
	path2 = "images/hotelstatus.png"
	img1 = ImageTk.PhotoImage(Image.open(path2))
	b2 = Button(sl_frame,image=img1,text='b2',bg='white',width=180,command=hotel_status)
	b2.image = img1
	b2.place(x=0,y=0)
	path3='images/records.jpg'
	img3 = ImageTk.PhotoImage(Image.open(path3))
	b3 = Button(sl_frame,image=img3,text='b2',bg='white',width=180,command=records)
	b3.image = img3
	b3.place(x=180*4,y=0)
	path4='images/unreserve.png'
	img4 = ImageTk.PhotoImage(Image.open(path4))
	b4 = Button(sl_frame,image=img4,text='b2',bg='white',width=180,command = unres)
	b4.image = img4
	b4.place(x=180*3,y=0)
	path5='images/logout.png'
	img5 = ImageTk.PhotoImage(Image.open(path5))
	b5 = Button(sl_frame,image=img5,text='b2',bg='white',width=180,height=100,command=Exitmod)
	b5.image = img5
	b5.place(x=180*5,y=0)
	path6='images/Bookroom.png'
	img6 = ImageTk.PhotoImage(Image.open(path6))
	b6 = Button(sl_frame,image=img6,text='b2',bg='white',width=180,height=100,command=reserve)
	b6.image = img6
	b6.place(x=180*2,y=0)
	Label(sl_frame,text='Hotel Status',font='msserif 13',bg='white').place(x=35,y=106)
	Label(sl_frame,text='Rooms',font='msserif 13',bg='white').place(x=248,y=106)
	Label(sl_frame,text='Reserve',font='msserif 13',bg='white').place(x=417,y=106)
	Label(sl_frame,text='Records',font='msserif 13',bg='white').place(x=774,y=106)
	Label(sl_frame,text='Unreserve',font='msserif 13',bg='white').place(x=570,y=106)
	Label(sl_frame,text='Exit',font='msserif 13',bg='white').place(x=968,y=106)
	sl_frame.pack_propagate(False)
	#-------------------extra frame------------------------------------------------------------------------------------------------------------------
	redf = Frame(root,height=6,width=1080,bg='lightsteelblue3')
	redf.place(x=0,y=70)
	redf1 = Frame(root,height=40,width=1080,bg='lightsteelblue3')
	redf1.place(x=0,y=210)
	reserve()
	mainloop()

def call_mainroot():
	mainroot()
call_mainroot()
