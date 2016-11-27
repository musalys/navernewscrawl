# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from sqlalchemy import create_engine
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker

server = 'your_server_host'
connection_string = 'mysql+mysqldb://root:<your_mysql_password>@{}:3306/<your_mysql_schema_name>'.format(server)
engine = create_engine(connection_string, pool_recycle = 3600, encoding='utf-8')
Session = sessionmaker(bind=engine)
