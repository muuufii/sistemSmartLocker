from flask import render_template,url_for,flash, redirect,request,Blueprint
from flask_login import current_user,login_required
from getlockersite import db
from getlockersite.models import SewaLocker,User,LockerCommand
from getlockersite.checkin_posts.forms import SewaForm,SewaForm2,AddFingerprintForm
from flask_restful import Api, Resource
import time as t


checkin_posts = Blueprint('checkin_posts',__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)





class DataLockerApi(Resource):
    def get(self):

        statusLoker = LockerCommand.query.filter_by(access='HIGH').first()
        enrollLoker = LockerCommand.query.filter_by(enroll='HIGH').first()

        if statusLoker:
            if statusLoker.toggle_lock < 2 :
                statusLoker.toggle_lock += 1
                db.session.commit()
            else:
                statusLoker.toggle_lock = 0
                statusLoker.access = None
                db.session.commit()
            return{'id':statusLoker.id}
        elif enrollLoker:
            return{'id_enroll': enrollLoker.userid}
        else:
            return{'id':0,'id_enroll':0}


        


#daftar fingerprint
class DataLockerFingerprint(Resource):

    def post(self,uid,pins,datafinger,datafinger1,datafinger2):
        
 
        if pins != 0 and datafinger == 'none' :        
            datauser = User.query.filter_by(pins=pins).first()
            getLocker = LockerCommand.query.filter_by(userid=None).first()
            
            if datauser:
                getLocker.userid = datauser.id
                getLocker.enroll = 'HIGH'

        elif uid != 0 and datafinger != 'none' :
            datauser = User.query.get(uid)
            getLocker = LockerCommand.query.filter_by(userid=datauser.id).first()

            datauser.addfinger(datafinger,datafinger1,datafinger2)
            getLocker.enroll = None
            datauser.status = 'True'
   
        db.session.commit()
#daftar fingerprint





class DataFingerCompare(Resource):


    def post(self,metode,datafingercomp):
        def dataCompare(pt1,pt2):
            distance = 0 
            for i in range(len(pt1)):
                distance += (pt1[i] - pt2[i]) ** 2
            return distance ** 0.5
            return distance

        #############################################

        def converter(datainput):
            datasave = []
            i = 0
            o = 2
            while o<= len(datainput):
                a = datainput[i:o]
                datasave.append(int(a,16))
                i+=2
                o+=2
            return datasave

        def compareDataInList(data1,data2,counter):
            dataMatchId = None
            result = dataCompare(data1,data2)
            if result <= 1100:
                dataMatchId = counter
            else:
                dataMatchId = None
            
            return dataMatchId


        def getUserID(val,data):
            dataList = {}
            dataList = data
            for key, value in dataList.items():
                if val == value:
                    return key



        def check(statusLoker):
            if statusLoker:
                if metode == 'access':
                    statusLoker.access = 'HIGH'
                    
                elif metode == 'access_checkout':
                    statusLoker.access = 'HIGH'
                    statusLoker.userid = None
            else:
                if idMatchMax[0] != 0:
                    getLocker = LockerCommand.query.filter_by(userid=None).first()
                    getLocker.userid = idMatchMax[0]
                    getLocker.access = 'HIGH'
                    idMatchMin[0] = 0

                elif idMatchMin[0] != 0:
                    getLocker = LockerCommand.query.filter_by(userid=None).first()
                    getLocker.userid = idMatchMin[0]
                    getLocker.access = 'HIGH'



        #############################################

        # ambil semua data finger user #
        idHaveData = []
        datauser = User.query.filter_by(status='True')
        for i in datauser:
            idHaveData.append(i.id)
        # ambil semua data finger user #

        ##############################################

        # proses match #
        idMatchMin = [0]
        idMatchMax = [0]
        totalMatch = 0

        for i in idHaveData:
            calluser = User.query.get(i)
            a = dataCompare(converter(datafingercomp),converter(calluser.userfinger))
            b = dataCompare(converter(datafingercomp),converter(calluser.userfinger1))
            c = dataCompare(converter(datafingercomp),converter(calluser.userfinger2))

            if a<=1120:
                totalMatch += 1
            if b<=1120:
                totalMatch += 1
            if c<=1120:
                totalMatch += 1

            if totalMatch == 3:
                idMatchMax[0] = i
            elif totalMatch == 2:
                idMatchMin[0] = i
            
            
            totalMatch = 0

        if idMatchMax[0] != 0:
            statusLoker = LockerCommand.query.filter_by(userid=idMatchMax[0]).first()
            check(statusLoker)
            idMatchMin[0] = 0

        elif idMatchMin[0] != 0:
            statusLoker = LockerCommand.query.filter_by(userid=idMatchMin[0]).first()
            check(statusLoker)
        

                

        # proses match #
        
        db.session.commit()
        
        


class DataUserShow(Resource):
    
    def get(self,uid):
        du = User.query.filter_by(id=uid)
        for isidu in du:
            if isidu:
                return isidu.json()

class LockerCommandApi(Resource):

    def  get(self):
        dc = LockerCommand.query.all()
        for isidc in dc:
            return isidc.json()

api.add_resource(DataLockerApi, '/getdlapi')
api.add_resource(DataLockerFingerprint, '/getduapi/<int:uid>/<int:pins>/<string:datafinger>/<string:datafinger1>/<string:datafinger2>')
api.add_resource(DataFingerCompare, '/datafingercompare/<string:metode>/<string:datafingercomp>')
api.add_resource(DataUserShow, '/usershow/<int:uid>')
api.add_resource(LockerCommandApi, '/lockerapi/getdlapi')



