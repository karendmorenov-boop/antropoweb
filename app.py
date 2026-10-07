# app.py - AntropoCalc
# Página web interactiva para el cálculo de parámetros antropométricos
# Proyecto de Biomecánica 2026-II
# Autores: Daniela Moreno, Isabella Bohorquez, Angelica Chaparro, Luis Tinjaca

import streamlit as st
from math import sqrt
import os

# --- Configuración de la página ---
st.set_page_config(page_title="AntropoCalc", page_icon="📏", layout="wide")

# ============================================================
# ESTILOS CSS PERSONALIZADOS
# ============================================================
st.markdown("""
<style>
    .stApp { background-color: #F7F9FC; }
    .banner-principal {
        background: linear-gradient(135deg, #2E86AB 0%, #27AE60 100%);
        padding: 30px; border-radius: 15px; text-align: center;
        margin-bottom: 25px; box-shadow: 0 6px 20px rgba(46, 134, 171, 0.3);
    }
    .banner-principal h1 { color: white; margin: 0; font-size: 42px; font-weight: bold; }
    .banner-principal p { color: white; margin: 10px 0 0 0; font-size: 18px; opacity: 0.95; }
    .banner-principal .autores {
        color: white; margin-top: 18px; font-size: 14px; opacity: 0.9;
        border-top: 1px solid rgba(255,255,255,0.3); padding-top: 12px;
    }
    .caja-seccion {
        background: linear-gradient(90deg, #E8F0FE 0%, #F0F7FF 100%);
        padding: 18px 22px; border-radius: 10px; border-left: 6px solid #2E86AB;
        margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .caja-seccion h2 { color: #2E86AB; margin: 0; font-size: 26px; }
    .caja-seccion p { margin: 6px 0 0 0; color: #444; font-size: 15px; }
    .card-categoria {
        padding: 20px; border-radius: 12px; text-align: center;
        margin: 10px 0; box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }
    .card-bajo-peso { background-color: #E3F2FD; border-top: 6px solid #2196F3; }
    .card-normal { background-color: #E8F5E9; border-top: 6px solid #4CAF50; }
    .card-sobrepeso { background-color: #FFF8E1; border-top: 6px solid #FFC107; }
    .card-obesidad { background-color: #FFEBEE; border-top: 6px solid #F44336; }
    .card-categoria h3 { margin: 10px 0 5px 0; font-size: 20px; }
    .card-categoria p { margin: 5px 0; font-size: 14px; color: #555; }
    .pie-pagina {
        text-align: center; color: #666; padding: 20px;
        margin-top: 30px; border-top: 2px solid #E8F0FE;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# FUNCIÓN AUXILIAR: IMAGEN O EMOJI DE RESPALDO
# ============================================================
def mostrar_imagen_o_emoji(ruta_imagen, emoji_respaldo, caption=""):
    if os.path.exists(ruta_imagen):
        st.image(ruta_imagen, caption=caption, use_container_width=True)
    else:
        st.markdown(
            f'<div style="text-align:center; font-size: 80px; padding: 10px;">{emoji_respaldo}</div>',
            unsafe_allow_html=True
        )
        if caption:
            st.caption(caption)

# ============================================================
# BANNER PRINCIPAL
# ============================================================
st.markdown("""
<div class="banner-principal">
    <h1>📏 AntropoCalc</h1>
    <p>Página web interactiva para el cálculo e interpretación de parámetros antropométricos</p>
    <div class="autores">
        <b>Autores:</b> Daniela Moreno · Isabella Bohorquez · Angelica Chaparro · Luis Tinjaca
    </div>
</div>
""", unsafe_allow_html=True)

# --- Ancla invisible al inicio (para el botón "Ir arriba") ---
st.markdown('<div id="top"></div>', unsafe_allow_html=True)

# --- Pestañas (ORDEN NUEVO) ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Guía Teórica", "📘 Guía de Uso", "🧮 Calculadora", "📊 Interpretación"
])

# ============================================================
# PESTAÑA 1: GUÍA TEÓRICA
# ============================================================
with tab1:
    st.markdown("""
    <div class="caja-seccion">
        <h2>📖 ¿Qué es la Antropometría?</h2>
        <p>La ciencia que estudia las medidas y dimensiones del cuerpo humano</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    La **antropometría** es la ciencia que estudia las medidas y dimensiones del cuerpo humano. 
    Proviene de las palabras griegas *anthropos* (hombre) y *metron* (medida). Es una herramienta 
    fundamental en biomecánica, nutrición, medicina del deporte y ergonomía, ya que permite evaluar 
    el estado nutricional, el riesgo cardiovascular y la composición corporal de una persona.

    En este proyecto se utilizan **medidas simples** que no requieren equipos especializados como 
    plicómetros o calibradores: solo necesitas una **báscula** para el peso y una **cinta métrica** 
    para las circunferencias.
    """)

    st.markdown("---")
    st.markdown("""
    <div class="caja-seccion" style="border-left-color: #27AE60; background: linear-gradient(90deg, #E8F8F0 0%, #F0FFF7 100%);">
        <h2 style="color: #27AE60;">📐 Guía de cada parámetro antropométrico</h2>
        <p>Qué es, para qué sirve, cómo se calcula y un ejemplo de cada uno</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🔵 1. Índice de Masa Corporal (IMC)"):
        st.markdown("**¿Qué es?**")
        st.write("""
        El Índice de Masa Corporal (IMC) es un indicador que relaciona el peso de una persona con su 
        talla. Fue desarrollado por el estadístico Adolphe Quetelet y es utilizado por la Organización 
        Mundial de la Salud (OMS) como el estándar principal para clasificar el estado nutricional de adultos.
        """)
        st.markdown("**¿Para qué sirve?**")
        st.write("""
        Permite identificar si una persona tiene bajo peso, peso normal, sobrepeso u obesidad. 
        Es una herramienta de tamizaje rápido que ayuda a detectar riesgos asociados al peso.
        """)
        st.markdown("**¿Cómo se calcula?**")
        st.latex(r"IMC = \frac{Peso\ (kg)}{Talla^2\ (m)}")
        st.markdown("**Datos necesarios:** Peso (kg) y talla (m).")
        st.info("**Ejemplo:** Si pesas 70 kg y mides 1.70 m → IMC = 70 / (1.70²) = 24.2 kg/m² (Peso normal).")

    with st.expander("🟢 2. Índice Cintura-Cadera (ICC)"):
        st.markdown("**¿Qué es?**")
        st.write("""
        El Índice Cintura-Cadera (ICC) compara la circunferencia de la cintura con la de la cadera. 
        Refleja la **distribución de la grasa corporal**: si predomina en el abdomen (forma de manzana) 
        o en las caderas (forma de pera).
        """)
        st.markdown("**¿Para qué sirve?**")
        st.write("""
        La grasa acumulada en el abdomen (grasa visceral) es más peligrosa que la de caderas y muslos, 
        porque se asocia con mayor riesgo de enfermedades cardiovasculares y metabólicas.
        """)
        st.markdown("**¿Cómo se calcula?**")
        st.latex(r"ICC = \frac{Cintura\ (cm)}{Cadera\ (cm)}")
        st.markdown("**Datos necesarios:** Circunferencia de cintura y cadera (cm).")
        st.info("**Ejemplo:** Cintura 80 cm, cadera 95 cm → ICC = 80 / 95 = 0.84.")

    with st.expander("🟠 3. Índice Cintura-Talla (ICT)"):
        st.markdown("**¿Qué es?**")
        st.write("""
        El Índice Cintura-Talla (ICT) relaciona la circunferencia de la cintura con la estatura. 
        Es un indicador reciente que ha ganado popularidad porque detecta el riesgo cardiometabólico 
        mejor que el IMC en muchos casos.
        """)
        st.markdown("**¿Para qué sirve?**")
        st.write("""
        Un valor de ICT ≥ 0.5 indica que la grasa abdominal es excesiva para la estatura de la persona, 
        lo cual se asocia con mayor riesgo de hipertensión, diabetes tipo 2 y enfermedades cardíacas.
        """)
        st.markdown("**¿Cómo se calcula?**")
        st.latex(r"ICT = \frac{Cintura\ (cm)}{Talla\ (cm)}")
        st.markdown("**Datos necesarios:** Circunferencia de cintura y talla (cm).")
        st.info("**Ejemplo:** Cintura 80 cm, talla 170 cm → ICT = 80 / 170 = 0.47 (Riesgo bajo).")

    with st.expander("🟣 4. Superficie Corporal (Mosteller)"):
        st.markdown("**¿Qué es?**")
        st.write("""
        La Superficie Corporal (SC) es el área total de la piel del cuerpo humano, expresada en metros 
        cuadrados (m²). Se estima mediante fórmulas a partir del peso y la talla.
        """)
        st.markdown("**¿Para qué sirve?**")
        st.write("""
        Se utiliza en medicina para dosificar medicamentos, calcular requerimientos energéticos, 
        estimar pérdidas de calor y líquidos, y realizar estudios de fisiología.
        """)
        st.markdown("**¿Cómo se calcula? (Fórmula de Mosteller)**")
        st.latex(r"SC = \sqrt{\frac{Talla\ (cm) \times Peso\ (kg)}{3600}}")
        st.markdown("**Datos necesarios:** Peso (kg) y talla (cm).")
        st.info("**Ejemplo:** Peso 70 kg, talla 170 cm → SC = √[(170 × 70) / 3600] = 1.82 m².")

    with st.expander("🔴 5. Peso Ideal (Fórmula de Lorentz)"):
        st.markdown("**¿Qué es?**")
        st.write("""
        El Peso Ideal (PI) es una estimación teórica del peso que una persona debería tener según su 
        talla y sexo. En este proyecto se usa la **Fórmula de Lorentz**.
        """)
        st.markdown("**¿Para qué sirve?**")
        st.write("""
        Sirve como referencia orientativa para establecer metas de peso en programas de nutrición, 
        rehabilitación o entrenamiento.
        """)
        st.markdown("**¿Cómo se calcula?**")
        st.latex(r"Hombre: PI = Talla - 100 - \frac{Talla - 150}{4}")
        st.latex(r"Mujer: PI = Talla - 100 - \frac{Talla - 150}{2}")
        st.markdown("**Datos necesarios:** Talla (cm) y sexo.")
        st.info("**Ejemplo (hombre):** Talla 170 cm → PI = 170 - 100 - (20/4) = 65 kg.")

    with st.expander("🔷 6. Circunferencia de Pantorrilla"):
        st.markdown("**¿Qué es?**")
        st.write("""
        La Circunferencia de Pantorrilla (CP) es el perímetro máximo de la pantorrilla. Es un indicador 
        sencillo del estado nutricional y de la masa muscular, especialmente útil en adultos mayores.
        """)
        st.markdown("**¿Para qué sirve?**")
        st.write("""
        Se utiliza para detectar desnutrición y pérdida de masa muscular (sarcopenia) en adultos mayores. 
        Un valor bajo (< 31 cm) se asocia con mayor riesgo de desnutrición y fragilidad.
        """)
        st.markdown("**¿Cómo se mide?**")
        st.write("""
        La persona debe estar de pie, con los pies ligeramente separados y el peso distribuido. 
        Se pasa la cinta métrica alrededor de la parte más prominente de la pantorrilla, sin comprimir 
        el músculo.
        """)
        st.markdown("**Datos necesarios:** Circunferencia de pantorrilla (cm).")
        st.info("**Ejemplo:** Pantorrilla 34 cm → Valor normal.")

# ============================================================
# PESTAÑA 2: GUÍA DE USO
# ============================================================
with tab2:
    st.markdown("""
    <div class="caja-seccion" style="border-left-color: #E67E22; background: linear-gradient(90deg, #FEF5E7 0%, #FFF9F0 100%);">
        <h2 style="color: #E67E22;">📘 Guía de Uso de la Plataforma</h2>
        <p>Aprende a usar AntropoCalc paso a paso</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧭 Paso 1: Navega entre las pestañas")
    st.write("""
    En la parte superior de la página encontrarás **4 pestañas**:
    - **📖 Guía Teórica:** Explica qué es la antropometría y cada parámetro.
    - **📘 Guía de Uso:** Esta sección que estás leyendo.
    - **🧮 Calculadora:** Aquí ingresas tus datos y obtienes los resultados.
    - **📊 Interpretación:** Tablas para entender qué significa cada resultado.
    """)

    st.markdown("### 📝 Paso 2: Ingresa tus datos")
    st.write("""
    1. Ve a la pestaña **🧮 Calculadora**.
    2. Completa los campos:
       - ⚖️ **Peso** en kilogramos (kg)
       - 📏 **Talla** en centímetros (cm)
       - 📐 **Cintura** en centímetros (cm)
       - 📐 **Cadera** en centímetros (cm)
       - 🦵 **Pantorrilla** en centímetros (cm)
       - ⚧ **Sexo** (Hombre/Mujer)
    3. Presiona el botón **🔍 Calcular parámetros**.
    """)

    st.markdown("### 📊 Paso 3: Interpreta tus resultados")
    st.write("""
    Después de calcular, verás los resultados con **íconos y colores**:
    - 🟢 **Verde:** Resultado saludable, sin riesgo.
    - 🟡 **Amarillo:** Resultado en zona de precaución, se recomienda vigilar.
    - 🔴 **Rojo:** Resultado de riesgo, se recomienda consultar a un profesional de la salud.

    También verás **imágenes representativas** de cada categoría de IMC para que sea más fácil de entender.
    """)

    st.markdown("### 💡 Paso 4: Recomendaciones")
    st.info("""
    **Importante:** AntropoCalc es una herramienta educativa. Los resultados son orientativos y 
    no reemplazan la evaluación de un profesional de la salud (médico, nutricionista o fisioterapeuta).
    """)

# ============================================================
# PESTAÑA 3: CALCULADORA
# ============================================================
with tab3:
    st.markdown("""
    <div class="caja-seccion">
        <h2>🧮 Calculadora de Parámetros</h2>
        <p>Apóyate de una báscula, una cinta métrica y/o un tallímetro para obtener estos parámetros según corresponda.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("formulario_antropometrico"):
        col1, col2 = st.columns(2)
        with col1:
            peso = st.number_input("⚖️ Peso (kg)", min_value=1.0, value=70.0, step=0.1)
            talla_cm = st.number_input("📏 Talla (cm)", min_value=50.0, value=170.0, step=0.1)
            cintura = st.number_input("📐 Circunferencia de cintura (cm)", min_value=10.0, value=80.0, step=0.1)
        with col2:
            cadera = st.number_input("📐 Circunferencia de cadera (cm)", min_value=10.0, value=95.0, step=0.1)
            pantorrilla = st.number_input("🦵 Circunferencia de pantorrilla (cm)", min_value=10.0, value=35.0, step=0.1)
            sexo = st.selectbox("⚧ Sexo", ["Hombre", "Mujer"])
        submitted = st.form_submit_button("🔍 Calcular parámetros")

    if submitted:
        st.markdown("---")
        st.markdown("""
        <div class="caja-seccion" style="border-left-color: #27AE60; background: linear-gradient(90deg, #E8F8F0 0%, #F0FFF7 100%);">
            <h2 style="color: #27AE60;">📊 Resultados</h2>
        </div>
        """, unsafe_allow_html=True)

        talla_m = talla_cm / 100

        # ---- IMC ----
        imc = peso / (talla_m ** 2)
        st.subheader("1. Índice de Masa Corporal (IMC)")
        if imc < 18.5:
            categoria, emoji, titulo, descripcion = "bajo_peso", "🧍‍♂️", "Bajo peso", "Tu peso está por debajo de lo recomendado."
        elif imc < 25:
            categoria, emoji, titulo, descripcion = "normal", "🧍", "Peso normal", "¡Felicidades! Tu peso es saludable."
        elif imc < 30:
            categoria, emoji, titulo, descripcion = "sobrepeso", "🧍‍♀️", "Sobrepeso", "Tu peso está ligeramente elevado."
        else:
            categoria, emoji, titulo, descripcion = "obesidad", "🧍‍♂️", "Obesidad", "Tu peso está muy elevado, consulta a un profesional."

        col_a, col_b = st.columns([1, 2])
        with col_a:
            st.metric("IMC", f"{imc:.2f} kg/m²")
            mostrar_imagen_o_emoji(f"img/{categoria}.png", emoji)
        with col_b:
            if categoria == "bajo_peso":
                st.warning(f"🔵 **{titulo}** — {descripcion}")
            elif categoria == "normal":
                st.success(f"🟢 **{titulo}** — {descripcion}")
            elif categoria == "sobrepeso":
                st.warning(f"🟡 **{titulo}** — {descripcion}")
            else:
                st.error(f"🔴 **{titulo}** — {descripcion}")

        # ---- ICC ----
        icc = cintura / cadera
        st.subheader("2. Índice Cintura-Cadera (ICC)")
        col_a, col_b = st.columns([1, 2])
        with col_a:
            st.metric("ICC", f"{icc:.2f}")
        with col_b:
            if sexo == "Hombre":
                if icc <= 0.90:
                    st.success("🟢 Riesgo cardiovascular: Saludable")
                else:
                    st.error("🔴 Riesgo cardiovascular: Alto")
            else:
                if icc <= 0.80:
                    st.success("🟢 Riesgo cardiovascular: Saludable")
                else:
                    st.error("🔴 Riesgo cardiovascular: Alto")

        # ---- ICT ----
        ict = cintura / talla_cm
        st.subheader("3. Índice Cintura-Talla (ICT)")
        col_a, col_b = st.columns([1, 2])
        with col_a:
            st.metric("ICT", f"{ict:.2f}")
        with col_b:
            if ict < 0.5:
                st.success("🟢 Riesgo cardiometabólico: Bajo")
            else:
                st.warning("🟡 Riesgo cardiometabólico: Elevado (≥ 0.5)")

        # ---- Superficie corporal ----
        superficie = sqrt((talla_cm * peso) / 3600)
        st.subheader("4. Superficie Corporal (Mosteller)")
        col_a, col_b = st.columns([1, 2])
        with col_a:
            st.metric("SC", f"{superficie:.2f} m²")
        with col_b:
            st.info("ℹ️ Valor de referencia clínica")

        # ---- Peso ideal ----
        st.subheader("5. Peso Ideal (Fórmula de Lorentz)")
        if sexo == "Hombre":
            peso_ideal = talla_cm - 100 - ((talla_cm - 150) / 4)
        else:
            peso_ideal = talla_cm - 100 - ((talla_cm - 150) / 2)
        col_a, col_b = st.columns([1, 2])
        with col_a:
            st.metric("PI", f"{peso_ideal:.2f} kg")
        with col_b:
            st.info("ℹ️ Estimación teórica basada en talla y sexo")

        # ---- Pantorrilla ----
        st.subheader("6. Circunferencia de Pantorrilla")
        col_a, col_b = st.columns([1, 2])
        with col_a:
            st.metric("Pantorrilla", f"{pantorrilla:.1f} cm")
        with col_b:
            if pantorrilla < 31:
                st.warning("🟡 Valor bajo: posible desnutrición o pérdida de masa muscular")
            elif pantorrilla > 40:
                st.info("ℹ️ Valor elevado: puede indicar retención de líquidos o mayor masa muscular")
            else:
                st.success("🟢 Valor normal")

# ============================================================
# PESTAÑA 4: INTERPRETACIÓN
# ============================================================
with tab4:
    st.markdown("""
    <div class="caja-seccion">
        <h2>📊 Tablas de Interpretación</h2>
        <p>Estas tablas te apoyarán para que logres realizar la interpretación de tus resultados; compáralos entre sí.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("1. Clasificación del IMC (OMS)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        mostrar_imagen_o_emoji("img/bajo_peso.png", "🧍‍♂️")
        st.markdown("""
        <div class="card-categoria card-bajo-peso">
            <h3 style="color: #1976D2;">Bajo peso</h3>
            <p><b>IMC:</b> &lt; 18.5</p>
            <p>Riesgo de desnutrición</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        mostrar_imagen_o_emoji("img/normal.png", "🧍")
        st.markdown("""
        <div class="card-categoria card-normal">
            <h3 style="color: #388E3C;">Peso normal</h3>
            <p><b>IMC:</b> 18.5 - 24.9</p>
            <p>Peso saludable</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        mostrar_imagen_o_emoji("img/sobrepeso.png", "🧍‍♀️")
        st.markdown("""
        <div class="card-categoria card-sobrepeso">
            <h3 style="color: #F57C00;">Sobrepeso</h3>
            <p><b>IMC:</b> 25.0 - 29.9</p>
            <p>Peso elevado</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        mostrar_imagen_o_emoji("img/obesidad.png", "🧍‍♂️")
        st.markdown("""
        <div class="card-categoria card-obesidad">
            <h3 style="color: #D32F2F;">Obesidad</h3>
            <p><b>IMC:</b> ≥ 30.0</p>
            <p>Alto riesgo para la salud</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("2. Interpretación del ICC")
    st.table({
        "Sexo": ["Hombre", "Hombre", "Mujer", "Mujer"],
        "ICC": ["≤ 0.90", "> 0.90", "≤ 0.80", "> 0.80"],
        "Riesgo cardiovascular": ["🟢 Saludable", "🔴 Alto", "🟢 Saludable", "🔴 Alto"]
    })

    st.subheader("3. Interpretación del ICT")
    st.table({
        "ICT": ["< 0.5", "≥ 0.5"],
        "Riesgo cardiometabólico": ["🟢 Bajo", "🟡 Elevado"]
    })

    st.subheader("4. Interpretación de la Circunferencia de Pantorrilla")
    st.table({
        "Pantorrilla (cm)": ["< 31", "31 - 40", "> 40"],
        "Interpretación": ["🟡 Riesgo de desnutrición", "🟢 Normal", "ℹ️ Elevado"]
    })

    st.markdown("---")
    st.caption("📚 Referencias: OMS (2024); Montoya Castillo et al. (2025); Li et al. (2024); Kiss et al. (2024); ICBF (2023).")
  
# ============================================================
# PIE DE PÁGINA
# ============================================================
st.markdown("""
<div class="pie-pagina">
    <p><b>AntropoCalc</b> · Proyecto de Biomecánica 2026-II</p>
    <p style="font-size: 13px;">Autores: Daniela Moreno · Isabella Bohorquez · Angelica Chaparro · Luis Tinjaca</p>
    <p style="font-size: 12px; color: #999;">Desarrollado con Python + Streamlit</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# BOTÓN FLOTANTE "IR ARRIBA"
# ============================================================
st.markdown("""
<a href="#top" style="
    position: fixed;
    bottom: 30px;
    right: 30px;
    background-color: #2E86AB;
    color: white;
    padding: 12px 18px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    z-index: 1000;
    font-size: 14px;
">
    ⬆ Ir arriba
</a>
""", unsafe_allow_html=True)