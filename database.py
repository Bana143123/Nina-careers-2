from sqlalchemy import create_engine, text

dbconn_string = 'mysql+pymysql://2q35n140237o0y79mo1h:pscale_pw_leCtzoPjO5tBL81ncJUZbyL5uA0O6EXTa7Z6CkHR9vf@aws.connect.psdb.cloud/nina?charset=utf8mb4'
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
