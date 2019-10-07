from flask import Flask, render_template

app = Flask(__name__, template_folder="client/build",
            static_folder="client/build/static")

@app.route('/prediction')
def predict():
    return "This is test api"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("Current path:" + path)
    return render_template('index.html')
    # return 'You want path: %s' % path

if __name__ == '__main__':
    app.run()
