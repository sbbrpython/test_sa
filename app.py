from modules.data_loader import load_dataset
from modules.synthetic_generator import SyntheticAudienceGenerator
from modules.persona_builder import build_personas
from modules.validator import compare_distributions

real_df = load_dataset(
    "data/survey.csv"
)
# print(real_df.head())

generator = SyntheticAudienceGenerator()

generator.train(real_df)

synthetic_df = generator.generate(
    rows=10000
)

print(synthetic_df.head())

persona_df = build_personas(
    synthetic_df
)

report = compare_distributions(
    real_df,
    synthetic_df
)

print(report)

synthetic_df.to_csv(
    "output/synthetic_audience.csv",
    index=False
)

persona_df.to_csv(
    "output/personas.csv",
    index=False
)


