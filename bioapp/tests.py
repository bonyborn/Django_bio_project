from django.test import TestCase
from .models import Bio

class BioModelTest(TestCase):

    def setUp(self):
        self.bio = Bio.objects.create(
            full_name="John Doe",
            age=30,
            profession="Software Developer",
            short_bio="A passionate developer.",
            hobbies="Coding, Reading"
        )

    def test_bio_creation(self):
        self.assertEqual(self.bio.full_name, "John Doe")
        self.assertEqual(self.bio.age, 30)
        self.assertEqual(self.bio.profession, "Software Developer")
        self.assertEqual(self.bio.short_bio, "A passionate developer.")
        self.assertEqual(self.bio.hobbies, "Coding, Reading")

    def test_bio_str(self):
        self.assertEqual(str(self.bio), "John Doe")