'''
Hashmap with Separate Chaining

execution instructions:
under ./Q4/source_code/ directory
> python hashmap.py <file_name>
example:
python hashmap.py hw2q4.txt

Notes on input data:
This implementation/driver code best works with .txt files where each line contains a 'Key:Value' pair formatted exactly like that with no spaces in between.
Depending on the datatype of the key and the value, please typecast properly (in line 84 of the driver code)before 'put'ting it in the hashmap. For example 
in my case, we have a text file named hw2q4.txt which contains '<city>:<population>' pair in each line. So when calling the put() function I typecasted the 
key to be a string and the value to be an integer. Since my hashFucntion() utlizes the Python inbuilt hash(), each data type passed into the hashFunction() 
gets converted into an integer before the mod operation is applied. Also as always, make sure to put all the input data into the data folder, if my driver
code is being used for testing purposes.
'''

from sys import argv

#size of hashmap
HASHMAP_SIZE = 500000

class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for num in range(self.size)]

    def hashFunction(self, key):
        return hash(key) % self.size

    # put function
    def put(self, key, value):
        # calculate hash value
        hashIndex = self.hashFunction(key)
        # find the bucket
        bucket = self.table[hashIndex]
        # search for duplicate in the bucket and if found update value
        for bucketIndex, entry in enumerate(bucket):
            if entry[0] == key:
                bucket[bucketIndex] = (key, value)
                return
        # otherwise append to bucket
        bucket.append((key, value))

    def get(self, key):
        index = self.hashFunction(key)
        bucket = self.table[index]
        # search for the key in the bucket and return corresponding value if found
        for bucketIndex, entry in enumerate(bucket):
            if entry[0] == key:
                return entry[1]
        # else return -1
        return -1

    def delete(self, key):
        index = self.hashFunction(key)
        bucket = self.table[index]
        # search for the key in the bucket and if found, pop() (key,value) tuple
        for bucketIndex, entry in enumerate(bucket):
            if entry[0] == key:
                bucket.pop(bucketIndex)
                return
        # else print the following
        print("No such entries found")

    def __str__(self):
        # print table bucket by bucket
        return "".join(str(entry) for entry in self.table)

def main():
    table = HashMap(HASHMAP_SIZE)
    # reading data into data[] list as 2 element lists
    if len(argv)<2:
        print ("***ERROR : Please input file name along in cmd line***")
        exit()
    f = open("../data/"+argv[1], 'r')
    lines = f.readlines()
    data = [(line.strip()).split(':') for line in lines]

    for tuple in data:
        # *************************************
        # CHANGE KEY AND VALUE TYPECASTING HERE
        # *************************************
        table.put(str(tuple[0]), int(tuple[1]))
    
    # print(table.get('Chicago'))
    # table.delete('Chicago')
    # print(table.get('Chicago'))

if __name__ == '__main__':
    main()