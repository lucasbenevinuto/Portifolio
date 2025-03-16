# Data Science & AI Engineer Portfolio

A modern, responsive portfolio website for Data Scientists and AI Engineers built with FastAPI and Jinja2 templates.

## Features

- Clean, modern design with responsive layout
- Showcase of AI/Data Science projects with details
- Skills & expertise visualization
- Professional timeline and experience
- Blog section for sharing insights and knowledge
- Contact form for potential clients/employers
- Optimized for all devices and browsers

## Tech Stack

- **Backend**: FastAPI, Python
- **Frontend**: HTML, CSS, JavaScript
- **Templating**: Jinja2
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins, Roboto Mono)

## Setup and Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python main.py
   ```

6. Open your browser and navigate to `http://localhost:8000`

## Project Structure

- **app/**: Main application directory
  - **routers/**: FastAPI route handlers
  - **schemas/**: Pydantic models
- **static/**: Static files (CSS, JS, images)
  - **css/**: Stylesheet files
  - **js/**: JavaScript files
  - **images/**: Image files
  - **files/**: Downloadable files (resume, etc.)
- **templates/**: Jinja2 HTML templates
- **main.py**: Main application entry point
- **requirements.txt**: Project dependencies

## Customization

To customize this portfolio for your own use:

1. Replace the sample project data in `app/routers/projects.py` with your own projects
2. Update the blog posts in `app/routers/blog.py` with your own content
3. Modify the skills and expertise in `templates/skills.html` to match your abilities
4. Update the about page information in `templates/about.html`
5. Replace placeholder images in `static/images/` with your own
6. Update contact information in `templates/contact.html`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [Jinja2](https://jinja.palletsprojects.com/) for templating
- [Font Awesome](https://fontawesome.com/) for icons

## Contact

For any questions or suggestions, please feel free to reach out:

- Email: your.email@example.com
- LinkedIn: [Your Name](https://linkedin.com/in/yourusername)
- GitHub: [Your GitHub](https://github.com/yourusername) 