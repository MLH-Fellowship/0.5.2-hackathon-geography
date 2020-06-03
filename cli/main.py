import typer

import helper


app = typer.Typer()


@app.command()
def get_word(char_code: str):
    word = helper.two_to_word(char_code)
    typer.echo(f"{word}")


@app.command()
def get_phrase(code: str):
    try:
        if len(code) != 12:
            error = typer.style("Incorrect OLC length. Format: 6PH57VP3+PR6", fg=typer.colors.RED)
            typer.echo(error)
            return
        phrase = helper.olc_to_phrase(code)
        typer.echo(f"{phrase}")
    except KeyError:
        error = typer.style("Not a valid OLC.", fg=typer.colors.RED)
        typer.echo(error)


if __name__ == "__main__":
    app()
