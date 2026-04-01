import pandas as pd
import streamlit as st

from demo_model import predict_sequence
from kmer_utils import extract_kmers, kmer_frequencies, validate_sequence
from paper_content import MODEL_RESULTS, PAPER_METADATA, SAMPLE_SEQUENCES, get_copy


def apply_styles() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg: #f7f1e6;
                --ink: #1e1b18;
                --muted: #6d635b;
                --line: rgba(30, 27, 24, 0.11);
                --accent: #0f766e;
                --accent-soft: rgba(15, 118, 110, 0.11);
                --warn: #9a5a08;
                --warn-soft: rgba(154, 90, 8, 0.10);
                --paper-shadow: 0 22px 50px rgba(22, 17, 12, 0.08);
            }
            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(15, 118, 110, 0.08), transparent 30%),
                    radial-gradient(circle at bottom right, rgba(154, 90, 8, 0.06), transparent 26%),
                    linear-gradient(180deg, #fbf6ed 0%, #f3ebde 50%, #f9f6f0 100%);
                color: var(--ink);
            }
            .block-container {
                max-width: 100%;
                padding-top: 0.75rem;
                padding-left: 2.5rem;
                padding-right: 2.5rem;
                padding-bottom: 4rem;
            }
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #14202d 0%, #0b1320 100%);
            }
            [data-testid="stSidebar"] * {
                color: #f8fafc;
            }
            [data-testid="stSidebar"] a {
                color: #c5f7ee !important;
            }
            [data-testid="stButton"] button,
            [data-testid="baseButton-secondary"] {
                border-radius: 999px;
                border: 1px solid rgba(15, 118, 110, 0.28);
                background: rgba(255, 255, 255, 0.5);
                color: var(--ink);
                font-weight: 600;
            }
            [data-testid="stButton"] button[kind="primary"] {
                background: linear-gradient(135deg, #0f766e 0%, #0c4a6e 100%);
                color: #f8fafc;
                border: none;
            }
            div[data-testid="stMetric"] {
                background: rgba(255, 252, 247, 0.72);
                border: 1px solid var(--line);
                border-radius: 20px;
                padding: 0.9rem 1rem;
            }
            .hero-shell {
                margin: 0 -2.5rem 2.5rem;
                padding: 1.2rem 2.5rem 2.8rem;
                position: relative;
                overflow: hidden;
                border-bottom: 1px solid var(--line);
            }
            .hero-grid {
                display: grid;
                grid-template-columns: minmax(0, 1.1fr) minmax(300px, 0.9fr);
                gap: 2.4rem;
                align-items: end;
            }
            .hero-copy {
                max-width: 42rem;
                animation: rise 700ms ease-out both;
            }
            .hero-kicker {
                text-transform: uppercase;
                letter-spacing: 0.14em;
                font-size: 0.76rem;
                color: var(--accent);
                font-weight: 700;
                margin-bottom: 0.8rem;
            }
            .hero-title {
                font-family: Georgia, "Times New Roman", serif;
                font-size: clamp(3rem, 7vw, 5.6rem);
                line-height: 0.92;
                margin: 0 0 0.8rem 0;
                max-width: 10ch;
            }
            .hero-subtitle {
                font-size: clamp(1.05rem, 2vw, 1.4rem);
                line-height: 1.35;
                margin-bottom: 1rem;
                max-width: 38rem;
            }
            .hero-body {
                color: var(--muted);
                font-size: 1.02rem;
                line-height: 1.65;
                max-width: 40rem;
                margin-bottom: 1.25rem;
            }
            .hero-cta {
                display: inline-flex;
                align-items: center;
                gap: 0.55rem;
                text-decoration: none;
                padding: 0.8rem 1.15rem;
                border-radius: 999px;
                background: var(--ink);
                color: #f8fafc !important;
                font-weight: 700;
                margin-right: 0.8rem;
            }
            .hero-micro {
                display: inline-block;
                color: var(--muted);
                font-size: 0.92rem;
                margin-top: 1rem;
            }
            .hero-meta {
                margin-top: 1.3rem;
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 0.8rem;
                max-width: 34rem;
            }
            .hero-meta .meta-item {
                border-top: 1px solid var(--line);
                padding-top: 0.7rem;
            }
            .hero-meta .label {
                display: block;
                color: var(--muted);
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                margin-bottom: 0.3rem;
            }
            .hero-meta .value {
                font-size: 0.95rem;
                line-height: 1.4;
            }
            .hero-visual {
                position: relative;
                min-height: 420px;
                animation: drift 9s ease-in-out infinite;
            }
            .hero-visual::before {
                content: "";
                position: absolute;
                inset: 14% 12% 10% 8%;
                background:
                    radial-gradient(circle at center, rgba(15, 118, 110, 0.18), transparent 44%),
                    radial-gradient(circle at 30% 28%, rgba(154, 90, 8, 0.12), transparent 34%);
                filter: blur(8px);
            }
            .hero-svg {
                position: absolute;
                inset: 0;
                width: 100%;
                height: 100%;
                opacity: 0.96;
            }
            .poster-note {
                position: absolute;
                right: 0;
                bottom: 0;
                max-width: 18rem;
                padding: 0.85rem 0.95rem;
                border-radius: 18px 18px 0 18px;
                background: rgba(255, 252, 247, 0.82);
                border: 1px solid var(--line);
                backdrop-filter: blur(8px);
                box-shadow: var(--paper-shadow);
                color: var(--muted);
                font-size: 0.9rem;
                line-height: 1.5;
            }
            .section-anchor {
                position: relative;
                top: -72px;
                visibility: hidden;
            }
            .section-shell {
                padding: 1.25rem 0 2rem;
                border-top: 1px solid var(--line);
            }
            .section-eyebrow {
                text-transform: uppercase;
                letter-spacing: 0.14em;
                color: var(--accent);
                font-size: 0.75rem;
                font-weight: 700;
                margin-bottom: 0.6rem;
                animation: fadeup 520ms ease-out both;
            }
            .section-title {
                font-family: Georgia, "Times New Roman", serif;
                font-size: clamp(1.8rem, 3vw, 2.8rem);
                line-height: 1.04;
                margin: 0 0 0.55rem 0;
            }
            .section-lead {
                max-width: 46rem;
                color: var(--muted);
                line-height: 1.65;
                margin-bottom: 1.2rem;
            }
            .flow-grid {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 1rem;
                margin-top: 1.2rem;
            }
            .flow-step {
                padding: 1.1rem 0.95rem 1rem;
                border-top: 2px solid rgba(15, 118, 110, 0.2);
                background: rgba(255, 252, 247, 0.45);
                min-height: 190px;
            }
            .flow-number {
                font-family: Georgia, "Times New Roman", serif;
                color: var(--accent);
                font-size: 1.8rem;
                line-height: 1;
                margin-bottom: 0.6rem;
            }
            .flow-title {
                font-weight: 700;
                margin-bottom: 0.45rem;
            }
            .takeaway-band {
                border-left: 4px solid var(--accent);
                padding-left: 1rem;
                margin-bottom: 1rem;
                font-size: 1.05rem;
                line-height: 1.6;
            }
            .callout-note {
                background: var(--warn-soft);
                border-left: 4px solid var(--warn);
                padding: 0.9rem 1rem;
                border-radius: 14px;
                margin-bottom: 0.85rem;
                animation: pulseaccent 3.4s ease-in-out infinite;
            }
            .workspace-kicker {
                color: var(--muted);
                text-transform: uppercase;
                letter-spacing: 0.12em;
                font-size: 0.74rem;
                margin-bottom: 0.5rem;
                font-weight: 700;
            }
            .pipeline-row {
                display: flex;
                flex-wrap: wrap;
                gap: 0.6rem;
                margin-bottom: 0.8rem;
            }
            .pipeline-chip {
                display: inline-flex;
                align-items: center;
                padding: 0.45rem 0.78rem;
                border-radius: 999px;
                background: var(--accent-soft);
                color: var(--accent);
                font-size: 0.86rem;
                font-weight: 600;
            }
            .annotation {
                color: var(--muted);
                line-height: 1.6;
            }
            @keyframes rise {
                from { opacity: 0; transform: translateY(18px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes fadeup {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes drift {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-8px); }
            }
            @keyframes pulseaccent {
                0%, 100% { box-shadow: 0 0 0 rgba(15, 118, 110, 0); }
                50% { box-shadow: 0 8px 28px rgba(15, 118, 110, 0.08); }
            }
            @media (max-width: 980px) {
                .block-container {
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
                .hero-shell {
                    margin-left: -1rem;
                    margin-right: -1rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
                .hero-grid {
                    grid-template-columns: 1fr;
                }
                .hero-title {
                    max-width: none;
                }
                .hero-visual {
                    min-height: 290px;
                }
                .flow-grid {
                    grid-template-columns: 1fr 1fr;
                }
            }
            @media (max-width: 640px) {
                .flow-grid {
                    grid-template-columns: 1fr;
                }
                .hero-meta {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> str:
    use_vietnamese = st.sidebar.toggle("Tiếng Việt", key="use_vietnamese")
    locale = "vi" if use_vietnamese else "en"
    copy = get_copy(locale)

    st.sidebar.title(copy["sidebar"]["brand"])
    st.sidebar.caption(copy["sidebar"]["caption"])
    st.sidebar.markdown(f"**{copy['sidebar']['nav_title']}**")
    nav_lines = [f"- [{label}](#{anchor})" for label, anchor in copy["sidebar"]["nav_items"]]
    st.sidebar.markdown("\n".join(nav_lines))
    st.sidebar.info(copy["sidebar"]["note"])
    return locale


def _render_anchor(anchor_id: str) -> None:
    st.markdown(f'<div id="{anchor_id}" class="section-anchor"></div>', unsafe_allow_html=True)


def _render_section_header(eyebrow: str, title: str, lead: str) -> None:
    st.markdown(
        f"""
        <div class="section-eyebrow">{eyebrow}</div>
        <h2 class="section-title">{title}</h2>
        <div class="section-lead">{lead}</div>
        """,
        unsafe_allow_html=True,
    )


def _hero_svg() -> str:
    return """
    <svg class="hero-svg" viewBox="0 0 540 420" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="dnaLineA" x1="120" y1="40" x2="370" y2="360" gradientUnits="userSpaceOnUse">
          <stop stop-color="#0f766e"/>
          <stop offset="1" stop-color="#134e4a"/>
        </linearGradient>
        <linearGradient id="dnaLineB" x1="380" y1="40" x2="150" y2="360" gradientUnits="userSpaceOnUse">
          <stop stop-color="#b45309"/>
          <stop offset="1" stop-color="#0c4a6e"/>
        </linearGradient>
      </defs>
      <rect x="34" y="24" width="472" height="360" rx="34" fill="rgba(255,252,247,0.48)" stroke="rgba(30,27,24,0.08)"/>
      <path d="M165 52C245 102 245 154 165 206C85 258 85 308 165 362" stroke="url(#dnaLineA)" stroke-width="8" stroke-linecap="round"/>
      <path d="M375 52C295 102 295 154 375 206C455 258 455 308 375 362" stroke="url(#dnaLineB)" stroke-width="8" stroke-linecap="round"/>
      <g stroke="rgba(30,27,24,0.18)" stroke-width="3.4" stroke-linecap="round">
        <path d="M165 72H375"/>
        <path d="M192 118H348"/>
        <path d="M204 162H336"/>
        <path d="M192 206H348"/>
        <path d="M171 250H369"/>
        <path d="M190 296H350"/>
        <path d="M210 340H330"/>
      </g>
      <g fill="#0f766e">
        <circle cx="165" cy="72" r="7"/>
        <circle cx="192" cy="118" r="6.5"/>
        <circle cx="204" cy="162" r="6.5"/>
        <circle cx="192" cy="206" r="6.5"/>
        <circle cx="171" cy="250" r="6.5"/>
        <circle cx="190" cy="296" r="6.5"/>
        <circle cx="210" cy="340" r="6.5"/>
      </g>
      <g fill="#b45309">
        <circle cx="375" cy="72" r="7"/>
        <circle cx="348" cy="118" r="6.5"/>
        <circle cx="336" cy="162" r="6.5"/>
        <circle cx="348" cy="206" r="6.5"/>
        <circle cx="369" cy="250" r="6.5"/>
        <circle cx="350" cy="296" r="6.5"/>
        <circle cx="330" cy="340" r="6.5"/>
      </g>
    </svg>
    """


def _localized_results_df(locale: str) -> pd.DataFrame:
    copy = get_copy(locale)
    return pd.DataFrame(MODEL_RESULTS).rename(columns=copy["table_labels"])


def _localized_prediction(locale: str, prediction: dict[str, object]) -> dict[str, object]:
    copy = get_copy(locale)
    label_map = copy["prediction_labels"]
    localized = dict(prediction)
    localized["label"] = label_map[prediction["label"]]
    localized["note"] = copy["demo"]["note"]

    translated_features = []
    for item in prediction["top_features"]:
        translated_item = dict(item)
        translated_item["effect"] = (
            label_map["effect_mutation"] if item["effect"] == "mutation-like DNA" else label_map["effect_normal"]
        )
        if locale == "vi":
            translated_item["reason"] = {
                "3-mer pattern weighted by the demo classifier.": "Mẫu 3-mer này được demo classifier gán trọng số.",
                "Higher GC content pushes the demo slightly toward mutation-like DNA.": "GC ratio cao hơn đẩy kết quả demo nhẹ về phía mutation.",
                "A strongly repeated motif increases the mutation-like score in this demo.": "Một motif lặp mạnh làm tăng điểm mutation trong demo này.",
            }.get(item["reason"], item["reason"])
        translated_features.append(translated_item)
    localized["top_features"] = translated_features
    return localized


def render_intro_section(locale: str) -> None:
    copy = get_copy(locale)
    hero = copy["hero"]
    intro = copy["intro"]

    _render_anchor("dna-sequence-classification")
    st.markdown(
        f"""
        <section class="hero-shell">
            <div class="hero-grid">
                <div class="hero-copy">
                    <div class="hero-kicker">{hero["eyebrow"]}</div>
                    <h1 class="hero-title">{hero["title"]}</h1>
                    <div class="hero-subtitle">{hero["subtitle"]}</div>
                    <div class="hero-body">{hero["body"]}</div>
                    <a class="hero-cta" href="#demo-dna-sequence">{hero["cta"]}</a>
                    <div class="hero-micro">{hero["micro"]}</div>
                    <div class="hero-meta">
                        <div class="meta-item">
                            <span class="label">{hero["meta_title"]}</span>
                            <span class="value">{PAPER_METADATA["journal"]}</span>
                        </div>
                        <div class="meta-item">
                            <span class="label">DOI</span>
                            <span class="value">{PAPER_METADATA["doi"]}</span>
                        </div>
                    </div>
                </div>
                <div class="hero-visual">
                    {_hero_svg()}
                    <div class="poster-note">{copy["sidebar"]["note"]}</div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<section class="section-shell">', unsafe_allow_html=True)
    _render_section_header("Overview", intro["section"], intro["lead"])
    left_column, right_column = st.columns([1.05, 0.95], gap="large")
    with left_column:
        for bullet in intro["bullets"]:
            st.markdown(f"- {bullet}")
    with right_column:
        st.markdown(
            f"""
            <div class="takeaway-band">
                <strong>{PAPER_METADATA["title"]}</strong><br>
                {PAPER_METADATA["author"]}<br>
                {PAPER_METADATA["issue"]}
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</section>", unsafe_allow_html=True)


def render_paper_context_section(locale: str) -> None:
    copy = get_copy(locale)
    section = copy["paper_context"]

    _render_anchor("paper-context-and-cfdna")
    st.markdown('<section class="section-shell">', unsafe_allow_html=True)
    _render_section_header("Paper context", section["section"], section["callout"])
    left_column, right_column = st.columns(2, gap="large")
    with left_column:
        st.markdown(f"#### {section['left_title']}")
        st.write(section["left_body"])
    with right_column:
        st.markdown(f"#### {section['right_title']}")
        st.write(section["right_body"])
    st.markdown("</section>", unsafe_allow_html=True)


def render_method_section(locale: str) -> None:
    copy = get_copy(locale)
    method = copy["method"]

    _render_anchor("method-and-3-mer-features")
    st.markdown('<section class="section-shell">', unsafe_allow_html=True)
    _render_section_header("Method", method["section"], method["lead"])
    method_columns = st.columns(len(method["steps"]), gap="medium")
    for column, step in zip(method_columns, method["steps"]):
        with column:
            st.markdown(
                (
                    f'<div class="flow-step">'
                    f'<div class="flow-number">{step["number"]}</div>'
                    f'<div class="flow-title">{step["title"]}</div>'
                    f'<div class="annotation">{step["body"]}</div>'
                    f"</div>"
                ),
                unsafe_allow_html=True,
            )
    st.markdown("</section>", unsafe_allow_html=True)


def render_results_section(locale: str) -> None:
    copy = get_copy(locale)
    section = copy["results"]
    results_df = _localized_results_df(locale)
    accuracy_column = copy["table_labels"]["Accuracy"]
    model_column = copy["table_labels"]["Model"]

    _render_anchor("results-and-limitations")
    st.markdown('<section class="section-shell">', unsafe_allow_html=True)
    _render_section_header("Reported results", section["section"], section["takeaway"])

    left_column, right_column = st.columns([1.1, 0.9], gap="large")
    with left_column:
        st.markdown(f"**{section['chart_title']}**")
        st.bar_chart(results_df[[model_column, accuracy_column]].set_index(model_column), height=310)
        st.markdown(f"**{section['table_title']}**")
        st.dataframe(results_df, use_container_width=True, hide_index=True)
    with right_column:
        st.markdown(f"**{section['limitations_title']}**")
        for item in section["limitations"]:
            st.markdown(f"- {item}")
        st.markdown(f"**{section['inconsistencies_title']}**")
        for inconsistency in section["inconsistencies"]:
            st.markdown(
                f'<div class="callout-note"><strong>{inconsistency["title"]}</strong><br>{inconsistency["body"]}</div>',
                unsafe_allow_html=True,
            )
    st.markdown("</section>", unsafe_allow_html=True)


def _set_demo_sequence(sequence: str) -> None:
    st.session_state["dna_input"] = sequence


def _localized_counts_df(locale: str, kmers: list[str], counts: dict[str, int]) -> pd.DataFrame:
    copy = get_copy(locale)
    raw_df = pd.DataFrame(
        [
            {
                "3-mer": kmer,
                "Count": count,
                "Relative frequency": round(count / len(kmers), 3),
            }
            for kmer, count in counts.items()
        ]
    )
    raw_df = raw_df.sort_values(["Count", "3-mer"], ascending=[False, True]).reset_index(drop=True)
    return raw_df.rename(columns=copy["table_labels"])


def render_demo_section(locale: str) -> None:
    copy = get_copy(locale)
    demo = copy["demo"]

    _render_anchor("demo-dna-sequence")
    st.markdown('<section class="section-shell">', unsafe_allow_html=True)
    _render_section_header("Interactive demo", demo["section"], demo["lead"])

    left_column, right_column = st.columns([1.05, 0.95], gap="large")
    with left_column:
        st.markdown(f'<div class="workspace-kicker">{demo["workspace_title"]}</div>', unsafe_allow_html=True)
        button_columns = st.columns(2)
        button_columns[0].button(
            demo["sample_labels"]["balanced"],
            key="sample_balanced",
            use_container_width=True,
            on_click=_set_demo_sequence,
            args=(SAMPLE_SEQUENCES["balanced"],),
        )
        button_columns[1].button(
            demo["sample_labels"]["mutation"],
            key="sample_mutation",
            use_container_width=True,
            on_click=_set_demo_sequence,
            args=(SAMPLE_SEQUENCES["mutation"],),
        )

        if "dna_input" not in st.session_state:
            st.session_state["dna_input"] = SAMPLE_SEQUENCES["balanced"]

        st.text_area(
            demo["input_label"],
            key="dna_input",
            height=140,
            help=demo["input_help"],
        )
        run_demo = st.button(demo["run_cta"], type="primary", key="run_demo")
        st.caption(demo["helper"])
    with right_column:
        st.markdown(f'<div class="workspace-kicker">{demo["preview_title"]}</div>', unsafe_allow_html=True)
        pipeline_html = "".join(f'<span class="pipeline-chip">{item}</span>' for item in demo["pipeline"])
        st.markdown(f'<div class="pipeline-row">{pipeline_html}</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="takeaway-band">
                <strong>{demo["output_title"]}</strong><br>
                {demo["note"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

    if not run_demo:
        st.info(demo["idle_note"])
        st.markdown("</section>", unsafe_allow_html=True)
        return

    try:
        cleaned = validate_sequence(st.session_state["dna_input"], min_length=3)
    except ValueError as error:
        st.error(str(error))
        st.markdown("</section>", unsafe_allow_html=True)
        return

    kmers = extract_kmers(cleaned, k=3)
    counts = kmer_frequencies(cleaned, k=3)
    counts_df = _localized_counts_df(locale, kmers, counts)
    prediction = _localized_prediction(locale, predict_sequence(cleaned))
    table_labels = copy["table_labels"]

    metrics = demo["metrics"]
    stats = st.columns(4)
    stats[0].metric(metrics["length"], len(cleaned))
    stats[1].metric(metrics["kmers"], len(kmers))
    stats[2].metric(metrics["unique"], len(counts_df))
    stats[3].metric(metrics["label"], prediction["label"])

    left_column, right_column = st.columns([1.05, 0.95], gap="large")
    with left_column:
        st.markdown(f"**{demo['cleaned_title']}**")
        st.code(cleaned, language="text")
        st.markdown(f"**{demo['kmers_title']}**")
        st.code(" | ".join(kmers[:18]) + (" | ..." if len(kmers) > 18 else ""), language="text")
        st.markdown(f"**{demo['table_title']}**")
        st.dataframe(counts_df, use_container_width=True, hide_index=True)
    with right_column:
        st.markdown(f"**{demo['chart_title']}**")
        st.bar_chart(counts_df.head(10).set_index(table_labels["3-mer"])[table_labels["Count"]], height=280)
        st.markdown(f"**{demo['output_title']}**")
        st.metric(demo["confidence_label"], f"{prediction['score']:.0%}")
        st.progress(
            float(prediction["mutation_probability"]),
            text=f"{demo['mutation_probability']}: {prediction['mutation_probability']:.0%}",
        )
        st.caption(prediction["note"])

    feature_df = pd.DataFrame(prediction["top_features"]).rename(columns=table_labels)
    st.markdown(f"**{demo['feature_title']}**")
    st.dataframe(feature_df, use_container_width=True, hide_index=True)
    st.markdown("</section>", unsafe_allow_html=True)


def render_footer_section(locale: str) -> None:
    copy = get_copy(locale)
    footer = copy["footer"]

    _render_anchor("conclusion-and-scale-up")
    st.markdown('<section class="section-shell">', unsafe_allow_html=True)
    _render_section_header("Scale-up", footer["section"], footer["takeaway_body"])
    left_column, right_column = st.columns([1.05, 0.95], gap="large")
    with left_column:
        st.markdown(f"#### {footer['takeaway_title']}")
        st.write(footer["takeaway_body"])
    with right_column:
        st.markdown(f"#### {footer['scale_title']}")
        for idea in footer["ideas"]:
            st.markdown(f"- {idea}")
    st.markdown("</section>", unsafe_allow_html=True)
