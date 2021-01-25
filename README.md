 ## Pokemon API for Mo
 
 Django project with API REST for insert and get pokemons and their evolutions.

## Getting Started

1) Clone project from https://github.com/juandfernandezd/pokemonApi
2) Open a terminal and install prerequisites
3) Change .env.example for .env and change user and db name

## Prerequisites

1) Python 3.7+
2) Virtualenv
3) Django
4) django-rest-framework

## Deployment 

1) Open a terminal into the project directory
2) Run command python manage.py migrate for create tables in database
3) Run command python manage.py runserver for deploy development server

## Commands

1) In the project directory you can execute command:
   * python manage.py register_evolution_chain <evolution_chain_id>
	* This command allows insert a complete evolution chain for a pokemon

## EndPoints 

1) localhost:8000/api/v1/pokemon/<pokemon_name>
	- GET: return a pokemon with its evolutions. Parameter: pokemon_name

		
## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Pip](https://pypi.org/project/pip/) - Package Management
* [Postgres](https://www.postgresql.org/) - Database used

## Contributing

Please read (https://github.com/juandfernandezd/pokemonApi) for details on our code of conduct, and the process for 
submitting pull requests to us.

## Authors

* **Juan David Fernandez Diaz**

## License

This project is licensed under the MIT License

