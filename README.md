# Machine Generated Paraphrases Readability Improvement
Improve the readability of generated paraphrases by using Simple PPDB

# Overview
This project use syntaxnet's trained model Parsey McParseface to 
generate pos tag. Then the program will replace target words in 
Simple PPDB with corresponding pos tag.

At last , the program will print average different readability score
for both original and replaced sentence.

The readability calculation methods used are 
automatic_readability_index and flesch_kincaid_readability
# Problem to solve
The readability of generated paraphrases can be improved by replacing
difficult words

But how to target the difficult words and replace them with words 
in correct form becomes a problem
# File Structure
    .
    └── ...
    ├── readability_cal.py      # main program 
    ├── uni_penny_mapping.txt   # mapping file for converting between penny tree tagging schema and universal dependency
    └── repl_loader.py          # utils to preload dict
    └── helper.py               # utils
    └── replaced.txt            # simplified replace dict
    └── beam_size_4_residual.txt # generated paraphrases
    └── ...
# Quick Start
1.
    First you need to download [Simple PPDB](https://cs.brown.edu/people/epavlick/data.html) and put it under 
    project folder.
2. 
    Then you should run
    
    ``python repl_loader.py``
    
    to read simple ppdb and save it to a pickle file
3. 
    ``python readability_cal.py``
    
    The program will replace words in `beam_size_4_residual.txt`
    according to the result of Parsey McParseface and will get new
    parse result after replacing target words.

# Current Result
automatic_readability_index:

    * original
    10.299129999999925
    
    * replaced
    10.192199999999964
    
    
flesch_kincaid_readability:

    * original:
    4.996375000000048
    
    * replaced
    4.9426620000000465
    
From the table above, we can see that the readability slightly
increase (higher score means more difficult). 


