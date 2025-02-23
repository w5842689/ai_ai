import gradio as gr
from image_gen import generate_image
from video_gen import generate_video
import time


def ui_generate_image(prompt: str):
    start = time.time()
    path = generate_image(prompt, f"image_{int(start)}.png")
    return path


def ui_generate_video(prompt: str, num_frames: int, fps: int):
    start = time.time()
    path = generate_video(prompt, num_frames, fps)
    return path


with gr.Blocks(title="AI生成器") as demo:
    gr.Markdown("## 图像 & 短视频生成器")
    with gr.Tab("图像生成"):
        with gr.Row():
            image_input = gr.Textbox(label="输入描述")
            image_output = gr.Image(label="生成结果")
        image_button = gr.Button("生成")

    with gr.Tab("视频生成"):
        with gr.Row():
            video_input = gr.Textbox(label="输入描述")
            frame_slider = gr.Slider(12, 48, value=24, label="帧数")
            fps_slider = gr.Slider(12, 60, value=24, label="帧率")
            video_output = gr.Video(label="生成视频")
        video_button = gr.Button("生成视频")

    image_button.click(
        fn=ui_generate_image,
        inputs=image_input,
        outputs=image_output
    )
    video_button.click(
        fn=ui_generate_video,
        inputs=[video_input, frame_slider, fps_slider],
        outputs=video_output
    )

if __name__ == "__main__":
    demo.launch(server_port=7860, server_name="0.0.0.0")