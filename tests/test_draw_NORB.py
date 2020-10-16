import os
import unittest

from meta_analysis.draw_NORB import draw_norb


class TestVisualization(unittest.TestCase):
    def test_draw_norb(self):
        norb_data_path = "tests/test_NORB.json"
        graph_name = "test"
        save_file_path = "norb_plot_test.pdf"
        try:
            os.remove(save_file_path)
        except FileNotFoundError:
            pass
        draw_norb(norb_data_path, graph_name)
        self.assertTrue(os.path.exists(save_file_path))


if __name__ == "__main__":
    unittest.main()
