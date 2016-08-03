import pickle

# the input function:
def pickleinput():
    print("Let's pickle a list of stuff we like.")
    # we'll use a try except loop to catch input errors like failing to use an integer to rate items:
    try:
        # our variables are lists that are constructed from user data:
        movie = [str(input("What's your favorite movie? ")), int(input("Rating (1-10): "))]
        band = [str(input("What's your favorite band? ")), int(input("Rating (1-10): "))]
        book = [str(input("What's your favorite book? ")), int(input("Rating (1-10): "))]
        # opening the data file in write-binary mode:
        writedatastream = open("stuffwelike.dat", "wb")
        # user feedback to provide reassurance that the data are being written:
        print("\nPickling your lists to stuffwelike.dat...")
        # writing the data using dump:
        pickle.dump(movie, writedatastream)
        pickle.dump(band, writedatastream)
        pickle.dump(book, writedatastream)
        # closing the file:
        writedatastream.close()
    # a simple exception rule that will show the Python error:
    except Exception as e:
        print("Oh, dear. I'm terribly sorry, but the following error occurred: \n", e.__str__())

# the output function
def pickleoutput():
    print("\nUnpickling lists...")
    # opening the data file in read-binary mode:
    readdatastream = open("stuffwelike.dat", "rb")
    try:
        # reading the data using load:
        readmovie = pickle.load(readdatastream)
        readband = pickle.load(readdatastream)
        readbook = pickle.load(readdatastream)
        # printing the lists:
        print(readmovie)
        print(readband)
        print(readbook)
    # again, a simple exception rule that will show the Python error:
    except Exception as e:
        print("Oh, dear. I'm terribly sorry, but the following error occurred: \n", e.__str__())
        input("Press the 'enter' key to exit. ")
    # closing the file:
    readdatastream.close()

# calling the functions
pickleinput()
pickleoutput()
input("Pickling and unpickling complete. Press the 'enter' key to exit. ")