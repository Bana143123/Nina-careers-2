from sqlalchemy import create_engine,text
dbconn_string ='mysql+pymysql://mnsod64c98hghcg3mit9:pscale_pw_44sxj6v5nfxt1MBAYBvS0H5WzOvTNM1aT4a58MNKUvv@aws.connect.psdb.cloud/nina?charset=utf8mb4'
engine = create_engine(dbconn_string,
                      connect_args={
                         "ssl": {
                           "ssl_ca": "/home/gord/client-ssl/ca.pem",
                           #"ssl_cert": "/home/gord/client-ssl/client-cert.pem",
                           #"ssl_key": "/home/gord/client-ssl/client-key.pem"
                         }
                       })

with engine.connect() as conn:
    result = conn.execute(text("select * from JOBS"))
result_dict=[]
for row in result.all():
  result_dict.append(row)
print(result_dict)