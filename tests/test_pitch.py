import unittest
from app.models import User, Pitch
from flask_login import current_user
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_frank = User(id = 2, username = 'frank',password = '54321', email = 'frankmutua@yahoo.com', bio = 'maniac', )
        self.new_pitch = Pitch(pitch_id=2, pitch_title='Data fetching with API',category = 'Technology', pitch_content ='This is how it goes', comments='This pitch just opened my mind', posted = '15/8/2021', user_id = 2, down_vote = 0, up_vote =0 )



    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_id,2)
        self.assertEquals(self.new_pitch.pitch_title,'Data fetching with API')
        self.assertEquals(self.new_pitch.category,'Technology')
        self.assertEquals(self.new_pitch.pitch_content,'This is how it goes')
        self.assertEquals(self.new_pitch.comments,'This pitch just opened my mind')
        self.assertEquals(self.new_pitch.posted,'15/8/2021')
        self.assertEquals(self.new_pitch.user_id, 2)
        self.assertEquals(self.new_pitch.up_vote,0)
        self.assertEquals(self.new_pitch.down_vote,0)





  
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)