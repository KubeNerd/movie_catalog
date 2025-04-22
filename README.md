# 🎬 Movie Catalog API

## 🔄 Visão Geral
O **Movie Catalog API** é um projeto de exemplo criado usando **Flask** seguindo o padrão **DDD (Domain-Driven Design)**.

A ideia é simples, mas poderosa: organizar e estruturar um pequeno sistema com camadas bem separadas, mantendo o código limpo, modular e fácil de evoluir.

Você pode:
- Adicionar filmes com título, ano e gênero.
- Listar todos os filmes cadastrados.
- Avaliar um filme com uma nota de 0 a 5 estrelas.

---

## 📁 Estrutura do Projeto

```
movie_catalog/
├── domain/
│   └── movie.py
├── application/
│   └── movie_service.py
├── infrastructure/
│   └── movie_repository.py
├── api/
│   └── movie_routes.py
├── main.py
└── requirements.txt
```

**Resumo das camadas:**

| Camada          | Função                                              |
|-----------------|-------------------------------------------------------------|
| domain/         | Define o que é um Filme (entidade principal)                |
| application/    | Orquestra os casos de uso: adicionar, listar, avaliar filmes |
| infrastructure/ | Guarda e busca filmes (em memória, simulando um banco)         |
| api/            | Define as rotas HTTP usando Flask                             |
| main.py         | Inicializa o servidor Flask e registra as rotas               |

---

## 🔧 Como rodar o projeto

1. Clone o repositório ou copie os arquivos.

2. Instale as dependências:
```bash
pip install flask
```

3. Rode a aplicação:
```bash
python main.py
```

4. A API estará disponível em:
```
http://127.0.0.1:5000/
```

---

## 💳 Testando via `curl`

Aqui estão exemplos para testar a API usando `curl` diretamente do terminal:

### 1. Adicionar um filme

```bash
curl -X POST http://127.0.0.1:5000/movies \
    -H "Content-Type: application/json" \
    -d '{"title": "Inception", "year": 2010, "genre": "Sci-Fi"}'
```

**Resposta esperada:**
```json
{
  "title": "Inception",
  "year": 2010,
  "genre": "Sci-Fi",
  "rating": null
}
```

### 2. Listar todos os filmes

```bash
curl http://127.0.0.1:5000/movies
```

**Resposta esperada:**
```json
[
  {
    "title": "Inception",
    "year": 2010,
    "genre": "Sci-Fi",
    "rating": null
  }
]
```

### 3. Avaliar um filme

```bash
curl -X POST http://127.0.0.1:5000/movies/Inception/rate \
    -H "Content-Type: application/json" \
    -d '{"score": 4.5}'
```

**Resposta esperada:**
```json
{
  "message": "Filme 'Inception' avaliado com sucesso!"
}
```

### 4. Tentar avaliar um filme inexistente

```bash
curl -X POST http://127.0.0.1:5000/movies/FakeMovie/rate \
    -H "Content-Type: application/json" \
    -d '{"score": 5}'
```

**Resposta esperada:**
```json
{
  "error": "Filme não encontrado."
}
```

---

## 💎 Características DDD aplicadas

- **Domain (Núcleo de Negócio)**: `Movie` define o que é um filme, com validações e comportamentos (ex: avaliar).
- **Application (Orquestração)**: `MovieService` coordena as operações: adicionar, listar, avaliar.
- **Infrastructure (Persistência)**: `MovieRepository` cuida de armazenar e buscar filmes (em memória).
- **Interface/API**: `movie_routes.py` recebe chamadas HTTP e usa o Service para responder.

Cada camada **faz apenas o que deve fazer**, sem mistura, seguindo o DDD de verdade.
