from pybliometrics.scopus import ScopusSearch, AuthorRetrieval

# Define search queries for the three areas
query_factors = 'social innovation AND higher education institutions AND factors'
query_change = 'social innovation AND higher education institutions AND organizational change'
query_impact = 'social innovation AND higher education institutions AND impact assessment'

# Conduct Scopus searches for each area
results_factors = ScopusSearch(query_factors)
results_change = ScopusSearch(query_change)
results_impact = ScopusSearch(query_impact)

# Function to display publication information with type specification and geographical location
def display_publications(results, publication_type):
    print(f"{publication_type.capitalize()} Publications:")
    for i, result in enumerate(results.results, start=1):
        authors = ', '.join(result.authors)
        author_affiliations = []

        # Retrieve and concatenate author affiliations
        for author_id in result.author_ids:
            author = AuthorRetrieval(author_id)
            author_affiliations.append(author.affiliation)

        # Display publication information and author affiliations
        print(f"{publication_type} {i}:")
        print("Title:", result.title)
        print("Authors:", authors)
        print("Author Affiliations:", ', '.join(author_affiliations))
        print("Publication Year:", result.coverDate)
        print("DOI:", result.doi)
        print("Citations:", result.citedby_count)
        print("Abstract:", result.description)
        print("\n")

# Display information for each area with publication types specified
display_publications(results_factors, "Book")
display_publications(results_change, "Journal Article")
display_publications(results_impact, "Report")
