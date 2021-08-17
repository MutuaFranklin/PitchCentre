
# import unittest
# from app.models import User, Pitch, Comment
# from flask_login import current_user
# from app import db

# class TestPitch(unittest.TestCase):

#     def setUp(self):
#         self.user_frank = User(id = 2, username = 'frank',password = '54321', email = 'frankmutua@yahoo.com', bio = 'maniac',profile_pic_path = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1200px-Image_created_with_a_mobile_phone.png', role = 'Admin')
#         self.new_pitch = Pitch(pitch_id=2, pitch_title='Data fetching with API',category = 'Technology', pitch_content ='This is how it goes', posted = '15/8/2021', user_id = 2, down_vote = 0, up_vote =0 )
#         self.new_comment = Comment(id = 1, pitch_id =2, pitch_comment='dope stuff',posted='12/6/2021',user_id =1)


#     def tearDown(self):
#         Comment.query.delete()
#         Pitch.query.delete()


#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_comment,Comment))


#     def test_check_instance_variables(self):
#         self.assertEquals(self.new_comment.id,1)
#         self.assertEquals(self.new_comment.pitch_id,2)
#         self.assertEquals(self.new_comment.pitch_comment,'dope stuff')
#         self.assertEquals(self.new_comment.posted,'12/6/2021')
#         self.assertEquals(self.new_comment.user_id, 1)






  
#     def test_save_comment(self):
#         self.new_pitch.save_pitch()()
#         self.assertTrue(len(Comment.query.all())>0)