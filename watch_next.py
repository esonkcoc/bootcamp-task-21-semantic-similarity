import spacy
nlp = spacy.load("en_core_web_md")

# Read the movie descriptions from the .txt file into the program.

def read_movie_descriptions(file_path):
    with open(file_path, 'r') as file:
        descriptions = file.readlines()
    return descriptions

descriptions = read_movie_descriptions('movies.txt')

# Process the movie descriptions to obtain their word vectors.

def process_descriptions(descriptions):
    processed_descriptions = []
    for description in descriptions:
        doc = nlp(description)
        processed_descriptions.append(doc)
    return processed_descriptions

processed_descriptions = process_descriptions(descriptions)

# Calculate the similarity scores between the provided movie description and each description from the .txt file.

def get_similarity_scores(target_description, processed_descriptions):
    similarity_scores = []
    target_doc = nlp(target_description)
    for description in processed_descriptions:
        similarity_scores.append(target_doc.similarity(description))
    return similarity_scores

target_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similarity_scores = get_similarity_scores(target_description, processed_descriptions)

#Based on the similarity scores, recommend the top movies that have the highest similarity to the target description.
def recommend_movies(similarity_scores, descriptions, num_recommendations=5):
    recommendations = []
    sorted_scores_indices = sorted(range(len(similarity_scores)), key=lambda k: similarity_scores[k], reverse=True)
    
# The lambda function is used as the key argument in the sorted() function. The lambda function takes one parameter, k, and returns the value of similarity_scores[k]. It is used to specify the sorting criteria for the sorted() function.
    
    for i in range(num_recommendations):
        index = sorted_scores_indices[i]
        recommendations.append(descriptions[index])
    return recommendations

recommendations = recommend_movies(similarity_scores, descriptions)
print("Recommended Movies:")
for movie in recommendations:
    print(movie)

"""lambda indicates the start of an anonymous function. k is the parameter of the lambda function. In this case, it represents an index value.: separates the parameter from the return value.
similarity_scores[k] is the expression that defines what will be returned by the lambda function. It retrieves the similarity score at index k from the similarity_scores list.
In the context of the sorted() function, the lambda function is used as the key to determine the sorting order. By using key=lambda k: similarity_scores[k], the sorted() function sorts the elements based on their corresponding similarity scores."""