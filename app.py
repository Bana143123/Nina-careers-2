from flask import Flask,render_template,jsonify
from database import fetchjobsfromdb

app = Flask(__name__)

'''JOBS=[
  {
    'id':1,
    'title':'Hair Groomer',
    'location':'Bengaluru, India',
    'salary':'Rs.70,000'
  },
  {
    'id':2,
    'title':'Facial specialist',
    'location':'Coimbatore, India',
    'salary':'Rs.50,000'
  },
  {
    'id':3,
    'title':'Spa Trainer',
    'location':'Paris, London',
  },
{
    'id':4,
    'title':'Accountant',
    'location':'Bengaluru, India',
    'salary':'Rs.1,70,000'
  }
]
'''

    

@app.route('/')
def hello_world():
  jobs=fetchjobsfromdb()
  return render_template('home.html',
                        jobs=jobs,
                        company_name='Nina')
@app.route('/jobs')
def job_item():
  jobs=fetchjobsfromdb()
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)