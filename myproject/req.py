from flask import Flask
from myproject.helper import Helper

app = Flask(__name__)

helper = Helper("test")

@app.route('/update/<qid>/<status>', methods=['GET'])
def update(qid, status):
	if helper.test == "test":
		helper.approve_status_update(qid,status)
	else:
		return "nothing"
