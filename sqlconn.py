import sqlite3

conn=sqlite3.connect('leaderboard.db')
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS leaderboard (username VARCHAR(10),score INT);")
conn.commit()
conn.close()

output:list

def update(name,points):
    conn=sqlite3.connect('leaderboard.db')
    cursor=conn.cursor()
    conn.commit()
    cursor.execute('''SELECT * FROM leaderboard;''')
    rows=cursor.fetchall()
    for i in rows:
        if i[0]==name:
            if i[1]<points:
                cursor.execute("UPDATE leaderboard SET score={} WHERE username='{}'".format(points,name))
            break
    else:
        cursor.execute('''INSERT INTO leaderboard (username,score) VALUES ('{}',{});'''.format(name,points))
    conn.commit()
    conn.close()

def sort(rows):
    for i in range(len(rows)):
        for j in range(len(rows)-1,i,-1):
            if rows[j][1]>rows[j-1][1]:
                rows[j],rows[j-1]=rows[j-1],rows[j]
    return rows


def recieve():
    global output
    conn=sqlite3.connect('leaderboard.db')
    cursor=conn.cursor()
    conn.commit()
    cursor.execute('''SELECT * FROM leaderboard ORDER BY score;''')
    rows=cursor.fetchall()
    output=sort(rows)
    conn.close()