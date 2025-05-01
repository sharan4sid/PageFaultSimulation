class PageReplacementSimulator:
    def __init__(self, frames, reference_string):
        self.frames = frames
        self.reference_string = list(map(int, reference_string))  
    def fifo(self):
        frame_queue = []
        page_faults = 0
        for page in self.reference_string:
            if page not in frame_queue:
                if len(frame_queue) < self.frames:
                    frame_queue.append(page)
                else:
                    frame_queue.pop(0)
                    frame_queue.append(page)
                page_faults += 1
        return page_faults

    def lru(self):
        frames = []
        page_faults = 0
        last_used = {}  

        for idx, page in enumerate(self.reference_string):
            last_used[page] = idx  
            if page not in frames:
                page_faults += 1
                if len(frames) >= self.frames:
                    
                    lru_page = min(frames, key=lambda x: last_used[x])
                    frames.remove(lru_page)
                frames.append(page)
        return page_faults

    def optimal(self):
        """Optimized Optimal algorithm implementation"""
        memory = []
        page_faults = 0
        for idx, page in enumerate(self.reference_string):
            if page not in memory:
                page_faults += 1
                if len(memory) < self.frames:
                    memory.append(page)
                else:
                    future_indices = {}
                    for frame in memory:
                        try:
                            future_indices[frame] = self.reference_string[idx+1:].index(frame)
                        except ValueError:
                            future_indices[frame] = float('inf')
                    to_remove = max(memory, key=lambda x: future_indices[x])
                    memory.remove(to_remove)
                    memory.append(page)
        return page_faults