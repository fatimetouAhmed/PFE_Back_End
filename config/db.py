from sqlalchemy import create_engine,MetaData
engine=create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
meta=MetaData()
con=engine.connect()