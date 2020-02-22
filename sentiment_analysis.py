# Name: Huda Mukhtar
# User ID: hmukhta
# Description: This module contains the functions necessary to calculate the sentiment values of each tweet and the
# average happiness for each region

# This function will calculate the sentiment of the tweet
def compute_tweets(tweet_File, key_file):

    # Create lists to separate the keywords from the sentiment values and one for the tweets
    keyWords = []
    sentimentValues = []

    # Initialize the happiness scores and tweet counts for each region
    countEast = 0
    happyE = 0
    countCentral = 0
    happyC = 0
    countMtn = 0
    happyM = 0
    countPacific = 0
    happyP = 0

    # Separate data in the file with the key words
    try:

        # Open the file with the key words
        keyFile = open(key_file, encoding='utf‐8', errors='ignore')

        # For processing the data, we separate the key words and their sentiment values
        for line in keyFile:
            values = line.split(",")
            # Add to the list of keywords and sentiment values respectively
            keyWords.append(values[0])
            sentimentValues.append(values[1])

        # Close the file after use
        keyFile.close()

    # Print error message when the file does not exist or is not found
    except IOError:
        print("Error: file not found.")

    # Separate data in the file with the tweets and process them
    try:

        # Open the file with the tweets
        tweets = open(tweet_File, encoding='utf‐8', errors='ignore')

        # For processing the data, we separate the tweet from the other information in the line
        for line in tweets:

            # Initialize the number of key words in a tweet and the total sentiment value
            sentiment_total = 0
            num_key = 0

            # Separate the values in the line
            values = line.split(" ")

            # Separate the data by its longitude, latitude
            # after removing square brackets and comma
            latitude, longitude = removeBracket(values[0], values[1])

            # Find the region that the tweet came from
            region = findRegion(float(latitude), float(longitude))

            # Remove unnecessary values from the tweet
            for index in range(5):
                values.pop(0)

            # Go through every word of the tweet
            for wrd in range(len(values)):

                # Remove any existing punctuation from each word
                # after lower-casing it
                word = puncRemove(values[wrd].lower())

                # Remove code from the last word of the tweet
                if wrd == (len(values)-1):
                    word = word.rstrip("\n")

                # Get the sentiment value
                sentimentVal = tweetChecker(word, keyWords, sentimentValues)

                # For every key word, add to the number of key words in the tweet
                # and add the sentiment value to the total sentiment value
                if sentimentVal != 0:
                    num_key += 1
                    sentiment_total += sentimentVal

            # Calculate the happiness score of the tweet if there were any key words
            if num_key != 0:

                happy = sentiment_total / num_key

                # Add a counted tweet and its happiness score for its region
                if region == "Eastern":
                    countEast += 1
                    happyE += happy
                elif region == "Central":
                    countCentral += 1
                    happyC += happy
                elif region == "Mountain":
                    countMtn += 1
                    happyM += happy
                elif region == "Pacific":
                    countPacific += 1
                    happyP += happy

        # Close the file after use
        tweets.close()

        # Calculate the average happiness of the region
        avgEast = avgRegion(happyE, countEast)
        avgCentral = avgRegion(happyC, countCentral)
        avgMtn = avgRegion(happyM, countMtn)
        avgPacific = avgRegion(happyP, countPacific)

        # Create a tuple for the average and counted tweet of each region
        east = (avgEast, countEast)
        central = (avgCentral, countCentral)
        mountain = (avgMtn, countMtn)
        pacific = (avgPacific, countPacific)

    # Print error message when the file does not exist or is not found
    except IOError:
        return []

    # return the tuples of each region's values
    return [east, central, mountain, pacific]


def removeBracket(latitude, longitude):
    # Remove square brackets and comma from the point
    # of the region of the tweet
    latitude = latitude.lstrip("[")
    latitude = latitude.rstrip(",")
    longitude = longitude.rstrip("]")
    # Return the updated values
    return latitude, longitude


# Remove the punctuation in a word
def puncRemove(word):

    # Define punctuation
    punctuation = '''!()$%^&'"\,<-@#>./[]{}?*_~;:'''

    # Check if the word has punctuation
    # Return the punctuation
    for char in punctuation:
        if char in word:
            word = word.replace(char, "")

    # Return the word without punctuation
    return word


# Check the sentiment value of the tweet
def tweetChecker(word, keyWords, sentimentValues):

    # Initialize sentiment value
    sentiment = 0

    # Go through all the key words in from the file
    for key in range(len(keyWords)):

        # If the key word is the same as the word from the tweet
        if keyWords[key] == word:
            # Add its sentiment value
            sentiment = int(sentimentValues[key])

    # Return the sentiment value
    return sentiment


# Check for the region of the tweet
def findRegion(latitude, longitude):

    # Check if the latitude is within the range of a timezone
    # Otherwise, do not check for the region of the point
    if not 24.660845 < latitude < 49.189787:
        return

    # Check for the region according to the longitude points and return it
    elif -87.518395 < longitude < -67.444574:
        return "Eastern"
    elif -101.998892 < longitude < -87.518395:
        return "Central"
    elif -115.236428 < longitude < -101.998892:
        return "Mountain"
    elif -125.242264 < longitude < -115.236428:
        return "Pacific"
    else:
        return


# Calculate the average sentiment for each region
def avgRegion(sent, count):

    # Do not calculate if there are no counted tweets
    if count == 0:
        return 0
    else:
        return sent / count
