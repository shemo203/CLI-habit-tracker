import typer, json
from habit_tracker.db import connect, initialize_schema, add_habit, get_habits

app = typer.Typer() #create typer class
habit_app = typer.Typer()
app.add_typer(habit_app, name = "habit")
@habit_app.command()
def setup():
    """Initialize the database"""
    con = connect()
    initialize_schema(con)
    con.closess
    typer.echo("Database setup")

@habit_app.command()  #make a new command and run these in sequence
def add(name: str):
    con = connect()
    try:
        initialize_schema(con)
        add_habit(con, name)
    finally:
        con.close()
    typer.echo(f"Added Habit: {name}")

@habit_app.command()
def show():
        con = connect()
        habits = get_habits(con)
        con.close()
        if not habits:
            typer.echo("No habits found, use habit add to start!")

@habit_app.command()
def save():
    con = connect()
    habits = get_habits(con) 
    con.close()
    filename = "data.json"
    
    try:
        with open(filename, "w") as f:
            json.dump(habits, f, indent=4)
        typer.echo(f"Data exported to {filename}")
    except Exception as e:
        typer.echo(f"Error saving file: {e}")



@habit_app.command()
def exit():
    exit

        


if __name__ == "__main__":
    app()




