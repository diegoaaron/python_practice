import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)

# status 
print("Status code: ", r.status_code)

# almacenando información del request
response_dict = r.json()
print("Total de repositorios: " + str(response_dict["total_count"]))

# explorando información
repo_dicts = response_dict["items"]

names, stars = [], []
print("Repositorios retornados: " + str(len(repo_dicts)))

# examinando el primer repositorio
print("Informacion del primer repositorio")

for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
    chart.title = "Proyecto en github mas votados"
    chart.x_labels = names

    chart.add('', stars)
    chart.render_to_file('python_repos.svg')

    print("nombre: " + repo_dict["name"])
    print("propietario: " + repo_dict["owner"]["login"])
    print("estrellas: " + str(repo_dict["stargazers_count"]))
    print("repositorio: " + repo_dict["html_url"])
    print("creacion: " + repo_dict["created_at"])
    print("actualizacion: " + repo_dict["updated_at"])
    print("descripcion: " + repo_dict["description"])

