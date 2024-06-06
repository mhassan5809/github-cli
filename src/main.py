import typer

repo_app = typer.Typer()
star_app = typer.Typer()


@repo_app.command(name="list")
def repo_list() -> None:
    print("repo list")


@repo_app.command(name="delete")
def repo_delete() -> None:
    print("repo delete")


@star_app.command(name="list")
def start_list() -> None:
    print("start list")


@star_app.command(name="delete")
def start_delete() -> None:
    print("start delete")


app = typer.Typer()
app.add_typer(repo_app, name="repo")
app.add_typer(star_app, name="starts")

if __name__ == "__main__":
    app()
