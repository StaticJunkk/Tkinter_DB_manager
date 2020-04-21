from tkinter import *
import sqlite3

root = Tk()
root.title("Tkinter Tut") 
#root.geometry("400x400")

conn = sqlite3.connect("address_book.db")
c = conn.cursor()
'''#Remove these to create the .db file first, then exclude these for further use
c.execute(""" CREATE TABLE addresses(
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer
          )""")
'''

def delete():
	  

	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	c.execute("DELETE from addresses WHERE oid = " + oid_del.get())
	conf_l = Label(root, text = "Deletion Confirmed!")
	conf_l.grid(row = 11, column = 0)
	oid_del.delete(0, END)
	conn.commit()
	conn.close()
    
    
    
	


def submit():

	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name,:address, :city, :state, :zipcode)",
             {
                'f_name' : f_name.get(),
                'l_name' : l_name.get(),
                'address' : address.get(),
                'city' : city.get(),
                'state' : state.get(),
                'zipcode' : zipcode.get()            
              })
	conn.commit()
	conn.close()
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)


def save():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	rid = oid_del.get()
	c.execute("""UPDATE addresses SET
          first_name = :first,
          last_name = :last,
          address = :address,
          city = :city,
          state = :state,
          zipcode = :zipcode
          

		WHERE oid = :oid""",
		{'first' : f_name_ed.get(),
		'last' : l_name_ed.get(),
		'address' : address_ed.get(),
		'city' : city_ed.get(),
		'state' : state_ed.get(),
		'zipcode' : zipcode_ed.get(),
		'oid' : rid

		})


	f_name_ed.delete(0, END)
	l_name_ed.delete(0, END)
	address_ed.delete(0, END)
	city_ed.delete(0, END)
	state_ed.delete(0, END)
	zipcode_ed.delete(0, END)



	conn.commit()
	conn.close()




def query():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	lbl = Label(root, anchor = CENTER)
	lbl.grid(row = 8, column = 0, columnspan = 2)
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	print_rec = ''
	n = len(records)
	for record in records[n-1]:
		print_rec += str(record) + " "

	lbl = Label(root, text = print_rec, anchor = CENTER)
	lbl.grid(row = 8, column = 0, columnspan = 2)
		
	conn.commit()
	conn.close()
	

    
def update():
	editor = Tk()
	editor.title("Update Record")
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	rid = oid_del.get()
	c.execute("SELECT * FROM addresses where oid = " + rid)
	records = c.fetchall()

	global f_name_ed
	global l_name_ed
	global address_ed
	global city_ed
	global state_ed
	global zipcode_ed



	f_name_ed = Entry(editor, width=30)
	f_name_ed.grid(row = 0, column = 1, padx = 30)

	l_name_ed = Entry(editor, width=30)
	l_name_ed.grid(row = 1, column = 1, padx = 30)

	address_ed = Entry(editor, width=30)
	address_ed.grid(row = 2, column = 1, padx = 30)

	city_ed = Entry(editor, width=30)
	city_ed.grid(row = 3, column = 1, padx = 30)

	state_ed = Entry(editor, width=30)
	state_ed.grid(row = 4, column = 1, padx = 30)

	zipcode_ed = Entry(editor, width=30)
	zipcode_ed.grid(row = 5, column = 1, padx = 30)



	#labels
	f_name_l_ed = Label(editor, text = "First Name")
	f_name_l_ed.grid(row = 0, column = 0)

	l_name_l_ed = Label(editor, text = "Last Name")
	l_name_l_ed.grid(row = 1, column = 0)

	address_l_ed = Label(editor,text = "Address")
	address_l_ed.grid(row = 2, column = 0)

	city_l_ed = Label(editor, text = "City")
	city_l_ed.grid(row = 3, column = 0)

	state_l_ed = Label(editor, text = "State")
	state_l_ed.grid(row = 4, column = 0)

	zipcode_l_ed = Label(editor,text = "zipcode")
	zipcode_l_ed.grid(row = 5, column = 0 )

	save_btn = Button(editor, text = "SAVE", command = save)
	save_btn.grid(row = 12, column = 0, columnspan = 2, ipadx = 100)

	for record in records:
			f_name_ed.insert(0, record[0])
			l_name_ed.insert(0, record[1])
			address_ed.insert(0, record[2])
			city_ed.insert(0, record[3])
			state_ed.insert(0, record[4])
			zipcode_ed.insert(0, record[5])
	conn.commit()
	conn.close()
    



 	
 	
 	
 	
    
	


	  




f_name = Entry(root, width=30)
f_name.grid(row = 0, column = 1, padx = 30)

l_name = Entry(root, width=30)
l_name.grid(row = 1, column = 1, padx = 30)

address = Entry(root, width=30)
address.grid(row = 2, column = 1, padx = 30)

city = Entry(root, width=30)
city.grid(row = 3, column = 1, padx = 30)

state = Entry(root, width=30)
state.grid(row = 4, column = 1, padx = 30)

zipcode = Entry(root, width=30)
zipcode.grid(row = 5, column = 1, padx = 30)

oid_del = Entry(root, width = 30)
oid_del.grid(row = 9, column = 1)


#labels
f_name_l = Label(root, text = "First Name")
f_name_l.grid(row = 0, column = 0)

l_name_l = Label(root, text = "Last Name")
l_name_l.grid(row = 1, column = 0)

address_l = Label(root,text = "Address")
address_l.grid(row = 2, column = 0)

city_l = Label(root, text = "City")
city_l.grid(row = 3, column = 0)

state_l = Label(root, text = "State")
state_l.grid(row = 4, column = 0)

zipcode_l = Label(root,text = "zipcode")
zipcode_l.grid(row = 5, column = 0 )

oid_del_l = Label(root, text = "Enter OID to be deleted/Updated", pady =10)
oid_del_l.grid(row = 9, column = 0)





#Submit Button
submit_btn = Button(root, text = "Add record to Database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, ipadx = 100)

#Query Button
qbtn = Button(root, text = "Show Record", command = query)
qbtn.grid(row = 7, column = 0, columnspan = 2, ipadx = 100)

delete_btn = Button(root, text = "Delete from Database", command =delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, ipadx = 100)

update_btn = Button(root, text = "Update Database", command = update)
update_btn.grid(row = 12, column = 0, columnspan = 2, ipadx = 100)




root.mainloop()
