import os
os.system(f"pip install -q torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1+cu118 torchtext==0.15.1 torchdata==0.6.0 --extra-index-url https://download.pytorch.org/whl/cu118 -U")

# os.system(f"git lfs install")
# os.system(f"git clone -b v1.4 https://github.com/camenduru/text-generation-webui")
# os.chdir(f"/home/demo/source/text-generation-webui")
# os.system(f"pip install -r requirements.txt")

# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pyg-7b/raw/main/config.json -d /home/demo/source/text-generation-webui/models/pyg-7b -o config.json")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pyg-7b/raw/main/generation_config.json -d /home/demo/source/text-generation-webui/models/pyg-7b -o generation_config.json")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pyg-7b/raw/main/special_tokens_map.json -d /home/demo/source/text-generation-webui/models/pyg-7b -o special_tokens_map.json")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pyg-7b/resolve/main/tokenizer.model -d /home/demo/source/text-generation-webui/models/pyg-7b -o tokenizer.model")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pyg-7b/raw/main/tokenizer_config.json -d /home/demo/source/text-generation-webui/models/pyg-7b -o tokenizer_config.json")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pyg-7b/resolve/main/model-00001-of-00002.safetensors -d /home/demo/source/text-generation-webui/models/pyg-7b -o model-00001-of-00002.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pyg-7b/resolve/main/model-00002-of-00002.safetensors -d /home/demo/source/text-generation-webui/models/pyg-7b -o model-00002-of-00002.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/4bit/pyg-7b/resolve/main/model.safetensors.index.json -d /home/demo/source/text-generation-webui/models/pyg-7b -o model.safetensors.index.json")

# os.system(f"python server.py --chat")

import gradio as gr
from subprocess import getoutput

def run(command):
    out = getoutput(f"{command}")
    return out

with gr.Blocks() as demo:
    command = gr.Textbox(show_label=False, max_lines=1, placeholder="command")
    out_text = gr.Textbox(show_label=False)
    btn_run = gr.Button("run command")
    btn_run.click(run, inputs=command, outputs=out_text)

demo.launch()