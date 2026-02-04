# À placer au début de TP2/app.py

import streamlit as st
from PIL import Image

from pipeline_utils import (
    DEFAULT_MODEL_ID,
    load_text2img,
    to_img2img,
    get_device,
    make_generator,
)

st.set_page_config(page_title="TP2 - Diffusion e-commerce", layout="wide")

@st.cache_resource
def get_text2img_pipe(model_id: str, scheduler_name: str):
    # TODO: charger le pipeline text2img
    return load_text2img(model_id, scheduler_name)


# À placer après le bloc précédent dans TP2/app.py

st.title("TP2 — Diffusion mini-product (e-commerce)")

mode = st.sidebar.selectbox("Mode", ["Text2Img", "Img2Img"])

model_id = st.sidebar.text_input("Model ID", value=DEFAULT_MODEL_ID)
scheduler_name = st.sidebar.selectbox("Scheduler", ["EulerA", "DDIM", "DPM++"])

seed = st.sidebar.number_input("Seed", min_value=0, max_value=10_000_000, value=42, step=1)
steps = st.sidebar.slider("Steps", 5, 60, 30)
guidance = st.sidebar.slider("Guidance (CFG)", 1.0, 15.0, 7.5, 0.5)

prompt = st.text_area("Prompt", value="e-commerce product shot of a glowing rectangular lightbox with a minimalist nature art print, on a clean dark wall, cinematic lighting, soft ambient glow, ultra-realistic, 8k, sharp focus")
negative_prompt = st.text_area("Negative prompt", value="text, watermark, logo, low quality, blurry, deformed")

init_image = None
strength = None
if mode == "Img2Img":
    up = st.file_uploader("Input image (img2img)", type=["png", "jpg", "jpeg"])
    strength = st.slider("Strength", 0.0, 0.95, 0.60, 0.05)
    if up is not None:
        init_image = Image.open(up).convert("RGB")
        st.image(init_image, caption="Input image", use_container_width=True)

run = st.button("Generate", type="primary")