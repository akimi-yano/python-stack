# Create a server file that generates the specified responses for the following url requests:

# 1.localhost:5000/ - have it say "Hello World!"
# 2.localhost:5000/dojo - have it say "Dojo!"
# 3.Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
# 4.Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times

from flask import Flask
app = Flask(__name__)

@app.route("/")
def say_hello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say_name(name):
    return f"Hi {name}!"

@app.route("/repeat/<number>/<name>")
def say_number_name(number, name):
    return name*int(number)

if __name__ == "__main__":
    app.run(debug=True)