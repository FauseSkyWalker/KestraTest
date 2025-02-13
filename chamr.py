import requests

url = "http://localhost:8080/api/v1/flows/hello-devops/run"  # Endpoint para rodar o fluxo
headers = {"Content-Type": "application/x-yaml"}

# Corpo da requisição no formato YAML
yaml_data = """
inputs: {}
"""

response = requests.post(url, headers=headers, data=yaml_data)

if response.status_code == 200:
    print("Fluxo 'hello-devops' executado com sucesso!")
else:
    print(f"Erro: {response.status_code}, {response.text}")


#curl -X POST "http://localhost:8080/api/v1/executions/trigger/default/hello-devops" -F "param=value"

#curl -X GET "http://localhost:8080/api/v1/flows/default/hello-devops" -H "Content-Type: application/json"

       #  curl -X POST "https://7d6c-45-230-85-179.ngrok-free.app/api/v1/executions/trigger/default/hello-devops" -F "param=value"
               