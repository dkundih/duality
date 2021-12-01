#import all relevant contents from the associated module.
from duality.cli import cli
from duality.cli.cli import (
    __CLIexeversion__,
    menu,
    greet,
    save_to,
    CLI, #client.
    MonteCarloCLI,
    DijkstraCLI,
    EOQCLI,
)

#all relevant contents.
__all__ = [
    cli,
    __CLIexeversion__,
    menu,
    greet,
    save_to,
    CLI, #client.
    MonteCarloCLI,
    DijkstraCLI,
    EOQCLI,
]
