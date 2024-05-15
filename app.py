import PySimpleGUI as sg

sg.theme('reddit')

janela_principal = [
    [sg.Text('E-mail'),sg.Input(key='email')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.FolderBrowse('Escolher Pasta Anexos',target='input_anexos'),sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher Pasta Planilha',target='input_planilha'),sg.Input(key='input_planilha')],
    [sg.Button('Salvar')]
]

janela = sg.Window('Principal',layout=janela_principal)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values['email']
        senha = values['senha']
        caminho_pasta_anexos = values['input_anexos']
        caminho_pasta_planilha = values['input_planilha']
        print(f'O e-mail digitado foi {email}')
        print(f'A senha digitada foi {senha}')
        print(f'O caminho da pasta de anexos é {caminho_pasta_anexos}')
        print(f'O caminho da pasta da planilha é {caminho_pasta_planilha}')
