from datetime import datetime
from enums.user.sex import Sex
from enums.user.school_type import SchoolType
from enums.user.deactivated import IsDeactivated
from enums.user.friend_status import FriendStatus
from types.users.Carrer import UsersCareer
from types.users.City import UsersCity
from types.users.Contacts import UsersContacts
from types.users.Connection import UsersConnection
from types.users.Counters import UsersCounters
from types.users.Country import UsersCountry
from types.users.Education import UsersEducation
from types.users.NameCases import UsersNameCases
from types.users.SurnameCases import UsersSurnameCases
from types.users.LastSeen import UsersLastSeen


class User:
    def __init__(self, user_id: int, first_name: str, last_name: str,
                 deactivated: IsDeactivated | None, is_closed: bool, can_access_closed: bool,
                 about: str, activities: str, birth_date: datetime, is_blacklisted: bool,
                 is_blacklisted_by_me: bool, books: str, can_post: bool, can_see_all_posts: bool,
                 can_see_audio: bool, can_send_friend_request: bool,
                 can_write_private_message: bool, career: list[UsersCareer] | None,
                 city: UsersCity | None, common_count: int, connections: list[UsersConnection] | None,
                 contacts: UsersContacts, counters: UsersCounters | None,
                 country: UsersCountry | None, crop_photo: object | None, domain: str,
                 education: UsersEducation | None, exports: object | None,
                 name_cases: UsersNameCases | None, followers_count: int, friend_status: FriendStatus | None,
                 games: str, has_mobile_phone: bool | None, has_photo: bool | None,
                 home_town: str, interests: str, is_favorite: bool | None, is_friend: bool | None,
                 is_hidden_from_feed: bool | None, is_no_index: bool | None,
                 surname_cases: UsersSurnameCases | None, last_seen: UsersLastSeen | None,
                 lists: str | None, maiden_name: str | None,):
        """
        Base_fields:
        :param user_id: ID of user
        :param first_name: first_name of user
        :param last_name:
        :param deactivated:
        :param is_closed:
        :param can_access_closed:

        Optional_fields:
        :param about: optional, some info about
        """
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.deactivated = deactivated
        self.is_closed = is_closed
        self.can_access_closed = can_access_closed

        self.about = about
        self.activities = activities
        self.birth_date = birth_date
        self.is_blacklisted = is_blacklisted
        self.is_blacklisted_by_me = is_blacklisted_by_me
        self.books = books
        self.can_post = can_post
        self.can_see_all_posts = can_see_all_posts
        self.can_see_audio = can_see_audio
        self.can_send_friend_request = can_send_friend_request
        self.can_write_private_message = can_write_private_message
        self.career = career
        self.city = city
        self.common_count = common_count
        self.connections = connections
        self.contacts = contacts
        self.counters = counters
        self.country = country
        self.crop_photo = crop_photo
        self.domain = domain
        self.education = education
        self.exports = exports
        self.name_cases = name_cases
        self.followers_count = followers_count
        self.friend_status = friend_status
        self.games = games
        self.has_mobile_phone = has_mobile_phone
        self.has_photo = has_photo
        self.home_town = home_town
        self.interests = interests
        self.is_favorite = is_favorite
        self.is_friend = is_friend
        self.is_hidden_from_feed = is_hidden_from_feed
        self.is_no_index = is_no_index
        self.surname_cases = surname_cases
        self.last_seen = last_seen
        self.lists = lists
        self.maiden_name = maiden_name

        self.age = self.count_age()

    def count_age(self) -> int:
        curr_date = datetime.now()
        age = curr_date.year - self.birth_date.year

        if (curr_date.month, curr_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

