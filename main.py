# Name: Huda Mukhtar
# User ID: hmukhta
# Program description: This program takes the input of two files (one with keywords and another with tweets) to calculate
# the happiness score for the tweet based on the key words and their sentiment values. The timezone of each tweet is located
# to calculate a final average happiness score based on all of the tweets with any keyword(s) found in that region
# To do this, another module is imported which performs these calculations
# and the final results are displayed to see which region is the happiest

# import the tweeting computing function from the sentiment analysis module created
from sentiment_analysis import compute_tweets

# This will be used to loop the input requests
# If an invalid file name is entered
valid = True

print("Hello!")

# Request the keyword and tweet file
tweets = input("Please enter the name of the file containing the tweets:")
key = input("Please enter the name of the file containing the key words:")
print("Thank you! Now I will be able to process the tweets.\n")

# Use the function to process the tweets' average sentiment and counted tweet values by region
results = compute_tweets(tweets, key)

# Until an invalid file is entered
while valid:

    # Split the tuples of the happiness average and counted tweets if they exist
    try:
        eastResult = str(results[0]).split(",")
        centralResult = str(results[1]).split(",")
        mountainResult = str(results[2]).split(",")
        pacificResult = str(results[3]).split(",")

        # Display calculated results
        print("\nIn the Eastern region, the happiness average is,", eastResult[0].replace("(", ""), "with", eastResult[1].replace(")", ""), "counted tweets.")
        print("In the Central region, the happiness average is,", centralResult[0].replace("(", ""), "with", centralResult[1].replace(")", ""), "counted tweets.")
        print("In the Mountain region, the happiness average is,", mountainResult[0].replace("(", ""), "with", mountainResult[1].replace(")", ""), "counted tweets.")
        print("In the Pacific region, the happiness average is,", pacificResult[0].replace("(", ""), "with", pacificResult[1].replace(")", ""), "counted tweets.")

        # End the program by exiting the loop
        valid = False

    # Otherwise ask for the files again
    except IndexError:

        # Print error message
        print("\nYikes! Something went wrong... your results are as shown below")
        print(results)
        print("\nTry again?")

        # Request the files again
        tweets = input("Please enter the name of the file containing the tweets:")
        key = input("Please enter the name of the file containing the key words:")
        results = compute_tweets(tweets, key)


