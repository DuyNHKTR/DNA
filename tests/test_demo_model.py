import unittest

from demo_model import predict_sequence


class DemoModelTests(unittest.TestCase):
    def test_balanced_sequence_trends_normal_like(self) -> None:
        result = predict_sequence("ATGCAATGCTTACGATACGTAGCTAACGTA")
        self.assertEqual(result["label"], "normal-like DNA")
        self.assertGreaterEqual(result["score"], 0.5)

    def test_gc_heavy_sequence_trends_mutation_like(self) -> None:
        result = predict_sequence("CGGCGCGGCCGCGGCGTCCGCGGGCCGCGC")
        self.assertEqual(result["label"], "mutation-like DNA")
        self.assertGreaterEqual(result["score"], 0.5)

    def test_predict_sequence_requires_valid_dna(self) -> None:
        with self.assertRaisesRegex(ValueError, "A, C, G, and T"):
            predict_sequence("ABCD")


if __name__ == "__main__":
    unittest.main()
