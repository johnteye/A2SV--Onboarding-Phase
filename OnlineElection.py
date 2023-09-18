
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        count = Counter()
        leader = -1
        for i, person in enumerate(persons):
            count[person] += 1
            if count[person] >= count[leader]:
                leader = person
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        index = bisect_right(self.times, t)
        return self.leaders[index - 1]
      
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
