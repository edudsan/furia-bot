from data_handler import load_data

def generate_response(message: str, platform: str) -> str:
    if message.startswith("/jogos"):
        games = load_data("data/times.json")
        return format_games(games)
    elif message == "/start":
        return "🐆 Bem-vindo ao FURIA Bot! Use /jogos, /eventos, /loja"
    # Adicione mais comandos aqui!