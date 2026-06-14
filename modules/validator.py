import pandas as pd

def compare_distributions(
        real_df,
        synthetic_df
):

    report = {}

    for col in real_df.columns:

        try:

            report[col] = {
                "real_mean":
                    real_df[col].mean(),

                "synthetic_mean":
                    synthetic_df[col].mean()
            }

        except:
            pass

    return report