
import threading
from mythread import MyThread
import time

class MainThread(threading.Thread):
    def __init__(self,settings):
        super().__init__()
        self.settings       = settings 
        self.stopped        = False
        # Initialize count values to zero
        self.activeThread   = 0
        self.played         = 0
        self.followed       = 0
        self.favorited      = 0
        self.highlighted    = 0
        self.reuped         = 0

        # Threads list
        self.threadList     = []

    # Start Threads
    def run(self):

        # start first thread
        thread = MyThread(self.settings)
        thread.start()

        self.threadList.append(thread)
        self.currentThread = thread

        while True:
            # remove not working thread from thread list
            for i in range(len(self.threadList)):
                if not self.threadList[i].is_working:
                    self.threadList.remove(i)
                    self.activeThread = self.activeThread - 1
            
            # set active thread count
            self.activeThread = len(self.threadList)

            # if active thread count is less than max thread count and current thread signed,not main thread stopped, then start new thread
            if(self.activeThread < self.settings['MAX_ACTIVE_THREAD']) and (self.currentThread.is_signed) and not self.stopped:
                thread = MyThread(self.settings)
                thread.start()
                self.threadList.append(thread)
                self.activeThread = self.activeThread + 1

                self.currentThread = thread

            # wait for one second
            time.sleep(1)

    # Stop All Running Threads
    def stop(self):
        self.stopped = True
        for i in range(len(self.threadList)):
            self.threadList[i].stop()
