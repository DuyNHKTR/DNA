from collections import Counter
from itertools import product
import re


VALID_BASES = frozenset({"A", "C", "G", "T"})
WHITESPACE_RE = re.compile(r"\s+")


def normalize_sequence(sequence: str) -> str:
    if sequence is None:
        raise ValueError("DNA sequence is required.")
    cleaned = WHITESPACE_RE.sub("", sequence.upper())
    if not cleaned:
        raise ValueError("DNA sequence is empty.")
    return cleaned


def validate_sequence(sequence: str, min_length: int = 1) -> str:
    cleaned = normalize_sequence(sequence)
    invalid = sorted(set(cleaned) - VALID_BASES)
    if invalid:
        raise ValueError(
            "DNA sequence may only contain A, C, G, and T. Invalid characters: "
            + ", ".join(invalid)
        )
    if len(cleaned) < min_length:
        raise ValueError(f"DNA sequence must be at least {min_length} bases long.")
    return cleaned


def extract_kmers(sequence: str, k: int = 3) -> list[str]:
    if k <= 0:
        raise ValueError("k must be a positive integer.")
    cleaned = validate_sequence(sequence)
    if len(cleaned) < k:
        return []
    return [cleaned[index : index + k] for index in range(len(cleaned) - k + 1)]


def kmer_frequencies(sequence: str, k: int = 3) -> dict[str, int]:
    kmers = extract_kmers(sequence, k=k)
    if not kmers:
        return {}
    counts = Counter(kmers)
    return dict(sorted(counts.items()))


def relative_kmer_frequencies(sequence: str, k: int = 3) -> dict[str, float]:
    counts = kmer_frequencies(sequence, k=k)
    total = sum(counts.values())
    if total == 0:
        return {}
    return {kmer: count / total for kmer, count in counts.items()}


def gc_ratio(sequence: str) -> float:
    cleaned = validate_sequence(sequence)
    gc_count = sum(1 for base in cleaned if base in {"G", "C"})
    return gc_count / len(cleaned)


def all_possible_kmers(k: int = 3) -> list[str]:
    if k <= 0:
        raise ValueError("k must be a positive integer.")
    return ["".join(items) for items in product(sorted(VALID_BASES), repeat=k)]
