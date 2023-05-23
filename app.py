import os
os.system(f"git lfs install")
os.system(f"git clone -b v1.4 https://github.com/camenduru/text-generation-webui")
os.chdir(f"/home/demo/source/text-generation-webui")
os.system(f"pip install -r requirements.txt")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pygmalion-7b/raw/main/config.json -d /home/demo/source/text-generation-webui/models/pygmalion-7b -o config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pygmalion-7b/raw/main/generation_config.json -d /home/demo/source/text-generation-webui/models/pygmalion-7b -o generation_config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pygmalion-7b/raw/main/special_tokens_map.json -d /home/demo/source/text-generation-webui/models/pygmalion-7b -o special_tokens_map.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pygmalion-7b/resolve/main/tokenizer.model -d /home/demo/source/text-generation-webui/models/pygmalion-7b -o tokenizer.model")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pygmalion-7b/raw/main/tokenizer_config.json -d /home/demo/source/text-generation-webui/models/pygmalion-7b -o tokenizer_config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pygmalion-7b/resolve/main/model-00001-of-00002.safetensors -d /home/demo/source/text-generation-webui/models/pygmalion-7b -o model-00001-of-00002.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pygmalion-7b/resolve/main/model-00002-of-00002.safetensors -d /home/demo/source/text-generation-webui/models/pygmalion-7b -o model-00002-of-00002.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pygmalion-7b/resolve/main/model.safetensors.index.json -d /home/demo/source/text-generation-webui/models/pygmalion-7b -o model.safetensors.index.json")

os.system(f"python server.py --chat")