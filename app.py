import streamlit as st

from services.translator import (
    MODEL_ID,
    load_translation_model,
    translate,
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Singlish AI",
    page_icon="🇱🇰",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# SESSION STATE
# =========================================================

if "translation" not in st.session_state:
    st.session_state.translation = ""

if "model_loaded" not in st.session_state:
    st.session_state.model_loaded = False


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("Singlish AI")

    st.caption(
        "Research platform for English–Singlish "
        "translation and low-resource NLP."
    )

    st.divider()

    st.subheader("Workspace")

    st.markdown("**🌐 Translator**")
    st.caption("English → Singlish")

    st.divider()

    st.subheader("Model")

    st.caption("Fine-tuned mT5")
    st.code(MODEL_ID, language=None)

    st.divider()

    st.caption(
        "Intelligent Systems Research Project"
    )


# =========================================================
# HEADER
# =========================================================

st.title("English → Singlish")

st.markdown(
    """
    Translate English into **Sri Lankan Singlish**
    using our fine-tuned multilingual Transformer model.
    """
)

st.divider()


# =========================================================
# TRANSLATION WORKSPACE
# =========================================================

left_col, right_col = st.columns(
    2,
    gap="large",
)


# -------------------------
# ENGLISH INPUT
# -------------------------

with left_col:

    st.subheader("English")

    english_text = st.text_area(
        "English input",
        height=220,
        placeholder=(
            "Type an English sentence here...\n\n"
            "Example: Where are you going?"
        ),
        label_visibility="collapsed",
    )

    character_count = len(english_text)

    st.caption(
        f"{character_count} characters"
    )


# -------------------------
# SINGLISH OUTPUT
# -------------------------

with right_col:

    st.subheader("Singlish")

    if st.session_state.translation:

        st.text_area(
            "Translation output",
            value=st.session_state.translation,
            height=220,
            disabled=True,
            label_visibility="collapsed",
        )

    else:

        st.info(
            "Your Singlish translation will appear here."
        )


# =========================================================
# ACTION
# =========================================================

st.write("")

button_col, clear_col, _ = st.columns(
    [1.4, 1, 4]
)


with button_col:

    translate_clicked = st.button(
        "Translate",
        type="primary",
        use_container_width=True,
    )


with clear_col:

    if st.button(
        "Clear",
        use_container_width=True,
    ):
        st.session_state.translation = ""
        st.rerun()


# =========================================================
# TRANSLATION
# =========================================================

if translate_clicked:

    if not english_text.strip():

        st.warning(
            "Enter an English sentence before translating."
        )

    else:

        try:

            with st.spinner(
                "Generating Singlish translation..."
            ):

                result = translate(english_text)

            st.session_state.translation = result

            st.rerun()

        except Exception as error:

            st.error(
                "The translation model could not be loaded "
                "or the translation failed."
            )

            with st.expander("Technical details"):
                st.exception(error)


# =========================================================
# INFORMATION
# =========================================================

st.divider()

with st.expander("About this model"):

    st.markdown(
        """
        This application uses a fine-tuned **mT5**
        sequence-to-sequence Transformer for
        English-to-Singlish translation.

        The model is part of research into low-resource
        NLP for Sri Lankan code-switched communication.

        **Current version**

        - Direction: English → Singlish
        - Architecture: mT5
        - Task: Neural machine translation
        - Model hosting: Hugging Face
        """
    )