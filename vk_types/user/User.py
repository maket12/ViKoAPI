from datetime import datetime
from enums.user.deactivated import IsDeactivated
from enums.user.friend_status import FriendStatus
from enums.user.relation import RelationStatus
from enums.user.sex import Sex
from enums.user.wall_default import WallDefault
from vk_types.user.user_subclasses.Carrer import UsersCareer
from vk_types.user.user_subclasses.City import UsersCity
from vk_types.user.user_subclasses.Contacts import UsersContacts
from vk_types.user.user_subclasses.Connection import UsersConnection
from vk_types.user.user_subclasses.Counters import UsersCounters
from vk_types.user.user_subclasses.Country import UsersCountry
from vk_types.user.user_subclasses.Education import UsersEducation
from vk_types.user.user_subclasses.NameCases import UsersNameCases
from vk_types.user.user_subclasses.SurnameCases import UsersSurnameCases
from vk_types.user.user_subclasses.LastSeen import UsersLastSeen
from vk_types.user.user_subclasses.Military import UsersMilitary
from vk_types.user.user_subclasses.Occupation import UsersOccupation
from vk_types.user.user_subclasses.Personal import UsersPersonal
from vk_types.user.user_subclasses.Relative import UsersRelative
from vk_types.user.user_subclasses.School import UsersSchool
from vk_types.user.user_subclasses.University import UsersUniversity


class User:
    """
    Represents a VK User object.\n
    Source: https://dev.vk.com/ru/reference/objects/user
    """
    def __init__(self, user_id: int, first_name: str, last_name: str,
                 deactivated: IsDeactivated | None, is_closed: bool | None, can_access_closed: bool | None,
                 about: str | None, activities: str | None, birth_date: datetime, is_blacklisted: bool | None,
                 is_blacklisted_by_me: bool | None, books: str | None, can_post: bool | None, can_see_all_posts: bool | None,
                 can_see_audio: bool | None, can_send_friend_request: bool | None,
                 can_write_private_message: bool | None, career: list[UsersCareer] | None,
                 city: UsersCity | None, common_count: int | None, connections: list[UsersConnection] | None,
                 contacts: UsersContacts | None, counters: UsersCounters | None,
                 country: UsersCountry | None, crop_photo: object | None, domain: str | None,
                 education: UsersEducation | None, exports: object | None,
                 name_cases: UsersNameCases | None, followers_count: int, friend_status: FriendStatus | None,
                 games: str | None, has_mobile_phone: bool | None, has_photo: bool | None,
                 home_town: str | None, interests: str, is_favorite: bool | None, is_friend: bool | None,
                 is_hidden_from_feed: bool | None, is_no_index: bool | None,
                 surname_cases: UsersSurnameCases | None, last_seen: UsersLastSeen | None,
                 lists: str | None, maiden_name: str | None, military: list[UsersMilitary] | None,
                 movies: str | None, music: str | None, nickname: str | None,
                 occupation: UsersOccupation | None, is_online: bool | None, is_online_mobile: bool | None,
                 is_online_app: bool | None, personal: UsersPersonal | None, photo_50: str | None,
                 photo_100: str | None, photo_200_orig: str | None, photo_200: str | None,
                 photo_400_orig: str | None, photo_id: str | None, photo_max: str | None,
                 photo_max_orig: str | None, quotes: str | None, relatives: list[UsersRelative] | None,
                 relation: RelationStatus, relation_partner: UsersRelative | None,
                 schools: list[UsersSchool] | None, screen_name: str | None, sex: Sex | None,
                 site: str | None, status: str | None, status_audio: str | None, timezone: int | None,
                 trending: bool | None, tv: str | None, universities: list[UsersUniversity] | None,
                 is_verified: bool | None, wall_default: WallDefault | None,
                 found_with: str | None):
        """
        Represents the user object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param user_id:
        :param first_name:
        :param last_name:
        :param deactivated:
        :param is_closed:
        :param can_access_closed:
        :param about:
        :param activities:
        :param birth_date:
        :param is_blacklisted:
        :param is_blacklisted_by_me:
        :param books:
        :param can_post:
        :param can_see_all_posts:
        :param can_see_audio:
        :param can_send_friend_request:
        :param can_write_private_message:
        :param career:
        :param city:
        :param common_count:
        :param connections:
        :param contacts:
        :param counters:
        :param country:
        :param crop_photo:
        :param domain:
        :param education:
        :param exports:
        :param name_cases:
        :param followers_count:
        :param friend_status:
        :param games:
        :param has_mobile_phone:
        :param has_photo:
        :param home_town:
        :param interests:
        :param is_favorite:
        :param is_friend:
        :param is_hidden_from_feed:
        :param is_no_index:
        :param surname_cases:
        :param last_seen:
        :param lists:
        :param maiden_name:
        :param military:
        :param movies:
        :param music:
        :param nickname:
        :param occupation:
        :param is_online:
        :param is_online_mobile:
        :param is_online_app:
        :param personal:
        :param photo_50:
        :param photo_100:
        :param photo_200_orig:
        :param photo_200:
        :param photo_400_orig:
        :param photo_id:
        :param photo_max:
        :param photo_max_orig:
        :param quotes:
        :param relatives:
        :param relation:
        :param relation_partner:
        :param schools:
        :param screen_name:
        :param sex:
        :param site:
        :param status:
        :param status_audio:
        :param timezone:
        :param trending:
        :param tv:
        :param universities:
        :param is_verified:
        :param wall_default:
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
        self.military = military
        self.movies = movies
        self.music = music
        self.nickname = nickname
        self.occupation = occupation
        self.is_online = is_online
        self.is_online_mobile = is_online_mobile
        self.is_online_app = is_online_app
        self.personal = personal
        self.photo_50 = photo_50
        self.photo_100 = photo_100
        self.photo_200_orig = photo_200_orig
        self.photo_200 = photo_200
        self.photo_400_orig = photo_400_orig
        self.photo_id = photo_id
        self.photo_max = photo_max
        self.photo_max_orig = photo_max_orig
        self.quotes = quotes
        self.relatives = relatives
        self.relation = relation
        self.relation_partner = relation_partner

        self.schools = schools
        self.screen_name = screen_name
        self.sex = sex
        self.site = site
        self.status = status
        self.status_audio = status_audio
        self.timezone = timezone
        self.trending = trending
        self.tv = tv
        self.universities = universities
        self.is_verified = is_verified
        self.wall_default = wall_default

        self.found_with = found_with

        self.age = self.count_age()

    def count_age(self) -> int:
        curr_date = datetime.now()
        age = curr_date.year - self.birth_date.year

        if (curr_date.month, curr_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def to_dict(self) -> dict:
        def _to_dict(value):
            if value is None:
                return None
            if isinstance(value, list):
                return [_to_dict(v) for v in value]
            if hasattr(value, "to_dict"):
                return value.to_dict()
            return value

        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "deactivated": self.deactivated.name if self.deactivated else None,
            "is_closed": self.is_closed,
            "can_access_closed": self.can_access_closed,
            "about": self.about,
            "activities": self.activities,
            "bdate": self.birth_date.strftime("%d.%m.%Y") if self.birth_date else None,
            "blacklisted": self.is_blacklisted,
            "blacklisted_by_me": self.is_blacklisted_by_me,
            "books": self.books,
            "can_post": self.can_post,
            "can_see_all_posts": self.can_see_all_posts,
            "can_see_audio": self.can_see_audio,
            "can_send_friend_request": self.can_send_friend_request,
            "can_write_private_message": self.can_write_private_message,
            "career": _to_dict(self.career),
            "city": _to_dict(self.city),
            "common_count": self.common_count,
            "connections": _to_dict(self.connections),
            "contacts": _to_dict(self.contacts),
            "counters": _to_dict(self.counters),
            "country": _to_dict(self.country),
            "crop_photo": _to_dict(self.crop_photo),
            "domain": self.domain,
            "education": _to_dict(self.education),
            "exports": _to_dict(self.exports),
            "name_cases": _to_dict(self.name_cases),
            "followers_count": self.followers_count,
            "friend_status": self.friend_status.value if self.friend_status else None,
            "games": self.games,
            "has_mobile": self.has_mobile_phone,
            "has_photo": self.has_photo,
            "home_town": self.home_town,
            "interests": self.interests,
            "is_favorite": self.is_favorite,
            "is_friend": self.is_friend,
            "is_hidden_from_feed": self.is_hidden_from_feed,
            "is_no_index": self.is_no_index,
            "surname_cases": _to_dict(self.surname_cases),
            "last_seen": _to_dict(self.last_seen),
            "lists": self.lists,
            "maiden_name": self.maiden_name,
            "military": _to_dict(self.military),
            "movies": self.movies,
            "music": self.music,
            "nickname": self.nickname,
            "occupation": _to_dict(self.occupation),
            "online": self.is_online,
            "online_mobile": self.is_online_mobile,
            "online_app": self.is_online_app,
            "personal": _to_dict(self.personal),
            "photo_50": self.photo_50,
            "photo_100": self.photo_100,
            "photo_200_orig": self.photo_200_orig,
            "photo_200": self.photo_200,
            "photo_400_orig": self.photo_400_orig,
            "photo_id": self.photo_id,
            "photo_max": self.photo_max,
            "photo_max_orig": self.photo_max_orig,
            "quotes": self.quotes,
            "relatives": _to_dict(self.relatives),
            "relation": self.relation.value if self.relation else None,
            "relation_partner": _to_dict(self.relation_partner),
            "schools": _to_dict(self.schools),
            "screen_name": self.screen_name,
            "sex": self.sex.value if self.sex else None,
            "site": self.site,
            "status": self.status,
            "status_audio": self.status_audio,
            "timezone": self.timezone,
            "trending": self.trending,
            "tv": self.tv,
            "universities": _to_dict(self.universities),
            "verified": self.is_verified,
            "wall_default": self.wall_default.value if self.wall_default else None,
            "found_with": self.found_with,
            "age": self.age,
        }
