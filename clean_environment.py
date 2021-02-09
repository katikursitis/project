import requests

try:
    print('Sending request to stop rest app server')
    requests.get('http://127.0.0.1:5000/stop_server')
    print('rest app server stopped')
except Exception as e:
    print(e)
    print('Error occurred when trying to close rest app server')

try:
    print('Sending request to stop web app server')
    requests.get('http://127.0.0.1:5001/stop_server')
    print('web app server stopped')
except Exception as e:
    print(e)
    print('Error occurred when trying to close web app server')