"""This magic method receives as
input a dictionary unpacked from a file or
byte string. The default behavior is to write
the resulting value to self.__dict__.
Let's modify the Reader class so that after
unpacking it can continue reading from the same
 place."""

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
        attributes = {**self.__dict__}
        attributes['fh'] = None
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])


# Create an instance of the Reader class and open a file:
file_path = 'example.txt'
reader = Reader(file_path)

# Read data from the file
data = reader.read(5)
print(f'Read data: {data}')  # Read data: Hello

# Serialize the reader object to a file using pickle
with open('reader.pkl', 'wb') as file:
    pickle.dump(reader, file)

# Close the original reader object
reader.close()

# Deserialize the reader object from the pickle file
with open('reader.pkl', 'rb') as file:
    deserialized_reader = pickle.load(file)

# Attempt to read data from the deserialized Reader object
data = deserialized_reader.read(25)
print(f'Read data from deserialized Reader: {data}') # Read data from deserialized Reader:  my loved Python

# Close the deserialized reader object
deserialized_reader.close()

