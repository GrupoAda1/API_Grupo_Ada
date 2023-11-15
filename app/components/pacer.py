from app.constrants.pacer import REQUISITOS

def pacer(sigla_funcao):
    tbody = ""

    for requisito in REQUISITOS:
        td = ""
        for i in range(4):
            input_name = f"inlineRadio{requisito}{sigla_funcao.title()}"
            input_id = f"inlineRadio{requisito}{i}"
            
            td += f"""<td>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="{input_name}" id="{input_id}" value="{i}" checked>
                    <label class="form-check-label" for="input_id">{i}</label>
                </div>
            </td>"""

        tbody += f'<tr><th scope="row">{requisito}</th>{td}</tr>'

    return f'''
    <div id="{sigla_funcao}_pacer" style="display: block;">
        <table class="table table-bordered">
            <thead>
                <tr>
                <th scope="col">Requisito</th>
                <th scope="col">Péssimo</th>
                <th scope="col">Ruim</th>
                <th scope="col">Bom</th>
                <th scope="col">Excelente</th>
                </tr>
            </thead>
            <tbody>
                {tbody}
            </tbody>
            </table>
    </div>
    '''