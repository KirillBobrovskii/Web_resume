$(function() {
    $(document).on('submit', '#send_email_form', function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: send_email_url,
            data: $(this).serialize(),
            success: function (is_send) {
                if (is_send) {
                    alert('Сообщение отправлено.');
                } else {
                    alert('Сообщение не отправлено!');
                }
            },
            error: function (is_send) {
                console.log(is_send.responseJSON.errors);
            }
        });
        $('textarea').val('');
    });
});