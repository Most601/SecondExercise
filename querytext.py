import sqlite3
from Tkinter import *

def myquery(q):
    con = sqlite3.connect("nmea_to_db.db")
    con.isolation_level = None
    cur = con.cursor()

    buffer = ""

    print "Enter your SQL commands to execute in sqlite3."
    print "Enter a blank line to exit."

    while True:
        line = q
        if line == "":
            break
        buffer += line
        if sqlite3.complete_statement(buffer):
            try:
                buffer = buffer.strip()
                cur.execute(buffer)

                if buffer.lstrip().upper().startswith("SELECT"):
                    #print cur.fetchall()
                    root = Tk()
                    root.title("Query ''Select'' result")
                    root.geometry("750x550")
                    app = Frame(root)
                    app.grid()
                    S = Scrollbar(root)
                    T = Text(app, height=100, width=100)
                    S.pack(side=RIGHT, fill=Y)
                    T.pack(side=LEFT, fill=Y)
                    S.config(command=T.yview)
                    T.config(yscrollcommand=S.set)
                    for row in cur.execute(buffer):
                        T.insert(INSERT,row)
                        T.insert(INSERT, "\n")
                    T.pack()    
                    break
            except sqlite3.Error as e:
                print "An error occurred:", e.args[0]
                break
            buffer = ""

    con.close()