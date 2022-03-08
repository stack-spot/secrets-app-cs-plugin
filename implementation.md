## **Implementação**

### **Inputs**
- Os inputs necessários para utilizar o plugin são:

| **Campo** | **Valor** | **Descrição** |
| :--- | :--- | :--- |
| CacheItemTTL | Padrão: 3600000 | TTL do cache em milliseconds | 
| MaxCacheSize | Padrão: 1024 | Quantidade máxima de items a serem cacheados antes de executar o LRU |
| VersionStage | Padrão: AWSCURRENT | Versão que o cache irá requisitar ao recuperar o segredo do Secrets Manager |
| RegionEndpoint | Padrão: "us-east-1" | Endpoint regional que será utilizado para requisitar o Secrets Manager |

Você pode sobrescrever a configuração padrão do cache adicionando a seção SecretsCache em seu `appsettings.json`.

```json
    "SecretsCache": {
        "CacheItemTTL": 3700000,
        "MaxCacheSize": 1024,
        "VersionStage": "AWSCURRENT",
        "RegionEndpoint": "sa-east-1"
    }
```

### **Configurações**
- Adicione ao seu `IServiceCollection` via `services.AddSecretsManager()` no `Startup` da aplicação ou `Program` tendo como parametro de entrada `IConfiguration` e `IWebHostEnvironment`

```csharp
    services.AddSecretsManager(Configuration, Env);
```
### **Uso**

- O código abaixo irá retornar uma cópia do seu segredo e armazenará em cache para consultas futuras.
```csharp
    [ApiController]
    [Route("[controller]")]
    public class SampleController : ControllerBase
    {
        private readonly ISecretsManagerCache _cache;

        public SampleController(ISecretsManagerCache cache)
        {
            _cache = cache;
        }

        [HttpGet]
        public async Task<IActionResult> Get()
        {
            var someEntity = await _cache.GetSecretString("Poc");
            return Ok(someEntity);
        }
    }
```

- Outra alternativa é utilizar a interface `ISecretsRepository` com tratamento de erros e implementar a deserialização do seu segredo.
```csharp
    var secret = await ISecretsRepository.GetSecret<T>(secretKey);
```
### **Exceptions**
- `SecretsRepositoryException`, acontece quando:
    - Secret não encontrada, retorna a mensagem `No secret was found for key {secretKey}`.
    - Erro inesperado, retorna a mensagem `An error occurred while getting the secret for key {secretKey}`., contendo a exception do erro.