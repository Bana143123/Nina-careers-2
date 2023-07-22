from flask import Flask,render_template,request
#from database import fetchjobsfromdb
import yaml as yl

app = Flask(__name__)


with open('config.yaml','r') as config:
  load=yl.safe_load(config)
#print(load)
jobs=load['JOBS']
@app.route('/')
def hello_world():
  
  return render_template('home.html',
                        jobs=jobs,
                        company_name='Nina')
@app.route('/jobs/<int:id>')
def job_item(id):
  if id<1 or id>len(jobs):
    return "no job found",404

  
  return render_template('jobpage.html',job=jobs[id-1])

@app.route('/jobs/<int:id>/apply',methods=['post'])
def apply(id):
  #data=request.form

  return render_template('submit.html',job=jobs[id-1])




if __name__ == '__main__':
  app.run(debug=True)