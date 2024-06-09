import base64


def set_rtl(st):
    st.markdown("""
    <style>
    body, html {
        direction: RTL;
        unicode-bidi: bidi-override;
        text-align: right;
    }
    # p, div, input, label, h1, h2, h3, h4, h5, h6, checkbox, stCheckbox {
    #     direction: RTL;
    #     unicode-bidi: bidi-override;
    #     # text-align: right;
    # }
    div[data-testid="InputInstructions"] > span:nth-child(1) {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)


def set_background(st, png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def set_form_color(st):
    css = """
    <style>
        [data-testid="stForm"] {
            background: LightGrey;
            stMarkdownContainer: Blue;
        }
    </style>
    """
    st.write(css, unsafe_allow_html=True)


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
