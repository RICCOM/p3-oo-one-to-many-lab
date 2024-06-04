class Pet:
   PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
   all = []
   def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        
        if owner is not None:
            if isinstance(owner, Owner):
                self.owner = owner
            else:
                raise Exception("The owner must be an instance of the Owner class.")
        else:
            self.owner = None
        
        Pet.all.append(self)



class Owner:
    def __init__(self, name):
        self.name = name

    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]   
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("The pet must be an instance of the Pet class.") 
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)    