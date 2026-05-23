# LocalizaPet

Plataforma web para centralizar alertas de animais domésticos perdidos e encontrados. O problema que motivou o projeto é simples: as buscas hoje acontecem em grupos de WhatsApp e redes sociais, onde as postagens somem rapidamente e não há como cruzar quem perdeu com quem encontrou. O LocalizaPet resolve isso com um mural persistente e organizado, acessível pelo navegador, sem app pra instalar.

Desenvolvido como Projeto Integrador do curso de Bacharelado em TI / Ciência de Dados / Engenharia de Computação da [UNIVESP](https://univesp.br), Polo Taquaritinga/Sertãozinho — 2026.

--- 

## Funcionalidades

- Cadastro e autenticação de usuários
- Publicação de alertas com foto, espécie, cores e status (perdido / encontrado)
- Preenchimento automático de endereço por CEP via [ViaCEP](https://viacep.com.br)
- Mural de alertas na página inicial, ordenado pelo mais recente
- Página de detalhes com botão de compartilhamento via WhatsApp
- Edição e exclusão restritas ao criador do anúncio

## Stack

- **Back-end:** Python 3 + Django 5.2
- **Banco de dados:** SQLite (via ORM do Django)
- **Front-end:** HTML5 + Tailwind CSS (CDN)
- **Processamento de imagens:** Pillow
- **Endereçamento:** API pública ViaCEP (fetch assíncrono no front-end)

## Como rodar localmente

Pré-requisitos: Python 3.10+ e pip.

```bash
git clone https://github.com/<seu-usuario>/localizapet.git
cd localizapet

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Acesse `http://localhost:8000`.

Para criar um superusuário e acessar o painel de administração (`/admin`):

```bash
python manage.py createsuperuser
```

## Estrutura do projeto

```
localizapet/
├── core/           # Configurações globais e roteamento raiz
├── pets/           # App principal: models, views, forms, URLs e templates
│   ├── migrations/ # 3 migrações incrementais documentando a evolução do modelo
│   └── templates/
├── templates/      # base.html compartilhado entre os apps
├── media/          # Uploads de imagem (gerado em runtime, não versionado)
└── requirements.txt
```

## Migrações

O modelo de dados evoluiu em três etapas ao longo do desenvolvimento:

1. `0001_initial` — estrutura básica do modelo `Animal`
2. `0002_alter_animal_cores` — campo `cores` tornado opcional
3. `0003_animal_usuario` — adição da chave estrangeira para `User`, habilitando autenticação e controle de propriedade

## Limitações conhecidas

- Sem busca ou filtros na listagem (por espécie, status, cidade ou cor)
- Sem paginação — pode ficar lento com volume alto de registros
- Contato entre usuários depende do WhatsApp externo; não há mensagens internas

## Equipe

Eduardo Hiroshi Ianagui, Isadora Aline Bombarda Barbosa, Kathelyn Vitoria Pergentino Reis Anastacio, Marco Antonio Dantas, Murilo Siqueira da Silva e Welington Ricardo Roque Cedran.

Tutor: Josué Marcos de Moura Cardoso.
