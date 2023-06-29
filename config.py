from starlette.config import Config

config = Config(".env")

OPENAI_API_KEY = config("OPENAI_API_KEY", default="")
