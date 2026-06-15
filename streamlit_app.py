import streamlit as st
import base64
import os

# ─────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Gestão Pedidos - Molicenter",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# UTILITÁRIOS
# ─────────────────────────────────────────────
def get_base64_image(image_path: str, fallback_path: str = "") -> str:
    """Converte imagem local para Base64. Tenta fallback se o principal não existir."""
    for path in [image_path, fallback_path]:
        if path and os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    return ""

def img_tag(base64_str: str, mime: str, url_fallback: str, alt: str, css_class: str) -> str:
    """Retorna tag <img> usando base64 local ou URL remota como fallback."""
    if base64_str:
        return f'<img src="data:{mime};base64,{base64_str}" class="{css_class}" alt="{alt}">'
    if url_fallback:
        return f'<img src="{url_fallback}" class="{css_class}" alt="{alt}">'
    return f'<div class="{css_class} img-placeholder">📦</div>'

# ─────────────────────────────────────────────
# IMAGENS LOCAIS E LINKS EXTERNOS (FALLBACK)
# ─────────────────────────────────────────────
logo_b64           = get_base64_image("passaro_logo.png")
embalagens_b64     = get_base64_image("Embalagens.jpg")
materiaprima_b64   = get_base64_image("materiaprima.jpg")
pioneiros_b64      = get_base64_image("Pioneiros.jpg")

IMG_FOLHAGEM = "https://images.unsplash.com/photo-1574316071802-0d684efa7bf5?w=400"
IMG_FLV      = "https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=400"
IMG_ORIENTAL = "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=400"
IMG_ACOUGUE  = "https://images.unsplash.com/photo-1544025162-d76694265947?w=400"
IMG_PADARIA  = "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400"

# ─────────────────────────────────────────────
# DADOS DOS CARDS - ESTRUTURADOS EM 3 COLUNAS
# ─────────────────────────────────────────────
COL1_CARDS = [
    {
        "title": "Folhagem",
        "link": "https://pedidos-folhagem.streamlit.app/",
        "schedule": ["Seg a Sáb até 12:00hrs"],
        "img_b64": "", "img_mime": "image/jpeg", "img_url": IMG_FOLHAGEM
    },
    {
        "title": "FLV Normal",
        "link": "https://pedidos-flv.streamlit.app/",
        "schedule": ["Terças-feira até 17:00hrs", "Quintas-feira até 14:00hrs"],
        "img_b64": "", "img_mime": "image/jpeg", "img_url": IMG_FLV
    },
    {
        "title": "FLV Ofertas",
        "link": "https://pedidos-flv-ofertas.streamlit.app/",
        "schedule": ["Quintas-feira até 14:00hrs"],
        "img_b64": "", "img_mime": "image/jpeg", "img_url": IMG_FLV  
    },
    {
        "title": "FLV Oriental",
        "link": "https://pedido-oriental.streamlit.app/",
        "schedule": ["Quintas-feira até 14:00hrs"],
        "img_b64": "", "img_mime": "image/jpeg", "img_url": IMG_ORIENTAL
    }
]

COL2_CARDS = [
    {
        "title": "Pioneiro + BF + Paraná",
        "link": "https://acougue-especiais.streamlit.app/",
        "schedule": ["Seg a Sex até 11:00hrs"],
        "img_b64": pioneiros_b64, "img_mime": "image/jpeg", 
        "img_url": "https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=400"
    },
    {
        "title": "Açougue Adriano",
        "link": "https://acougue-total.streamlit.app/",
        "schedule": ["Quartas-feira até 15:00hrs", "Sábado até 15:00hrs"],
        "img_b64": "", "img_mime": "image/jpeg", "img_url": IMG_ACOUGUE
    },
    {
        "title": "Peças Açougue",
        "link": "https://acougue-pecas.streamlit.app/",
        "schedule": [
            "Seg / Qua / Sex — Arapongas até 15:00h",
            "Ter / Qui / Sáb — Maringá até 15:00h"
        ],
        "img_b64": "", "img_mime": "image/jpeg", "img_url": IMG_ACOUGUE  
    }
]

COL3_CARDS = [
    {
        "title": "Embalagens",
        "link": "https://pedidos-embalagem.streamlit.app/",
        "schedule": ["Sexta-feira até as 17:30hrs"],
        "img_b64": embalagens_b64, "img_mime": "image/jpeg", 
        "img_url": "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=400"
    },
    {
        "title": "Padaria e Confeitaria",
        "link": "https://pedidos-padariaconfeitaria.streamlit.app/",
        "schedule": ["Sábado"],
        "img_b64": "", "img_mime": "image/jpeg", "img_url": IMG_PADARIA
    },
    {
        "title": "Matéria Prima",
        "link": "https://pedidos-materiaprima.streamlit.app/",
        "schedule": ["Até Sábado"],
        "img_b64": materiaprima_b64, "img_mime": "image/jpeg", 
        "img_url": "https://images.unsplash.com/photo-1556909114-44e3e70034e2?w=400"
    }
]

# ─────────────────────────────────────────────
# CSS - DESIGN MODERNO E EXPANDIDO
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ── Base do Tema ── */
.stApp, .main {
    background-color: #0a0a0a !important;
    color: #ffffff !important;
}

/* ── Simulando o efeito de Zoom 90% ao usar melhor o espaço ── */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 1rem !important;
    max-width: 92% !important; /* Estica o painel para ocupar 92% da tela */
}

/* ── Banner Moderno ── */
.banner-container {
    background: linear-gradient(135deg, #07263b 0%, #0e4a74 100%);
    padding: 12px 24px;
    border-radius: 10px;
    margin-bottom: 25px;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: 0 4px 15px rgba(0, 147, 233, 0.15);
    border: 1px solid rgba(255,255,255,0.1);
}
.banner-logo {
    height: 44px;
    width: auto;
    object-fit: contain;
}
.banner-title {
    font-family: 'Segoe UI', Tahoma, sans-serif;
    font-size: 24px; /* Aumentado */
    font-weight: 800;
    color: #fff;
    letter-spacing: 0.5px;
}

/* ── Estilo do Card ── */
.card-pedido {
    background: rgba(30, 30, 30, 0.6);
    backdrop-filter: blur(8px);
    border-radius: 12px;
    padding: 14px; /* Aumentado */
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    margin-bottom: 16px; 
    border: 1px solid rgba(255,255,255,0.08);
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: all 0.25s ease;
}
.card-pedido:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 147, 233, 0.25);
    border-color: rgba(0, 147, 233, 0.5);
    background: rgba(40, 40, 40, 0.8);
}

/* ── Imagem mais proporcional ── */
.card-img {
    width: 100%;
    height: 120px; /* Mais alta, parecendo que o zoom está maior */
    object-fit: cover;
    border-radius: 8px;
    opacity: 0.9;
    transition: opacity 0.3s;
}
.card-pedido:hover .card-img {
    opacity: 1.0;
}

/* ── Botão principal ── */
.btn-titulo {
    background-color: #ffffff;
    color: #0B3C5D !important;
    font-weight: 800;
    font-size: 16px; /* Fonte Maior */
    padding: 10px 12px;
    border-radius: 6px;
    text-decoration: none;
    display: block;
    width: 100%;
    box-sizing: border-box;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    transition: all 0.2s ease;
}
.btn-titulo:hover {
    background-color: #e0f2ff;
    color: #07263b !important;
    transform: scale(1.02);
}

/* ── Texto de Horários ── */
.texto-horario {
    font-size: 13px; /* Aumentado para acompanhar o resto */
    color: #b0b0b0;
    line-height: 1.4;
    font-weight: 500;
}

/* ── Ocultar Menu Streamlit ── */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FUNÇÕES DE RENDERIZAÇÃO
# ─────────────────────────────────────────────
def render_schedule(schedule: list[str]) -> str:
    return "<br>".join(schedule) if schedule else ""

def render_card(card: dict) -> str:
    img_html = img_tag(
        card.get("img_b64", ""),
        card.get("img_mime", "image/jpeg"),
        card.get("img_url", ""),
        card["title"],
        "card-img"
    )
    sched_html = (
        f'<div class="texto-horario">{render_schedule(card["schedule"])}</div>'
        if card.get("schedule") else ""
    )

    return f"""
    <div class="card-pedido">
        {img_html}
        <a href="{card['link']}" target="_blank" class="btn-titulo">{card['title']}</a>
        {sched_html}
    </div>
    """

# ─────────────────────────────────────────────
# BANNER
# ─────────────────────────────────────────────
if logo_b64:
    logo_src = f'<img src="data:image/png;base64,{logo_b64}" class="banner-logo" alt="Logo Molicenter">'
else:
    logo_src = '<span style="font-size:28px">🛒</span>'

st.markdown(f"""
<div class="banner-container">
    {logo_src}
    <div class="banner-title">Gestão Pedidos - Molicenter</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LAYOUT EM 3 COLUNAS
# ─────────────────────────────────────────────
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    for card in COL1_CARDS:
        st.markdown(render_card(card), unsafe_allow_html=True)

with col2:
    for card in COL2_CARDS:
        st.markdown(render_card(card), unsafe_allow_html=True)

with col3:
    for card in COL3_CARDS:
        st.markdown(render_card(card), unsafe_allow_html=True)

# ─────────────────────────────────────────────
# RODAPÉ
# ─────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:20px; color:#666666; font-size:12px; font-weight: 500;">
    Molicenter Supermercados © 2026 — Painel Web de Pedidos Centralizados
</div>
""", unsafe_allow_html=True)
