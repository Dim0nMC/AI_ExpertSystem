class Query:

    def __init__(self, options=["y", "n"]):
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


class Criterion:

    def __init__(self, value):
        self.value = value


class Condition(Criterion):
    pass


class All(Criterion):
    pass


class Any(Criterion):
    pass


criteria = {
    "default": Query(["y", "n"]),
    "Genre": Query(
        ["pop", "rock", "electronic", "rap", "children", "Trap", "Hip-Hop", "Lo-fi"]
    ),
    "Country": Query(["Russia", "USA", "UK", "Germany", "Japan"]),
    "Period": Query(["80s", "90s", "2000s", "2010s"]),
    "Tempo": Query(["fast", "slow"]),
    "Vocal": Query(["yes", "no"]),
    "Mood": Query(["sad", "happy", "tense", "thoughtful", "focused"]),
    "Russian Rock": Condition(All(["Genre:rock", "Country:Russia"])),
    "For Relaxation": Condition(
        All([Any(["Genre:Lo-fi", "Mood:thoughtful"]), "Tempo:slow"])
    ),
    "For Workout": Condition(Any(["Mood:happy", "Mood:thoughtful", "Tempo:fast"])),
    "Party": Condition(All(["Tempo:fast", Any(["Vocal:yes", "Mood:happy"])])),
    "For Study": Condition(Any(["Tempo:slow", "Vocal:no", "Mood:focused"])),
    "Children's Party": Condition(
        All(["Genre:children", Any(["Mood:happy", "Tempo:fast"])])
    ),
    "In Car": Condition(
        All(
            [
                Any(["Mood:happy", "Mood:sad"]),
                Any(["Genre:pop", "Genre:rap", "Genre:electronic", "Genre:rock"]),
            ]
        )
    ),
    "Dance": Condition(
        All(["Mood:happy", Any(["Genre:pop", "Genre:rock", "Genre:electronic"])])
    ),
    "Track:Искала": Condition(All(["Russian Rock", "Period:2000s", "Tempo:fast"])),
    "Track:Superman": Condition(
        All(["Genre:pop", "Country:USA", "Period:2010s", "Tempo:slow"])
    ),
    "Track:Do or Die": Condition(
        All(["Genre:rap", "Country:UK", "Period:90s", "Tempo:fast"])
    ),
    "Track:Blue Monday": Condition(
        All(["Genre:electronic", "Country:Germany", "Period:80s", "Tempo:slow"])
    ),
    "Track:Oblivion": Condition(
        All(
            [
                "Genre:Hip-Hop",
                "Genre:rap",
                "Country:USA",
                "Period:2010s",
                "Tempo:slow",
                "Mood:sad",
            ]
        )
    ),
    "Track:Etoile et toi": Condition(
        All(
            [
                "Genre:pop",
                "Country:Japan",
                "Period:2010s",
                "Tempo:slow",
                "Mood:thoughtful",
            ]
        )
    ),
    "Track:Busy signals": Condition(
        All(
            [
                Any(["Genre:Hip-Hop", "Genre:rap"]),
                "Country:USA",
                "Period:2010s",
                "Tempo:fast",
                "Mood:happy",
                "Vocal:no",
            ]
        )
    ),
    "Track:April showers": Condition(
        All(
            [
                "Genre:Hip-Hop",
                "Country:USA",
                "Period:2010s",
                "Tempo:fast",
                "Mood:happy",
                "Vocal:yes",
            ]
        )
    ),
    "Track:I'm ready": Condition(
        All(
            [
                "Genre:pop",
                "Country:USA",
                "Period:2010s",
                "Tempo:fast",
                "Mood:happy",
                "Vocal:yes",
            ]
        )
    ),
    "Track:Crimewave": Condition(
        All(
            [
                "Genre:electronic",
                "Country:USA",
                "Period:2000s",
                "Tempo:fast",
                "Mood:happy",
                "Vocal:yes",
            ]
        )
    ),
    "Track:Brother Louie": Condition(
        All(["Genre:pop", "Country:Germany", "Period:90s", "Tempo:fast", "Disco"])
    ),
        'Track:Ветер':
    Condition(
        All([
            'Genre:rock', 'Country:Russia', 'Period:2000s', 'Tempo:slow',
            'Mood:thoughtful'
        ])),
    'Track:Я сошла с ума':
    Condition(
        All([
            'Genre:pop', 'Country:Russia', 'Period:2000s', 'Tempo:fast',
            'Mood:sad', 'Mood:thoughtful'
        ])),
    'Track:I Wonder':
    Condition(
        All([
            'Genre:electronic', 'Country:USA', 'Period:2000s', 'Tempo:fast',
            'Mood:happy'
        ])),
    'Track:Rap God':
    Condition(All(['Genre:Rap', 'Country:USA', 'Period:2010s', 'Tempo:fast'])),
    'Track:Lost Angeles':
    Condition(
        All([
            'Genre:Trap', 'Genre:Hip-Hop', 'Country:Russia', 'Period:2020s',
            'Tempo:fast'
        ])),
    'Track:The Show Must Go On':
    Condition(
        All([
            'Genre:rock', 'Country:UK', 'Period:90s',
            'Tempo:slow', 'Mood:tense'
        ])),
    'Track:U Cant Touch This':
    Condition(
        All([
            Any(['Genre:pop', 'Genre:rap']), 'Country:USA', 'Period:90s',
            'Tempo:fast', 'Mood:happy'
        ])),
    'Track:Акид':
    Condition(
        All([
            'Genre:rap', 'Country:Russia', 'Period:2010s', 'Tempo:fast',
            'For Workout'
        ])),
    'Track:В одного':
    Condition(
        All([
            'Genre:rap', 'Country:Russia', 'Period:2010s', 'Tempo:fast',
            'Party'
        ])),
    'Track:London Bridge':
    Condition(All(['Genre:pop', 'Country:USA', 'Period:2000s', 'Party'])),
    'Track:Junkie':
    Condition(All(['Genre:rap', 'Country:USA', 'Period:2010s', 'For Workout']))
}


class KnowledgeBase:

    def __init__(self, criteria):
        self.criteria = criteria
        self.memory = {}

    def get(self, name):
        if name in self.memory.keys():
            return self.memory[name]
        for key in self.criteria.keys():
            if key == name or key.startswith(name + ":"):
                value = "y" if key == name else key.split(":")[1]
                result = self.evaluate(self.criteria[key], field=name)
                if result == "y":
                    self.memory[name] = value
                    return value
        result = self.evaluate(self.criteria["default"], field=name)
        self.memory[name] = result
        return result

    def evaluate(self, expression, field=None):
        if isinstance(expression, Query):
            print(field)
            return expression.prompt()
        elif isinstance(expression, Condition):
            return self.evaluate(expression.value)
        elif isinstance(expression, All) or isinstance(expression, list):
            expression = expression.value if isinstance(expression, All) else expression
            for item in expression:
                if self.evaluate(item) == "n":
                    return "n"
            return "y"
        elif isinstance(expression, Any):
            for item in expression.value:
                if self.evaluate(item) == "y":
                    return "y"
            return "n"
        elif isinstance(expression, str):
            return self.get(expression)
        else:
            print("Unknown expression: {}".format(expression))

kb = KnowledgeBase(criteria)

kb.get("Track")
print(kb.memory["Track"])
