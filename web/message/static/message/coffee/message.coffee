# toggles visibility of a contact's message list
$(".contact-list-item").click ->
    console.log $("#msg-list-#{$(this).data('contact')}").toggle()
    return
