from huggingface_hub import hf_hub_download
import yaml
import os


def read_config(config_path: str):
    with open(config_path, "r") as stream:
        config = yaml.full_load(stream)
    return config


def check_dir(directory: str) -> str:
    if os.path.exists(directory):
        return directory
    else:
        os.mkdir(directory)
        return directory


def download_files(model_name, version):
    model_path = hf_hub_download(
        repo_id=model_name, filename="llama-2-7b.ggmlv3.q4_0.bin", local_dir="./models"
    )
    config_path = hf_hub_download(
        repo_id=model_name, filename="config.json", local_dir=check_dir("./models")
    )
    return model_path, config_path


if __name__ == "__main__":
    config_file = "./config.yml"
    config = read_config(config_file)
    # Download the files from HF hub
    model_repo_name = config["NAME"]
    model_version = config["VERSION"]
    model_path, cnf_path = download_files(model_repo_name, model_version)
    print(f"files downloaded at {model_path} and {cnf_path}")
