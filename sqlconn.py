import sqlite3

def update(name,points):
    conn=sqlite3.connect('leaderboard.db')
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO leaderboard (username,score) VALUES ('{}',{});'''.format(name,points))
    conn.commit()
    cursor.execute('''SELECT * FROM leaderboard;''')
    rows=cursor.fetchall()
    print("update")
    for i in rows:
        print(i)
    conn.close()