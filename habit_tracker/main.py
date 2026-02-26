import typer
from habit_tracker.db import connect, initialize_schema, add_habit

app = typer.Typer() #create typer class
habit_app = typer.Typer()
app.add_typer(habit_app, name = "habit")

@habit_app.command()  #make a new command and run these in sequence
def add(name: str):
    con = connect()
    try:
        initialize_schema(con)
        add_habit(con, name)
    finally:
        con.close()
    typer.echo(f"Added Habit: {name}")

if __name__ == "__main__":
    app()