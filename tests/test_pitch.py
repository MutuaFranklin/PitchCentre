import unittest
from app.models import User, Pitch
from flask_login import current_user
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_frank = User(id = 2, username = 'frank',password = '54321', email = 'frankmutua@yahoo.com', bio = 'maniac', )
        self.new_pitch = Pitch(pitch_id=2, pitch_title='Data fetching with API',category = 'Technology', pitch_content ='This is how it goes', comments='This pitch just opened my mind', posted = '15/8/2021', user = self.user_frank, down_vote = 0, up_vote =0 )



    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_id,2)



  
    def test_save_pitch(self):
        self.new_review.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)