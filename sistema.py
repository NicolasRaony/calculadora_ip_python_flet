import flet as ft

def main(pagina):
    texto = ft.Text("Sistema de Chat")

    chat = ft.Column()

    def enviar_mensagem_todos(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)    
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_todos)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    campo_envio = ft.Row([campo_mensagem, botao_enviar_mensagem])
    def abrir_chat(evento):
        popup.open = False
        pagina.remove(texto, botao_chat)
        pagina.add(chat)
        pagina.pubsub.send_all("{} entrou no chat".format(nome_usuario.value))
        pagina.add(campo_envio)
        pagina.update()
    
    def cancelar_popup(evento):
        popup.open = False
        pagina.update()

    botao_iniciar_chat = ft.ElevatedButton("Iniciar Chat", on_click=abrir_chat)
    botao_cancelar_popup = ft.ElevatedButton('Cancelar', on_click=cancelar_popup)
    titulo_popup = ft.Text('Chat')
    nome_usuario = ft.TextField(label="Nome de Usuario", on_submit=abrir_chat)
    popup = ft.AlertDialog(
        modal = True,
        title = titulo_popup,
        content = nome_usuario,
        actions= [botao_iniciar_chat, botao_cancelar_popup]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_chat = ft.ElevatedButton("Entrar no Chat", on_click=abrir_popup)

    pagina.add(texto, botao_chat)

ft.app(target = main, view=ft.WEB_BROWSER)