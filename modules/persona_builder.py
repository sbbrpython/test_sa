import pandas as pd

def create_persona(row):

    age = row.get("Age", 30)
    income = row.get("Income", 1000000)

    if age < 30:
        segment = "Young Professional"

    elif age < 50:
        segment = "Mid-Career Professional"

    else:
        segment = "Senior Consumer"

    if income > 1500000:
        buying_style = "Premium"

    else:
        buying_style = "Value Driven"

    return {
        "segment": segment,
        "buying_style": buying_style
    }

def build_personas(df):

    personas = []

    for _, row in df.iterrows():

        persona = create_persona(row)

        personas.append(persona)

    return pd.DataFrame(personas)