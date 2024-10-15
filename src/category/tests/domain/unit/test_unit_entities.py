from dataclasses import is_dataclass
from datetime import datetime
import unittest
from category.domain.entities import Category

class TestCategory(unittest.TestCase):

    def test_if_is_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        category = Category('Movie', 'test', True, datetime.now())
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'test')
        self.assertTrue(category.is_active)
        self.assertIsInstance(category.created_at, datetime)

        created_at = datetime.now()
        category = Category(
            name='Movie',
            description='test',
            is_active=False,
            created_at=created_at
        )

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'test')
        self.assertFalse(category.is_active)
        self.assertEqual(category.created_at, created_at)

    def test_if_created_at_is_generated_in_constructor(self):
        category1 = Category(name='Movie 1')
        category2 = Category(name='Movie 2')
        
        self.assertNotEqual(
            category1.created_at.timestamp(),
            category2.created_at.timestamp()
        )