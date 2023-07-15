from sqlalchemy import create_engine, text

dbconn_string = 'mysql+pymysql://qqbfgd5h4dol9qna4t0u:pscale_pw_NLhbIX1aGz6mGp97JZGyZP3r8Sryzo0zqtEKTXqDxHg@aws.connect.psdb.cloud/nina?charset=utf8mb4'
engine = create_engine(
  dbconn_string,
  connect_args={"ssl": {
    "ssl_ca": "/home/gord/client-ssl/ca.pem",
  }})

with engine.connect() as conn:
  result = conn.execute(text("select * from JOBS"))
result_dict = []
for row in result.all():
  result_dict.append(row)
print(result_dict)


def fetchjobsfromdb():
  with engine.connect() as conn:
    result = conn.execute(text("select * from JOBS"))
    jobs = [dict(row._asdict()) for row in result]
    return jobs
