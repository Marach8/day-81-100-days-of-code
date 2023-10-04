from flask import Flask, request

marach = Flask(__name__)

@marach.route('/robot', methods=['POST'])
def robot():
  page = ''
  a = request.form
  if a['text'].lower() == 'error' and a['question'] == 'no':
    page += 'Welcome, You are not a robot🎉'
  else:
    page += 'You are a robot🙄'

  return page


@marach.route('/')
def home():
  page = ''
  file = open('template.html', 'r')
  page = file.read()
  file.close()
  return page

marach.run(host='0.0.0.0', port=81)