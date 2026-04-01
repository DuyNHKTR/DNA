from math import exp

from kmer_utils import gc_ratio, relative_kmer_frequencies, validate_sequence


MUTATION_WEIGHTS = {
    "CCC": 1.3,
    "CCG": 1.5,
    "CGA": 1.1,
    "CGC": 2.2,
    "CGG": 1.8,
    "GCC": 1.4,
    "GCG": 2.0,
    "GGC": 1.6,
    "GGG": 1.3,
    "TCG": 1.2,
}

NORMAL_WEIGHTS = {
    "AAT": 1.3,
    "ATA": 1.6,
    "ATG": 0.8,
    "ATT": 1.3,
    "CAT": 0.6,
    "TAA": 1.1,
    "TAT": 1.5,
    "TTA": 1.2,
}


def _sigmoid(value: float) -> float:
    return 1.0 / (1.0 + exp(-value))


def predict_sequence(sequence: str) -> dict[str, object]:
    cleaned = validate_sequence(sequence, min_length=3)
    relative_frequencies = relative_kmer_frequencies(cleaned, k=3)
    gc_content = gc_ratio(cleaned)
    dominance = max(relative_frequencies.values(), default=0.0)

    raw_score = 0.0
    top_features: list[dict[str, object]] = []

    for kmer, frequency in relative_frequencies.items():
        weight = MUTATION_WEIGHTS.get(kmer, 0.0) - NORMAL_WEIGHTS.get(kmer, 0.0)
        if weight == 0.0:
            continue
        impact = frequency * weight
        raw_score += impact
        top_features.append(
            {
                "feature": kmer,
                "value": round(frequency, 3),
                "impact": round(impact, 3),
                "effect": "mutation-like DNA" if impact > 0 else "normal-like DNA",
                "reason": "3-mer pattern weighted by the demo classifier.",
            }
        )

    gc_impact = (gc_content - 0.5) * 1.2
    raw_score += gc_impact
    top_features.append(
        {
            "feature": "GC ratio",
            "value": round(gc_content, 3),
            "impact": round(gc_impact, 3),
            "effect": "mutation-like DNA" if gc_impact > 0 else "normal-like DNA",
            "reason": "Higher GC content pushes the demo slightly toward mutation-like DNA.",
        }
    )

    dominance_impact = max(0.0, dominance - 0.16) * 1.4
    raw_score += dominance_impact
    if dominance_impact > 0:
        top_features.append(
            {
                "feature": "Dominant 3-mer",
                "value": round(dominance, 3),
                "impact": round(dominance_impact, 3),
                "effect": "mutation-like DNA",
                "reason": "A strongly repeated motif increases the mutation-like score in this demo.",
            }
        )

    mutation_probability = _sigmoid(raw_score * 3.2)
    label = "mutation-like DNA" if mutation_probability >= 0.5 else "normal-like DNA"
    confidence = mutation_probability if label == "mutation-like DNA" else 1 - mutation_probability

    top_features = sorted(top_features, key=lambda item: abs(float(item["impact"])), reverse=True)[:5]

    return {
        "label": label,
        "score": round(confidence, 3),
        "mutation_probability": round(mutation_probability, 3),
        "top_features": top_features,
        "note": (
            "This demo classifier is illustrative. It explains the DNA -> 3-mer -> prediction pipeline, "
            "but it does not reproduce the paper's training setup and it is not a clinical tool."
        ),
    }
