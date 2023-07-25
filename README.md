# Flixcareers - Dynamic Job Search Platform

Flixcareers is a dynamic job search platform built with Django and SQLite, offering a user-friendly experience for job seekers and employers to connect effectively.

## Features

- User-friendly interface for effortless job searching
- Job listings can be filtered by location or category
- Detailed job information, accessible through clickable links
- Seamless job posting feature for employers to reach a wider pool of candidates

## Screenshots

1. Homepage - Effortless Job Search:
   ![App Screenshot](screenshots\Screenshot (165) - Copy.png)
2. Detailed Job Information:
   ![App Screenshot](screenshots\Screenshot (166).png)
3. Employer Job Posting Interface:
   ![App Screenshot](screenshots\Screenshot (170).png)
4. Subscribtion Page:
   ![App Screenshot](screenshots\Screenshot (169).png)
5. Thankyou Page:
   ![App Screenshot](screenshots\Screenshot (167).png)

## Technologies Used

- Django
- SQLite
- HTML/CSS
- JavaScript
- Bootstrap

## Getting Started

To run Flixcareers locally on your machine, follow the instructions below.

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Aditya-kr-jha/JobApp.git

```

2. Create and activate a virtual environment (optional but recommended):

```bash
pip install virtualenv
virtualenv venv
venv\Scripts\activate # for windows

```

3. Install the required dependencies:

```bash
pip install -r requirements.txt

```

4. Run the migrations to create the database using

```bash
python manage.py migrate

```

5. Start the development server:

```bash
python manage.py runserver

```

Access the application by navigating to http://127.0.0.1:8000/ in your web browser.

## Future Enhancements

In the future, we plan to implement the following enhancements:

- Personalized user accounts and user authentication
- Email notifications for job updates and application status
- Advanced search filters for precise job searches
- Data analytics tools to provide meaningful insights to employers
- Mobile app development for increased accessibility

## Contributing

Contributions to Flixcareers are welcome! If you find any issues or have new ideas to enhance the platform, please submit a pull request.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License Feel free to use, modify, and distribute the code for personal and commercial purposes.
