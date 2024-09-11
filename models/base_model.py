import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance or recreate one from a dictionary"""
        if kwargs:
            # Recreate an instance from a dictionary
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert string to datetime object
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    # Assign other attributes normally
                    setattr(self, key, value)
        else:
            # Create a new instance with new id and current datetime
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the `updated_at` with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance's __dict__"""
        obj_dict = self.__dict__.copy()  # Get a copy of the instance's __dict__
        obj_dict['__class__'] = self.__class__.__name__  # Add the class name
        obj_dict['created_at'] = self.created_at.isoformat()  # Convert created_at to ISO format string
        obj_dict['updated_at'] = self.updated_at.isoformat()  # Convert updated_at to ISO format string
        return obj_dict

