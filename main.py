import os

import yadisk
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

y = yadisk.YaDisk(token=TOKEN)
print(y.check_token())