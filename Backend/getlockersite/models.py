#models.py
from getlockersite import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
import time as t

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    userfinger = db.Column(db.String())
    userfinger1 = db.Column(db.String())
    userfinger2 = db.Column(db.String())
    userfinger3 = db.Column(db.String())
    userfinger4 = db.Column(db.String())
    status = db.Column(db.String(8))
    pins = db.Column(db.Integer)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    



    def __init__(self,email,username,password,userfinger,pins):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.userfinger = userfinger
        self.pins = pins

    def addfinger(self,userfinger,userfinger1,userfinger2):
        self.userfinger=userfinger
        self.userfinger1=userfinger1
        self.userfinger2=userfinger2
    
    def addstatus(self,status):
        self.status=status  


    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"

    def counter(self,dataTarget,variabelTujuan):
        i = 0
        j = 2
        while j<= len(dataTarget):
            
            a = "0x"+dataTarget[i:j]+','
            variabelTujuan.append(a)
            i+=2
            j+=2



    def json(self):
        return {'id':self.id , 'user_finger':self.userfinger}


class SewaLocker(db.Model):

    

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,nullable=False)
    sewa = db.Column(db.Integer())
    nomorlocker = db.Column(db.String(32))
    finger_data = db.Column(db.String(128))
    finger_data1 = db.Column(db.String(128))
    finger_data2 = db.Column(db.String(128))
    finger_data3 = db.Column(db.String(128))
    finger_data4 = db.Column(db.String(128))
    userpin = db.Column(db.Integer)
    toggle_enroll = db.Column(db.String(32))
    akses = db.Column(db.String(8))

    def __init__(self,sewa,user_id,nomorlocker,finger_data,userpin,toggle_enroll):
        self.sewa = sewa
        self.user_id = user_id
        self.nomorlocker = nomorlocker
        self.finger_data = finger_data
        self.userpin = userpin
        self.toggle_enroll = toggle_enroll


    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.sewa} {self.user_id} {self.nomorlocker} "



    def json(self):
        isidata = 'false'
        if self.finger_data != 'empty':
            isidata = 'true'
      
        return {'user_id':self.user_id , 'toggle_enroll':self.toggle_enroll, 'akses':self.akses, 'datafinger':isidata}



        

class LockerCommand(db.Model):

    

    id = db.Column(db.Integer,primary_key=True)
    userid = db.Column(db.Integer())
    access = db.Column(db.String(8))
    enroll = db.Column(db.String(8))
    toggle_lock = db.Column(db.Integer())


    
    
    def toggle(self):
        self.toggle_lock += 1
