var $doc = $(document);
$doc.ready(function() {
    "use strict";

    var set_data_func = function (event) {

        var iframe_code = $('#id_iframe_code').val()
        var src = $(iframe_code).attr('src')
        try {
            var link = src.replace('embed', 'download')
        }
        catch (e) {
            console.log("Invalid link to parse")
        }
        idLink.val(link)
    }

    var idLink = $('#id_link');

    $('#id_iframe_code').on('input', set_data_func)

});
