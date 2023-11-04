"""Not all Python objects can, in principle,
 be serialized. For example, you cannot serialize
 a file descriptor or any system resource.
  But what do you do when you have a class whose
   object you want to package using pickle,
    but it has non-serializable attributes?
     In such a situation, you can use magic methods
      that control serialization and deserialization
       using pickle."""


"""The __getstate__ magic method is called when pickle
 tries to get the byte string representation of an object.
  In a typical implementation, __getstate__ returns a
   __dict__ dictionary that stores all the attributes of 
   the class. But you can change this method."""

import pickle


class Reader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['fh'] = None
        return attributes


# Example usage to open and read from a serialized Reader
file_path = 'example.txt'

# Create a Reader object
reader = Reader(file_path)

# Read data from the file:
data = reader.read(5)
print(f'Read data: {data}')


# Close the file
reader.close()

# ========================================

