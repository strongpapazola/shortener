from flask import Flask, request, redirect
import json

app = Flask(__name__)
filedata = "/home/infra/backup/shortener-prod/doYWtqc2hsZGtqYWhzbGprZGFqa2xzaGRha3NqaGRs.json"
#filedata = "/var/www/shortener/doYWtqc2hsZGtqYWhzbGprZGFqa2xzaGRha3NqaGRs.json"
endpoint = ""
#endpoint = "/s"

def appendfile(data):
	f = open(filedata,"w")
	f.write(str(data))
	f.close()

def showfile():
	if open(filedata,"r").read() == "":
		return []
	else:
		return json.loads(open(filedata,"r").read())

@app.route('/admin', methods=["GET","POST"])
#@app.route(endpoint+'/YXNsa2pkZ2doYWtqc2hsZGtqYWhzbGprZGFqa2xzaGRha3NqaGRsa2Fqc2hkbGthanNoZAo', methods=["GET","POST"])
def admin():
	shorturl = "http://"+request.headers['Host']+"/s/"
	html = """
<form method="POST" action="">
<input type="text" name="name" placeholder="Name"><br><input type="text" name="link" placeholder="Link"><br><button type="submit">Submit</button>
</form>
"""

	try:
		if "name" in request.form and "link" in request.form:
			name = request.form["name"]
			link = request.form["link"]
			data = showfile()
			data.append({"name":name,"s_link":shorturl+name,"link":link,"count":0,"ips":[]})
			appendfile(json.dumps(data, indent=3).replace("'","\""))
			return html+"<br>Cara pakai : "+shorturl+"[namalink]<br>Cara tau lokasi ip : http://ipinfo.io/[ip]<br><pre>"+json.dumps(list(reversed(showfile())),indent=3)+"</pre>"
		else:
			return html+"<br>Cara pakai : "+shorturl+"[namalink]<br>Cara tau lokasi ip : http://ipinfo.io/[ip]<br><pre>"+json.dumps(list(reversed(showfile())),indent=3)+"</pre>"
	except Exception as e:
		return str(e)

@app.route(endpoint+'/<rute>', methods=["GET"])
def rute(rute):
	try:
		data = showfile()
		for i in range(0, len(data)):
			if rute == data[i]['name']:
				if data[i]['ips'] != []:
					for j in data[i]['ips']:
						if request.remote_addr != j:
							data[i]['ips'].append(request.remote_addr)
							data[i]['count'] = data[i]['count'] + 1
							appendfile(json.dumps(data,indent=3).replace("'","\""))
				else:
					data[i]['ips'].append(request.remote_addr)
					data[i]['count'] = data[i]['count'] + 1
					appendfile(json.dumps(data,indent=3).replace("'","\""))
				return redirect(data[i]['link'],code=301)
		return "404 Error Not Found"
	except Exception as e:
		return str(e)

if "__main__" == __name__:
	app.run(host="0.0.0.0",port=5000)
#	app.run(host="0.0.0.0",port=8000,debug=True)
