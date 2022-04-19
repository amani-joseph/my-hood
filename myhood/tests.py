from django.test import TestCase
import os

# Create your tests here.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myhoodproject.settings')
import django
django.setup()

from django.contrib.auth.models import User
# Create your tests here.
from myhood.models import Profile, Neighbourhood, Business, Post


class ProfileTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='Joe', password="j03")
        self.hood = Neighbourhood.objects.create(name="Muthaiga", city_address="Nairobi, Mutahiga", population_count=0,location="-1.367673, 36.836323", user=self.test_user)
        
        self.test_profile = Profile(user=self.test_user,image='default.png', bio="My Bio", hood=self.hood)

    # testing instance
    def test_instance(self):
        profile = self.test_profile
        self.assertEqual(self.test_profile, profile)

    # testing save method
    def test_save_profile_method(self):
        original_len = Profile.get_all_profiles()
        print(f'original len {len(original_len)}')
        self.test_profile.save_profile()

        new_len = Profile.get_all_profiles()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_profile_method(self):
        self.test_profile.save_profile()
        original_len = Profile.objects.all()
        print(f'the categorys are{len(original_len)}')
        Profile.delete_profile(self.test_profile.id)
        new_len = Profile.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_profile_by_id_method(self):
        self.test_profile.save_profile()
        req_result = Profile.get_profile_by_id(self.test_profile.id)
        self.assertTrue(req_result is not None)

    def test_search_profile_by_neigh_name_method(self):
        self.test_profile.save_profile()

        req_result = Profile.search_profile_by_neigh_name(self.test_profile.neighborhood_name)
        self.assertTrue(req_result is not None)


class NeighborhoodTestClass(TestCase):
    # set up method
    def setUp(self):
         self.test_user = User.objects.create(username='theuser', password="12345")
         self.test_neighborhood = Neighbourhood(name="Muthaiga", city_address="Nairobi, Mutahiga", population_count=0,location="-1.367673, 36.836323", user=self.test_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.test_neighborhood, Neighbourhood))

    def tearDown(self):
      Neighbourhood.objects.filter(id=1).delete()

    def test_create_neighborhood(self):
        self.test_neighborhood.save_neighborhood()
        self.assertTrue(len(Neighbourhood.objects.all())>0)

    def test_delete_neighborhood(self):
        self.test_neighborhood.delete_neighborhood(1)
        self.assertTrue(len(Neighbourhood.objects.all()) == 0)

    def test_find_neighborhood(self):
        self.test_neighborhood.save_neighborhood()
        self.assertTrue(len(Neighbourhood.objects.filter(id=1)) == 1)

    def test_update_neighborhood(self):
        self.test_neighborhood.save_neighborhood()
        pass


class BusinessTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='amani', password="password")
        self.test_business = Business( name='Tech Lead',email="techlead@gmail.com",user=self.test_user, address="Lenana,Ngong Road", neighbourhood=self.test_neighborhood, location="-1.367673, 36.836323")

    # testing instance
    def test_instance(self):
        business = self.test_business
        self.assertEqual(self.test_business, business)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def tearDown(self):
        Business.objects.filter(id=1).delete()

    def test_create_business(self):
        self.new_business.create_business()
        self.assertTrue(len(Business.objects.all())>0)

    def test_delete_business(self):
        self.new_business.delete_business(1)
        self.assertTrue(len(Business.objects.all()) == 0)

    def test_find_business(self):
        self.new_business.create_business()
        self.assertTrue(len(Business.objects.filter(id=1)) == 1)

    def test_update_business(self):
        pass


class PostTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='amani', password="password")
        self.test_neighborhood = Neighbourhood(name="Muthaiga", city_address="Nairobi, Mutahiga", population_count=0,location="-1.367673, 36.836323", user=self.test_user)
        self.test_post = Post( message='Hello There ',image="image.png", pub_date="2022-04-19",user=self.test_user, neighbourhood=self.test_neighborhood)

    # testing instance
    def test_instance(self):
        post = self.test_post
        self.assertEqual(self.test_instance, post)

    def test_instance(self):
        self.assertTrue(isinstance(self.test_post, Business))

    def tearDown(self):
        Post.objects.filter(id=1).delete()

    def test_create_business(self):
        self.test_post.create_biz()
        self.assertTrue(len(Post.objects.all())>0)

    def test_delete_business(self):
        self.test_post.delete_biz(1)
        self.assertTrue(len(Post.objects.all()) == 0)

    def test_find_business(self):
        self.test_post.create_biz()
        self.assertTrue(len(Post.objects.filter(id=1)) == 1)

    def test_update_business(self):
        pass