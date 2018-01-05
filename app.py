'''
    * Starting point of the application
'''

# import app & configs
from src import app, web_config

# start the app
app.run(
    host=web_config.CONFIG['host'],
    port=web_config.CONFIG['port']
)
