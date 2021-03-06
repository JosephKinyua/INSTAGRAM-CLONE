from django.test import TestCase
from .models import Location, Profile, Post, Comments
from django.contrib.auth.models import User


class TestLocation(TestCase):
  def setUp(self):
    self.location = Location(location='Nyandarua')
    self.location.save()

  def TearDown(self):
    Location.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.location, Location))

  def test_saveLocation(self):
    self.location.save()
    location = Location.objects.all()
    self.assertTrue(len(location)>0)

  def test_deleteLocation(self):
    self.location.saveLocation()
    self.location2 = Location.objects.create(location='Mombasa')
    Location.deleteLocation(self.location2.id)
    self.assertTrue(len(Location.objects.all())==1)

  def test_updateLocation(self):
    update_term = 'Mombasa'
    self.location.saveLocation()
    Location.updateLocation(self.location.id, update_term)  
    updated_one = Location.objects.get(id=self.location.id)
    self.assertEqual(updated_one.location, 'Mombasa')



class TestPost(TestCase):
  def setUp(self):
    self.location = Location(location='Nyandarua')
    self.location.save()
    self.new_user = User(username = "JosephKinyua")
    self.new_user.save()
    self.new_post = Post(picture='test.jpg',caption = 'this is amazing' , uploadedBy = self.new_user, location=self.location)
    self.new_post.save_picture()
  
  def tearDown(self):
    Post.objects.all().delete()
    User.objects.all().delete()
    Location.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.new_post, Post))

  def test_savePicture(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'this is wow' , uploadedBy = self.new_user, location=self.location)
    self.new_post2.save_picture()
    self.assertEqual(len(Post.objects.all()),2)

  def test_deletePicture(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'this is wow' , uploadedBy = self.new_user, location=self.location)
    self.new_post2.save_picture()
    self.assertEqual(len(Post.objects.all()),2)
    Post.delete_picture(self.new_post2.id)
    self.assertEqual(len(Post.objects.all()),1)

  def test_update(self):
    self.new_post.save_picture()
    self.new_post.update_caption(self.new_post.id, 'loving it')
    updated_post = Post.objects.get(id=self.new_post.id)
    self.assertEqual(updated_post.caption, 'loving it')   
  
  def test_allpics(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'this is wow' , uploadedBy = self.new_user, location=self.location)
    self.new_post2.save_picture()
    self.assertEqual(len(Post.all_pictures()), 2)

  def test_userPictures(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'this is wow' , uploadedBy = self.new_user, location=self.location)
    self.new_post2.save_picture()
    usrpic = Post.user_pictures(self.new_user.username)
    self.assertEqual(len(usrpic), 2)