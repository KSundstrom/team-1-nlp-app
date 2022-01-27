#!/usr/bin/env python3


"""
When you have worked through the tutorial on Boolean search, it is time to create your own search application.
Copy over the relevant code from the tutorial notebook into your own Python program. Then extend the program with some cool features:

1. The queries should not be hard-coded. Instead your program should ask the user to type the query. Make this run in a loop, so that the user can run as many queries they like. Also come up with some user input that tells the program to quit, such as an empty string or a specific keyword.

2. Your search application should print the contents of the retrieved documents. (A vector consisting of ones and zeros won't do!) If there are too many matching documents, maybe you want to show only the top n documents. (Still you could print out how many matching documents there are in total.) If the documents are long, maybe you want to truncate the output to the m first words or characters only.

3. If you just copy the code from the tutorial, your program will crash if you enter a word (term) that does not occur in any document in the collection. Modify your program to work correctly also in the case that a term is unknown. For instance, what documents should be retrieved for a search such as: (1) "unknownweirdword", (2) "NOT unknownweirdword", or (3) "unknownweirdword OR this"?  (If this is too difficult, don't get stuck here, but come back to it later.)

4. Have you noticed that not all words in the toy data were actually indexed by the code in the tutorial? Which ones? Would you like to index all words containing alpha-numerical characters? Can you solve that? The answer can be found here: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html  (Again, don't waste time on this one if it is too difficult, but return to it later.)

5. This task is important. You need to index some "real" documents from a text file. When you run your program, it should start by reading document contents from a file and index these documents. After this, the user should be able to type queries and retrieve matching documents. Initially, you can use our example data sets: One contains 100 articles extracted from English Wikipedia and the other contains 1000 articles extracted from English Wikipedia (with topics mostly starting with the letter A). When you read these files, you need to produce a list of strings, such that an entire article (document) is in one string. You can locate the boundaries between two articles from the </article> tag, which always occurs on a line of its own in the file. The text is UTF-8 encoded.

6. If you like, you can use some other data, for instance a Wikipedia dump for some other language, such as Finnish: https://linguatools.org/tools/corpora/wikipedia-monolingual-corpora/. First you need to download a Wikipedia XML file. Then you need to uncompress it with bunzip2. Then you need to convert the XML format to plain text using the Perl script xml2txt.pl, which is available for download on the web page. You need to use the option -articles in order to preserve the article tags: perl xml2txt.pl -articles INPUT_FILE.xml OUTPUT_FILE.txt.

Add your code to your GitHub project. Create issues and assign them within the team. Remember to put the relevant issue numbers (such as #11) in the beginning of your commit messages.

Also, from now on, start keeping track of your working hours. In the Wiki area of your team repository on GitHub, please add a document in which you record the following information for each time someone works on the project:

    Date
    Number of hours
    Name of team member
    Brief note on what you worked on
"""


def main():
    pass


if __name__ == '__main__':
    main()
