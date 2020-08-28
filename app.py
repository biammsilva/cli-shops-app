import typer

app = typer.Typer()


@app.command()
def main():
    typer.echo(f"Hello")


if __name__ == "__main__":
    app()