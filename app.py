'''
    * Starting point of the application
'''

# Import app
from src import app, web_config as config

# Run the app
app.run(
    host=config.WEBCONFIG['host'],
    port=config.WEBCONFIG['port']
)
