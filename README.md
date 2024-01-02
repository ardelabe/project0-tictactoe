# CS50 AI 

This repository's code refers to a project from CS50 AI (2024): https://cs50.harvard.edu/ai/2024/

# OVERVIEW

The code takes actors, actresses and the movies they're starring as nodes of a graph. Each person-movie is a node. 

Then it implements that idea where any Holliwood personality is at most 4 steps from Kevin Bacon - where you can input two personalities and the code returns a path that links them between nodes of costarring personalities. 

# THE DEVELOPMENT

I didn't code it all, the base code was almost completed. I just had to select the correct class to order my frontier (to always find the shortest path), and write the shortest_path funcion, that takes the source and target personality as arguments. And returns a list with the link nodes between them (if there is any). 
