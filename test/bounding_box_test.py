import unittest

from digital_ink_library.boundingbox import BoundingBox


class BoundingBoxTestCase(unittest.TestCase):

    def test_constructor_simple(self):
        bounding_box = BoundingBox(0, 0, 1, 1)
        self.assertEqual(bounding_box.x_min, 0)
        self.assertEqual(bounding_box.y_min, 0)
        self.assertEqual(bounding_box.x_max, 1)
        self.assertEqual(bounding_box.y_max, 1)
        self.assertEqual(bounding_box.width, 1)
        self.assertEqual(bounding_box.height, 1)

    def test_equals(self):
        bb1 = BoundingBox(0, 0, 1, 1)
        bb2 = BoundingBox(0, 0, 1, 1)
        self.assertTrue(bb1 == bb2)
        self.assertEqual(bb1, bb2)

    def test_constructor_switched_bounds(self):
        with self.assertRaises(ValueError): BoundingBox(2, 1, 1, 0)
        with self.assertRaises(ValueError): BoundingBox(0, 1, 0, -1)
        with self.assertRaises(ValueError): BoundingBox(0, 2, 1, 1)
        with self.assertRaises(ValueError): BoundingBox(-1, 1, 0, 0)
        with self.assertRaises(ValueError): BoundingBox(1, 0, 0, 1)

    def test_merge(self):
        bb1 = BoundingBox(0, 0, 1, 1)
        bb1a = BoundingBox(0.5, 0.5, 1.5, 1.5)
        bb2 = BoundingBox(-2, -2, -1, -1)

        bb1_bb1a = bb1.merge(bb1a)

        self.assertEqual(bb1_bb1a, bb1a.merge(bb1))
        self.assertEqual(bb1_bb1a.x_min, 0)
        self.assertEqual(bb1_bb1a.x_max, 1.5)
        self.assertEqual(bb1_bb1a.y_min, 0)
        self.assertEqual(bb1_bb1a.y_max, 1.5)
        self.assertEqual(bb1_bb1a.width, 1.5)
        self.assertEqual(bb1_bb1a.height, 1.5)

        bb2_bb1 = bb1.merge(bb2)

        self.assertEqual(bb2_bb1, bb2.merge(bb1))
        self.assertEqual(bb2_bb1.x_min, -2)
        self.assertEqual(bb2_bb1.x_max, 1)
        self.assertEqual(bb2_bb1.y_min, -2)
        self.assertEqual(bb2_bb1.y_max, 1)
        self.assertEqual(bb2_bb1.width, 3)
        self.assertEqual(bb2_bb1.height, 3)

    def test_intersects(self):
        bb1 = BoundingBox(0, 0, 1, 1)
        bb1a = BoundingBox(0.5, 0.5, 1.5, 1.5)
        bb2 = BoundingBox(-2, -2, -1, -1)

        bb1_intersects_bb2 = bb1.intersects(bb2)
        bb2_intersects_bb1 = bb2.intersects(bb1)

        self.assertEqual(bb2_intersects_bb1, bb1_intersects_bb2)
        self.assertFalse(bb2_intersects_bb1)

        bb3 = BoundingBox(0.25, 0.25, 0.75, 0.75)
        bb1_intersects_bb3 = bb1.intersects(bb3)
        bb3_intersects_bb1 = bb3.intersects(bb1)

        self.assertEqual(bb1_intersects_bb3, bb3_intersects_bb1)
        self.assertTrue(bb1_intersects_bb3)
        self.assertFalse(bb2.intersects(bb3))
        self.assertTrue(bb1.intersects(bb1a))
        self.assertTrue(bb1a.intersects(bb1))

    def test_get_intersection(self):
        a = BoundingBox(0, 0, 2, 2)
        b = BoundingBox(1, 1, 3, 3)

        a_b = a.get_intersection(b)
        self.assertEqual(a_b, b.get_intersection(a))
        self.assertEqual(a_b.x_min, 1)
        self.assertEqual(a_b.x_max, 2)
        self.assertEqual(a_b.y_min, 1)
        self.assertEqual(a_b.y_max, 2)
        self.assertEqual(a_b.width, 1)
        self.assertEqual(a_b.height, 1)

        c = BoundingBox(0, 0, 2, 1)
        d = BoundingBox(1, -1, 3, 2)

        c_d = c.get_intersection(d)
        self.assertEqual(c_d, d.get_intersection(c))
        self.assertEqual(c_d.x_min, 1)
        self.assertEqual(c_d.y_min, 0)
        self.assertEqual(c_d.x_max, 2)
        self.assertEqual(c_d.y_max, 1)
        self.assertEqual(c_d.width, 1)
        self.assertEqual(c_d.height, 1)

        e = BoundingBox(0, 0, 1, 1)
        f = BoundingBox(2, 2, 3, 3)

        e_f = e.get_intersection(f)
        self.assertEqual(e_f, f.get_intersection(e))
        self.assertIsNone(e_f)

        g = BoundingBox(0, 0, 3, 3)
        h = BoundingBox(1, 1, 2, 2)

        g_h = g.get_intersection(h)
        self.assertEqual(g_h, h.get_intersection(g))
        self.assertEqual(g_h.x_min, 1)
        self.assertEqual(g_h.y_min, 1)
        self.assertEqual(g_h.x_max, 2)
        self.assertEqual(g_h.y_max, 2)
        self.assertEqual(g_h.width, 1)
        self.assertEqual(g_h.height, 1)

        i = BoundingBox(0, 0, 2, 1)
        j = BoundingBox(1, 0, 3, 1)

        i_j = i.get_intersection(j)
        self.assertEqual(i_j, j.get_intersection(i))
        self.assertEqual(i_j.x_min, 1)
        self.assertEqual(i_j.y_min, 0)
        self.assertEqual(i_j.x_max, 2)
        self.assertEqual(i_j.y_max, 1)
        self.assertEqual(i_j.width, 1)
        self.assertEqual(i_j.height, 1)


if __name__ == '__main__':
    unittest.main()
