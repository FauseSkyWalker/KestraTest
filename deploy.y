name: Kestra CI/CD

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  validate:
    runs-on: ubuntu-latest
    name: Kestra Validate
    steps:
      - name: Checkout content
        uses: actions/checkout@v4
        
      - name: Deploy flows
        uses: kestra-io/validate-action@master       
        with:
          namespace: company.team
          directory: ./kestra/flows
          resource: flow
          server: https://ecd2-45-230-85-67.ngrok-free.app

        
