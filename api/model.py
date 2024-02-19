# from tinydb import TinyDB, Query


# class UserModel:

#     def __init__(self, path='db.json'):
#         self.db = TinyDB(path)

#     def upsert_user(self, user):
#         if not self.db.search(Query().id == user.id):
#             self.db.insert(user.serialize())

#     def get_user(self, user_id):
#         user = self.db.search(Query().id == user_id)
#         return UserData.deserialize(user[0])

#     def remove_user(self, user_id):
#         self.db.remove(Query().id == user_id)


class UserData:
    
    def __init__(self, user=None):
        if user:
            user_info = user['properties']
            self.nickname = user_info['nickname']
            self.profile = user_info['profile_image'] 
            self.thumbnail = user_info['thumbnail_image']
        else:
            self.nickname = None
            self.profile = None
            self.thumbnail = None

    def __str__(self):
        return f"<UserData>(nickname:{self.nickname})"

    def serialize(self):
        return {
            "nickname": self.nickname,
            "profile": self.profile,
            "thumbnail": self.thumbnail
        }

    @staticmethod
    def deserialize(user_data):
        user = UserData()
        user.nickname = user_data['nickname']
        user.profile = user_data['profile']
        user.thumbnail = user_data['thumbnail']
        return user