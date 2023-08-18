import streamlit as st
import matplotlib.pyplot as plt
from pybliometrics.scopus import ScopusSearch, AuthorRetrieval

# Define search query for the impact analysis
query_impact = 'social innovation AND higher education institutions AND impact assessment'

# Conduct Scopus search for impact analysis
results_impact = ScopusSearch(query_impact)

# Function to display publication information with type specification and geographical location
def display_publications(results, publication_type):
    st.subheader(f"{publication_type.capitalize()} Publications:")
    for i, result in enumerate(results.results, start=1):
        # Display publication information
        st.write(f"**{publication_type} {i}:**")
        st.write("**Title:**", result.title)
        st.write("**Authors:**", ', '.join(result.authors))
        st.write("**Publication Year:**", result.coverDate)
        st.write("**DOI:**", result.doi)
        st.write("**Citations:**", result.citedby_count)
        st.write("**Abstract:**", result.description)
        st.write("\n")
        
        # Create a simple bar chart for citations
        plt.bar(result.title, result.citedby_count)
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Citations")
        st.pyplot(plt)

# Streamlit app
st.title("Bibliometric Analysis - Impact Analysis")
display_publications(results_impact, "Report")
