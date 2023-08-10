from huggingface_hub import snapshot_download
import yaml
import os


def read_config(config_path: str):
    with open(config_path, "r") as stream:
        config = yaml.full_load(stream)
    print(type(config))
    return config


def check_dir(directory: str) -> str:
    if os.path.exists(directory):
        return directory
    else:
        os.mkdir(directory)
        return directory


def download_files(model_name):
    snapshot_download(repo_id=model_name, local_dir=check_dir("./models"))


if __name__ == "__main__":
    config_file = "./config.yml"
    config = read_config(config_file)
    # Download the files from HF hub
    model_repo_name = config["NAME"]
    download_files(model_repo_name)
    print("files downloaded")
