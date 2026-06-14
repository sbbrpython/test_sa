# Defer importing SyntheticAudienceGenerator until the function runs so
# the module can be imported even if optional dependencies (like sdv)
# are not installed in the environment.
def run_generation(file):

    import pandas as pd
    import io

    try:
        from modules.synthetic_generator import SyntheticAudienceGenerator
    except Exception as e:
        raise ImportError(
            "Failed to import SyntheticAudienceGenerator. Make sure the 'sdv' package and other dependencies are installed. Original error: " + str(e)
        )

    # Robust CSV reader: try common encodings, then fall back to decoding with replace.
    def _safe_read_csv(path):
        encodings = ["utf-8", "utf-8-sig", "cp1252", "latin1"]
        for enc in encodings:
            try:
                return pd.read_csv(path, encoding=enc)
            except UnicodeDecodeError:
                continue
            except Exception:
                # other errors (e.g., parser errors) should propagate
                raise

        # Final fallback: read bytes and decode with replacement to avoid decode errors
        with open(path, "rb") as f:
            raw = f.read()

        # Try to decode with a best-effort encoding, else replace invalid bytes
        for enc in ["utf-8", "cp1252", "latin1"]:
            try:
                text = raw.decode(enc)
                return pd.read_csv(io.StringIO(text))
            except Exception:
                continue

        # As a last resort, decode with replacements so we never fail on bad bytes
        text = raw.decode("utf-8", errors="replace")
        return pd.read_csv(io.StringIO(text))

    df = _safe_read_csv(file.name)
    generator = SyntheticAudienceGenerator()

    generator.train(df)

    synthetic = generator.generate(5000)

    output_file = "synthetic.csv"

    synthetic.to_csv(
        output_file,
        index=False
    )

    return output_file

if __name__ == '__main__':
    import gradio as gr

    ui = gr.Interface(
        fn=run_generation,
        inputs=gr.File(),
        outputs=gr.File()
    )

    ui.launch(share=True)