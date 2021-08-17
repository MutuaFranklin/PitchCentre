
import unittest
from app.models import User, Comment
from flask_login import current_user
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_frank = User(id = 1, username = 'frank', email = 'frankmutua@yahoo.com', password_secure = '54321')
        self.new_comment = Comment(id = 1, pitch_id =2, pitch_comment='dope stuff',posted='12/6/2021',user_id =1)


    def tearDown(self):
        Comment.query.delete()
        User.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,1)
        self.assertEquals(self.new_comment.pitch_id,2)
        self.assertEquals(self.new_comment.pitch_comment,'dope stuff')
        self.assertEquals(self.new_comment.posted,'12/6/2021')
        self.assertEquals(self.new_comment.user_id, 1)


  
    # def test_save_comment(self):
    #     self.new_comment.save_comment()
    #     self.assertTrue(len(Comment.query.all())>0)