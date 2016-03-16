from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return "<h2>whoru panchod</h2><a href="/my-link/">Click me</a>"
#render_template('template.html')

@app.route('/my-link/')
def my_link():
  print 'I got clicked!'

  return 'Click.'

if __name__ == '__main__':
  app.run()