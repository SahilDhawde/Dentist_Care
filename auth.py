import bcrypt
from database import conn
def register_user(n,e,p):
 d=conn();c=d.cursor()
 try:
  c.execute('INSERT INTO users(name,email,password) VALUES(?,?,?)',(n,e,bcrypt.hashpw(p.encode(),bcrypt.gensalt())));d.commit();return True
 except: return False
def login_user(e,p):
 d=conn();c=d.cursor();c.execute('SELECT * FROM users WHERE email=?',(e,));u=c.fetchone()
 return bool(u and bcrypt.checkpw(p.encode(),u['password']))
