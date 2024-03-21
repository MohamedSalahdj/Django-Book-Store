# Book-story

Book-story is a Django project that serves as a platform for managing and sharing book-related content. It offers features for users to browse, upload, and discuss books, enhancing the reading experience for book enthusiasts.

## Features

- **User Authentication:** Secure user authentication system allowing users to register, login, and manage their accounts.
- **Book Management:** Comprehensive book management system enabling users to upload, edit, and delete book entries, along with associated metadata such as author, genre, and publication date.
- **Search and Filtering:** Robust search and filtering functionality allowing users to find books based on various criteria such as title, author, genre, and publication date.
- **Discussion Forums:** Interactive discussion forums where users can engage in discussions about books, share recommendations, and ask questions.
- **User Profiles:** Personalized user profiles showcasing users' uploaded books, discussions, and other activities within the platform.
- **Admin Panel:** Administrative dashboard for managing users, books, discussions, and other site content efficiently.

## Installation

To run the Book-story project locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/MohamedSalahdj/Django-Book-Store.git
   ```

2. Navigate to the project directory:

   ```
   cd Django-Book-Store
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```
   python manage.py migrate
   ```

5. Create a superuser:

   ```
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```