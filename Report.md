# dockerized-LLM

# STEPS FOLLOWED IN ASSIGNMENT

1. Download the models during the build of the docker container by using a separate script and relevant packages
2. Create an inference script using the python binding of Llama cpp for inference
2. Create a fastapi endpoint which can serve a text completion of the input prompt via JSON
3. Dockerize the entire code and expose the endpoint via port 8000

# IDEA

The initial idea was to download and run the models from hugging face

## CHALLENGE 1

- Initial challenge is that off the shelf inference of hugging face scripts and transformers library using from_pretrained would download the model  every single time inference request is called which is very suboptimal. 

## SOLUTION 1

Write an initial script to download the model to local directory while building the docker image and then use

## CHALLENGE 2
While going through the Large language model on my local system I noticed that just using off the shelf python models are bad for the following reasons
- Downloads a lot of unneccessary information which is not required during inference time if we use snapshot download
- The resource requirements for simple 7B parameter models are way too high (requires a minimum 8GB GPU and 16GB plus CPU RAM to load the model) while the local system which is representative of the low resource environment mentioned in the assignment has 4GB RAM of CPU (only available for inference and no other tasks running in the background) and No GPU

## SOLUTION 2

- I have previously read about quantized models which reduces the requirements of the CPU because it converts the float16 bit weights into smaller data types. So I chose to opt for such a model from The Bloke who had quantized LLama V2 LLM model.
- Other optimized way was to use the llama-cpp-python package which provided python API bindings for the Llama CPP repository for running inference on low resource requirements. 

## ADVANTAGES OF SOLUTION 2
-   The advantages of solution 2 from a docker perspective is that it eliminated the need for GPU packages and Pytorch which by itself is a very heavy package thereby creating as light weight as possible inference environment in terms of docker image size. 




