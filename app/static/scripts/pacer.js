let devTeamCont = 1; 
const modal = document.getElementById("customModal");
   
const mostrarPacerIndividual = (pacerId) => {
    let pacer = document.getElementById(pacerId);
    let dropdownIcon = document.getElementById(`dropdown-icon-${pacerId}`);
    
    pacer.style.display = (pacer.style.display == 'none')? "block" : "none";
    dropdownIcon.style.transform = (pacer.style.display == 'none') ? 'rotate(180deg)' : 'rotate(0)';
};

const removerDev = (devId) => {
    const devElement = document.getElementById(devId);
    if (devElement) {
        devElement.remove();
    }
};

const pegaNome = (nameId) => {
    return document.querySelector(`input[id="name_${nameId}"]`).value;
};

const pegaValoresPacer = (nameId) => {
    const requisitos = ["Proatividade", "Autonomia", "Colaboracao", "Entrega"];

    let valores = {"Nome": pegaNome(nameId), "Notas": {"Proatividade": 0, "Autonomia": 0, "Colaboracao": 0, "Entrega": 0}};
    for (let key of requisitos){
        valores["Notas"][`${key}`] = document.querySelector(`input[name="inlineRadio${key}${nameId}"]:checked`).value;
    };

    return valores;

};

const adicionaBodyModal = (notas_equipe) => {
    let tabelasContainer = document.getElementById("modal-body");

    tabelasContainer.innerHTML = '';

    for (let pessoa of notas_equipe) {
        let tabela = document.createElement('table');
        tabela.classList.add('table', 'table-bordered');

        let headerRow = document.createElement('thead');
        let headerCell = document.createElement('th');
        headerCell.setAttribute('colspan', '2');
        headerCell.classList.add('modal_titulo', 'text-center', 'border-0', 'fs-5', 'fw-bold');
        headerCell.textContent = `${pessoa.Nome} (${pessoa.Funcao})`;
        headerRow.appendChild(headerCell);
        tabela.appendChild(headerRow);

        let corpoTabela = document.createElement('tbody');
        for (let categoria in pessoa.Notas) {
            let notaPessoaTr = document.createElement('tr');
            notaPessoaTr.classList.add('row')

            let categoriaTh = document.createElement('th');
            categoriaTh.classList.add('col-6')
            categoriaTh.textContent = categoria;
            notaPessoaTr.appendChild(categoriaTh);

            let notaTd = document.createElement('td');
            notaTd.classList.add('col-6')
            notaTd.textContent = `${pessoa.Notas[categoria]}`;
            notaPessoaTr.appendChild(notaTd);

            corpoTabela.appendChild(notaPessoaTr);
        }

        tabela.appendChild(corpoTabela);

        tabelasContainer.appendChild(tabela);
    }
};

const mostrarModal = () => {
    modal.showModal();
};

const fecharModal = () => {
    modal.close();
};

const mostrarNotasFinaisEquipe = (e) => {
    e.preventDefault();

    let notas_equipe = [
        {"Funcao": "Product Owner", ...pegaValoresPacer("Po")},
        {"Funcao": "Scrum Master", ...pegaValoresPacer("Sm")},
        {"Funcao": "Dev", ...pegaValoresPacer("Dev")},
    ];

    if (devTeamCont >= 1){
        for (let i=2; i<=devTeamCont; i++){
            const devKey = `Dev${i}`;;

            if (document.getElementById(`dev-${i}`)) {
                notas_equipe.push({"Funcao": "Dev", ...pegaValoresPacer(devKey)});
            };
        };
    };

    adicionaBodyModal(notas_equipe);
    mostrarModal();
};