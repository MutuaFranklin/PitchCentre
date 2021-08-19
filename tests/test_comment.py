import unittest
from app.models import Pitch, Comment
from flask_login import current_user
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch_id=2, pitch_title='Data fetching with API',category = 'Technology Pitch', pitch_content ='This is how it goes', posted = '15/8/2021', user_id = 2, down_vote = 0, up_vote =0 )
        self.new_comment = Comment(id =3, pitch_id=2, pitch_comment ='Great stuff', posted ='12/7/2021', user_id=2)


    def tearDown(self):
        Comment.query.delete()
        Pitch.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,3)
        self.assertEquals(self.new_comment.pitch_id,2)
        self.assertEquals(self.new_comment.pitch_comment, 'Great stuff')
        self.assertEquals(self.new_comment.posted,'12/7/2021')
        self.assertEquals(self.new_comment.user_id,2)


  
    def test_save_comment(self):
        db.session.add(self.new_pitch)
        db.session.commit()
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())==1)
