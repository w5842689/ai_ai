from moviepy.editor import ImageSequenceClip
import os
from pathlib import Path
from .image_gen import generate_image

VIDEO_DIR = Path("D:/ai_output/videos")
VIDEO_DIR.mkdir(parents=True, exist_ok=True)


def generate_video(prompt: str, num_frames: int = 24, fps: int = 24) -> str:
    # 生成多帧图像
    frame_dir = VIDEO_DIR / "temp_frames"
    frame_dir.mkdir(exist_ok=True)

    frame_paths = []
    for i in range(num_frames):
        frame_prompt = f"{prompt}, frame {i} of {num_frames}"
        path = generate_image(frame_prompt, f"frame_{i:04d}.png")
        frame_paths.append(path)

    # 合成视频
    video_path = VIDEO_DIR / "output_video.mp4"
    clip = ImageSequenceClip(frame_paths, fps=fps)
    clip.write_videofile(str(video_path), codec="libx264")

    # 清理临时帧
    for path in frame_paths:
        os.remove(path)
    os.rmdir(frame_dir)

    return str(video_path)