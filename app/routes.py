from app import app, scrap
from flask import render_template, send_file ,flash, url_for
from flask import request
from app.forms import LoginForm
import requests, json, random

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html',title='LESSON')
	
@app.route('/imagesearch',methods=['POST','GET'])
def rest_imagesearch():
	this_query = request.args['query']
	this_rest = scrap.imagesearch(this_query)
	return json.dumps(this_rest, indent=4)
	
@app.route('/instagramprofile',methods=['POST','GET'])
def rest_instaprofile():
	this_user = request.args['username']
	this_rest = scrap.instaprofile(this_user)
	return json.dumps(this_rest, indent=4)

@app.route('/instagrampost',methods=['POST','GET'])
def rest_instapost():
	this_user = request.args['username']
	this_rest = scrap.instapost(this_user)
	return json.dumps(this_rest, indent=4)

@app.route('/instagramstory',methods=['POST','GET'])
def rest_instastory():
	this_user = request.args['username']
	this_rest = scrap.instastory(this_user)
	return json.dumps(this_rest, indent=4)
	
@app.route('/smuledownload',methods=['POST','GET'])
def rest_downloadsmule():
	this_user = request.args['url_recording']
	this_rest = scrap.downloadsmule(this_user)
	return json.dumps(this_rest, indent=4)

@app.route('/smuleid',methods=['POST','GET'])
def rest_idsmule():
	this_user = request.args['userid']
	this_rest = scrap.idsmule(this_user)
	return json.dumps(this_rest, indent=4)

@app.route('/smuleperform',methods=['POST','GET'])
def rest_performsmule():
	this_user = request.args['userid']
	this_rest = scrap.performsmule(this_user)
	return json.dumps(this_rest, indent=4)

@app.route('/smuleid_record',methods=['POST','GET'])
def rest_idrecordsmule():
	this_user = request.args['id_record']
	this_rest = scrap.idrecordsmule(this_user)
	return json.dumps(this_rest, indent=4)

@app.route('/smulesongbook',methods=['POST','GET'])
def rest_songbooksmule():
	this_user = request.args['userid']
	this_rest = scrap.songbooksmule(this_user)
	return json.dumps(this_rest, indent=4)

