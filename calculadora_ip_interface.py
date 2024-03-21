import flet as ft

def main(page: ft.Page):
    def informacoes(classe, ip, mascara):
        def info_envio(address, network, broadcast, firsthost, lasthost, netmask, hosts_net, subnets, subnets_valores):
            informacoes_ip = ft.Column([ft.Text(address), ft.Text(network), ft.Text(broadcast), ft.Text(firsthost), ft.Text(lasthost), ft.Text(netmask),  ft.Text(hosts_net), ft.Text(subnets), subnets_valores])

            informacoes_rede = ft.Container(
                content= informacoes_ip,
                padding=15,
                width= 280,
                alignment= ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                border_radius=10
            )

            centralizar_info = ft.Row([informacoes_rede], alignment=ft.MainAxisAlignment.CENTER)

            page.add(titulo, envio_info, centralizar_info)

        ip_entrada.value = ''
        def calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular):
            match calcular:
                case True:
                    address = f'Address: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} | {classe}'
                    jumps = []
                    jumps2 = []
                    for i in range(0, range_lista[0], range_lista[1]):
                        jumps.append(i)
                        jumps2.append(i)
                    del (jumps2[0])
                    for j in range(0, len(jumps)):
                        if j <= len(jumps2) - 1:
                            if ip[1] >= jumps[j] and ip[1] < jumps2[j]:
                                ip[1] = jumps[j]
                                network = ('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], octetos[0], octetos[0]))
                                broadcast = (' Broadcast: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, octetos[3], octetos[3]))
                                firsthost = (' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], octetos[0], octetos[1]))
                                lasthost = (' Lasthost: {}.{}.{}.{}'.format(ip[0], jumps2[j] - 1, octetos[3], octetos[2]))
                        else:
                            if ip[1] >= jumps[j]:
                                ip[1] = jumps[j]
                                network = ('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], octetos[0], octetos[0]))
                                broadcast = (' Broadcast: {}.{}.{}.{}'.format(ip[0], octetos[3], octetos[3], octetos[3]))
                                firsthost = (' Firsthost: {}.{}.{}.{}'.format(ip[0], jumps[j], octetos[0], octetos[1]))
                                lasthost = (' Lasthost: {}.{}.{}.{}'.format(ip[0], octetos[3], octetos[3], octetos[2]))
                    netmask = (f'\nNetmask: {net_mask}')
                    subnets = ('\nSubnets:')
                    subnets_valores = ft.Column(
                        height=200,
                        width=250,
                        scroll=ft.ScrollMode.ALWAYS
                    )
                    for i in range(0, range_lista[0], range_lista[1]):
                        ip[1] = i
                        subnets_valores.controls.append(ft.Text(' {}.{}.{}.{}'.format(ip[0], ip[1], octetos[0], octetos[0])))
                    hosts_net = ('\nHosts/Net: {}'.format(hostsnet))
                case False:
                    address = f'Address: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} | {classe}'
                    network = f'{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}'
                    broadcast = 'N/A'
                    firsthost = 'N/A'
                    lasthost = 'N/A'
                    netmask = net_mask
                    hosts_net = 'N/A'
                    subnets = 'N/A'
                    subnets_valores = ft.Row()

            info_envio(address, network, broadcast, firsthost, lasthost, netmask, hosts_net, subnets, subnets_valores)
        
        page.remove(*page.controls)
        match mascara:
            case 8:
                informacoes_ip = ft.Text(
                f'\nNetwork: {ip[0]}.{0}.{0}.{0}\nBroadcast: {ip[0]}.{255}.{255}.{255}\nFirsthost: {ip[0]}.{0}.{0}.{1}\nLasthost: {ip[0]}.{255}.{255}.{254}\nNetmask: 255.0.0.0 = 8\nSubnets:\n {ip[0]}.{0}.{0}.{0}\nHosts/Net: {2**24 - 2}'
            )   
                page.add(titulo, envio_info, informacoes_ip)
            case 9:
                calcular = bool(1)
                range_lista = [129, 128]
                octetos = [0, 1, 254, 255]
                net_mask = '255.128.0.0 = 9'
                hostsnet = (2 ** 23 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 10:
                calcular = bool(1)
                range_lista = [193, 64]
                octetos = [0, 1, 254, 255]
                net_mask = '255.192.0.0 = 10'
                hostsnet = (2 ** 22 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 11:
                calcular = bool(1)
                range_lista = [225, 32]
                octetos = [0, 1, 254, 255]
                net_mask = '255.224.0.0 = 11'
                hostsnet = (2 ** 21 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 12:
                calcular = bool(1)
                range_lista = [241, 16]
                octetos = [0, 1, 254, 255]
                net_mask = '255.240.0.0 = 12'
                hostsnet = (2 ** 20 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 13:
                calcular = bool(1)
                range_lista = [249, 8]
                octetos = [0, 1, 254, 255]
                net_mask = '255.248.0.0 = 13'
                hostsnet = (2 ** 19 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 14:
                calcular = bool(1)
                range_lista = [253, 4]
                octetos = [0, 1, 254, 255]
                net_mask = '255.252.0.0 = 14'
                hostsnet = (2 ** 18 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 15:
                calcular = bool(1)
                range_lista = [255, 2]
                octetos = [0, 1, 254, 255]
                net_mask = '255.254.0.0 = 15'
                hostsnet = (2 ** 17 - 2) 
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 16:
                informacoes_ip = ft.Text(
                f'\nNetwork: {ip[0]}.{ip[1]}.{0}.{0}\nBroadcast: {ip[0]}.{ip[1]}.{255}.{255}\nFirsthost: {ip[0]}.{ip[1]}.{0}.{1}\nLasthost: {ip[0]}.{ip[1]}.{255}.{254}\nNetmask: 255.255.0.0 = 16\nSubnets:\n {ip[0]}.{ip[1]}.{0}.{0}\nHosts/Net: {2 ** 16 - 2}'
                )   
                page.add(titulo, envio_info, informacoes_ip)
            case 17:
                calcular = bool(1)
                range_lista = [129, 128]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.128.0 = 17'
                hostsnet = (2 ** 15 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 18:
                calcular = bool(1)
                range_lista = [193, 64]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.192.0 = 18'
                hostsnet = (2 ** 14 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 19:
                calcular = bool(1)
                range_lista = [225, 32]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.224.0 = 19'
                hostsnet = (2 ** 13 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 20:
                calcular = bool(1)
                range_lista = [241, 16]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.240.0 = 20'
                hostsnet = (2 ** 12 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 21:
                calcular = bool(1)
                range_lista = [249, 8]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.248.0 = 21'
                hostsnet = (2 ** 11 - 2) 
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 22:
                calcular = bool(1)
                range_lista = [253, 4]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.252.0 = 22'
                hostsnet = (2 ** 10 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 23:
                calcular = bool(1)
                range_lista = [255, 2]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.254.0 = 23'
                hostsnet = (2 ** 9 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 24:
                informacoes_ip = ft.Text(
                f'\nNetwork: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}\nBroadcast: {ip[0]}.{ip[1]}.{ip[2]}.{255}\nFirsthost: {ip[0]}.{ip[1]}.{ip[2]}.{1}\nLasthost: {ip[0]}.{ip[1]}.{ip[2]}.{254}\nNetmask: 255.255.255.0 = 24\nSubnets:\n {ip[0]}.{ip[1]}.{0}.{0}\nHosts/Net: {2**8 - 2}'
                )   
                page.add(titulo, envio_info, informacoes_ip) 
            case 25:
                calcular = bool(1)
                range_lista = [129, 128]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.255.128 = 25'
                hostsnet = (2 ** 7 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 26:
                calcular = bool(1)
                range_lista = [193, 64]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.255.192 = 26'
                hostsnet = (2 ** 6 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 27:
                calcular = bool(1)
                range_lista = [225, 32]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.255.224 = 27'
                hostsnet = (2 ** 5 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 28:
                calcular = bool(1)
                range_lista = [241, 16]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.255.241 = 28'
                hostsnet = (2 ** 4 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 29:
                calcular = bool(1)
                range_lista = [249, 8]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.255.248 = 29'
                hostsnet = (2 ** 3 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 30:
                calcular = bool(1)
                range_lista = [253, 4]
                octetos = [0, 1, 254, 255]
                net_mask = '255.255.255.252 = 30'
                hostsnet = (2 ** 2 - 2) 
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular)
            case 31:
                calcular = bool(0)
                net_mask = '255.255.255.254 = 31'
                calculo_ip('', '', net_mask, '', calcular)
            case 32:
                calcular = bool(0)
                net_mask = '255.255.255.255 = 32'
                calculo_ip('', '', net_mask, '', calcular)
            case _:
                abrir_popup(None)


    def classificacao(lista_ip, mascara):
        classe = ''
        if lista_ip[0] >= 1 and lista_ip[0] < 10:
            classe = 'Class A - Public'
        elif lista_ip[0] > 10 and lista_ip[0] < 128:
            classe = 'Class A - Public'
        elif lista_ip[0] > 127 and lista_ip[0] < 172:
            classe = 'Class B - Public'
        elif lista_ip[0] == 172:
            if lista_ip[1] > 31:
                classe = 'Class B - Public'
            if lista_ip[1] > 15 and lista_ip[1] < 32:
                classe = 'Class B - Private'
        elif lista_ip[0] > 172 and lista_ip[0] < 192:
            classe = 'class B - Público'
        elif lista_ip[0] == 192:
            if lista_ip[1] == 168:
                classe = 'Class C - Private'
            else:
                classe = 'Class C - Public'
        elif lista_ip[0] > 192 and lista_ip[0] < 224:
            classe = 'Class C - Public'
        elif lista_ip[0] > 223 and lista_ip[0] < 240:
            classe = 'Class D - Public'
        elif lista_ip[0] > 239 and lista_ip[0] < 256:
            classe = 'Class E - Public'
        elif lista_ip[0] == 10:
            classe = 'Class A - Private'
        else:
            classe = 0
            abrir_popup(None)

        '''aprovacao = []
        for i in range(1, 4):
            if lista_ip[i] > 0 and lista_ip[i] <= 255:
                aprovacao.append('ok')
            if len(aprovacao) == 4:
                print(aprovacao)
                break
            else:
                continue'''

        if classe != 0:
            page.add(ft.Text(classe))
            informacoes(classe, lista_ip, mascara)
        

    def cancelar_popup(event):
        popup_enderecoinv.open = False
        page.remove(*page.controls)
        page.add(titulo, envio_info)
        page.update()

    botao_cancelar_popup = ft.ElevatedButton('Ok', on_click=cancelar_popup, width=180)
    popup_enderecoinv = ft.AlertDialog( 
        modal= True,
        open= False,
        title= ft.Text("ERRO!", text_align=ft.TextAlign.CENTER),
        content= ft.Text("Endereço IP inválido!\nO endereço IP deve seguir junto a sua mascara, o formato '0.0.0.0/24' com \nvalores de octetos e mascaras válidos"),
        actions= [botao_cancelar_popup], actions_alignment=ft.MainAxisAlignment.CENTER 
    )

    def abrir_popup(event):
        page.dialog = popup_enderecoinv
        popup_enderecoinv.open = True
        ip_entrada.value = ''
        page.remove(*page.controls)
        page.update()

    def tratamento_ip(event):
        ip_entrada.value = (ip_entrada.value).split('.')

        lista_ip = ip_entrada.value

        while True:
            try:
                mascara = lista_ip[3].split('/')
                lista_ip[3] = mascara[0]
                mascara.pop(0)
                mascara = int(mascara[0])
                break
            except IndexError:
                ip_entrada.value = ''
                lista_ip = ''
                mascara = 0
                abrir_popup(event)
                break
            
        if lista_ip == '':
            abrir_popup(event)
        else:
            for item in range(len(lista_ip)):
                lista_ip[item] = int(lista_ip[item])

            classificacao(lista_ip, mascara)

        
    ip_entrada = ft.TextField(
        label="Endereço Ip", hint_text='0.0.0.0/0',
        on_submit=tratamento_ip,
        max_length=18
        )

    page.title = "Calculadora IP"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('Calculadora IP', size=50, weight=ft.FontWeight.W_400, text_align=ft.TextAlign.END)
    enviar_botao = ft.ElevatedButton('Enviar',on_click=tratamento_ip)
    envio_info = ft.Row([ip_entrada, enviar_botao], alignment=ft.MainAxisAlignment.CENTER)

    page.add(titulo, envio_info)
    page.scroll = 'always'

ft.app(target=main)