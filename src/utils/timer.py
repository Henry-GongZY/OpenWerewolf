import time

class Timer:
    """
    A simple Timer class to measure elapsed time.
    Now, This class is a countdown timer.
    """

    def __init__(self, duration: int):
        """
        Initializes the Timer with a duration.

        Args:
            duration (int): The duration of the timer in seconds.
        """
        self.start_time = None
        self.duration = duration
        self.end_time = None

    def start(self):
        """
        Starts the countdown timer.
        """
        self.start_time = time.time()
        self.end_time = self.start_time + self.duration

    def get_remaining_time(self) -> float:
        """
        Returns the remaining time in seconds.

        Returns:
            float: The remaining time in seconds, or 0 if the timer has finished.
        """
        if self.start_time is None:
            return self.duration
        
        remaining_time = self.end_time - time.time()
        return max(0, remaining_time)

    def is_finished(self) -> bool:
        """
        Checks if the timer has finished.

        Returns: 
            bool: True if the timer has finished, False otherwise.
        """
        return self.get_remaining_time() == 0