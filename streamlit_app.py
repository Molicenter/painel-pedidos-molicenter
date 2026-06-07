import streamlit as st
import base64
import os

# Configuração da página
st.set_page_config(page_title="Gestão Pedidos - Molicenter", page_icon="🛒", layout="wide")

# Função para converter imagem local para Base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

logo_base64 = get_base64_image("passaro_logo.png")

# Estilização CSS
st.markdown("""
    <style>
    .stApp { background-color: #121212 !important; }
    .banner-container { background: #0B3C5D; padding: 15px; border-radius: 8px; margin-bottom: 25px; display: flex; align-items: center; color: white; }
    .card-pedido { background-color: #1e1e1e; border-radius: 10px; padding: 15px; border: 1px solid #2d2d2d; margin-bottom: 20px; }
    .card-group-title { font-size: 18px; font-weight: bold; color: #0093E9; margin-bottom: 15px; text-align: center; }
    .item-grupo { background: rgba(255,255,255,0.05); padding: 10px; border-radius: 5px; margin-bottom: 10px; }
    .btn-titulo { color: #ffffff !important; font-weight: bold; text-decoration: none; display: block; margin-bottom: 5px; }
    .texto-horario { font-size: 11px; color: #aaaaaa; }
    </style>
""", unsafe_allow_html=True)

# Banner
st.markdown(f"""<div class="banner-container"><img src="data:image/png;base64,{logo_base64}" style="height:40px; margin-right:15px;"> <h2>Gestão Pedidos - Molicenter</h2></div>""", unsafe_allow_html=True)

# Links
LINKS = {
    "folhagem": "https://docs.google.com/spreadsheets/d/1y1mCjctvQTwqvxhk67uYnSX4vs_SROAAa7-kZAz07jg/edit?gid=0#gid=0",
    "flv_normal": "https://docs.google.com/spreadsheets/d/1MROR0Tl__10OI--8-VqZdT5e1il64XSdwW3-xR23Cu8/edit?usp=drive_link",
    "flv_ofertas": "https://docs.google.com/spreadsheets/d/1Ic_iNC34IQTUwZhN0qdf6bsTM-EjwshVnNlwjdnI8mI/edit?usp=drive_link",
    "flv_oriental": "https://pedido-oriental.streamlit.app/",
    "acougue_adriano": "https://docs.google.com/spreadsheets/d/19e0N0FWVdrKtWMG-UroqwPpVKQOqgJ524bBAOuEcyBY/edit?gid=0#gid=0",
    "pecas_manoel": "https://docs.google.com/spreadsheets/d/19e0N0FWVdrKtWMG-UroqwPpVKQOqgJ524bBAOuEcyBY/edit?gid=0#gid=0",
    "pioneiro": "https://docs.google.com/spreadsheets/d/1bBB75w4lshM9Xg70VCuJAzLASpYrp35zYDp8y2vB3Fc/edit?usp=drive_link",
    "padaria": "https://docs.google.com/spreadsheets/d/14nfvS6jRIJFdTgPpYDxUZNThLSBM4zASFXl_XnOLJOI/edit?gid=0#gid=0",
    "embalagens": "https://docs.google.com/spreadsheets/d/1x2QjCgvjpBl5-QZAqZCNay7aoUvgohjJoAQFdGn4cfE/edit?gid=0#gid=0",
    "materia_prima": "https://docs.google.com/spreadsheets/d/1WDZBbT1J-aSjGNXFfy9HbhKAmAhU5zquqRHYJUXpR0o/edit?gid=0#gid=0"
}

# Layout 3 colunas
c1, c2, c3 = st.columns(3)

with c1: # HORTIFRUTI
    st.markdown("""<div class="card-pedido"><div class="card-group-title">HORTIFRUTI</div>""", unsafe_allow_html=True)
    st.markdown(f'<div class="item-grupo"><a href="{LINKS["folhagem"]}" target="_blank" class="btn-titulo">Folhagem</a><div class="texto-horario">Seg a Sáb até 12:00hrs</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="item-grupo"><a href="{LINKS["flv_normal"]}" target="_blank" class="btn-titulo">FLV Normal</a><div class="texto-horario">Terças até 17:00h | Quintas até 14:00h</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="item-grupo"><a href="{LINKS["flv_ofertas"]}" target="_blank" class="btn-titulo">FLV Ofertas</a><div class="texto-horario">Quintas-feira até 14:00hrs</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="item-grupo"><a href="{LINKS["flv_oriental"]}" target="_blank" class="btn-titulo">FLV Oriental</a><div class="texto-horario">Acesso via Sistema Web</div></div></div>', unsafe_allow_html=True)

with c2: # AÇOUGUE
    st.markdown("""<div class="card-pedido"><div class="card-group-title">AÇOUGUE</div>""", unsafe_allow_html=True)
    st.markdown(f'<div class="item-grupo"><a href="{LINKS["acougue_adriano"]}" target="_blank" class="btn-titulo">Açougue Adriano</a><div class="texto-horario">Quartas e Sáb até 15:00h</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="item-grupo"><a href="{LINKS["pecas_manoel"]}" target="_blank" class="btn-titulo">Peças Manoel</a><div class="texto-horario">Seg/Qua/Sex (Arapongas) | Ter/Qui/Sáb (Maringá)</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="item-grupo"><a href="{LINKS["pioneiro"]}" target="_blank" class="btn-titulo">Pioneiro + BF + Paraná</a><div class="texto-horario">Seg a Sex até 11:00hrs</div></div></div>', unsafe_allow_html=True)

with c3: # OUTROS
    st.markdown(f'<div class="card-pedido"><a href="{LINKS["padaria"]}" target="_blank" class="btn-titulo">Padaria e Confeitaria</a><div class="texto-horario">Sábado</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card-pedido"><a href="{LINKS["embalagens"]}" target="_blank" class="btn-titulo">Embalagens</a><div class="texto-horario">Sexta-feira até 17:30hrs</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card-pedido"><a href="{LINKS["materia_prima"]}" target="_blank" class="btn-titulo">Matéria Prima</a><div class="texto-horario">Até Sábado</div></div>', unsafe_allow_html=True)
