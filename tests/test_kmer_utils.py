import unittest

from kmer_utils import extract_kmers, gc_ratio, kmer_frequencies, validate_sequence


class KmerUtilsTests(unittest.TestCase):
    def test_extract_kmers_uses_sliding_window(self) -> None:
        self.assertEqual(extract_kmers("ATGC"), ["ATG", "TGC"])

    def test_extract_kmers_returns_empty_when_sequence_is_shorter_than_k(self) -> None:
        self.assertEqual(extract_kmers("AT", k=3), [])

    def test_kmer_frequencies_counts_repeated_patterns(self) -> None:
        self.assertEqual(kmer_frequencies("ATATAT", k=3), {"ATA": 2, "TAT": 2})

    def test_validate_sequence_rejects_invalid_characters(self) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid characters"):
            validate_sequence("ATNX", min_length=3)

    def test_gc_ratio_computes_expected_fraction(self) -> None:
        self.assertAlmostEqual(gc_ratio("GGAT"), 0.5)


if __name__ == "__main__":
    unittest.main()
