from flask import Flask

app = Flask(__name__)

@ app.route('/')
def home():
    return 'aws 홈페이지'

if __name__ == '__main__' :
    # debug=True : 서버 내용이 수정되면 자동 재가동
    app.run(debug=True, host='0.0.0.0')