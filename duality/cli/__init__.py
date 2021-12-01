#import all relevant contents from the associated module.
from duality.cli import cli
from duality.cli.cli import (
    menu,
    dualityCLI,
    MonteCarloCLI,
    DijkstraCLI,
    EOQCLI,
)

#all relevant contents.
__all__ = [
    cli,
    menu,
    dualityCLI,
    MonteCarloCLI,
    DijkstraCLI,
    EOQCLI,
]
