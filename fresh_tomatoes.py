import os
import re
from shutil import copyfile
import webbrowser


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:       
        # Load the template for display the movies
        movie_tile_content_file = open('movie_template.html')
        movie_tile_content = movie_tile_content_file.read()
        movie_tile_content_file.close()

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=movie.trailer_youtube_url
            # storyline= movie.storyline
        )

    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('dist\\index.html', 'w')

    # Load the template for display the movies
    main_page_content_file = open('template.html')
    main_page_content = main_page_content_file.read()
    main_page_content_file.close()

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # Copy CSS and JS to dist folder
    copyfile('main.css', 'dist\\main.css')
    copyfile('main.js', 'dist\\main.js')
    copyfile('favicon.ico', 'dist\\favicon.ico')

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)