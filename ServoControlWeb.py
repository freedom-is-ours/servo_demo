from types import GetSetDescriptorType
import flask
from flask.globals import request
from flask_selfdoc import Autodoc
import json
import time
import subprocess

from drivertest import servo_switch,servo_360,servo_state

app = flask.Flask(__name__)
auto = Autodoc(app)
dev1 = servo_switch()
dev2 = servo_360()

try:
    with open('/home/pi/servo_demo/static/webinterface_settings.json', 'r') as f:
        web_settings = json.load(f)
except FileNotFoundError:
    web_settings = {
        "id":[0,1,2,3,4,5,6,7], #通道 1-7
        "class":[0,1,0,0,0,0,0,0], #类型 0：180型 or 1：360型
        "remark":["532shutter","atten","399shutter","-","-","-","-","-"], #备注
        "hotkey1":[[0,"open"],[0,"-"],[90,"open"],[0,"-"],[0,"-"],[0,"-"],[0,"-"],[0,"-"]],
        "hotkey2":[[90,"close"],[90,"-"],[0,"close"],[90,"-"],[90,"-"],[90,"-"],[90,"-"],[90,"-"]]
    }
    with open('/home/pi/servo_demo/static/webinterface_settings.json', 'w') as f:
        json.dump(web_settings, f)
    
state = servo_state(len=len(web_settings["id"]))

@app.route('/')
@auto.doc("public")
def index():
    return flask.render_template('servohttp.html' , settings = web_settings , servo = state)

@app.route('/set_angle/<int:channel>', methods=['POST', 'GET'])
@auto.doc("public")
def set_angle(channel):
    if request.method == "POST":
        temp_a = int(flask.request.form["angle"])
    dev1.set_angle(channel, temp_a)
    state.angles[channel] = temp_a
    return flask.redirect((flask.url_for('index')))

@app.route('/stepless/<int:channel>', methods=['POST', 'GET'])
@auto.doc("public")
def rotating(channel):
    temp_s = flask.request.form["speed"]
    if flask.request.form["direction"] == "1" :
        temp_d = 1
    elif flask.request.form["direction"] == "-1" :
        temp_d = -1
    else :
        temp_d = 0
    dev2.stepless(channel,temp_d,temp_s)
    state.speed[channel] = temp_s
    return flask.redirect((flask.url_for('index')))

@app.route('/stepping/<int:channel>', methods=['POST', 'GET'])
@auto.doc("public")
def step(channel):
    #print(flask.request.form)
    temp_s = flask.request.form["Stepsize"]
    temp_m = flask.request.form["Multi"]
    if flask.request.form["step"] == "CW" :
        temp_d = 1
    elif flask.request.form["step"] == "CCW" :
        temp_d = -1
    dev2.stepping(channel,temp_d,temp_s,temp_m)
    state.stepsize[channel] = temp_s
    state.multi[channel] = temp_m
    return flask.redirect((flask.url_for('index')))

@app.route('/editjson',methods=['POST', 'GET'])
@auto.doc("public")
def editjson():
    return flask.render_template('edit.html')

@app.route('/change',methods=['POST', 'GET'])
def edit():
    #编辑json，用于修改class hotkey，remark等,
    editdict = flask.request.form.to_dict()
    if editdict["channeledit"] != "16":
        if int(editdict["channeledit"]) in web_settings["id"]:
            cha =web_settings["id"].index(int(editdict["channeledit"]))
            web_settings["class"][cha] = int(editdict["classedit"])
            web_settings["remark"][cha] = editdict["remarkedit"]
            web_settings["hotkey1"][cha] = [int(editdict["hotkey1_angle_edit"]),editdict["hotkey1_text_edit"]]
            web_settings["hotkey2"][cha] = [int(editdict["hotkey2_angle_edit"]),editdict["hotkey2_text_edit"]]
        '''
        else : #增加 不能做 解决办法将id和index分开 用列表框住字典实现为佳，当前用字典套列表不好一一对应
            cha = int(editdict["channeledit"])
            web_settings["id"].append(cha)
            web_settings["class"].append(int(editdict["classedit"]))
            web_settings["remark"].append(editdict["remarkedit"])
            web_settings["hotkey1"].append([int(editdict["hotkey1_angle_edit"]),editdict["hotkey1_text_edit"]])
            web_settings["hotkey2"].append([int(editdict["hotkey2_angle_edit"]),editdict["hotkey2_text_edit"]])
        '''
    with open('/home/pi/servo_demo/static/webinterface_settings.json', 'w') as f:
        json.dump(web_settings, f)        
    return flask.redirect((flask.url_for('index')))

@app.route("/del",methods=['POST', 'GET']) 
def delete(): #删减 不能做
    '''
    ddict = flask.request.form.to_dict()
    cha =web_settings["id"].index(int(ddict["channeldelete"]))
    del web_settings["id"][cha]
    del web_settings["class"][cha]
    del web_settings["remark"][cha]
    del web_settings["hotkey1"][cha]
    del web_settings["hotkey2"][cha]
    with open('static/webinterface_settings.json', 'w') as f:
        json.dump(web_settings, f)
    '''
    return flask.redirect((flask.url_for('index')))

@app.route('/doc')
def documentation():
    """Shows the documentation rendered by autodoc. """
    return auto.html('public', title='ServoControl Routing Table')

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=1,port="10086")
