from config import CONFIG
from src import app

# run app
app.run(host=CONFIG['host'], port=CONFIG['port'])