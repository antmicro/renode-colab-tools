import base64
import IPython
from IPython.display import display
from pathlib import Path
import shutil

# we do this every time, because it doesn't hurt
def provision_speedscope():
    colab_dir = Path(Path.home() / ".ipython/nbextensions/google.colab/speedscope")
    colab_dir.mkdir(parents=True, exist_ok=True)

    mod_path = Path(__file__).parent.resolve() / 'speedscope'
    for file in mod_path.iterdir():
        shutil.copy(file, colab_dir / file.name)


def display_speedscope(path):

    provision_speedscope()

    # the name is used to uniquely identify container divs
    name = Path(path).name
    text = base64.b64encode(Path(path).read_text().encode('ascii')).decode('ascii')

    content = """
<div id="asciinema-cast-player-{name}" style="width: 50%"></div>
<iframe src="/nbextensions/google.colab/speedscope/index.html#profileURL={path}" width="552" height="400" frameBorder="0" />
""".format(path=path, name=name)
    display(IPython.display.HTML(content))


