// Submit post on submit
// $('#filters-form').on('submit', function(event){
//     submitFilters();
// });
//
$('#headquarter_id_1').change(function() {
    refreshBungalow1();
});
//
$('input[id=arrival_date]').change(function() {
    refreshBungalow1();
});

function refreshBungalow1(){

    var requestData = {
        'headquarter_id' : $('#headquarter_id_1 option:selected').val(),
        'arrival_date' : $('#arrival_date').val(),
        'csrfmiddlewaretoken' : getCookie('csrftoken')
    }

    console.log("AJAX REQUEST", requestData)
    $.ajax({
        url : "create/refresh_bungalow", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(data) {

    console.log("AJAX REQUEST", requestData)
            $('#bungalow_1_content').html(data);
            $('#stay_days_1').prop('disabled', true);
            $('#reserve_1').prop('disabled', true);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("ERROR"); // another sanity check
        }
    });
}

function refreshStay1(requestData){
    $.ajax({
        url : "./post", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(data) {
            $('#stay1-content').html(data);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("ERROR"); // another sanity check
        }
    });
}

function pickHeadquarter2(){
//    Refresh Bungalow
    refreshBungalow2();

}

function refreshBungalow2(){

}

function submitFilters() {
    // event.preventDefault();

    var requestData = getFilters();
    requestData.csrfmiddlewaretoken = getCookie('csrftoken');

    reloadTable(requestData);
};

function prevPage() {
    console.log('PREV Page')
    event.preventDefault();

    var requestData = getFilters();
    requestData.page = $('#page').text() - 1;
    requestData.csrfmiddlewaretoken = getCookie('csrftoken');

    reloadTable(requestData);
};

function nextPage() {
    console.log('NEXT Page')
    event.preventDefault();

    var requestData = getFilters();
    requestData.page = parseInt($('#page').text(),10) + 1;
    requestData.csrfmiddlewaretoken = getCookie('csrftoken');

    reloadTable(requestData);
};

function getFilters() {
    var filter = {
//        'bungalow_type_id' : $('#bungalow_type_id option:selected').val(),
        'headquarter_id' : $('#headquarter_id option:selected').val(),
        'status' : $('#status option:selected').val(),
    }
    return filter;
};

function reloadTable(requestData){
    $.ajax({
        url : "post", // the endpoint
        type : "POST", // http method
        data : requestData, // data sent with the post request

        // handle a successful response
        success : function(data) {
            $('#table-content').html(data);

            // Prevent Default Current Page
            $( "#current-page" ).click(function(event) {
                console.log('CURRENT')
            });
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log("ERROR"); // another sanity check
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function check_in() {
    console.log($('#reservation_id').text())
    console.log("CHECK IN")

    $.ajax({
        url : "check_in", // the endpoint
        type : "POST", // http method
        data : {
            'reservation_id' : $('#reservation_id').text(),
            'csrfmiddlewaretoken' :  getCookie('csrftoken')
        }, // data sent with the post request

        // handle a successful response
        success : function(data) {
            // $('#table-content').html(data);
            console.log("SUCCESS"); // another sanity check
            location.reload();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log("ERROR"); // another sanity check
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function check_out() {
    console.log($('#reservation_id').text())
    console.log("CHECK OUT")

    $.ajax({
        url : "check_out", // the endpoint
        type : "POST", // http method
        data : {
            'reservation_id' : $('#reservation_id').text(),
            'csrfmiddlewaretoken' :  getCookie('csrftoken')
        }, // data sent with the post request

        // handle a successful response
        success : function(data) {
            // $('#table-content').html(data);
            console.log("SUCCESS"); // another sanity check
            location.reload();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log("ERROR"); // another sanity check
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}