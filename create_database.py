from models.database import create_db, DATABASE_NAME
import os.path
from models import Members, Servers, Emojies, IgnorLists, RoleLists, Votums, Message, BoostLists, database

if not os.path.exists(DATABASE_NAME):
    create_db()

