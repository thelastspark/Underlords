class Item:
    def __init__(self, name, coords, image=None, ID=None, melee=False, ranged=False, preventMana=False, localID=-1,
                 legacyID=-1):
        self.name = name
        self.coords = coords
        self.image = image  # maybe at somepoint in the future - not now tho >.>
        self.hero = None
        self.ID = ID
        self.melee = melee
        self.ranged = ranged
        self.preventMana = preventMana
        self.localID = localID
        self.legacyID = legacyID