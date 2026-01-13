import pandas as pd

def map_inputs(age, years_at_company, years_with_manager,
               job_level, overtime, burnout_risk, job_satisfaction,
               modelo=None):
    """
    Convierte los inputs de la demo en un DataFrame listo para predecir,
    alineado con las columnas que espera el modelo de demo.
    """
    
    total_working_years = max(years_at_company, 0.25)

    # DataFrame base con las 8 columnas principales
    df = pd.DataFrame({
        "Age": [age],
        "TotalWorkingYears": [total_working_years],
        "YearsAtCompany": [years_at_company],
        "YearsWithCurrManager": [years_with_manager],
        "JobLevel": [job_level],
        "OverTime": [1 if overtime=="Varias veces por semana o diariamente" else 0],
        "BurnoutRisk": [burnout_risk],
        "JobSatisfaction": [job_satisfaction]
    })

    # Si se pasa un modelo, rellenar columnas faltantes con 0 y reordenar
    if modelo is not None:
        cols_modelo = modelo.feature_names_in_
        for col in cols_modelo:
            if col not in df.columns:
                df[col] = 0
        df = df[cols_modelo]

    return df
