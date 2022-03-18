### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python:
1.fast,powerful, widely used, supports different programming paradigms.
(data science, machine learning, making servers,etc.)
2."high level" : express concepts at a high level (little more than JS)
3.runs on servers(not in browsers), used to develop both desktop & web application.


JS:
1.front-end & back-end, use Node JS to write server, connect to a DB, etc.
2.runs in browsers, client-side scripting language.
3.conforms to ECMAScript specification.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
dic = {"a": 1, "b": 2}
1.dic.get("c")


- What is a unit test?
Testing code in isolated small pieces.

- What is an integration test?
Program units are combined and tested as groups in multiple ways.

- What is the role of web application framework, like Flask?
1.handle web requests
2.produce dynamic HTML
3.handle forms
4.handle cookies
5.connect to databases
6.provide user log-in/log-out
7.cache pages for performance

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  1. passing info as a parameter in a route URL ('/foods/pretzel')
  -subject of page
  2. passing info as URL query param ('foods?type=pretzel')
  -extra info about page
  -usually used coming from form

- How do you collect data from a URL placeholder parameter using Flask?

@app.route('/user/<username>')
def show_user_profile(username):
    """Show user profile for user."""
    name = USERS[username]
    return f"<h1>Profile for {name}</h1>"

- How do you collect data from the query string using Flask?

@app.route("/search")
def search():
    """Handle GET requests like /search?term=fun"""
    term = request.args["term"]
    return f"<h1>Searching for {term}</h1>"

- How do you collect data from the body of the request using Flask?

@app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""
    comment = request.form["comment"]
    return f'<h1>Received "{comment}".</h1>'

- What is a cookie and what kinds of things are they commonly used for?

A cookie is a way to store small bits of information on client(brower).
Cookies are name/string-value pair stored by the client(brower).
The server tells client to store these cookies, the client sends cookies to the server with each request.

- What is the session object in Flask?
The session object is like a dictionary.
It contains information for the current browser, preserve type(lists stay lists,etc.)
It is "signed" and "serialized" so users can't modify data- only Flask can.
In Flask, sessions are stored in browser as a cookie.

- What does Flask's `jsonify()` do?
Method that properly return JSON data. 
