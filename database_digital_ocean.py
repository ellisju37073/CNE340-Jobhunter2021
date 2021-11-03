from sqlalchemy import create_engine

hostname="147.182.207.57"
uname="pythoneverything"
pwd="python123"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}"
            .format(host=hostname, user=uname, pw=pwd))
engine.execute("Create DATABASE fuel")