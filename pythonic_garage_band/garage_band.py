from abc import ABC, abstractmethod


class Band:

    instance_of_a_class = []

    def __init__(self, name, members = None):
        self.name = name
        self.members = members
        Band.instance_of_a_class.append(self)
        print(self.instance_of_a_class)

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}: This is not the last day."

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}: You rock."

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instance_of_a_class

    @staticmethod
    def create_from_data(data):
        """this method allows file format inputting members as musician objects such as:
        BandData = {"Band Name": "Volcano",
            "Members": [Guitarist("Tom"), Drummer("Robert"), Bassist("Riley")]}
         or inputting a dictionary with name and instrument to create the musician objects, such as:
        [{"Band Name": "Volcano",
          "Members": [{"Name": "Tom", "Instrument": "guitar"},
                      {"Name": "Robert", "Instrument": "drums"},
                      {"Name": "Riley", "Instrument": "bass"}]}]
        """

        members_list = data["Members"]
        if len(members_list) > 0:
            for i, member in enumerate(members_list):
                if member is dict:
                    if member["Instrument"] == "guitar":
                        members_list[i] = Guitarist(member["Name"], member["Instrument"])
                    elif member["Instrument"] == "drums":
                        members_list[i] = Drummer(member["Name"], member["Instrument"])
                    elif member["Instrument"] == "bass":
                        members_list[i] = Bassist(member["Name"], member["Instrument"])

        return Band(data["Band Name"], members_list)


class Musician(ABC):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    @abstractmethod
    def play_solo(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    def __init__(self, name, solo = "face melting guitar wailing"):
        super().__init__(name, "guitar")
        self.solo = solo

    def play_solo(self):
        return self.solo

    def __str__(self):
        return self.__class__.__name__ + " " + self.name

    def __repr__(self):
        return "This is " + self.__class__.__name__ + " " + self.name


class Bassist(Musician):
    def __init__(self, name, solo = "thump, thump"):
        super().__init__(name, "bass")
        self.solo = solo

    def play_solo(self):
        return self.solo

    def __str__(self):
        return self.__class__.__name__ + " " + self.name

    def __repr__(self):
        return "This is " + self.__class__.__name__ + " " + self.name


class Drummer(Musician):
    def __init__(self, name, solo = "boom boom"):
        super().__init__(name, "drums")
        self.solo = solo

    def play_solo(self):
        return self.solo

    def __str__(self):
        return self.__class__.__name__ + " " + self.name

    def __repr__(self):
        return "This is " + self.__class__.__name__ + " " + self.name


    if __name__ == "__main__":
        band = Band("Proud")
        assert band.name == "Proud"
        assert band.members == None
        assert len(Band.to_list()) == 1


