# Defining all the necessary classes of the project

#import

# First of all defining Classes of the UML Data Model
class IdentifiableEntity(object):
    def __init__(self, id):
        self.id = id

    def getId(self):
        return self.id

# The cultural Heritage Object class definition
class CulturalHeritageObject(IdentifiableEntity):
    def __init__(self, title, owner, date, place):
        self.title = title
        self.owner = owner
        self.date = date
        self.place = place

    def getTitle(self):
        return self.title


# Defining 10 types of Cultural Heritage Objects classes
class Map(CulturalHeritageObject):
    pass

class Model(CulturalHeritageObject):
    pass

class Painting(CulturalHeritageObject):
    pass

class Specimen(CulturalHeritageObject):
    pass

class Herbarium(CulturalHeritageObject):
    pass

class PrintedMaterial(CulturalHeritageObject):
    pass

class PrintedVolume(CulturalHeritageObject):
    pass

class ManuscriptVolume(CulturalHeritageObject):
    pass

class ManuscriptPlate(CulturalHeritageObject):
    pass

class NauticalChart(CulturalHeritageObject):
    pass


class Person(IdentifiableEntity):
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name

class Activity(object):
    def __init__(self, institute, person, tool, start, end, refersTo):
        self.institute = institute
        self.person = person
        self.tool = tool
        self.start = start
        self.end = end
        self.refersTo = refersTo

    def getResponsibleInstitute(self):
        return self.institute

    def getResponsiblePerson(self):
        return self.person

    def getTools(self):
        return self.tool

    def getStartDate(self):
        return self.start

    def getEndDate(self):
        return self.end

    def refersTo(self):
        return self.refersTo

class Acquisition(Activity):
    def __init__(self,technique):
        self.technique = technique

    def getTechnique(self):
        return self.technique

class Processing(Activity):
    pass

class Modelling(Activity):
    pass

class Optimising(Activity):
    pass

class Exporting(Activity):
    pass





