import objects

class ObjectHolder(dict):
  def __init__(self, *args, **kwargs):
    dict.__init__(self, *args, **kwargs)
    self.players = []
    self.checkers = []

  def __setitem__(self, key, value):
    if key in self:
      self.__delitem__(key)
    dict.__setitem__(self, key, value)
    if isinstance(value, objects.Player):
      self.players.append(value)
    if isinstance(value, objects.Checker):
      self.checkers.append(value)

  def __delitem__(self, key):
    value = self[key]
    dict.__delitem__(self, key)
    if value in self.players:
      self.players.remove(value)
    if value in self.checkers:
      self.checkers.remove(value)

  def clear(self):
    for i in self.keys():
      del self[i]
