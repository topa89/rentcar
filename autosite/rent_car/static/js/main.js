
$(document).ready(function () {
    var form = $('#form_order');


    form.on('submit', function (e) {
        e.preventDefault();

        var data = {};
        data.car = $('#car_name').text();
        data.name = $('#name').val();
        data.phone = $('#phone-number').val();
        data.srok = $('#srok option:selected').text();

        var csrf_token = $('#form_order [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr('action');

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                $('#order_modal').modal('hide');
                $('#order_success_modal').modal('show');
            }
        });

    });

    $('.popup-link').magnificPopup({
        delegate: 'a',
        type: 'image',
        gallery: {
            enabled: true,
        },
        zoom: {
            enabled: true,
            duration: 300
        }
    });

});
