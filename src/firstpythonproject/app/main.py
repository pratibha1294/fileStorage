import uvicorn


def run():
    uvicorn.run(
        "firstpythonproject.app.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        app_dir="src",
    )


if __name__ == "__main__":
    run()