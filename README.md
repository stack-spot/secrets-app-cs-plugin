- **Descrição:** O plugin **`secrets-app-cs-plugin`** adiciona em uma Stack a capacidade de provisionar o uso de segredos armazenados na AWS Secrets Manager. 

- **Categoria:** Secrets. 
- **Stack:** DotNET.
- **Criado em:** 03/02/2022. 
- **Última atualização:** 03/02/2022.
- **Download:** https://github.com/stack-spot/secrets-app-cs-plugin.git.


## **Visão Geral**
### **secrets-app-cs-plugin**

O **`secrets-app-cs-plugin`** adiciona em uma Stack a capacidade de provisionar o uso de segredos armazenados na AWS Secrets Manager, reduzindo o risco da exposição de dados sensíveis no código, como logins e senhas de vários tipos (banco de dados, recursos de rede etc), chaves de API, chaves de criptografia e similares.

## **Uso**

### **Pré-requisitos**
Para utilizar esse plugin, é necessário ter uma Stack DotNET criada pelo STK CLI.  

### **Instalação**
Para fazer o download do **secrets-app-cs-plugin**, siga seguinte passo:  

- Copie e cole a URL abaixo no seu navegador/terminal:  

```
https://github.com/stack-spot/secrets-app-cs-plugin.git
```

## **Configuração**

### **Inputs**
Os inputs necessários para utilizar o plugin são:
| **Campo** | **Valor** | **Descrição** |
| :--- | :--- | :--- |
| CacheItemTTL | Padrão: 3600000 | TTL do cache em milliseconds | 
| MaxCacheSize | Padrão: 1024 | Quantidade máxima de items a serem cacheados antes de executar o LRU |
| VersionStage | Padrão: AWSCURRENT | Versão que o cache irá requisitar ao recuperar o segredo do Secrets Manager |
| RegionEndpoint | Padrão: "us-east-1" | Endpoint regional que será utilizado para requisitar o Secrets Manager |

### **Exemplo de uso**
- [**Nuget**](https://www.nuget.org/packages/StackSpot.Secrets/)