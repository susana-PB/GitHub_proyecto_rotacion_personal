# functions.py

import pandas as pd

def map_inputs(age, years_at_company, years_with_manager,
               job_level, overtime, burnout_risk, job_satisfaction):

    total_working_years = max(years_at_company, 0.25)  # coherente para 3 meses

    df = pd.DataFrame({
        "Age": [age],
        "TotalWorkingYears": [total_working_years],  # 🔥 CLAVE
        "YearsAtCompany": [years_at_company],
        "YearsWithCurrManager": [years_with_manager],
        "JobLevel": [job_level],
        "OverTime": [1 if overtime=="Varias veces por semana o diariamente" else 0],
        "BurnoutRisk": [burnout_risk],
        "JobSatisfaction": [job_satisfaction]
    })
    return df
