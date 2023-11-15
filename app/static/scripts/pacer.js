let devTeamCont = 1;
const showPacer = (e, pacerId) => {
    e.preventDefault()
    let pacer = document.getElementById(pacerId);
    
    pacer.style.display = (pacer.style.display == 'none')? "block" : "none";
};

function removerDev(devId) {
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

const submitForm = (e) => {
    e.preventDefault();

    let notas_equipe = {
        "ProductOwner": pegaValoresPacer("Po"),
        "ScrumMaster": pegaValoresPacer("Sm"),
        "Dev": pegaValoresPacer("Dev"),
    };

    if (devTeamCont >= 1){
        for (let i=2; i<=devTeamCont; i++){
            const devKey = `Dev${i}`;
            if (document.getElementById(`dev-${i}`)) {
                notas_equipe[devKey] = pegaValoresPacer(devKey);
            };
        };
    };

    console.log(notas_equipe);
    
};