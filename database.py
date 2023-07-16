from sqlalchemy import create_engine, text
import os



my_secret = os.environ['reddy']
engine = create_engine(
  my_secret,
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
