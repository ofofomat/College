id = 0


class Task:

    def __init__(self, description='', done=False) -> None:
        global id
        id = id + 1
        self.id = id
        self.description = description
        self.done = done

    def get_id(self):
        return self.id

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_done(self):
        if not self.done:
            self.done = not self.done

    def get_done(self):
        return self.done
