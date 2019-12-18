from app import app, scrap
from flask import render_template, send_file ,flash, url_for
from flask import request
from app.forms import LoginForm
import requests, json, random

@app.route("/")
@app.route("/index")
def home():
	return render_template("index.html",title="LESSON")
	
@app.route("/")
@app.route("/photofunia")
def home1():
	return render_template("photofunia.html",title="LESSON")
	
@app.route("/imagesearch",methods=["POST","GET"])
def rest_imagesearch():
	this_query = request.args["query"]
	this_rest = scrap.imagesearch(this_query)
	return json.dumps(this_rest, indent=4)
	
@app.route("/instagramprofile",methods=["POST","GET"])
def rest_instaprofile():
	this_user = request.args["username"]
	this_rest = scrap.instaprofile(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/instagrampost",methods=["POST","GET"])
def rest_instapost():
	this_user = request.args["username"]
	this_rest = scrap.instapost(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/instagramstory",methods=["POST","GET"])
def rest_instastory():
	this_user = request.args["username"]
	this_rest = scrap.instastory(this_user)
	return json.dumps(this_rest, indent=4)
	
@app.route("/smuledownload",methods=["POST","GET"])
def rest_downloadsmule():
	this_user = request.args["url_recording"]
	this_rest = scrap.downloadsmule(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/smuleid",methods=["POST","GET"])
def rest_idsmule():
	this_user = request.args["userid"]
	this_rest = scrap.idsmule(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/smuleperform",methods=["POST","GET"])
def rest_performsmule():
	this_user = request.args["userid"]
	this_rest = scrap.performsmule(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/smuleid_record",methods=["POST","GET"])
def rest_idrecordsmule():
	this_user = request.args["id_record"]
	this_rest = scrap.idrecordsmule(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/smulesongbook",methods=["POST","GET"])
def rest_songbooksmule():
	this_user = request.args["userid"]
	this_rest = scrap.songbooksmule(this_user)
	return json.dumps(this_rest, indent=4)
	
@app.route("/beach_sign",methods=["POST","GET"])
def rest_beach_sign():
	this_user = request.args["effects"]
	this_rest = scrap.beach_sign(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/neon_writing",methods=["POST","GET"])
def rest_neon_writing():
	this_user = request.args["effects"]
	this_rest = scrap.neon_writing(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/retro_wave",methods=["POST","GET"])
def rest_retro_wave():
	this_user = request.args["text1"]
	this_user1 = request.args["text2"]
	this_user2= request.args["text3"]
	this_rest = scrap.retro_wave(this_user,this_user1,this_user2)
	return json.dumps(this_rest, indent=4)

@app.route("/brussels_museum",methods=["POST","GET"])
def rest_brussels_museum():
	this_user = request.args["url"]
	this_rest = scrap.brussels_museum(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/love_letter",methods=["POST","GET"])
def rest_love_letter():
	this_user = request.args["url"]
	this_rest = scrap.love_letter(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/golden_valentine",methods=["POST","GET"])
def rest_golden_valentine():
	this_user = request.args["url"]
	this_rest = scrap.golden_valentine(this_user)
	return json.dumps(this_rest, indent=4)
	
@app.route("/flowers",methods=["POST","GET"])
def rest_flowers():
	this_user = request.args["url"]
	this_user1 = request.args["text"]
	this_rest = scrap.flowers(this_user,this_user1)
	return json.dumps(this_rest, indent=4)

@app.route("/missing_person",methods=["POST","GET"])
def rest_missing_person():
	this_user = request.args["url"]
	this_user1 = request.args["text1"]
	this_user2 = request.args["text2"]
	this_user3 = request.args["text3"]
	this_rest = scrap.missing_person(this_user,this_user1,this_user2,this_user3)
	return json.dumps(this_rest, indent=4)
	
@app.route("/brooches",methods=["POST","GET"])
def rest_brooches():
	this_user = request.args["url"]
	this_user1 = request.args["url2"]
	this_rest = scrap.brooches(this_user,this_user1)
	return json.dumps(this_rest, indent=4)
	
@app.route("/two_valentines",methods=["POST","GET"])
def rest_two_valentines():
	this_user = request.args["url"]
	this_user1 = request.args["text"]
	this_user2 = request.args["url2"]
	this_user3 = request.args["text2"]
	this_rest = scrap.two_valentines(this_user,this_user1,this_user2,this_user3)
	return json.dumps(this_rest, indent=4)
	
@app.route("/valentine",methods=["POST","GET"])
def rest_valentine():
	this_user = request.args["url"]
	this_user1 = request.args["text"]
	this_rest = scrap.valentine(this_user,this_user1)
	return json.dumps(this_rest, indent=4)

@app.route("/watercolour_splash",methods=["POST","GET"])
def rest_watercolour_splash():
	this_user = request.args["url"]
	this_rest = scrap.watercolour_splash(this_user)
	return json.dumps(this_rest, indent=4)

@app.route("/neon_sign",methods=["POST","GET"])
def rest_neon_sign():
	this_user = request.args["text"]
	this_rest = scrap.neon_sign(this_user)
	return json.dumps(this_rest, indent=4)

