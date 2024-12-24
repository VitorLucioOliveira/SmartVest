// Objeto para armazenar o estado de cada assinante (aberto ou fechado)
const subscriberState = {};

function toggleInfo(element) {
    const infoDiv = element.nextElementSibling;
    const subscriberId = element.dataset.id;

    // Alterna o estado e armazena
    infoDiv.classList.toggle('active');
    subscriberState[subscriberId] = infoDiv.classList.contains('active');
}

var socket = io.connect('http://' + document.domain + ':' + location.port);

// Recebe a atualização dos tópicos do servidor
socket.on('atualizacao_topicos', function(data) {
    var topicosContainer = document.getElementById('topicos');
    topicosContainer.innerHTML = ''; // Limpa a lista antes de atualizar

    data.topicos.forEach(function(topico) {
        // Cria um contêiner específico para cada tópico
        const topicoDiv = document.createElement('div');
        topicoDiv.className = 'container';

        topicoDiv.innerHTML = `
            <div class="topico">
                <img class="topico_img" src="static/img/Radio.png" alt="Icone">
                <h1 class="topico_titulo">${topico.nome}</h1>
            </div>
            <ul class="subscriber_list"></ul>
        `;

        // Seleciona o contêiner da lista de assinantes
        const subscriberList = topicoDiv.querySelector('.subscriber_list');

        topico.subscribers.forEach(subscriber => {
            const subscriberId = `${topico.nome}-${subscriber.nome}`;
            const isActive = subscriberState[subscriberId] ? 'active' : '';

            // Cria o elemento do assinante e aplica o estado armazenado
            const subscriberItem = document.createElement('li');
            subscriberItem.className = 'subscriber';

            subscriberItem.innerHTML = `
                <div class="subscriber_id" data-id="${subscriberId}" onclick="toggleInfo(this)">
                    <img class="subscriber_img" src="static/img/account.png" alt="conta">
                    <p>${subscriber.id}</p>
                </div>
                <div class="subscriber_info ${isActive}">
                    <p>Alerta: ${subscriber.alerta}</p>
                </div>
            `;

            // Adiciona o assinante à lista
            subscriberList.appendChild(subscriberItem);
        });

        // Adiciona o tópico atualizado ao contêiner principal
        topicosContainer.appendChild(topicoDiv);
    });
});
