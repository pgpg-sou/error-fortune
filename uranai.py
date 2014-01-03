# ! /usr/bin/python
# -*- coding: utf-8 -*- 

from __future__ import with_statement
from flask import Flask, request, session, jsonify, g, redirect, url_for, \
	 abort, render_template, json
from pymongo import Connection

app = Flask(__name__)
app.config.from_object
app.config.from_envvar('FLASKER_SETTINGS', silent=True)

DB = 'uranai'

# ok
@app.before_request
def before_request():
	g.con = connect_db()

#ok
@app.teardown_request
def teardown_request(exception):
	g.con.disconnect()

@app.route('/')
def index():
	col = kind_db_connect('uranai')
	data = col.find({ 'error' : { "$exists" : True }})
	print data
	return render_template('main.html', data=data)

@app.route('/inputdb', methods=['GET'])
def inputdb_get():
	col = kind_db_connect('uranai')
	data = col.find({ 'error' : { "$exists" : True }})
	print data
	return render_template('inputdb.html', data=data)

@app.route('/inputdb', methods=['POST'])
def inputdb_post():
	col = kind_db_connect('uranai')

	col.insert({'error' : request.form['error'], \
				'result' : request.form['result']})
	return redirect(url_for('inputdb_get'))

@app.route('/delete/<error_name>')
def delete(error_name):
	col = kind_db_connect('uranai')
	col.remove({ 'error' : error_name })
	return redirect(url_for('inputdb_get'))

# @app.route('/result', methods=['GET'])
@app.route('/result', methods=['GET'])
def result():
	print 'hoge'
	col = kind_db_connect('uranai')
	data = col.find_one({ 'error' : request.args.get('error_name', '') })
	return jsonify(error=data['error'], 
					un=data['un'], 
					result=data['result'])
    	# return jsonify(username=str_s,
     #               email='g.user.email',
     #               id='g.user.id')

# functions

def connect_db():
	con = Connection('localhost', 27017)
	return con

def kind_db_connect(kind_db):
	db = g.con[DB]
	col = db[kind_db]
	return col

if __name__ == '__main__':
	app.run();
