import torch
import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


MODEL_ID = "Madushanavod/english-singlish-mt5"

MAX_SOURCE_LENGTH = 64
MAX_TARGET_LENGTH = 64


@st.cache_resource(show_spinner=False)
def load_translation_model():
    """
    Load the fine-tuned English-to-Singlish mT5 model.

    Streamlit caches the model so it is not downloaded and
    initialized again after every UI interaction.
    """

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    model = AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_ID
    )

    model.eval()

    return tokenizer, model


def translate(text: str) -> str:
    """
    Translate English text into Singlish using the fine-tuned
    mT5 model.
    """

    text = text.strip()

    if not text:
        return ""

    tokenizer, model = load_translation_model()

    # IMPORTANT:
    # Keep the same task prefix used during model training.
    prompt = f"translate English to Singlish: {text}"

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=MAX_SOURCE_LENGTH,
        truncation=True,
    )

    with torch.inference_mode():
        output_ids = model.generate(
            **inputs,
            max_length=MAX_TARGET_LENGTH,
            num_beams=4,
            early_stopping=True,
        )

    translation = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True,
    )

    return translation.strip()