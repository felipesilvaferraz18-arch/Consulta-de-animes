import requests
from deep_translator import GoogleTranslator

def buscar_anime():
    print("--- 🎌 Consulta de Animes 🎌 ---")
    nome = input("Digite o nome do anime: ")

    # URL da API Jikan (v4)
    url = f"https://api.jikan.moe/v4/anime?q={nome}&limit=1"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if dados['data']:
            anime = dados['data'][0]
            
            # 1. Mapeamento do Status para Português
            mapa_status = {
                "Finished Airing": "Finalizado",
                "Currently Airing": "Em lançamento",
                "Not yet aired": "Ainda não estreou",
                "On Hiatus": "Em hiato",
                "Discontinued": "Descontinuado"
            }
            status_en = anime.get('status', '')
            status_pt = mapa_status.get(status_en, status_en)

            # 2. Tradução da Sinopse
            sinopse_en = anime.get('synopsis')
            if sinopse_en:
                # Traduz do inglês (en) para o português (pt)
                sinopse_pt = GoogleTranslator(source='en', target='pt').translate(sinopse_en)
            else:
                sinopse_pt = "Sinopse não disponível."

            # Exibição dos resultados
            print(f"\n✅ Resultado encontrado:")
            print(f"Título: {anime['title']}")
            print(f"Nota: {anime.get('score', 'N/A')}")
            print(f"Episódios: {anime.get('episodes', '?')}")
            print(f"Status: {status_pt}")
            # Exibe os primeiros 300 caracteres da sinopse traduzida
            print(f"Sinopse: {sinopse_pt[:300]}...")

        else:
            print("\n❌ Anime não encontrado.")

    except Exception as e:
        print(f"Erro na conexão ou tradução: {e}")

# Correção da condicional main (sem espaços extras)
if __name__ == "__main__":
    buscar_anime()

# Tenha instalado o python e o GoogleTranslator para poder rodar no seu terminal 
# execute no terminal o seguinte comando após instalar os dois softwares
# comando: python3 buscaranimes.py (você deve estar no diretório aonde foi baixado o arquivo e dentro da pasta que você criou para executar esse comando)
