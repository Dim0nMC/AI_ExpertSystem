class Query():

  def __init__(self, options=['y', 'n']):
    self.options = options

  def prompt(self):
    if max([len(option) for option in self.options]) > 1:
      for index, option in enumerate(self.options):
        print("{0}. {1}".format(index, option))
      choice = int(input())
      return self.options[choice]
    else:
      print("/".join(self.options))
      return input()


class Criterion():

  def __init__(self, value):
    self.value = value


class Condition(Criterion):
  pass


class All(Criterion):
  pass


class Any(Criterion):
  pass


criteria = {
    'default':
    Query(['y', 'n']),
    'Genre':
    Query([
        'pop', 'rock', 'electronic', 'rap', 'children', 'Trap', 'Hip-Hop',
        'Lo-fi'
    ]),
    'Country':
    Query(['Russia', 'USA', 'UK', 'Germany', 'Japan']),
    'Period':
    Query(['80s', '90s', '2000s', '2010s']),
    'Tempo':
    Query(['fast', 'slow']),
    'Vocal':
    Query(['yes', 'no']),
    'Mood':
    Query([
        'sad', 'happy', 'tense', 'thoughtful', 'focused'
    ]),
    'Russian Rock':
    Condition(All(['Genre:rock', 'Country:Russia'])),
    'For Relaxation':
    Condition(All([Any(['Genre:Lo-fi', 'Mood:thoughtful']), 'Tempo:slow'])),
    'For Workout':
    Condition(Any(['Mood:happy', 'Mood:thoughtful', 'Tempo:fast'])),
    'Party':
    Condition(All(['Tempo:fast',
            Any(['Vocal:yes', 'Mood:happy'])])),
    'For Study':
    Condition(Any(['Tempo:slow', 'Vocal:no', 'Mood:focused'])),
    'Children\'s Party':
    Condition(All(['Genre:children',
            Any(['Mood:happy', 'Tempo:fast'])])),
    'In Car':
    Condition(
        All([
            Any(['Mood:happy', 'Mood:sad']),
            Any(['Genre:pop', 'Genre:rap', 'Genre:electronic', 'Genre:rock'])
        ])),
    'Dance':
    Condition(
        All([
            'Mood:happy',
            Any(['Genre:pop', 'Genre:rock', 'Genre:electronic'])
        ])),
    'Track:Искала':
    Condition(All(['Russian Rock', 'Period:2000s', 'Tempo:fast'])),
    'Track:Superman':
    Condition(All(['Genre:pop', 'Country:USA', 'Period:2010s', 'Tempo:slow'])),
    'Track:Do or Die':
    Condition(All(['Genre:rap', 'Country:UK', 'Period:90s',
            'Tempo:fast'])),

}


kb = KnowledgeBase(criteria)

kb.get('Track')
print(kb.memory['Track'])
