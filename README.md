# DNA Sequence Classification Demo

This workspace contains a Streamlit demo that presents the paper context first and then explains a DNA-sequence pipeline based on 3-mer features.

## Run locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start Streamlit:

```bash
streamlit run app.py
```

## Notes

- The product demo is framed as **DNA sequence classification**.
- The paper uses **cfDNA** only as the motivating application context.
- The built-in classifier is a lightweight **demo classifier**. It is not a reproduction of the paper and not a clinical tool.
