# Office space allocation

Room allocation system for one of Andela Kenya’s facilities called The Dojo

**Installation**

`$ git clone -b develop https://github.com/oscamaina/andela-21`

`$ cd andela-21/`

Create and activate a virtual environment

```

$ virtualenv env
$ cd venv/Scripts
& activate
& cd..
& cd..

```

Install dependencies
`$ pip install -r requirements.txt`

**Run the application**
```

$ python app.py

```

**Commands**
```

app.py create_room <room_type> <room_name>...
app.py add_person <first_name> <second_name> <category> [<accommodation>]
app.py print_room <room_name>
app.py print_allocations [--o=filename]
app.py print_unallocated [--o=filename]
app.py reallocate_person <person_identifier> <new_room_name>
app.py load_people <file_name>
app.py save_state [--db_name=dbname]
app.py load_state <dbname>
app.py exit
app.py (-i | --interactive)
app.py (-h | --help)

```
