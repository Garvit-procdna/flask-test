from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server, its working'

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)
