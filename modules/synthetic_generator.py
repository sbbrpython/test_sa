from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer


class SyntheticAudienceGenerator:

    def __init__(self):
        self.model = None

    def train(self, df):

        metadata = SingleTableMetadata()
        metadata.detect_from_dataframe(df)

        self.model = CTGANSynthesizer(
            metadata=metadata
        )

        self.model.fit(df)

    def generate(self, rows):

        synthetic_df = self.model.sample(
            num_rows=rows
        )

        return synthetic_df