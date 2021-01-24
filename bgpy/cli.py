from .server import run
from .interface import terminate
from typer import Typer, echo, Abort
from typing import Optional
from pathlib import Path

try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata  # type: ignore

app = Typer(add_completion=False)


@app.command("server")
def run_server(
    host: str, port: int, log_file: Optional[Path] = None
) -> None:
    """Run a bgpy server on the given host, which starts listening to the provided
    port.
    Note: Before calling 'initialize()' and passing 'init_task()', exec_task()'
    and 'exit_task()' to the server, it will not respond to requests.
    """
    if str(log_file) == "None":
        log_file = None
    try:
        run(host=host, port=int(port), log_file=log_file)
    except OSError as e:
        echo(e)
        Abort()


@app.command("terminate")
def terminate_server(
    host: str, port: int, log_file: Optional[Path] = None
) -> None:
    """Terminate a bgpy server on the given host, which is listening to the
    provided port.
    """
    if str(log_file) == "None":
        log_file = None
    try:
        terminate(host=host, port=int(port), log_file=log_file)
    except OSError as e:
        echo(e)
        Abort()


@app.command("version")
def version_info():
    """Prints the version of the package.
    """
    package = "bgpy"
    version = metadata.version(package)
    echo(f"{package} {version}")


def main():
    app()
