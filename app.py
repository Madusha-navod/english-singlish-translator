# # import streamlit as st

# # from services.translator import (
# #     MODEL_ID,
# #     load_translation_model,
# #     translate,
# # )


# # # =========================================================
# # # PAGE CONFIGURATION
# # # =========================================================

# # st.set_page_config(
# #     page_title="Singlish AI",
# #     page_icon="🇱🇰",
# #     layout="wide",
# #     initial_sidebar_state="expanded",
# # )


# # # =========================================================
# # # SESSION STATE
# # # =========================================================

# # if "translation" not in st.session_state:
# #     st.session_state.translation = ""

# # if "model_loaded" not in st.session_state:
# #     st.session_state.model_loaded = False


# # # =========================================================
# # # SIDEBAR
# # # =========================================================

# # with st.sidebar:

# #     st.title("Singlish AI")

# #     st.caption(
# #         "Research platform for English–Singlish "
# #         "translation and low-resource NLP."
# #     )

# #     st.divider()

# #     st.subheader("Workspace")

# #     st.markdown("**🌐 Translator**")
# #     st.caption("English → Singlish")

# #     st.divider()

# #     st.subheader("Model")

# #     st.caption("Fine-tuned mT5")
# #     st.code(MODEL_ID, language=None)

# #     st.divider()

# #     st.caption(
# #         "Intelligent Systems Research Project"
# #     )


# # # =========================================================
# # # HEADER
# # # =========================================================

# # st.title("English → Singlish")

# # st.markdown(
# #     """
# #     Translate English into **Sri Lankan Singlish**
# #     using our fine-tuned multilingual Transformer model.
# #     """
# # )

# # st.divider()


# # # =========================================================
# # # TRANSLATION WORKSPACE
# # # =========================================================

# # left_col, right_col = st.columns(
# #     2,
# #     gap="large",
# # )


# # # -------------------------
# # # ENGLISH INPUT
# # # -------------------------

# # with left_col:

# #     st.subheader("English")

# #     english_text = st.text_area(
# #         "English input",
# #         height=220,
# #         placeholder=(
# #             "Type an English sentence here...\n\n"
# #             "Example: Where are you going?"
# #         ),
# #         label_visibility="collapsed",
# #     )

# #     character_count = len(english_text)

# #     st.caption(
# #         f"{character_count} characters"
# #     )


# # # -------------------------
# # # SINGLISH OUTPUT
# # # -------------------------

# # with right_col:

# #     st.subheader("Singlish")

# #     if st.session_state.translation:

# #         st.text_area(
# #             "Translation output",
# #             value=st.session_state.translation,
# #             height=220,
# #             disabled=True,
# #             label_visibility="collapsed",
# #         )

# #     else:

# #         st.info(
# #             "Your Singlish translation will appear here."
# #         )


# # # =========================================================
# # # ACTION
# # # =========================================================

# # st.write("")

# # button_col, clear_col, _ = st.columns(
# #     [1.4, 1, 4]
# # )


# # with button_col:

# #     translate_clicked = st.button(
# #         "Translate",
# #         type="primary",
# #         use_container_width=True,
# #     )


# # with clear_col:

# #     if st.button(
# #         "Clear",
# #         use_container_width=True,
# #     ):
# #         st.session_state.translation = ""
# #         st.rerun()


# # # =========================================================
# # # TRANSLATION
# # # =========================================================

# # if translate_clicked:

# #     if not english_text.strip():

# #         st.warning(
# #             "Enter an English sentence before translating."
# #         )

# #     else:

# #         try:

# #             with st.spinner(
# #                 "Generating Singlish translation..."
# #             ):

# #                 result = translate(english_text)

# #             st.session_state.translation = result

# #             st.rerun()

# #         except Exception as error:

# #             st.error(
# #                 "The translation model could not be loaded "
# #                 "or the translation failed."
# #             )

# #             with st.expander("Technical details"):
# #                 st.exception(error)


# # # =========================================================
# # # INFORMATION
# # # =========================================================

# # st.divider()

# # with st.expander("About this model"):

# #     st.markdown(
# #         """
# #         This application uses a fine-tuned **mT5**
# #         sequence-to-sequence Transformer for
# #         English-to-Singlish translation.

# #         The model is part of research into low-resource
# #         NLP for Sri Lankan code-switched communication.

# #         **Current version**

# #         - Direction: English → Singlish
# #         - Architecture: mT5
# #         - Task: Neural machine translation
# #         - Model hosting: Hugging Face
# #         """
# #     )

# # ----------new code----------------------

# import streamlit as st

# from services.translator import (
#     MODEL_ID,
#     InvalidTranslationError,
#     translate,
# )


# # =========================================================
# # PAGE CONFIGURATION
# # =========================================================

# st.set_page_config(
#     page_title="Singlish AI",
#     page_icon="🇱🇰",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )


# # =========================================================
# # SESSION STATE
# # =========================================================

# if "translation" not in st.session_state:
#     st.session_state.translation = ""

# if "model_loaded" not in st.session_state:
#     st.session_state.model_loaded = False

# def clear_translation():
#     st.session_state.translation = ""


# def clear_workspace():
#     st.session_state.english_input = ""
#     clear_translation()


# # =========================================================
# # SIDEBAR
# # =========================================================

# with st.sidebar:

#     st.title("Singlish AI")

#     st.caption(
#         "Research platform for English–Singlish "
#         "translation and low-resource NLP."
#     )

#     st.divider()

#     st.subheader("Workspace")

#     st.markdown("**🌐 Translator**")
#     st.caption("English → Singlish")

#     st.divider()

#     st.subheader("Model")

#     st.caption("Fine-tuned mT5")
#     st.code(MODEL_ID, language=None)

#     st.divider()

#     st.caption(
#         "Intelligent Systems Research Project"
#     )


# # =========================================================
# # HEADER
# # =========================================================

# st.title("English → Singlish")

# st.markdown(
#     """
#     Translate English into **Sri Lankan Singlish**
#     using our fine-tuned multilingual Transformer model.
#     """
# )

# st.divider()


# # =========================================================
# # TRANSLATION WORKSPACE
# # =========================================================

# left_col, right_col = st.columns(
#     2,
#     gap="large",
# )


# # -------------------------
# # ENGLISH INPUT
# # -------------------------

# with left_col:

#     st.subheader("English")

#     english_text = st.text_area(
#         "English input",
#         key="english_input",
#         on_change=clear_translation,
#         height=220,
#         placeholder=(
#             "Type an English sentence here...\n\n"
#             "Example: Where are you going?"
#         ),
#         label_visibility="collapsed",
#     )

#     character_count = len(english_text)

#     st.caption(
#         f"{character_count} characters"
#     )


# # -------------------------
# # SINGLISH OUTPUT
# # -------------------------

# with right_col:

#     st.subheader("Singlish")

#     if st.session_state.translation:

#         st.text_area(
#             "Translation output",
#             value=st.session_state.translation,
#             height=220,
#             disabled=True,
#             label_visibility="collapsed",
#         )

#     else:

#         st.info(
#             "Your Singlish translation will appear here."
#         )


# # =========================================================
# # ACTION
# # =========================================================

# st.write("")

# button_col, clear_col, _ = st.columns( 
#     [1.4, 1, 4]
# )


# with button_col:

#     translate_clicked = st.button(
#         "Translate",
#         type="primary",
#         use_container_width=True,
#     )


# with clear_col:

#     st.button(
#         "Clear",
#         use_container_width=True,
#         on_click=clear_workspace,
#     )


# # =========================================================
# # TRANSLATION
# # =========================================================

# if translate_clicked:

#     if not english_text.strip():

#         st.warning(
#             "Enter an English sentence before translating."
#         )

#     else:

#         st.session_state.translation = ""

#         try:
#             with st.spinner(
#                 "Generating Singlish translation..."
#             ):

#                 result = translate(english_text)

#             st.session_state.translation = result

#             st.rerun()

#         except (InvalidTranslationError, ValueError) as error:

#             st.warning(str(error))

#         except Exception as error:

#             st.error(
#                 "The translation model could not be loaded "
#                 "or the translation failed."
#             )

#             with st.expander("Technical details"):
#                 st.exception(error)


# # =========================================================
# # INFORMATION
# # =========================================================

# st.divider()
# with st.expander("About this model"):

#     st.markdown(
#         """
#         This application uses a fine-tuned **mT5**
#         sequence-to-sequence Transformer for
#         English-to-Singlish translation.

#         The model is part of research into low-resource
#         NLP for Sri Lankan code-switched communication.

#         **Current version**

#         - Direction: English → Singlish
#         - Architecture: mT5
#         - Task: Neural machine translation
#         - Model hosting: Hugging Face
#         """
#     )
"""Singlish AI interface. Run from the repository with: streamlit run app.py"""

from html import escape

import streamlit as st

from services.translator import MODEL_ID, InvalidTranslationError, translate

st.set_page_config(
    page_title="Singlish AI",
    page_icon="🇱🇰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom styling is limited to the interface; translation uses the existing service.
st.markdown(
    """
<style>
    .stApp { background: #F6F7FB; color: #17233C; }
    .block-container { max-width: 1100px; padding-top: 3rem; padding-bottom: 2rem; }
    h1, h2, h3 { color: #17233C; }
    .brand-bar { display: flex; align-items: center; justify-content: space-between;
        gap: 16px; flex-wrap: wrap; padding-bottom: 24px; }
    .brand { display: flex; align-items: center; gap: 12px;
        font-size: 22px; font-weight: 700; }
    .brand-symbol { background: #5145CD; color: white; border-radius: 12px;
        padding: 9px 12px; font-size: 19px; }
    .language-badge { border: 1px solid #DCE2EF; background: white;
        border-radius: 24px; padding: 8px 14px; font-size: 13px; color: #59677E; }
    .eyebrow { margin-top: 14px; color: #5145CD; font-size: 12px;
        font-weight: 700; letter-spacing: 1.8px; }
    .hero-title { font-size: clamp(28px, 4vw, 42px); line-height: 1.2;
        letter-spacing: -1px; margin: 10px 0 12px; font-weight: 750; }
    .hero-description { color: #59677E; font-size: 16px;
        line-height: 1.6; margin-bottom: 28px; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: white; border-radius: 18px; }
    [data-testid="stTextArea"] textarea {
        background: #F8F9FC; color: #17233C; border-radius: 12px;
        font-size: 18px; line-height: 1.7; }
    [data-testid="stTextArea"] textarea:focus {
        border-color: #5145CD; box-shadow: 0 0 0 2px #E5E2FF; }
    .result-box { background: #F0EEFF; border: 1px solid #E3DFFF;
        border-radius: 12px; padding: 18px; min-height: 220px;
        color: #17233C; font-size: 20px; line-height: 1.7;
        white-space: pre-wrap; overflow-wrap: anywhere; }
    .result-empty { color: #626A80; font-size: 16px; }
    [data-testid="stBaseButton-primary"] {
        background: #5145CD; border-color: #5145CD; color: white;
        border-radius: 10px; min-height: 44px; }
    [data-testid="stBaseButton-primary"]:hover {
        background: #4035AE; border-color: #4035AE; color: white; }
    [data-testid="stBaseButton-secondary"],
    [data-testid="stBaseButton-secondaryFormSubmit"] {
        background: white; color: #17233C; border-color: #DCE2EF;
        border-radius: 10px; min-height: 44px; }
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stWidgetLabel"] p { color: #17233C; }
    [data-testid="stCaptionContainer"] { color: #59677E; }
    .review-note { color: #59677E; font-size: 13px; line-height: 1.7;
        margin: 20px 0; }
    .footer { display: flex; justify-content: space-between; gap: 12px;
        flex-wrap: wrap; border-top: 1px solid #DCE2EF; margin-top: 28px;
        padding-top: 18px; color: #59677E; font-size: 12px; }
    @media (max-width: 640px) {
        .block-container { padding: 2rem 1rem; }
        [data-testid="stHorizontalBlock"] { flex-wrap: wrap; }
        [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
            min-width: 100%; flex: 1 1 100%; }
    }
    </style>
    """,
     unsafe_allow_html=True,
)

# Callbacks run before the next page render, so widget values can be reset safely.
for key, default in {
    "english_input": "",
    "translation": "",
    "translation_error": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


def clear_translation():
    st.session_state.translation = ""
    st.session_state.translation_error = ""


def clear_workspace():
    st.session_state.english_input = ""
    clear_translation()


def use_example(sentence):
    st.session_state.english_input = sentence
    clear_translation()


st.markdown(
    """
    <div class="brand-bar">
      <div class="brand"><span class="brand-symbol" aria-hidden="true">ආ</span>Singlish AI</div>
      <span class="language-badge">English → Singlish</span>
    </div>
    <div class="eyebrow">A LITTLE MORE LOCAL</div>
    <h1 class="hero-title">Your words. In Singlish.</h1>
    <p class="hero-description">Translate English into Sinhala written with English letters.</p>
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown("**English → Singlish**")
    left, right = st.columns(2, gap="large")

    with left:
        st.subheader("English")
        english_text = st.text_area(
            "English text",
            key="english_input",
            on_change=clear_translation,
            height=220,
            placeholder="Type an English sentence here…",
            label_visibility="collapsed",
        )
        st.caption(f"{len(english_text)} characters · Short sentences work best")
        translate_clicked = st.button(
            "Translate →", type="primary", use_container_width=True
        )
        st.button("Clear", on_click=clear_workspace, use_container_width=True)

    with right:
        st.subheader("Singlish")
        # Render the result after processing the action, avoiding an extra rerun.
        output_slot = st.empty()
        st.caption("Sinhala, in English letters")
        copy_slot = st.empty()
        
    if translate_clicked:
        clear_translation()
        if not english_text.strip():
            st.session_state.translation_error = "Enter an English sentence first."
        else:
            try:
                with st.spinner("Translating your sentence…"):
                    st.session_state.translation = translate(english_text)
            except (InvalidTranslationError, ValueError) as error:
                st.session_state.translation_error = str(error)
            except Exception:
                st.session_state.translation_error = (
                    "We couldn't complete the translation. Please try again. "
                    "If this continues, check the model and app logs."
                )

    result = st.session_state.translation
    # Escape model output before inserting it into HTML.
    if result:
        output_slot.markdown(
            f'<div class="result-box" role="status">{escape(result)}</div>',
            unsafe_allow_html=True,
        )
        # Streamlit's native code block supplies a Copy control without custom JS.
        with copy_slot.container():
            with st.expander("Copy translation", expanded=False):
                st.code(result, language=None, wrap_lines=True)
                st.download_button(
                    "Download text", data=result, file_name="singlish-translation.txt",
                    mime="text/plain", use_container_width=True,
                )
    else:
        output_slot.markdown(
            '<div class="result-box result-empty" role="status">'
            'Your Singlish translation will appear here.</div>',
            unsafe_allow_html=True,
        )
    if st.session_state.translation_error:
         st.warning(st.session_state.translation_error)

st.write("")
st.caption("TRY A PHRASE")
examples = ("I am fine.", "Where are you going?", "Thank you.")
for column, sentence in zip(st.columns(3), examples):
    with column:
        st.button(
            sentence,
            on_click=use_example,
            args=(sentence,),
            use_container_width=True,
        )

st.markdown(
    '<p class="review-note">Singlish spellings can vary. '
    'Review translations before using them in important messages.</p>',
    unsafe_allow_html=True,
)

with st.expander("About this translator"):
    st.write(
        "This research project uses a fine-tuned mT5 model for "
        "English-to-Singlish translation. Generated translations may contain errors."
    )
    st.caption("Model hosted on Hugging Face")
    st.code(MODEL_ID, language=None)
    st.caption(
        "The current model accepts up to 64 input tokens, including its task prefix. "
        "A token is not the same as a word or character."
    )

st.markdown(
    '<div class="footer"><span>Made for everyday expression.</span>'
    '<span>English → Singlish research project</span></div>',
    unsafe_allow_html=True,
)
