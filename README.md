# Django Text Record Application

This project is a Django-based web application integrated with a relational database (SQLite) designed to validate data persistence through HTTP URL access.

## Project Requirements

The application meets the following functional and technical requirements:

- **Database Configuration**: The Django project is configured with a properly connected database backend (SQLite).
- **Application & Model**: A Django application (`myapp`) has been created containing a model (`Record`) that defines a database table for text-based records.
- **Migrations**: Database migrations have been performed to ensure the table is successfully created.
- **Data Insertion (`/add`)**: A view function is mapped to the URL path `/add` that, when triggered via a browser request, inserts a new record into the database.
- **Data Retrieval (`/show`)**: A separate view function is mapped to the URL path `/show` that retrieves all stored records and displays them in the HTTP response.
- **URL Routing**: Routing is configured appropriately to ensure both endpoints function correctly.
- **Verification**:
    - The `/add` endpoint successfully persists data to the database.
    - The `/show` endpoint accurately reflects the stored records.
    - The implementation demonstrates successful data insertion and retrieval through defined URL routes.

## Functional Validation

The completed project clearly validates database write and read operations triggered directly through HTTP URL access:

1.  **Write Operation**: Visit `http://127.0.0.1:8000/add` to insert a text record.
2.  **Read Operation**: Visit `http://127.0.0.1:8000/show` to view all persisted records.
3.  **Admin Verification**: Records can also be managed through the Django Administration panel at `/admin`.
