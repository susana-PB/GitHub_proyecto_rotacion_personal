import streamlit as st
import joblib
from functions import map_inputs
import base64

# ========== CONFIGURACIÓN DE IMAGEN ==========
# ELIGE UNA OPCIÓN:

# OPCIÓN B: Imagen local  
def cargar_imagen_base64(ruta):
     with open(ruta, "rb") as f:
         datos = base64.b64encode(f.read()).decode()
     return f"data:image/png;base64,{datos}"
HOJA_URL = cargar_imagen_base64("images/hoja.png")

# ========== CSS PERSONALIZADO ==========
st.markdown(f"""
<style>
    /* 1. FONDO VERDE PASTEL SUAVE */
    .stApp {{
        background-color: #E8F5E9 !important;
        background-image: linear-gradient(180deg, #F1F8E9 0%, #E8F5E9 100%) !important;
    }}
    
    /* 2. CABECERO CON IMAGEN DE HOJA */
    .cabecero {{
        text-align: center;
        padding: 20px 0 10px 0;
        margin-bottom: 30px;
        border-bottom: 1px solid #C8E6C9;
    }}
    
    .hoja-img {{
        height: 180px !important;            
        width: auto !important;
        margin-bottom: 20px !important;
        opacity: 0.9 !important;
        filter: drop-shadow(2px 2px 6px rgba(0,0,0,0.1)) !important;
    }}
    
    /* 3. TÍTULO SIN NEGRITA, CENTRADO */
    .titulo-principal {{
        color: #1B5E20 !important;
        font-weight: 400 !important;
        font-size: 2.2rem !important;
        text-align: center !important;
        font-family: 'Segoe UI', 'Arial', sans-serif !important;
        letter-spacing: 0.5px !important;
        margin-top: 10px !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.05) !important;
    }}
    
    /* 4. SECCIONES "INFORMACIÓN DEL EMPLEADO" - VERDES OSCUROS */
    h2, h3 {{
        color: #2E7D32 !important;
        font-weight: 500 !important;
        border-left: 5px solid #388E3C !important;
        padding-left: 15px !important;
        margin-top: 35px !important;
        background-color: rgba(200, 230, 201, 0.2) !important;
        padding: 12px 15px !important;
        border-radius: 0 10px 10px 0 !important;
    }}
    
    /* 5. CONTROLES DE ENTRADA */
/* 5. CONTROLES DE ENTRADA */
    /* Inputs numéricos y select - VERDES */
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {{
        background-color: #DCEEDC !important;
        border: 2px solid #A5D6A7 !important;
        border-radius: 10px !important;
        color: #1B5E20 !important;
        font-weight: 500 !important;
    }}

    /* Selectbox completo (Nivel del puesto) */
    .stSelectbox > div {{
        background-color: #DCEEDC !important;
        border-radius: 10px !important;
    }}

    /* Texto seleccionado */
    .stSelectbox div[data-baseweb="select"] span {{
        color: #1B5E20 !important;
        font-weight: 500 !important;
    }}

    /* Hover / foco (inputs y select) */
    .stNumberInput input:focus,
    .stSelectbox div[data-baseweb="select"]:focus-within {{
        border-color: #388E3C !important;
        box-shadow: 0 0 0 2px rgba(56,142,60,0.25) !important;
    }}


        /* 6. ENCUESTA - PREGUNTAS EN NEGRO */
    .encuesta-texto {{
        color: #000000 !important;
        font-weight: 500 !important;
        margin-bottom: 8px !important;
    }}
    
    /* Radio buttons */
    .stRadio > div {{
        background-color: #000000 !important;
        padding: 15px !important;
        border-radius: 10px !important;
        border: 2px solid #C8E6C9 !important;
    }}
    
    .stRadio > div > label {{
        color: #000000 !important;
    }}
    
    /* Sliders */
    .stSlider > div > div > div {{
        background-color: #388E3C !important;
    }}
    
    .stSlider > div > div > div + div {{
        color: #1B5E20 !important;
        font-weight: bold !important;
    }}
    
    /* 7. BOTONES */
    .stButton > button {{
        background-color: #1B5E20 !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 14px 40px !important;
        font-size: 17px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        display: block !important;
        margin: 30px auto !important;
        width: 60% !important;
        max-width: 400px !important;
        box-shadow: 0 4px 15px rgba(27, 94, 32, 0.2) !important;
    }}
    
    .stButton > button:hover {{
        background-color: #144017 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(27, 94, 32, 0.3) !important;
    }}
    
    /* 8. SECCIÓN DE RESULTADOS */
    .resultados-box {{
        background-color: white !important;
        border-radius: 15px !important;
        padding: 25px !important;
        margin: 20px 0 !important;
        border-left: 6px solid #388E3C !important;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05) !important;
    }}
    
    /* 9. TEXTO DENTRO DE RESULTADOS - NEGRO */
    .resultados-box p {{
        color: #000000 !important;
    }}
    
    .resultados-box li {{
        color: #000000 !important;
    }}
    
    /* 10. MEJORAS GENERALES */
    .stNumberInput input {{
        color: #2E7D32 !important;
        font-weight: 500 !important;
    }}
    
    .main .block-container {{
        padding-top: 10px !important;
    }}
    
    div[data-testid="stVerticalBlock"] {{
        background-color: transparent !important;
    }}
</style>
""", unsafe_allow_html=True)

# ========== CABECERO CON IMAGEN ==========
st.markdown(f"""
<div class="cabecero">
    <img src="{HOJA_URL}" class="hoja-img">
</div>
""", unsafe_allow_html=True)

# ========== TÍTULO PRINCIPAL ==========
st.markdown('<h1 class="titulo-principal">Simulación de Evaluación Temprana de Rotación de Empleados</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #1B5E20; font-size: 1.2rem; text-align: center; margin-top: 5px;">Responde la encuesta a los 3 meses de ingreso para simular predicción de riesgo.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #000000;">Este modelo es una simulación simplificada con las 8 principales features de la encuesta temprana (edad, antigüedad, manager, nivel de puesto y señales clave de satisfacción y burnout). No refleja exactamente el modelo completo de producción, pero permite visualizar de manera temprana el riesgo de rotación de empleados.</p>', unsafe_allow_html=True)

# ========== CARGAR MODELO ==========
model_path = "models/modelo_demo_app.pkl"
modelo = joblib.load(model_path)
UMBRAL_ALTO_RIESGO = 0.35

# ========== SECCIÓN 1: INFORMACIÓN DEL EMPLEADO ==========
st.header("Información del empleado")

# Aplicar clase a cada pregunta para que sea negra
st.markdown('<div class="encuesta-texto">Edad</div>', unsafe_allow_html=True)
age = st.number_input("", 18, 65, 30, label_visibility="collapsed")

st.markdown('<div class="encuesta-texto">Años en la empresa (0.25 = 3 meses)</div>', unsafe_allow_html=True)
years_at_company = st.number_input("", 0.0, 40.0, 0.25, step=0.25, label_visibility="collapsed", key="company")

st.markdown('<div class="encuesta-texto">Años con el mismo manager (0.25 = 3 meses)</div>', unsafe_allow_html=True)
years_with_manager = st.number_input("", 0.0, 40.0, 0.25, step=0.25, label_visibility="collapsed", key="manager")

st.markdown('<div class="encuesta-texto">Nivel de puesto</div>', unsafe_allow_html=True)
job_level = st.selectbox("", [1,2,3,4,5], label_visibility="collapsed")

# ========== SECCIÓN 2: ENCUESTA ==========
st.header("Encuesta de satisfacción a 3 meses")

st.markdown('<div class="encuesta-texto">¿Con qué frecuencia realizas horas extra en tu puesto actual?</div>', unsafe_allow_html=True)
st.markdown('<div style="color: #666; font-size: 12px; font-style: italic; margin-top: -8px; margin-bottom: 12px;">Medidor de OverTime</div>', unsafe_allow_html=True)
overtime = st.radio(
    "",
    ["Nunca o rara vez", "Varias veces por semana o diariamente"],
    label_visibility="collapsed"
)

st.markdown('<div class="encuesta-texto">¿En los últimos 30 días, ¿con qué frecuencia te has sentido agotado/a mental o emocionalmente al final de tu jornada laboral?</div>', unsafe_allow_html=True)
st.markdown('<div style="color: #666; font-size: 12px; font-style: italic; margin-top: -8px; margin-bottom: 12px;">Medidor de BurnoutRisk</div>', unsafe_allow_html=True)
st.markdown('<div class="escala-texto" style="color: #666; font-size: 14px; margin-top: -5px; margin-bottom: 15px;">1 = nunca | 5 = siempre</div>', unsafe_allow_html=True)
burnout_risk = st.slider("", 1,5,3, label_visibility="collapsed")

st.markdown('<div class="encuesta-texto">¿Cómo de satisfecho/a te sientes con tu trabajo actual?</div>', unsafe_allow_html=True)
st.markdown('<div style="color: #666; font-size: 12px; font-style: italic; margin-top: -8px; margin-bottom: 12px;">Medidor de JobSatisfaction</div>', unsafe_allow_html=True)
st.markdown('<div class="escala-texto" style="color: #666; font-size: 14px; margin-top: -5px; margin-bottom: 15px;">1 = muy insatisfecho/a | 4 = muy satisfecho/a</div>', unsafe_allow_html=True)
job_satisfaction = st.slider("", 1,4,3, label_visibility="collapsed")

# ========== SECCIÓN OPCIONAL ==========
st.subheader("Preguntas opcionales")
st.markdown('<div class="encuesta-texto">¿Consideras que tu desarrollo profesional está siendo apoyado por la empresa?</div>', unsafe_allow_html=True)
st.markdown('<div style="color: #666; font-size: 12px; font-style: italic; margin-top: -8px; margin-bottom: 12px;">Medidor de Desarrollo profesional</div>', unsafe_allow_html=True)
st.markdown('<div class="escala-texto" style="color: #666; font-size: 14px; margin-top: -5px; margin-bottom: 15px;">1 = nada | 4 = totalmente</div>', unsafe_allow_html=True)
career_support = st.slider("",1,4,3, label_visibility="collapsed", key="career")

st.markdown('<div class="encuesta-texto">¿Sientes que tu esfuerzo y logros son reconocidos adecuadamente?</div>', unsafe_allow_html=True)
st.markdown('<div style="color: #666; font-size: 12px; font-style: italic; margin-top: -8px; margin-bottom: 12px;">Medidor de Reconocimiento</div>', unsafe_allow_html=True)
st.markdown('<div class="escala-texto" style="color: #666; font-size: 14px; margin-top: -5px; margin-bottom: 15px;">1 = nunca | 4 = siempre</div>', unsafe_allow_html=True)
recognition = st.slider("",1,4,3, label_visibility="collapsed", key="recognition")

st.markdown('<div class="encuesta-texto">¿Cómo de satisfecho/a te sientes con tu equilibrio entre vida personal y laboral?</div>', unsafe_allow_html=True)
st.markdown('<div style="color: #666; font-size: 12px; font-style: italic; margin-top: -8px; margin-bottom: 12px;">Medidor de Equilibrio vida-trabajo</div>', unsafe_allow_html=True)
st.markdown('<div class="escala-texto" style="color: #666; font-size: 14px; margin-top: -5px; margin-bottom: 15px;">1 = muy insatisfecho/a | 4 = muy satisfecho/a</div>', unsafe_allow_html=True)
work_life_balance = st.slider("",1,4,3, label_visibility="collapsed", key="balance")

st.markdown('<div class="encuesta-texto">¿Te sientes cómodo/a con la cultura y el ambiente de tu equipo?</div>', unsafe_allow_html=True)
st.markdown('<div style="color: #666; font-size: 12px; font-style: italic; margin-top: -8px; margin-bottom: 12px;">Medidor de Cultura y clima</div>', unsafe_allow_html=True)
st.markdown('<div class="escala-texto" style="color: #666; font-size: 14px; margin-top: -5px; margin-bottom: 15px;">1 = nada cómodo/a | 4 = muy cómodo/a</div>', unsafe_allow_html=True)
team_culture = st.slider("",1,4,3, label_visibility="collapsed", key="team")

# ========== BOTÓN DE PREDICCIÓN ==========
if st.button("Calcular riesgo de rotación"):
    df_input = map_inputs(
        age,
        years_at_company,
        years_with_manager,
        job_level,
        overtime,
        burnout_risk,
        job_satisfaction,
        modelo=modelo  # importante para alinear columnas
    )

    proba = modelo.predict_proba(df_input)[:,1][0]
    riesgo = "Alto" if proba >= UMBRAL_ALTO_RIESGO else ("Medio" if proba >= 0.20 else "Bajo")
    import matplotlib.pyplot as plt

# Dentro del bloque del botón, después de calcular 'proba'
    st.subheader("📈 Visualización del riesgo")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    ax.barh([0], [proba], color='#D32F2F' if riesgo=="Alto" else '#FF9800' if riesgo=="Medio" else '#388E3C', height=0.5)
    ax.set_xlim(0,1)
    ax.set_yticks([])
    ax.set_xticks([0, 0.25, 0.35, 0.5, 0.75, 1])
    ax.set_xticklabels(['0%','25%','35%','50%','75%','100%'])
    ax.axvline(0.35, color='gray', linestyle='--', alpha=0.7)  # umbral alto riesgo
    ax.axvline(0.20, color='gray', linestyle='--', alpha=0.5)  # umbral medio riesgo
    ax.set_title("Probabilidad de rotación")
    st.pyplot(fig)

    # ========== RESULTADOS ==========
    st.subheader("📊 Resultados")
    st.markdown(f'<p style="color: #000000; font-size: 16px; margin: 15px 0;"><strong>Probabilidad de rotación:</strong> <code style="background: #000000; padding: 4px 8px; border-radius: 4px;">{proba:.1%}</code></p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: #000000; font-size: 16px; margin: 15px 0;"><strong>Nivel de riesgo:</strong> <code style="background: #000000; padding: 4px 8px; border-radius: 4px;">{riesgo}</code></p>', unsafe_allow_html=True)
    
    # ========== INSIGHT SOBRE BURNOUT (solo si aplica) ==========
    if burnout_risk >= 4:
        st.markdown(f'''
        <div style="
            color: #1B5E20;
            background-color: #F1F8E9;
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #4CAF50;
            margin: 15px 0;
            font-size: 15px;
        ">
        <strong>🔍 Insight sobre burnout ({burnout_risk}/5):</strong><br>
        Nuestro análisis revela que burnout muy alto (4-5/5) puede indicar
        intervenciones HR activas, lo que podría moderar el riesgo de rotación
        comparado con burnout alto (3/5).
        </div>
        ''', unsafe_allow_html=True)
    elif burnout_risk == 3:
        st.markdown(f'''
        <div style="
            color: #FF9800;
            background-color: #FFF3E0;
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #FF9800;
            margin: 15px 0;
            font-size: 15px;
        ">
        <strong>⚠️ Punto crítico - burnout {burnout_risk}/5:</strong><br>
        Nuestro análisis identifica burnout 3/5 como el nivel de máximo riesgo.
        Recomendamos intervención preventiva en esta etapa.
        </div>
        ''', unsafe_allow_html=True)
    
    st.subheader("💡 Recomendaciones")
    if riesgo=="Alto":
        st.markdown(f'''
        <div style="
            color: #000000; 
            font-size: 16px; 
            line-height: 1.6;
            background-color: #FFEBEE;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #D32F2F;
            margin: 15px 0;
        ">
        <p style="margin-top: 0; color: #D32F2F; font-weight: bold;">🚨 Acciones inmediatas recomendadas:</p>
        <ul style="margin: 10px 0; padding-left: 20px;">
            <li style="margin-bottom: 8px;"><strong>Programa anti-burnout</strong> obligatorio</li>
            <li style="margin-bottom: 8px;"><strong>Revisión carga trabajo</strong> con manager</li>
            <li style="margin-bottom: 8px;"><strong>Plan desarrollo carrera</strong> interno</li>
            <li><strong>Mentoría 1:1</strong> semanal</li>
        </ul>
        </div>
        ''', unsafe_allow_html=True)
    elif riesgo=="Medio":
        st.markdown(f'''
        <div style="
            color: #000000; 
            font-size: 16px; 
            line-height: 1.6;
            background-color: #FFF3E0;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #FF9800;
            margin: 15px 0;
        ">
        <p style="margin-top: 0; color: #FF9800; font-weight: bold;">⚠️ Acciones preventivas recomendadas:</p>
        <ul style="margin: 10px 0; padding-left: 20px;">
            <li style="margin-bottom: 8px;"><strong>Encuesta de satisfacción</strong> específica</li>
            <li style="margin-bottom: 8px;"><strong>Flexibilidad horaria</strong> opcional</li>
            <li><strong>Reconocimiento de logros</strong> mensual</li>
        </ul>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div style="
            color: #000000; 
            font-size: 16px; 
            line-height: 1.6;
            background-color: #E8F5E9;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #388E3C;
            margin: 15px 0;
        ">
        <p style="margin-top: 0; color: #388E3C; font-weight: bold;">✅ Estado óptimo - Mantenimiento:</p>
        <ul style="margin: 10px 0; padding-left: 20px;">
            <li><strong>Seguimiento normal</strong> según política HR</li>
            <li><strong>Continuar con programas</strong> de engagement existentes</li>
            <li><strong>Encuesta anual</strong> de satisfacción</li>
        </ul>
        </div>
        ''', unsafe_allow_html=True)