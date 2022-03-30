from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello(*args, **kwargs):
	print(kwargs)
	return f"Hello World! \n{request.data}"

if __name__ == '__main__':
	app.run()
