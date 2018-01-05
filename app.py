'''
    * Starting point of the application
'''

# import app & configs
from src import app
from src.web_config import CONFIG

# start the app
app.run(
    host = CONFIG['host'],
    port = CONFIG['port']
)