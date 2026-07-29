import base64
import IPython
from IPython.display import display
from pathlib import Path


def display_asciicast(path):
    name = Path(path).name
    text = base64.b64encode(Path(path).read_text().encode('ascii')).decode('ascii')
    assets = Path(__file__).parent / 'asciinema'
    css = (assets / 'asciinema-player.css').read_text()
    js = (assets / 'asciinema-player.min.js').read_text()

    content = f"""
<style>{css}</style>
<div id="asciinema-cast-player-{name}" style="width: 50%"></div>
<script>{js}</script>
<script>
AsciinemaPlayer.create('data:text/plain;base64,{text}', document.getElementById('asciinema-cast-player-{name}'));
</script>
"""
    display(IPython.display.HTML(content))
