from collections import defaultdict, deque
from typing import Dict, Deque, Tuple

class Twitter:
    def __init__(self,per_user_cap = 1000):
        self._time = 0
        self.tweets: Dict[int, Deque[Tuple[int, int]]] = defaultdict(deque)
        self.followees: Dict[int, set] = defaultdict(set)
        self.PER_USER_TWEET_CAP = per_user_cap

    def postTweet(self, userId : int, tweetId: int):
        if userId not in self.followees:
            self.followees[userId].add(userId)
        
        self._time += 1
        self.tweets[userId].appendleft((self._time,tweetId))

        if len(self.tweets[userId]) > self.PER_USER_TWEET_CAP:
            self.tweets[userId].pop()

    def follow(self, followerId : int, followeeId : int):
        if followeeId not in self.followees:
            self.followees[followerId].add(followerId)
        self.followees[followeeId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int):
        if followerId == followeeId:
            return  
        if followerId in self.followees:
            self.followees[followerId].discard(followeeId)


t = Twitter(per_user_cap=5)

t.postTweet(1,101)
t.postTweet(1,102)

t.postTweet(2,201)

t.follow(1,2)
t.follow(2,1)

print("Follow graph after follow actions:", {u: sorted(list(s)) for u, s in t.followees.items()})

# Unfollow
t.unfollow(1, 2)  # user 1 unfollows user 2
print("Follow graph after unfollow:", {u: sorted(list(s)) for u, s in t.followees.items()})

print("User 1 tweets (newest first):", list(t.tweets[1]))
print("User 2 tweets (newest first):", list(t.tweets[2]))
