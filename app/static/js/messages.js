const conversations = JSON.parse(document.getElementById('conversationData').textContent);

let selectedId = conversations[0]?.id ?? null;
let searchTerm = '';
let direction = 'all';

const conversationPane = document.getElementById('conversationPane');
const chatPane = document.getElementById('chatPane');
const conversationList = document.getElementById('conversationList');
const messageStream = document.getElementById('messageStream');

function escapeHtml(value) {
  const element = document.createElement('div');
  element.textContent = String(value);
  return element.innerHTML;
}

function initials(phone) {
  return phone.replace(/\D/g, '').slice(-2);
}

function visibleConversations() {
  const normalized = searchTerm.toLocaleLowerCase('es');
  return conversations.filter(conversation => {
    const hasDirection = direction === 'all'
      || conversation.messages.some(message => message.direction === direction);
    const searchable = `${conversation.name} ${conversation.phone} ${conversation.messages
      .map(message => message.text)
      .join(' ')}`.toLocaleLowerCase('es');

    return hasDirection && searchable.includes(normalized);
  });
}

function needsAttention(message) {
  if (message.direction === 'inbound') return true;
  return !/^(2\d\d)\b/.test(message.status)
    && !['Enviado', 'Entregado'].includes(message.status);
}

function renderMetrics() {
  const messages = conversations.flatMap(conversation => conversation.messages);
  const pending = conversations.filter(
    conversation => needsAttention(conversation.messages.at(-1))
  ).length;
  const values = [
    [conversations.length, 'Conversaciones'],
    [messages.length, 'Mensajes'],
    [messages.filter(message => message.direction === 'inbound').length, 'Entrantes'],
    [pending, 'Por atender']
  ];

  document.getElementById('metrics').innerHTML = values.map(([value, label], index) => `
    <div class="col-3 ${index < values.length - 1 ? 'border-end hairline' : ''}">
      <div class="text-center py-3 px-1">
        <div class="h4 fw-semibold letter-tight mb-0">${value}</div>
        <div class="small text-pipe-muted text-truncate">${label}</div>
      </div>
    </div>
  `).join('');
}

function renderConversationList() {
  const visible = visibleConversations();
  document.getElementById('conversationCount').textContent = visible.length;

  if (!visible.length) {
    conversationList.innerHTML = `
      <div class="h-100 d-flex align-items-center justify-content-center text-center text-pipe-muted p-4">
        <div><i class="bi bi-search fs-3 d-block mb-2"></i>No encontramos conversaciones con esos filtros.</div>
      </div>
    `;
    return;
  }

  conversationList.innerHTML = visible.map(conversation => {
    const last = conversation.messages.at(-1);
    const pending = needsAttention(last);

    return `
      <button class="conversation-button list-group-item list-group-item-action border-0 rounded-3 p-3 ${conversation.id === selectedId ? 'active' : ''}" type="button" data-id="${escapeHtml(conversation.id)}">
        <span class="d-flex align-items-center gap-3">
          <span class="contact-avatar rounded-circle">${escapeHtml(initials(conversation.phone))}</span>
          <span class="flex-grow-1 overflow-hidden text-start">
            <span class="d-flex align-items-center justify-content-between gap-2">
              <span class="fw-semibold text-truncate">${escapeHtml(conversation.name)}</span>
              <span class="small text-pipe-muted flex-shrink-0">${escapeHtml(last.time)}</span>
            </span>
            <span class="small text-pipe-muted d-block text-truncate">${escapeHtml(conversation.phone)}</span>
            <span class="small d-flex align-items-center gap-2 mt-1">
              ${pending
                ? '<i class="bi bi-circle-fill text-primary status-dot" aria-label="Pendiente"></i>'
                : '<i class="bi bi-check2-all text-primary"></i>'}
              <span class="text-pipe-muted text-truncate">${last.direction === 'outbound' ? 'Bot: ' : ''}${escapeHtml(last.text)}</span>
            </span>
          </span>
        </span>
      </button>
    `;
  }).join('');

  conversationList.querySelectorAll('[data-id]').forEach(button => {
    button.addEventListener('click', () => selectConversation(button.dataset.id));
  });
}

function renderSelectedConversation() {
  const conversation = conversations.find(item => item.id === selectedId);
  if (!conversation) {
    messageStream.innerHTML = `
      <div class="h-100 d-flex align-items-center justify-content-center text-center text-pipe-muted p-4">
        <div><i class="bi bi-chat fs-3 d-block mb-2"></i>Aún no hay conversaciones para mostrar.</div>
      </div>
    `;
    return;
  }

  document.getElementById('selectedAvatar').textContent = initials(conversation.phone);
  document.getElementById('selectedName').textContent = conversation.name;
  document.getElementById('selectedPhone').textContent = conversation.phone;

  const filteredMessages = direction === 'all'
    ? conversation.messages
    : conversation.messages.filter(message => message.direction === direction);

  if (!filteredMessages.length) {
    messageStream.innerHTML = `
      <div class="h-100 d-flex align-items-center justify-content-center text-center text-pipe-muted p-4">
        <div><i class="bi bi-funnel fs-3 d-block mb-2"></i>Esta conversación no tiene mensajes con el filtro seleccionado.</div>
      </div>
    `;
    return;
  }

  messageStream.innerHTML = `
    <div class="small text-center text-pipe-muted mb-4">Historial de mensajes</div>
    ${filteredMessages.map(message => `
      <div class="d-flex mb-3 ${message.direction === 'outbound' ? 'justify-content-end message-out' : 'message-in'}">
        <div class="message-bubble border-0 rounded-4 px-3 py-2">
          <div class="small">${escapeHtml(message.text)}</div>
          <div class="message-meta d-flex align-items-center justify-content-end gap-1 text-pipe-muted mt-1 small">
            <span>${escapeHtml(message.time)}</span>
            <span>· ${escapeHtml(message.status)}</span>
            ${message.direction === 'outbound' ? '<i class="bi bi-check2-all"></i>' : ''}
          </div>
        </div>
      </div>
    `).join('')}
  `;
  messageStream.scrollTop = messageStream.scrollHeight;
}

function selectConversation(id) {
  selectedId = id;
  renderConversationList();
  renderSelectedConversation();

  if (window.innerWidth < 768) {
    conversationPane.classList.remove('d-flex');
    conversationPane.classList.add('d-none');
    chatPane.classList.remove('d-none');
    chatPane.classList.add('d-flex');
  }
}

document.getElementById('searchInput').addEventListener('input', event => {
  searchTerm = event.target.value.trim();
  renderConversationList();
});

document.querySelectorAll('.filter-button').forEach(button => {
  button.addEventListener('click', () => {
    direction = button.dataset.direction;
    document.querySelectorAll('.filter-button').forEach(filter => {
      const active = filter === button;
      filter.classList.toggle('btn-light', active);
      filter.classList.toggle('shadow-sm', active);
      filter.classList.toggle('active', active);
      filter.classList.toggle('btn-link', !active);
      filter.classList.toggle('text-secondary', !active);
      filter.classList.toggle('text-decoration-none', !active);
      filter.setAttribute('aria-pressed', active);
    });
    renderConversationList();
    renderSelectedConversation();
  });
});

document.getElementById('backButton').addEventListener('click', () => {
  chatPane.classList.remove('d-flex');
  chatPane.classList.add('d-none');
  conversationPane.classList.remove('d-none');
  conversationPane.classList.add('d-flex');
});

renderMetrics();
renderConversationList();
renderSelectedConversation();
