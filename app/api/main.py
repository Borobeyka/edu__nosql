import uvicorn
from fastapi import FastAPI

from app.api.routers.base import get_all_routers
from app.config.secrets import ENV

app = FastAPI(title=ENV.get("FA_TITLE"), description=ENV.get("FA_DESC"))

for router in get_all_routers():
    app.include_router(router)


def main():
    uvicorn.run(
        "app.api.main:app",
        host="0.0.0.0",
        port=int(ENV.get("FA_PORT")),
        timeout_keep_alive=10000,
        reload=ENV.get("FA_RELOAD") == "1",
        debug=ENV.get("FA_DEBUG") == "1",
    )


if __name__ == "__main__":
    main()
