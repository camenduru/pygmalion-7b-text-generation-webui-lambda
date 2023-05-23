import os

os.system(f"git lfs install")

os.system(f"git clone -b v1.2 https://github.com/camenduru/text-generation-webui")
os.chdir(f"/home/demo/source/text-generation-webui")

os.system(f"pip install -r requirements.txt")

os.system(f"mkdir /home/demo/source/text-generation-webui/repositories")
os.system(f"cd /home/demo/source/text-generation-webui/repositories")
os.system(f"git clone -b v1.2 https://github.com/camenduru/GPTQ-for-LLaMa.git")
os.system(f"cd GPTQ-for-LLaMa")
os.system(f"python setup_cuda.py install")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/vicuna-v1.1-13b-GPTQ-4bit-128g/raw/main/config.json -d /home/demo/source/text-generation-webui/models/vicuna-v1.1-13b-GPTQ-4bit-128g -o config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/vicuna-v1.1-13b-GPTQ-4bit-128g/raw/main/generation_config.json -d /home/demo/source/text-generation-webui/models/vicuna-v1.1-13b-GPTQ-4bit-128g -o generation_config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/vicuna-v1.1-13b-GPTQ-4bit-128g/raw/main/special_tokens_map.json -d /home/demo/source/text-generation-webui/models/vicuna-v1.1-13b-GPTQ-4bit-128g -o special_tokens_map.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/vicuna-v1.1-13b-GPTQ-4bit-128g/resolve/main/tokenizer.model -d /home/demo/source/text-generation-webui/models/vicuna-v1.1-13b-GPTQ-4bit-128g -o tokenizer.model")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/vicuna-v1.1-13b-GPTQ-4bit-128g/raw/main/tokenizer_config.json -d /home/demo/source/text-generation-webui/models/vicuna-v1.1-13b-GPTQ-4bit-128g -o tokenizer_config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/vicuna-v1.1-13b-GPTQ-4bit-128g/resolve/main/4bit-128g.safetensors -d /home/demo/source/text-generation-webui/models/vicuna-v1.1-13b-GPTQ-4bit-128g -o 4bit-128g.safetensors")

os.chdir(f"/home/demo/source/text-generation-webui")
os.system(f"python server.py --share --chat --wbits 4 --groupsize 128")