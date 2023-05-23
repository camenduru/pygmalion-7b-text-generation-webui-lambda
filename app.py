import os

os.system(f"git lfs install")

os.system(f"git clone -b v1.2 https://github.com/camenduru/text-generation-webui")
os.chdir(f"/home/demo/source/text-generation-webui")

os.system(f"pip install -r requirements.txt")

os.system(f"mkdir /home/demo/source/text-generation-webui/repositories")
os.chdir(f"/home/demo/source/text-generation-webui/repositories")
os.system(f"git clone -b v1.2 https://github.com/camenduru/GPTQ-for-LLaMa")
os.chdir(f"GPTQ-for-LLaMa")
os.system(f"python setup_cuda.py install")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lmsys/vicuna-13b-delta-v1.1/raw/main/config.json -d /home/demo/source/text-generation-webui/models/vicuna-13b-delta-v1.1 -o config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lmsys/vicuna-13b-delta-v1.1/raw/main/generation_config.json -d /home/demo/source/text-generation-webui/models/vicuna-13b-delta-v1.1 -o generation_config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lmsys/vicuna-13b-delta-v1.1/raw/main/special_tokens_map.json -d /home/demo/source/text-generation-webui/models/vicuna-13b-delta-v1.1 -o special_tokens_map.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lmsys/vicuna-13b-delta-v1.1/resolve/main/tokenizer.model -d /home/demo/source/text-generation-webui/models/vicuna-13b-delta-v1.1 -o tokenizer.model")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lmsys/vicuna-13b-delta-v1.1/raw/main/tokenizer_config.json -d /home/demo/source/text-generation-webui/models/vicuna-13b-delta-v1.1 -o tokenizer_config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lmsys/vicuna-13b-delta-v1.1/resolve/main/pytorch_model-00001-of-00003.bin -d /home/demo/source/text-generation-webui/models/vicuna-13b-delta-v1.1 -o pytorch_model-00001-of-00003.bin")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lmsys/vicuna-13b-delta-v1.1/resolve/main/pytorch_model-00002-of-00003.bin -d /home/demo/source/text-generation-webui/models/vicuna-13b-delta-v1.1 -o pytorch_model-00002-of-00003.bin")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lmsys/vicuna-13b-delta-v1.1/resolve/main/pytorch_model-00003-of-00003.bin -d /home/demo/source/text-generation-webui/models/vicuna-13b-delta-v1.1 -o pytorch_model-00003-of-00003.bin")

os.chdir(f"/home/demo/source/text-generation-webui")
os.system(f"python server.py --chat")