# GPT4PXL REST API
### Starting the app

First change your working directory to `gpt4all/gpt4all-api`.
Then add the zephyr-7B-alpha-GGUF to the models folder.
You can find that here https://huggingface.co/TheBloke/zephyr-7B-alpha-GGUF/blob/main/zephyr-7b-alpha.Q4_K_M.gguf

Then you can start the docker container and start to use the api
```bash
python3 modelPull.py
```
```bash
docker compose up --build
```


## ignore this 

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



