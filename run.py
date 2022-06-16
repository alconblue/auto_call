from src import create_app
from dotenv import load_dotenv

load_dotenv('.env')

app = create_app()

app.run(debug=True)