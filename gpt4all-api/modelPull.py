from huggingface_hub import hf_hub_download
import os

# Specify the filename to download
selected_filename = "zephyr-7b-alpha.Q4_K_M.gguf"

directory = os.getcwd()
destination_path = os.path.join(directory, "gpt4all_api/models", selected_filename)

# Check if the file already exists in the destination folder
if os.path.exists(destination_path):
    print(f"File '{selected_filename}' already exists in the /models folder.")
else:
    # Download the selected file
    print(f"Downloading '{selected_filename}'.")
    hf_hub_download(repo_id="TheBloke/zephyr-7B-alpha-GGUF", filename=selected_filename, local_dir=directory + "/gpt4all_api/models", local_dir_use_symlinks=False)
    print(f"File '{selected_filename}' downloaded successfully into the /models folder.")