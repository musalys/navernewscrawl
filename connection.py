# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from sqlalchemy import create_engine
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker

server = 'ec2-35-164-25-57.us-west-2.compute.amazonaws.com'
connection_string = 'mysql+mysqldb://root:Dldbstjr89!@{}:3306/navernewscrawl'.format(server)
engine = create_engine(connection_string, pool_recycle = 3600, encoding='utf-8')
Session = sessionmaker(bind=engine)
