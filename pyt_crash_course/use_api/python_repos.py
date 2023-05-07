import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)

# status 
print("Status code: ", r.status_code)

# almacenando información del request
response_dict = r.json()
print("Total de repositorios: " + str(response_dict["total_count"]))

# explorando información
repo_dicts = response_dict["items"]
print("Repositorios retornados: " + str(len(repo_dicts)))

# examinando el primer repositorio
repo_dict = repo_dicts[0]
print("\nKeys" + str(len(repo_dict)))
for key in sorted(repo_dict.keys()):
    print(key)