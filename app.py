from flask import Flask
app=Flask(__name__)

@app.route('/')
def api():
    return 'devesh mehta'

if __name__=='__main__':
    app.run()