"""Auto-generated TL types. Do not edit manually."""
from __future__ import annotations
from typing import Any, List, Optional, TYPE_CHECKING
from sent.tl.tlobject import TLObject, register, serialize_bool
from sent.tl.serialization import BinaryReader, BinaryWriter

@register
class StatsBroadcastStats(TLObject):
    CONSTRUCTOR_ID = 963421692
    __slots__ = ('period', 'followers', 'views_per_post', 'shares_per_post', 'reactions_per_post', 'views_per_story', 'shares_per_story', 'reactions_per_story', 'enabled_notifications', 'growth_graph', 'followers_graph', 'mute_graph', 'top_hours_graph', 'interactions_graph', 'iv_interactions_graph', 'views_by_source_graph', 'new_followers_by_source_graph', 'languages_graph', 'reactions_by_emotion_graph', 'story_interactions_graph', 'story_reactions_by_emotion_graph', 'recent_posts_interactions')
    def __init__(self, period: 'StatsDateRangeDays', followers: 'StatsAbsValueAndPrev', views_per_post: 'StatsAbsValueAndPrev', shares_per_post: 'StatsAbsValueAndPrev', reactions_per_post: 'StatsAbsValueAndPrev', views_per_story: 'StatsAbsValueAndPrev', shares_per_story: 'StatsAbsValueAndPrev', reactions_per_story: 'StatsAbsValueAndPrev', enabled_notifications: 'StatsPercentValue', growth_graph: 'StatsGraph', followers_graph: 'StatsGraph', mute_graph: 'StatsGraph', top_hours_graph: 'StatsGraph', interactions_graph: 'StatsGraph', iv_interactions_graph: 'StatsGraph', views_by_source_graph: 'StatsGraph', new_followers_by_source_graph: 'StatsGraph', languages_graph: 'StatsGraph', reactions_by_emotion_graph: 'StatsGraph', story_interactions_graph: 'StatsGraph', story_reactions_by_emotion_graph: 'StatsGraph', recent_posts_interactions: 'Vector'):
        self.period = period
        self.followers = followers
        self.views_per_post = views_per_post
        self.shares_per_post = shares_per_post
        self.reactions_per_post = reactions_per_post
        self.views_per_story = views_per_story
        self.shares_per_story = shares_per_story
        self.reactions_per_story = reactions_per_story
        self.enabled_notifications = enabled_notifications
        self.growth_graph = growth_graph
        self.followers_graph = followers_graph
        self.mute_graph = mute_graph
        self.top_hours_graph = top_hours_graph
        self.interactions_graph = interactions_graph
        self.iv_interactions_graph = iv_interactions_graph
        self.views_by_source_graph = views_by_source_graph
        self.new_followers_by_source_graph = new_followers_by_source_graph
        self.languages_graph = languages_graph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph
        self.story_interactions_graph = story_interactions_graph
        self.story_reactions_by_emotion_graph = story_reactions_by_emotion_graph
        self.recent_posts_interactions = recent_posts_interactions
    def to_dict(self):
        return {"period": self.period, "followers": self.followers, "views_per_post": self.views_per_post, "shares_per_post": self.shares_per_post, "reactions_per_post": self.reactions_per_post, "views_per_story": self.views_per_story, "shares_per_story": self.shares_per_story, "reactions_per_story": self.reactions_per_story, "enabled_notifications": self.enabled_notifications, "growth_graph": self.growth_graph, "followers_graph": self.followers_graph, "mute_graph": self.mute_graph, "top_hours_graph": self.top_hours_graph, "interactions_graph": self.interactions_graph, "iv_interactions_graph": self.iv_interactions_graph, "views_by_source_graph": self.views_by_source_graph, "new_followers_by_source_graph": self.new_followers_by_source_graph, "languages_graph": self.languages_graph, "reactions_by_emotion_graph": self.reactions_by_emotion_graph, "story_interactions_graph": self.story_interactions_graph, "story_reactions_by_emotion_graph": self.story_reactions_by_emotion_graph, "recent_posts_interactions": self.recent_posts_interactions}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(963421692, signed=False)
        writer.write(bytes(self.period))
        writer.write(bytes(self.followers))
        writer.write(bytes(self.views_per_post))
        writer.write(bytes(self.shares_per_post))
        writer.write(bytes(self.reactions_per_post))
        writer.write(bytes(self.views_per_story))
        writer.write(bytes(self.shares_per_story))
        writer.write(bytes(self.reactions_per_story))
        writer.write(bytes(self.enabled_notifications))
        writer.write(bytes(self.growth_graph))
        writer.write(bytes(self.followers_graph))
        writer.write(bytes(self.mute_graph))
        writer.write(bytes(self.top_hours_graph))
        writer.write(bytes(self.interactions_graph))
        writer.write(bytes(self.iv_interactions_graph))
        writer.write(bytes(self.views_by_source_graph))
        writer.write(bytes(self.new_followers_by_source_graph))
        writer.write(bytes(self.languages_graph))
        writer.write(bytes(self.reactions_by_emotion_graph))
        writer.write(bytes(self.story_interactions_graph))
        writer.write(bytes(self.story_reactions_by_emotion_graph))
        writer.write(bytes(self.recent_posts_interactions))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        period = reader.tgread_object()
        followers = reader.tgread_object()
        views_per_post = reader.tgread_object()
        shares_per_post = reader.tgread_object()
        reactions_per_post = reader.tgread_object()
        views_per_story = reader.tgread_object()
        shares_per_story = reader.tgread_object()
        reactions_per_story = reader.tgread_object()
        enabled_notifications = reader.tgread_object()
        growth_graph = reader.tgread_object()
        followers_graph = reader.tgread_object()
        mute_graph = reader.tgread_object()
        top_hours_graph = reader.tgread_object()
        interactions_graph = reader.tgread_object()
        iv_interactions_graph = reader.tgread_object()
        views_by_source_graph = reader.tgread_object()
        new_followers_by_source_graph = reader.tgread_object()
        languages_graph = reader.tgread_object()
        reactions_by_emotion_graph = reader.tgread_object()
        story_interactions_graph = reader.tgread_object()
        story_reactions_by_emotion_graph = reader.tgread_object()
        recent_posts_interactions = reader.tgread_object()
        return cls(period, followers, views_per_post, shares_per_post, reactions_per_post, views_per_story, shares_per_story, reactions_per_story, enabled_notifications, growth_graph, followers_graph, mute_graph, top_hours_graph, interactions_graph, iv_interactions_graph, views_by_source_graph, new_followers_by_source_graph, languages_graph, reactions_by_emotion_graph, story_interactions_graph, story_reactions_by_emotion_graph, recent_posts_interactions)

@register
class StatsMegagroupStats(TLObject):
    CONSTRUCTOR_ID = 4018141462
    __slots__ = ('period', 'members', 'messages', 'viewers', 'posters', 'growth_graph', 'members_graph', 'new_members_by_source_graph', 'languages_graph', 'messages_graph', 'actions_graph', 'top_hours_graph', 'weekdays_graph', 'top_posters', 'top_admins', 'top_inviters', 'users')
    def __init__(self, period: 'StatsDateRangeDays', members: 'StatsAbsValueAndPrev', messages: 'StatsAbsValueAndPrev', viewers: 'StatsAbsValueAndPrev', posters: 'StatsAbsValueAndPrev', growth_graph: 'StatsGraph', members_graph: 'StatsGraph', new_members_by_source_graph: 'StatsGraph', languages_graph: 'StatsGraph', messages_graph: 'StatsGraph', actions_graph: 'StatsGraph', top_hours_graph: 'StatsGraph', weekdays_graph: 'StatsGraph', top_posters: 'Vector', top_admins: 'Vector', top_inviters: 'Vector', users: 'Vector'):
        self.period = period
        self.members = members
        self.messages = messages
        self.viewers = viewers
        self.posters = posters
        self.growth_graph = growth_graph
        self.members_graph = members_graph
        self.new_members_by_source_graph = new_members_by_source_graph
        self.languages_graph = languages_graph
        self.messages_graph = messages_graph
        self.actions_graph = actions_graph
        self.top_hours_graph = top_hours_graph
        self.weekdays_graph = weekdays_graph
        self.top_posters = top_posters
        self.top_admins = top_admins
        self.top_inviters = top_inviters
        self.users = users
    def to_dict(self):
        return {"period": self.period, "members": self.members, "messages": self.messages, "viewers": self.viewers, "posters": self.posters, "growth_graph": self.growth_graph, "members_graph": self.members_graph, "new_members_by_source_graph": self.new_members_by_source_graph, "languages_graph": self.languages_graph, "messages_graph": self.messages_graph, "actions_graph": self.actions_graph, "top_hours_graph": self.top_hours_graph, "weekdays_graph": self.weekdays_graph, "top_posters": self.top_posters, "top_admins": self.top_admins, "top_inviters": self.top_inviters, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(4018141462, signed=False)
        writer.write(bytes(self.period))
        writer.write(bytes(self.members))
        writer.write(bytes(self.messages))
        writer.write(bytes(self.viewers))
        writer.write(bytes(self.posters))
        writer.write(bytes(self.growth_graph))
        writer.write(bytes(self.members_graph))
        writer.write(bytes(self.new_members_by_source_graph))
        writer.write(bytes(self.languages_graph))
        writer.write(bytes(self.messages_graph))
        writer.write(bytes(self.actions_graph))
        writer.write(bytes(self.top_hours_graph))
        writer.write(bytes(self.weekdays_graph))
        writer.write(bytes(self.top_posters))
        writer.write(bytes(self.top_admins))
        writer.write(bytes(self.top_inviters))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        period = reader.tgread_object()
        members = reader.tgread_object()
        messages = reader.tgread_object()
        viewers = reader.tgread_object()
        posters = reader.tgread_object()
        growth_graph = reader.tgread_object()
        members_graph = reader.tgread_object()
        new_members_by_source_graph = reader.tgread_object()
        languages_graph = reader.tgread_object()
        messages_graph = reader.tgread_object()
        actions_graph = reader.tgread_object()
        top_hours_graph = reader.tgread_object()
        weekdays_graph = reader.tgread_object()
        top_posters = reader.tgread_object()
        top_admins = reader.tgread_object()
        top_inviters = reader.tgread_object()
        users = reader.tgread_object()
        return cls(period, members, messages, viewers, posters, growth_graph, members_graph, new_members_by_source_graph, languages_graph, messages_graph, actions_graph, top_hours_graph, weekdays_graph, top_posters, top_admins, top_inviters, users)

@register
class StatsMessageStats(TLObject):
    CONSTRUCTOR_ID = 2145983508
    __slots__ = ('views_graph', 'reactions_by_emotion_graph')
    def __init__(self, views_graph: 'StatsGraph', reactions_by_emotion_graph: 'StatsGraph'):
        self.views_graph = views_graph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph
    def to_dict(self):
        return {"views_graph": self.views_graph, "reactions_by_emotion_graph": self.reactions_by_emotion_graph}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2145983508, signed=False)
        writer.write(bytes(self.views_graph))
        writer.write(bytes(self.reactions_by_emotion_graph))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        views_graph = reader.tgread_object()
        reactions_by_emotion_graph = reader.tgread_object()
        return cls(views_graph, reactions_by_emotion_graph)

@register
class StatsStoryStats(TLObject):
    CONSTRUCTOR_ID = 1355613820
    __slots__ = ('views_graph', 'reactions_by_emotion_graph')
    def __init__(self, views_graph: 'StatsGraph', reactions_by_emotion_graph: 'StatsGraph'):
        self.views_graph = views_graph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph
    def to_dict(self):
        return {"views_graph": self.views_graph, "reactions_by_emotion_graph": self.reactions_by_emotion_graph}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(1355613820, signed=False)
        writer.write(bytes(self.views_graph))
        writer.write(bytes(self.reactions_by_emotion_graph))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        views_graph = reader.tgread_object()
        reactions_by_emotion_graph = reader.tgread_object()
        return cls(views_graph, reactions_by_emotion_graph)

@register
class StatsPublicForwards(TLObject):
    CONSTRUCTOR_ID = 2466479648
    __slots__ = ('count', 'forwards', 'next_offset', 'chats', 'users')
    def __init__(self, count: int, forwards: 'Vector', chats: 'Vector', users: 'Vector', next_offset: str = None):
        self.count = count
        self.forwards = forwards
        self.next_offset = next_offset
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {"count": self.count, "forwards": self.forwards, "next_offset": self.next_offset, "chats": self.chats, "users": self.users}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(2466479648, signed=False)
        flags = 0
        if self.next_offset is not None: flags |= 1 << 0
        writer.write_int(flags, signed=False)
        writer.write_int(self.count, signed=True)
        writer.write(bytes(self.forwards))
        if flags & (1 << 0):
            writer.write_string(self.next_offset)
        writer.write(bytes(self.chats))
        writer.write(bytes(self.users))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int(signed=False)
        count = reader.read_int()
        forwards = reader.tgread_object()
        if flags & (1 << 0):
            next_offset = reader.read_string()
        else:
            next_offset = None
        chats = reader.tgread_object()
        users = reader.tgread_object()
        return cls(count, forwards, next_offset, chats, users)

@register
class StatsPollStats(TLObject):
    CONSTRUCTOR_ID = 697941741
    __slots__ = ('votes_graph')
    def __init__(self, votes_graph: 'StatsGraph'):
        self.votes_graph = votes_graph
    def to_dict(self):
        return {"votes_graph": self.votes_graph}
    def _bytes(self):
        writer = BinaryWriter()
        writer.write_int(697941741, signed=False)
        writer.write(bytes(self.votes_graph))
        return writer.get_bytes()
    @classmethod
    def from_reader(cls, reader):
        votes_graph = reader.tgread_object()
        return cls(votes_graph)

