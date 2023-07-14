'''Script to seed the team_up database'''

import os
import crud
import model
import server

os.system('dropdb team_up')
os.system('createdb team_up')

model.connect_to_db(server.app)
model.db.create_all()

