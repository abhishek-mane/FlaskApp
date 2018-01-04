'''
    * Starting point of the application
'''

# Import app
from src import APP as app, config

# Run the app
app.run(
    host=config.WEBCONFIG['host'],
    port=config.WEBCONFIG['port']
)
