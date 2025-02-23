import torch
from diffusers import StableDiffusionPipeline
from pathlib import Path

# 模型和输出路径
MODEL_DIR = Path("D:/ai_models/v1-5-pruned-emaonly.safetensors")
OUTPUT_DIR = Path("D:/ai_output/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 加载模型（自动下载或读取本地缓存）
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/v1-5-pruned-emaonly.safetensors",
    torch_dtype=torch.float16,
    cache_dir=MODEL_DIR
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
pipe.enable_attention_slicing()  # 减少显存占用

def generate_image(prompt: str, filename: str = "output.png") -> str:
    image = pipe(prompt, num_inference_steps=25).images[0]
    output_path = OUTPUT_DIR / filename
    image.save(output_path)
    return str(output_path)
from diffusers import StableDiffusionPipeline
import os

# 强制离线模式
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["HF_HOME"] = "D:/ai_models/huggingface"

# 指定本地模型路径（替换 [随机ID] 为实际值）
model_path = "D:/ai_models/huggingface/hub/models--runwayml--stable-diffusion-v1-5/snapshots/[随机ID]"

pipe = StableDiffusionPipeline.from_pretrained(
    model_path,
    safety_checker=None,
    requires_safety_checker=False,
    local_files_only=True  # 强制使用本地文件
)