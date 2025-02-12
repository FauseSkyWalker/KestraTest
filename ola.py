import requests

url = "http://localhost:8080/api/v1/flows"
headers = {"Content-Type": "application/x-yaml"}

yaml_data = """
id: hello-devops
namespace: default
tasks:
  - id: print-message
    type: "io.kestra.plugin.scripts.shell.Script"
    script: |
      echo "Hello DevOps World"
"""

response = requests.post(url, headers=headers, data=yaml_data)

if response.status_code == 200:
    print("Fluxo 'hello-devops' criado com sucesso!")
else:
    print(f"Erro: {response.status_code}, {response.text}")
