# GPT4PXL REST API
### Starting the app

First change your working directory to `gpt4all/gpt4all-api`.

Now you can build the FastAPI docker image. You only have to do this on initial build or when you add new dependencies to the requirements.txt file:
```bash
DOCKER_BUILDKIT=1 docker build -t gpt4all_api --progress plain -f gpt4all_api/Dockerfile.buildkit .
```

Then, start the backend with:

```bash
docker compose up --build
```

This will run both the API and locally hosted GPU inference server. If you want to run the API without the GPU inference server, you can run:

```bash
docker compose up --build gpt4all_api
```

To run the API with the GPU inference server, you will need to include environment variables (like the `MODEL_ID`). Edit the `.env` file and run
```bash
docker compose --env-file .env up --build
```


#### Spinning up your app
Run `docker compose up` to spin up the backend. Monitor the logs for errors in-case you forgot to set an environment variable above.



