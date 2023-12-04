import pygal

wm = pygal.Worldmap()
wm.title = "America completa"

wm.add('America del norte', ['ca', 'mx', 'us'])
wm.add('America del centro', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('America del sur', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file("americas.svg")