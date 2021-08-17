<<<<<<< HEAD
import unittest
from app.models import Pitch, Comment
from flask_login import current_user
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch_id=2, pitch_title='Data fetching with API',category = 'Technology Pitch', pitch_content ='This is how it goes', posted = '15/8/2021', user_id = 2, down_vote = 0, up_vote =0 )
        self.new_comment = Comment(id =3, pitch_id=2, pitch_comment ='Great stuff', posted ='12/7/2021', user_id=2)
=======

import unittest
from app.models import User, Comment
from flask_login import current_user
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_frank = User(id = 1, username = 'frank', email = 'frankmutua@yahoo.com', password_secure = '54321')
        self.new_comment = Comment(id = 1, pitch_id =2, pitch_comment='dope stuff',posted='12/6/2021',user_id =1)
>>>>>>> 322c028a2a9dc8bbd373e888aba8e0eac26e43e4


    def tearDown(self):
        Comment.query.delete()
<<<<<<< HEAD
        Pitch.query.delete()
=======
        User.query.delete()

>>>>>>> 322c028a2a9dc8bbd373e888aba8e0eac26e43e4

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
<<<<<<< HEAD
        self.assertEquals(self.new_comment.id,3)
        self.assertEquals(self.new_comment.pitch_id,2)
        self.assertEquals(self.new_comment.pitch_comment, 'Great stuff')
        self.assertEquals(self.new_comment.posted,'12/7/2021')
        self.assertEquals(self.new_comment.user_id,2)


  
    def test_save_comment(self):
        db.session.add(self.new_pitch)
        db.session.commit()
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
=======
        self.assertEquals(self.new_comment.id,1)
        self.assertEquals(self.new_comment.pitch_id,2)
        self.assertEquals(self.new_comment.pitch_comment,'dope stuff')
        self.assertEquals(self.new_comment.posted,'12/6/2021')
        self.assertEquals(self.new_comment.user_id, 1)


  
    # def test_save_comment(self):
    #     self.new_comment.save_comment()
    #     self.assertTrue(len(Comment.query.all())>0)
>>>>>>> 322c028a2a9dc8bbd373e888aba8e0eac26e43e4
