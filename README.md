# Predictive Employee Attrition: From EDA to ML Deployment

**Análisis predictivo de rotación de personal con Machine Learning**\
*Proyecto integral de Data Science & People Analytics*

## 📋 Descripción

Este proyecto aborda la rotación de personal desde un enfoque integral:
1.  **Análisis Exploratorio (EDA):** Identificación de factores psicosociales y laborales asociados al abandono.
2.  **Modelado Predictivo (ML):** Desarrollo y comparación de modelos de Machine Learning para predecir la probabilidad individual de rotación.
3.  **Despliegue y Aplicación:** Creación de una herramienta interactiva para RRHH y análisis del trade-off entre detección y carga operativa.

## 🎯 Objetivos

### Fase EDA
- Identificar patrones y factores clave asociados a la rotación.
- Crear variables proxy para constructos psicosociales (BurnoutRisk, CulturaPositiva, etc.).
- Validar hipótesis sobre bienestar y retención.

### Fase ML
- Desarrollar un modelo predictivo robusto para anticipar la rotación.
- Comparar algoritmos (Regresión Logística, Random Forest, XGBoost).
- Optimizar el modelo priorizando la detección temprana (Recall).
- Analizar el trade-off mediante ajuste del umbral de decisión.

## 🛠️ Tecnologías utilizadas

### Análisis y Modelado
- **Python 3.11+**
- `pandas`, `numpy` (manipulación de datos)
- `matplotlib`, `seaborn` (visualización)
- `scikit-learn` (preprocesamiento, modelado, evaluación)
- `xgboost` (modelado con gradient boosting)
- `joblib` (serialización de modelos)

### Despliegue y Demo
- `streamlit` (aplicación web interactiva)
- `Git & GitHub` (control de versiones)

## 📊 Dataset

- **Fuente:** IBM HR Analytics Employee Attrition & Performance (Kaggle)
- **Muestras:** 1.470 empleados
- **Características:** 35 variables (demográficas, laborales, psicosociales)
- **Target:** `Attrition` (binaria: 16% rotación, 84% permanencia)
- **Nota:** Desbalance moderado gestionado con estrategias específicas.

## 🔍 Hallazgos Clave

### Del EDA
- **Horas extra** triplican la probabilidad de rotación (30% vs 10%).
- **Burnout** duplica las tasas de abandono.
- **Cultura positiva** y **alto engagement** reducen significativamente la rotación.

### Del Modelado Predictivo
- **Modelo final:** Random Forest optimizado con umbral de decisión ajustado.
- **Rendimiento óptimo:** Recall del 68.1% con intervención sobre el 30.3% de la plantilla.
- **Trade-off identificado:** A menor umbral, mayor detección pero más falsas alarmas.
- **Variables más influyentes:** Salario mensual, experiencia total, edad y horas extra.

## 🏗️ Estructura del Proyecto

proyecto_rotacion_personal/
├── data/ # Datasets (original, procesado)
│ ├── metadata # Metadatos guardados
│ ├── processed # Dataset procesado
│ └── raw # Dataset original 
├── notebooks/ # Jupyter Notebooks del análisis
│ ├── 01_eda_preprocesamiento.ipynb
│ ├── 02_modelado_evaluacion.ipynb
│ └── 03_interpretacion_resultados.ipynb
│ └── 04_produccion.ipynb
├── models/ # Modelos experimentales y entrenados  
├── src/ # Código fuente (scripts, módulos)
├── demo/ # Aplicación Streamlit interactiva
├── docs/ # Documentación (memorias, presentaciones)
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo


## 🚀 Cómo Ejecutar el Proyecto

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/proyecto_rotacion_personal.git 
    cd employee-attrition-prediction
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Explorar el análisis:**
    - Abrir los notebooks en `notebooks/` en orden numérico.

4.  **Ejecutar la demo:**
    ```bash
    streamlit run demo/app.py
    ```

## 📈 Resultados y Aplicación

El modelo final permite:
- **Detección temprana:** Identificar empleados en riesgo con 3 meses de antelación.
- **Intervención estratificada:** Acciones diferenciadas según nivel de riesgo.
- **Optimización de recursos:** Balance entre cobertura (Recall) y carga operativa.

## 📄 Documentación Adicional

- **Memoria Técnica:** `docs/Memoria_Proyecto_ML.pdf`
- **Presentación Ejecutiva:** `docs/Presentacion_Resultados.pdf`

## 👥 Autora

**Susana Pérez Barroeta** - [Enlace a GitHub/LinkedIn]

*Última actualización: Enero 2026*