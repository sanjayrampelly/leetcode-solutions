class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        updatedarrivaltime=arrivalTime+delayedTime

        if (updatedarrivaltime<24):
            return updatedarrivaltime
        else:
            return updatedarrivaltime%24