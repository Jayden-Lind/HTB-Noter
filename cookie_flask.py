from flask import Flask, session, request
from flask.sessions import SecureCookieSessionInterface
    
app = Flask("example")
app.secret_key = "secret123"

# 1. this is what I was looking for
session_serializer = SecureCookieSessionInterface() \
                        .get_signing_serializer(app)
    
@app.route("/")
def test():
    username = request.args.get('username')
    session["logged_in"] = (True)
    session["username"] = (username)

    # 2. and this is how I needed to use it
    session_cookie = session_serializer.dumps(dict(session))
    print(session_cookie)
    return session_cookie



app.run(debug=True)