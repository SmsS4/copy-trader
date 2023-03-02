from fastapi import FastAPI
import uvicorn
from copy_trader import routes
from fastapi import Request
from pprint import pprint


def main() -> None:
    """
    Main function to start copy trader server
    """
    app = FastAPI()
    """
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        request_body = await request.body()
        print(type(request_body))
        pprint(request_body)
        if len(request_body) >= 5:
            print(request_body[-1])
            print(request_body[-2])
            print(request_body[-3])
            print(request_body[-4])
            print(request_body[-5])
        response = await call_next(request)
        return response
    """
    app.include_router(routes.router)
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
