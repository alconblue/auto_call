from flask import Flask, request
from flask.helpers import send_from_directory
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from flask_cors import cross_origin
from flask_cors import CORS

def create_app():
	app = Flask(__name__, static_folder='frontend/build', static_url_path='')
	CORS(app)

	app.config.from_pyfile('settings.py')
	client = Client(app.config.get('TWILIO_ACCOUNT_SID'), app.config.get('TWILIO_AUTH_TOKEN'))

	@app.route('/', methods=['GET'])
	def serve():
		try:
			return send_from_directory(app.static_folder, 'index.html')
		except Exception as e:
			print(e)
		return send_from_directory(app.static_folder, 'index.html')

	@app.route('/call', methods=['POST'])
	def call():
		json = request.get_json(force=True)
		resp = VoiceResponse()
		resp.say(json['message'])
		ph_no = json['ph_no']
		if ph_no[0] == '+' and ph_no[1:].isnumeric():
			try:
				client.calls.create(twiml=str(resp), to=ph_no, from_=app.config.get("TWILIO_FROM_NUMBER"))
			except Exception as e:
				print(e)
				return "Input incorrect", 400
			return "Queued"
		return "Phone number should include country code and be only numbers", 400

	return app