# External Libs
import os
import uvicorn
# Modules

# Vals
PORT = int(os.getenv["SERVER_PORT", "5000"])

# Middlewares

# Routes


if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, log_level="info")