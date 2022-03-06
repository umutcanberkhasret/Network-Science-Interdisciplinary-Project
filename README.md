# Network-Science-Interdisciplinary-Project

A joint project undertaken by students from Network Science and Social Network Analysis master courses offered by  University of Padua. 

Here, we are examining gender-based violence by focusing on two Islamic countries, Pakistan and Egypt, is reflected.
The main goal was to build a Semantic Network, then graphically represent the relationships between hashtags and 
words used, based on their co-occurrence, to express one's beliefs and feelings about a given topic. 

We analyzed the database according to two main techniques: 
  - Topic analysis
  - Hashtag analysis

In this research, Twitter, a social media platform, is used as a means of information. In specific, the Sandbox tier of 
Twitter API was utilized throughout the whole data retrieval process.

The general workflow was explained in steps below: 
  - Making queries and retrieving a predefined number of tweets according to the selected hashtags
  - Converting obtained JSON files into Pandas data frames for future modifications.
  - Filtering out unused parameters after parsing and creating a simpler table 
  - Applying necessary alterations to the data so that it is adequately articulate. 
  - Extracting words and hashtags from the data. 
  - Designing three different networks with only extracted words, only extracted hashtags, and the overall 
    network with the complete data. 
  - Exporting node & edge lists to be used on Gephi. 
  - Adjusting node sizes according to PageRank and node colors according to modularity/communities. 
  - After importing node & edge lists at hand, choosing the right layout for that specific network. 
  - Calculating various network metrics and exporting them in CSV format. 
  - Tailoring the network design to our liking, exporting the final network picture. 
  - PDF and CDDF and gamma calculations and creating related plots based on the exported metrics


For findings, check Gender-based Violence in Pakistan and Egypt final report.
