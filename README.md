# DJANGO-BLOG
A simple blog written in django 2.0 and bootstrap4

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need following python modules to run this project in your local system

```
django 2.0.7
django-ckeditor 5.5.0
django-taggit 0.22.2
pillow 5.2.0

```
you can also check the requirement file
### Installing

To get the project up and running in your system, follow given below steps

clone the project

```
git clone https://github.com/BBijaya/DJANGO-BLOG.git
```

Install django and other required python modules using pip

```
pip install Django==2.0.7 django-ckeditor==5.5.0 django-extensions==2.0.7 django-taggit==0.22.2 Pillow==5.2.0
```
Now after all the required modules are installed (first cd inot the project dir) and run:
```
python manage.py runserver
```
Dont forget to apply migrations , otherwise the url below will throw error
```
python manage.py migrate
```
This will start the local development server, acces the blog by going in the following url : http://127.0.0.1:8000/
Add posts images and see how the blog works



## Built With

* [Django](https://www.djangoproject.com/ - The web framework used
* [WYSWYG editor](https://ckeditor.com/) - Dependency Management


## Authors

* **Bijaya Budhathoki** - *Initial work* - (https://bijayabudhathoki.com)

## License

This project is licensed under the GPL License - see the [LICENSE.md](LICENSE.md) file for details


