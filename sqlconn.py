import sqlite3

conn=sqlite3.connect('leaderboard.db')
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS leaderboard (username VARCHAR(10),score INT);")
cursor.execute("DELETE FROM leaderboard;")
conn.commit()
conn.close()


def update(name,points):
    conn=sqlite3.connect('leaderboard.db')
    cursor=conn.cursor()
    conn.commit()
    cursor.execute('''SELECT * FROM leaderboard;''')
    rows=cursor.fetchall()
    for i in rows:
        if i[0]==name:
            cursor.execute("UPDATE leaderboard SET score={} WHERE username='{}'".format(points,name))
            break
    else:
        cursor.execute('''INSERT INTO leaderboard (username,score) VALUES ('{}',{});'''.format(name,points))
    conn.commit()
    
    cursor.execute('''SELECT * FROM leaderboard;''')
    Rows=cursor.fetchall()
    for i in Rows:
        print(i)
    conn.close()