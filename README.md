- **Descrição:** O plugin secrets-app-cs-plugin adiciona em uma stack a capacidade de provisionar o uso de segredos armazenados na AWS Secrets Manager. 

- **Categoria:** Secrets. 
- **Stack:** dotnet.
- **Criado em:** 03/02/2022. 
- **Última atualização:** 03/02/2022.
- **Download:** https://github.com/stack-spot/secrets-app-cs-plugin.git.


## **Visão Geral**
### **secrets-app-cs-plugin**

O **secrets-app-cs-plugin** adiciona em uma stack a capacidade de provisionar o uso de segredos armazenados na AWS Secrets Manager, reduzindo o risco da exposição de dados sensíveis no código, como logins e senhas de vários tipos (banco de dados, recursos de rede, etc.), chaves de API, chaves de criptografia e similares.

## **Uso**

### **Pré-requisitos**
Para utilizar esse plugin, é necessário ter uma stack dotnet criada pelo cli.

### **Instalação**
Para fazer o download do **secrets-app-cs-plugin**, siga os passos abaixo:

**Passo 1.** Copie e cole a URL abaixo no seu navegador/terminal:
```
https://github.com/stack-spot/secrets-app-cs-plugin.git
```

## **Configuração**

### **Inputs**
Os inputs necessários para utilizar o plugin são:
| **Campo** | **Valor** | **Descrição** |
| :--- | :--- | :--- |
| AWS region| Padrão: "us-east-1" | Região da AWS a ser utilizada para configuração do SQS. |

### **Exemplo de uso**
- [**Nuget**](https://www.nuget.org/packages/StackSpot.Secrets/)
