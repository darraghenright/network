import requests
from flask import jsonify, Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Call out to the `service` container, which is part of a 
    different Docker Compose stack but on a shared network,
    and relay the response details back to the client.

    Because the `service` container shares the same network
    as the `api` container, we can use its `container_name`
    to resolve its hostname when making networked requests.
    '''
    response = requests.get('http://service:5000/')

    return jsonify({
        'status_code': response.status_code,
        'text': response.text
    })

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
