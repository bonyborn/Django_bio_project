from django.test import TestCase
from .models import Bio

class BioModelTest(TestCase):

    def setUp(self):
        self.bio = Bio.objects.create(
            full_name="Bony Born",
            age=23,
            profession="Software Developer",
            short_bio="A passionate developer.",
            hobbies="Coding, Reading, Dancing, Travelling"
        )

    def test_bio_creation(self):
        self.assertEqual(self.bio.full_name, "Bony Born")
        self.assertEqual(self.bio.age, 23)
        self.assertEqual(self.bio.profession, "Software Developer")
        self.assertEqual(self.bio.short_bio, "A passionate developer.")
        self.assertEqual(self.bio.hobbies, "Coding, Reading, Dancing, Travelling")

    def test_bio_str(self):
        self.assertEqual(str(self.bio), "Bony Born - Software Developer")