from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!  Usman kia hall hain kase ho tumhri dost kasi hai abbay wali jisko tum dekhte rehte lecture k time Running and Fucking Running........!!! I\'m host %s' % socket.gethostname()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
